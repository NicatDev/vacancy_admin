<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Relations\Pivot;
use Illuminate\Database\Eloquent\SoftDeletes;

/**
 * @property int $id
 * @property int $candidate_id
 * @property int $skill_id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property \Illuminate\Support\Carbon|null $deleted_at
 *
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill onlyTrashed()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill whereCandidateId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill whereDeletedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill whereSkillId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill whereUpdatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill withTrashed(bool $withTrashed = true)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|CandidateSkill withoutTrashed()
 *
 * @mixin \Eloquent
 */
class CandidateSkill extends Pivot
{
    use SoftDeletes;

    protected $table = 'candidate_skill';

    protected $fillable = [
        'candidate_id',
        'skill_id',
    ];
}
