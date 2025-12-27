<?php

namespace App\Models;

use Astrotomic\Translatable\Contracts\Translatable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Spatie\MediaLibrary\HasMedia;

/**
 * @property int $id
 * @property int $industry_id
 * @property string $name
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property-read \App\Models\Industry $industry
 *
 * @method static \Database\Factories\OccupationFactory factory($count = null, $state = [])
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Occupation newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Occupation newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Occupation query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Occupation whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Occupation whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Occupation whereIndustryId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Occupation whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Occupation whereUpdatedAt($value)
 *
 * @mixin \Eloquent
 */
class Occupation extends Model implements Translatable
{
    use HasFactory;
    use \Astrotomic\Translatable\Translatable;

    protected $fillable = [
    ];

    public $translatedAttributes = [
        'name',
    ];

    public function industry(): BelongsTo
    {
        return $this->belongsTo(Industry::class);
    }
}
