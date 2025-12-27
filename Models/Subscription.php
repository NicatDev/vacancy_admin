<?php

namespace App\Models;

use App\Services\SubscriptionService\Enums\PlanType;
use App\Services\SubscriptionService\Enums\Status;
use Database\Factories\SubscriptionFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasOneThrough;

class Subscription extends Model
{
    /** @use HasFactory<SubscriptionFactory> */
    use HasFactory;

    protected $fillable = [
        'paypal_process_id',
        'company_id',
        'pricing_plan_id',
        'subscribed_by_id',
        'status',
        'started_at',
        'suspended_at',
        'expired_at',
        'cancelled_at',
    ];

    protected $casts = [
        'status' => Status::class,
        'started_at' => 'datetime',
        'suspended_at' => 'datetime',
        'expired_at' => 'datetime',
        'cancelled_at' => 'datetime',
    ];

    public function plan(): BelongsTo
    {
        return $this->belongsTo(
            PricingPlan::class,
            'pricing_plan_id',
            'id',
        );
    }

    public function pricingPlan(): BelongsTo
    {
        return $this->plan();
    }

    public function company(): BelongsTo
    {
        return $this->belongsTo(
            Company::class,
            'company_id',
            'id'
        );
    }

    public function subscribedBy(): BelongsTo
    {
        return $this->belongsTo(
            User::class,
            'subscribed_by_id',
            'id',
        );
    }

    public function isPlan(PlanType $type): bool
    {
        return $type === $this->getAttribute('plan')->getAttribute('type');
    }

    public function isRegularPlan(): bool
    {
        return $this->isPlan(PlanType::REGULAR);
    }

    public function isOneTimePlan(): bool
    {
        return $this->isPlan(PlanType::ONE_TIME);
    }

    public function isActive(): bool
    {
        return $this->isStatus(Status::ACTIVE);
    }

    public function isPending(): bool
    {
        return $this->isStatus(Status::PENDING);
    }

    public function isExpired(): bool
    {
        return now() >= $this->getAttribute('expired_at');
    }

    public function isSuspended(): bool
    {
        return $this->isStatus(Status::SUSPENDED);
    }

    public function isCancelled(): bool
    {
        return $this->isStatus(Status::CANCELLED);
    }

    public function isLimitReached(): bool
    {
        $startedAt = $this->getAttribute('started_at');

        $postCount = JobPost::query()
            ->where('company_id', $this->getAttribute('company_id'))
            ->where('job_posts.status', \App\Services\JobPostService\Status::ACTIVE)
            ->whereDate('job_posts.created_at', '>=', $startedAt)
            ->count();

        $maxPostCount = $this->getAttribute('plan')->getAttribute('max_post_limit');

        if ($postCount < $maxPostCount) {
            return false;
        }

        return true;
    }

    public function isStatus(Status $status): bool
    {
        return $status === $this->getAttribute('status');
    }

    public function scopeActive($query)
    {
        return $query->where('status', Status::ACTIVE);
    }
}
