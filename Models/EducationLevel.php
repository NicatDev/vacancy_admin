<?php

namespace App\Models;

use Astrotomic\Translatable\Contracts\Translatable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

/**
 * @property int $id
 * @property string $name
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property \Illuminate\Support\Carbon|null $deleted_at
 *
 * @method static \Database\Factories\EducationLevelFactory factory($count = null, $state = [])
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel onlyTrashed()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel whereDeletedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel whereUpdatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel withTrashed(bool $withTrashed = true)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|EducationLevel withoutTrashed()
 *
 * @mixin \Eloquent
 */
class EducationLevel extends Model implements Translatable
{
    use HasFactory;
    use SoftDeletes;
    use \Astrotomic\Translatable\Translatable;

    protected $fillable = [
    ];

    public $translatedAttributes = [
        'name'
    ];
}
