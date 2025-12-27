<?php

namespace App\Models;

use App\Interfaces\ProfileInterface;
use App\Services\JobPostService\Exceptions\CompanyCantPost;
use App\Services\SubscriptionService\Enums\PlanType;
use App\Services\SubscriptionService\Enums\Status as SubscriptionStatus;
use Database\Factories\CompanyFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Relations\HasOne;
use Illuminate\Database\Eloquent\Relations\MorphOne;
use Illuminate\Database\Eloquent\SoftDeletes;
use Spatie\MediaLibrary\HasMedia;
use Spatie\MediaLibrary\InteractsWithMedia;
use Spatie\MediaLibrary\MediaCollections\Models\Media;

/**
 * @property int $id
 * @property int $user_id
 * @property string $website
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property-read \App\Models\User $user
 *
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Company newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Company newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Company query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Company whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Company whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Company whereUpdatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Company whereUserId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Company whereWebsite($value)
 *
 * @mixin \Eloquent
 */
class Company extends Model implements ProfileInterface, HasMedia
{
    /** @use HasFactory<CompanyFactory> */
    use HasFactory;
    use SoftDeletes;
    use InteractsWithMedia;

    protected $fillable = [
        'website',
        'user_id',
        'max_post_limit',
        'name',
        'location',
        'summary',
        'employees_count',
        'voen',
        'status',
        'activated_by_id',
        'activated_at',
        'founded_at',
    ];

    protected $with = [
        'user',
        'logo',
    ];

    protected $attributes = [
        'max_post_limit' => 0,
        'status' => false,
        'summary' => null,
        'founded_at' => null,
        'location' => null,
        'employees_count' => 1,
    ];

    protected $casts = [
        'max_post_limit' => 'int',
        'status' => 'boolean',
        'activated_by_id' => 'int',
        'activated_at' => 'datetime',
        'founded_at' => 'date',
        'employees_count' => 'int',
    ];

    protected static function booted(): void
    {
        parent::booted();

        static::addGlobalScope('onlyCompany', function ($builder) {
            $builder->whereHas('user.roles', function ($query) {
                $query->where('name', \App\Enums\Role::COMPANY);
            });
        });
    }

    public function user(): \Illuminate\Database\Eloquent\Relations\BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function profile(): static
    {
        return $this;
    }

    public function externalLinks(): \Illuminate\Database\Eloquent\Relations\HasMany
    {
        return $this->hasMany(ExternalLink::class);
    }

    public function external_links(): \Illuminate\Database\Eloquent\Relations\HasMany
    {
        return $this->externalLinks();
    }

    public function phoneNumbers(): \Illuminate\Database\Eloquent\Relations\HasMany
    {
        return $this->hasMany(
            Phone::class,
            'company_id',
            'id'
        );
    }

    public function phone_numbers(): \Illuminate\Database\Eloquent\Relations\HasMany
    {
        return $this->phoneNumbers();
    }

    public function subscriptions(): \Illuminate\Database\Eloquent\Relations\HasMany
    {
        return $this->hasMany(
            Subscription::class,
            'company_id',
            'id'
        );
    }

    /**
     * Get the active regular subscription plan for the company.
     *
     * Returns the latest regular plan subscription that is either:
     * - ACTIVE status
     * - SUSPENDED status but still within the paid period (not expired)
     *
     * Business Logic (from README.md):
     * Even if a subscription is suspended, if the current time is between
     * started_at and expired_at, the company should still have unlimited
     * post access until the end of the paid period.
     *
     * @return HasOne<Subscription>
     */
    public function regularPlan(): HasOne
    {
        return $this->hasOne(Subscription::class)
            ->whereHas('plan', function ($query) {
                $query->where('type', PlanType::REGULAR);
            })
            ->where(function ($query) {
                // ACTIVE status - unlimited posts
                $query->where('status', SubscriptionStatus::ACTIVE)
                    // OR SUSPENDED but within paid period (started_at <= now < expired_at)
                    ->orWhere(function ($q) {
                        $q->where('status', SubscriptionStatus::SUSPENDED)
                            ->where('started_at', '<=', now())
                            ->where('expired_at', '>', now());
                    });
            })
            ->orderByDesc('id');
    }

