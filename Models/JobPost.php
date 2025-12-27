<?php

namespace App\Models;

use App\Services\JobPostBoostService\OrderStatus;
use App\Services\JobPostService\Status;
use Database\Factories\JobPostFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Relations\HasOneThrough;
use Illuminate\Database\Eloquent\SoftDeletes;

class JobPost extends Model
{
    /** @use HasFactory<JobPostFactory> */
    use HasFactory;
    use SoftDeletes;

    protected $fillable = [
        'title',
        'location',
        'experience',
        'salary',
        'info',
        'responsibilities',
        'requirements',
        'view_count',
        'company_id',
        'occupation_id',
        'employment_type_id',
        'education_level_id',
        'created_by_id',
        'status',
        'published_at',
        'expired_at',
    ];

    protected $attributes = [
        'view_count' => 0,
    ];

    protected $casts = [
        'status' => Status::class,
        'published_at' => 'datetime',
        'expired_at' => 'datetime',
        'view_count' => 'integer',
    ];

    public function company(): BelongsTo
    {
        return $this->belongsTo(Company::class);
    }

    public function industry(): HasOneThrough
    {
        return $this->hasOneThrough(
            Industry::class,
            Occupation::class,
            'id',
            'id',
            'occupation_id',
            'industry_id',
        );
    }

    public function occupation(): BelongsTo
    {
        return $this->belongsTo(Occupation::class);
    }

    public function employment_type(): BelongsTo
    {
        return $this->belongsTo(EmploymentType::class);
    }

    public function educationLevel(): BelongsTo
    {
        return $this->belongsTo(EducationLevel::class);
    }

    public function education_level(): BelongsTo
    {
        return $this->belongsTo(EducationLevel::class);
    }

    public function createdBy(): BelongsTo
    {
        return $this->belongsTo(
            User::class,
            'created_by_id',
            'id'
        );
    }

    public function isActive(): bool
    {
        return Status::ACTIVE === $this->getAttribute('status')
            && now() <= $this->getAttribute('expired_at');
    }

    public function isDraft(): bool
    {
        return Status::DRAFT === $this->getAttribute('status')
            && null === $this->getAttribute('published_at')
            && null === $this->getAttribute('expired_at');
    }

    public function scopeActive($query)
    {
        $query->where('status', Status::ACTIVE)
            ->whereDate('published_at', '<=', now())
            ->whereDate('expired_at', '>=', now());
    }

    public function applications(): HasMany
    {
        return $this->hasMany(
            JobApplication::class,
            'job_post_id',
            'id',
        );
    }

    public function boosts(): HasMany
    {
        return $this->hasMany(Boost::class, 'job_post_id');
    }

    public function activeBoost(): HasMany
    {
        return $this->boosts()
            ->where('status', OrderStatus::PAID)
            ->where('valid_until', '>=', now())
            ->latest();
    }

    public function increaseViewCount(): void
    {
        $this->increment('view_count');
    }
}
