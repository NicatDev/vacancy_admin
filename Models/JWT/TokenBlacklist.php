<?php

namespace App\Models\JWT;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

/**
 * @property int $id
 * @property string $jwt_token_id
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 *
 * @method static \Illuminate\Database\Eloquent\Builder<static>|TokenBlacklist newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|TokenBlacklist newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|TokenBlacklist query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|TokenBlacklist whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|TokenBlacklist whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|TokenBlacklist whereJwtTokenId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|TokenBlacklist whereUpdatedAt($value)
 *
 * @mixin \Eloquent
 */
class TokenBlacklist extends Model
{
    use HasFactory;

    protected $table = 'jwt_token_blacklist';

    protected $fillable = [
        'jwt_token_id',
    ];
}
