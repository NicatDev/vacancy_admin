<?php

namespace App\Models;

use App\Services\SubscriptionService\Enums\PlanType;
use Database\Factories\PricingPlanFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class PricingPlan extends Model
{
    /** @use HasFactory<PricingPlanFactory> */
    use HasFactory;
    use SoftDeletes;

    protected $fillable = [
        'name',
        'slug',
        'paypal_plan_id',
        'type',
        'price',
        'features',
        'max_post_limit',
        'duration_months',
    ];

    protected $casts = [
        'name' => 'string',
        'slug' => 'string',
        'type' => PlanType::class,
        'price' => 'decimal:2',
        'features' => 'collection',
        'max_post_limit' => 'integer',
        'duration_months' => 'integer',
    ];

    public function isOneTimePlan(): bool
    {
        return $this->getAttribute('type') === PlanType::ONE_TIME;
    }

    public function isRegularPlan(): bool
    {
        return $this->getAttribute('type') === PlanType::REGULAR;
    }
}
