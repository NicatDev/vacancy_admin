<?php

namespace App\Models;

use Astrotomic\Translatable\Contracts\Translatable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\SoftDeletes;

/**
 * @property int $id
 * @property string $label
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property \Illuminate\Support\Carbon|null $deleted_at
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Candidate> $candidates
 * @property-read int|null $candidates_count
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Language> $languages
 * @property-read int|null $languages_count
 *
 * @method static \Database\Factories\LevelFactory factory($count = null, $state = [])
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level onlyTrashed()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level whereDeletedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level whereLabel($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level whereUpdatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level withTrashed(bool $withTrashed = true)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Level withoutTrashed()
 *
 * @mixin \Eloquent
 */
class Level extends Model implements Translatable
{
    use HasFactory;
    use SoftDeletes;
    use \Astrotomic\Translatable\Translatable;

    protected $fillable = [
    ];

    public $translatedAttributes = [
        'label'
    ];

    protected static function boot()
    {
        parent::boot();

        self::deleted(function (self $level) {
            CandidateLanguageLevel::query()
                ->where('level_id', $level->getKey())
                ->delete();
        });

        self::restored(function (self $level) {
            CandidateLanguageLevel::query()
                ->where('level_id', $level->getKey())
                ->restore();
        });
    }

    public function languages(): BelongsToMany
    {
        return $this->belongsToMany(
            Language::class,
            'candidate_language_level',
            'level_id',
            'language_id'
        );
    }

    public function candidates(): BelongsToMany
    {
        return $this->belongsToMany(
            Candidate::class,
            'candidate_language_level',
            'level_id',
            'candidate_id',
        );
    }
}
