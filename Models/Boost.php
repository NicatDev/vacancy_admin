<?php

namespace App\Models;

use App\Services\JobPostBoostService\OrderStatus;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Boost extends Model
{
    /** @use HasFactory<\Database\Factories\BoostFactory> */
    use HasFactory;

    protected $fillable = [
        'job_post_id',
        'booster_id',
        'status',
        'order_id',
        'valid_until',
    ];

    protected $attributes = [
        'status' => OrderStatus::PENDING,
    ];

    protected $casts = [
        'booster_id' => 'integer',
        'job_post_id' => 'integer',
        'status' => OrderStatus::class,
        'order_id' => 'string',
        'valid_until' => 'datetime',
    ];

    public function booster(): BelongsTo
    {
        return $this->belongsTo(User::class, 'booster_id');
    }

    public function post(): BelongsTo
    {
        return $this->belongsTo(JobPost::class, 'job_post_id');
    }

    public function jobPost(): BelongsTo
    {
        return $this->post();
    }

    public function boostPost(): true
    {
        return $this->update([
            'status' => OrderStatus::PAID,
        ]);
    }
}
