<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\SoftDeletes;

class Service extends Model
{
    use HasFactory;
    use SoftDeletes;

    protected static function boot(): void
    {
        parent::boot();

        self::deleting(function ($model) {
            CandidateService::query()
                ->where('service_id', $model->getKey())
                ->delete();
        });

        self::restoring(function ($model) {
            CandidateService::query()
                ->onlyTrashed()
                ->where('service_id', $model->getKey())
                ->restore();
        });
    }

    protected $fillable = [
        'name',
    ];

    public function candidates(): BelongsToMany
    {
        return $this->belongsToMany(Candidate::class, 'candidate_service');
    }
}
