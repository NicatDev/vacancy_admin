<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class JobApplication extends Model
{
    /** @use HasFactory<\Database\Factories\JobApplicationFactory> */
    use HasFactory;

    protected $fillable = [
        'job_post_id',
        'candidate_id',
        'applied_by_id',
    ];

    protected $with = [
        'job'
    ];

    public function job_post(): BelongsTo
    {
        return $this->belongsTo(
            JobPost::class,
            'job_post_id',
            'id',
        );
    }

    public function job(): BelongsTo
    {
        return $this->job_post();
    }

    public function candidate(): BelongsTo
    {
        return $this->belongsTo(
            Candidate::class,
            'candidate_id',
            'id',
        );
    }

    public function appliedBy(): BelongsTo
    {
        return $this->belongsTo(
            User::class,
            'applied_by_id',
            'id'
        );
    }
}