    /**
     * Get the latest one-time plan subscription for the company.
     *
     * Returns the most recent PAID one-time plan. Note that companies can
     * purchase multiple one-time plans, but this returns only the latest one.
     *
     * Business Logic (from README.md):
     * One-time plans add to company.max_post_limit. Multiple purchases are allowed.
     *
     * @return HasOne<Subscription>
     */
    public function oneTimePlan(): HasOne
    {
        return $this->hasOne(Subscription::class)
            ->whereHas('plan', function ($query) {
                $query->where('type', PlanType::ONE_TIME);
            })
            ->where('status', SubscriptionStatus::PAID)
            ->orderByDesc('id');
    }

    /**
     * Check if company has an active regular plan.
     *
     * @return bool
     */
    public function hasRegularPlan(): bool
    {
        return $this->regularPlan()->exists();
    }

    /**
     * Check if company has any paid one-time plan.
     *
     * Note: This checks if at least one one-time plan exists with PAID status.
     * Companies can have multiple one-time plans.
     *
     * @return bool
     */
    public function hasOneTimePlan(): bool
    {
        return $this->oneTimePlan()->exists();
    }

    /**
     * Check if company has any active plan (regular or one-time).
     *
     * Priority order (from README.md):
     * 1. Regular plan (ACTIVE or valid SUSPENDED)
     * 2. One-time plan with remaining limit (max_post_limit > 0)
     *
     * @return bool
     */
    public function hasActivePlan(): bool
    {
        return $this->hasRegularPlan()
            || ($this->hasOneTimePlan() && $this->getAttribute('max_post_limit') > 0);
    }

    /**
     * Get the currently active subscription plan.
     *
     * Returns subscription in priority order (from README.md):
     * 1. Regular plan (if exists and valid) - provides unlimited posts
     * 2. One-time plan (if exists) - uses max_post_limit
     * 3. null (if no plans available)
     *
     * @return Subscription|null
     */
    public function activePlan(): ?Subscription
    {
        // Priority 1: Check for active regular plan (unlimited posts)
        // Using dynamic property access to leverage Eloquent lazy loading
        if ($this->regularPlan !== null) {
            return $this->regularPlan;
        }

        // Priority 2: Check for one-time plan (limited posts)
        if ($this->oneTimePlan !== null) {
            return $this->oneTimePlan;
        }

        // No active plan found
        return null;
    }

    public function decreasePostLimit(): void
    {
        $this->decrement('max_post_limit');
    }

    /**
     * @throws CompanyCantPost
     */
    public function canPostOrFail(): true
    {
        return $this->hasActivePlan() || throw new CompanyCantPost();
    }

    public function registerMediaCollections(): void
    {
        $this->addMediaCollection('logo')
            ->singleFile()
            ->acceptsMimeTypes(['image/png']);
    }

    public function jobPosts(): HasMany
    {
        return $this->hasMany(
            JobPost::class,
            'company_id',
            'id',
        );
    }

    public function posts(): HasMany
    {
        return $this->jobPosts();
    }

    public function logo(): MorphOne
    {
        return $this->morphOne(Media::class, 'model')->where(
            'collection_name',
            'logo'
        );
    }

    public function scopeActive($query)
    {
        $query->where('status', true);
    }

    public function isActive(): bool
    {
        return $this->getAttribute('status') === true;
    }

    public function activate(User $performer): true
    {
        return $this->update([
            'status' => true,
            'activated_by_id' => $performer->getKey(),
            'activated_at' => now(),
        ]);
    }

    public function activated_by(): BelongsTo
    {
        return $this->belongsTo(User::class, 'activated_by_id');
    }

    public function activatedBy(): BelongsTo
    {
        return $this->activated_by();
    }
}
