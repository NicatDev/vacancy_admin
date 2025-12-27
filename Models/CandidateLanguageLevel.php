<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\SoftDeletes;

/**
 * @property int $id
 * @property int $candidate_id
 * @property int $language_id
 * @property int $level_id
 * @property \Illuminate\Support\Carbon|null $deleted_at
 * @property-read \App\Models\Candidate $candidate
 * @property-read \App\Models\Language $language
 * @property-read \App\Models\Level $level
 *
 * @method static \Database\Factories\CandidateLanguageLevelFactory factory($count = null, $state = [])
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel onlyTrashed()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel whereCandidateId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel whereDeletedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel whereLanguageId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel whereLevelId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel withTrashed(bool $withTrashed = true)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateLanguageLevel withoutTrashed()
 *
 * @mixin \Eloquent
 */
class CandidateLanguageLevel extends Model
{
    use HasFactory;
    use SoftDeletes;

    protected $table = 'candidate_language_level';

    protected $fillable = [
        'candidate_id',
        'language_id',
        'level_id',
    ];

    public function language(): BelongsTo
    {
        return $this->belongsTo(Language::class);
    }

    public function level(): BelongsTo
    {
        return $this->belongsTo(Level::class);
    }

    public function candidate(): BelongsTo
    {
        return $this->belongsTo(Candidate::class);
    }
}
