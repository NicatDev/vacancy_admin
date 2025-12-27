<?php

namespace App\Models;

use App\Interfaces\ProfileInterface;
use Illuminate\Database\Eloquent\Attributes\Scope;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\SoftDeletes;
use Spatie\MediaLibrary\HasMedia;
use Spatie\MediaLibrary\InteractsWithMedia;

/**
 * @property ?User $user
 * @property int $id
 * @property string $name
 * @property int $user_id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property \Illuminate\Support\Carbon|null $deleted_at
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Language>|mixed $languages
 * @property-read int|null $languages_count
 *
 * @method static \Database\Factories\CandidateFactory factory($count = null, $state = [])
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate onlyTrashed()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate whereDeletedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate whereUpdatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate whereUserId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate withTrashed(bool $withTrashed = true)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate withoutTrashed()
 * @method static mixed|\Illuminate\Database\Eloquent\Collection<int, \App\Models\Language> languages()
 *
 * @property string $speciality
 * @property string $summary
 * @property int $salary_expectation
 * @property-read \Illuminate\Database\Eloquent\Collection<int, \App\Models\Skill> $skills
 * @property-read int|null $skills_count
 *
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate whereSalaryExpectation($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate whereSpeciality($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Candidate whereSummary($value)
 *
 * @mixin \Eloquent
 */
class Candidate extends Model implements ProfileInterface, HasMedia
{
    use HasFactory;
    use SoftDeletes;
    use InteractsWithMedia;

    protected $fillable = [
        'user_id',
        'name',
        'summary',
        'speciality',
        'salary_expectation',
    ];

//    protected $with = [
//        'user'
//    ];

    protected static function boot(): void
    {
        parent::boot();

        self::deleted(function ($candidate) {
            CandidateLanguageLevel::query()->where('candidate_id', $candidate->getKey())->delete();
            $candidate->getAttribute('user')->delete();
        });

        self::restored(function ($candidate) {
            CandidateLanguageLevel::query()->where('candidate_id', $candidate->getKey())->restore();
            User::withTrashed()->findOrFail($candidate->getAttribute('user_id'))->restore();
        });
    }

    protected static function booted(): void
    {
        parent::booted();

        static::addGlobalScope('onlyCandidate', function ($builder) {
            $builder->whereHas('user', function ($query) {
                $query->withTrashed()->whereHas('roles', function ($query) {
                    $query->where('name', \App\Enums\Role::CANDIDATE->value);
                });
            });
        });
    }

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function profile(): static
    {
        return $this;
    }

    public function languages(): BelongsToMany
    {
        return $this->belongsToMany(Language::class, 'candidate_language_level');
    }

    public function skills(): BelongsToMany
    {
        return $this->belongsToMany(Skill::class, 'candidate_skill');
    }

    public function services(): BelongsToMany
    {
        return $this->belongsToMany(Service::class, 'candidate_service');
    }

    public function registerMediaCollections(): void
    {
        $this->addMediaCollection('resume')
            ->acceptsMimeTypes(['application/pdf'])
            ->useDisk('resume')
            ->singleFile();

        $this->addMediaCollection('candidate_avatar')
            ->acceptsMimeTypes(['image/png'])
            ->useDisk('candidate_avatar')
            ->singleFile();
    }
}
