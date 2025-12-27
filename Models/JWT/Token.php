<?php

namespace App\Models\JWT;

use App\Casts\TokenCast;
use App\Contracts\JWT\TokenServiceInterface;
use App\Enums\JWT\TokenType;
use Illuminate\Database\Eloquent\Casts\Attribute;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasOne;
use Illuminate\Support\Carbon;
use Psr\Container\ContainerExceptionInterface;
use Psr\Container\NotFoundExceptionInterface;

/**
 * @property string $id
 * @property string $tokenable_type
 * @property int $tokenable_id
 * @property mixed $token
 * @property Carbon|null $created_at
 * @property Carbon|null $updated_at
 * @property-read mixed $encrypt
 * @property-read \App\Models\JWT\TokenBlacklist|null $isRevoked
 *
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Token newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Token newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Token query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Token whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Token whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Token whereToken($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Token whereTokenableId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Token whereTokenableType($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Token whereUpdatedAt($value)
 *
 * @mixin \Eloquent
 */
class Token extends Model
{
    use HasFactory;

    protected $table = 'jwt_tokens';

    protected $keyType = 'string';

    public $incrementing = false;

    protected $fillable = [
        'id',
        'token',
        'tokenable_id',
        'tokenable_type',
    ];

    protected $hidden = [
        'tokenable_id',
        'tokenable_type',
    ];

    protected $casts = [
        'token' => TokenCast::class,
    ];

    public function isAccessToken(): bool
    {
        return $this->tokenIs(TokenType::ACCESS);
    }

    public function isRefreshToken(): bool
    {
        return $this->tokenIs(TokenType::REFRESH);
    }

    public function tokenIs(TokenType $type): bool
    {
        return $this->token->claims()->get('typ') === $type->value;
    }

    public function isRevoked(): HasOne
    {
        return $this->hasOne(TokenBlacklist::class, 'jwt_token_id', 'id');
    }

    /**
     * @throws ContainerExceptionInterface
     * @throws NotFoundExceptionInterface
     */
    protected function encrypt(): Attribute
    {
        return Attribute::make(
            get: fn (mixed $value, array $attributes) => app()->get(TokenServiceInterface::class)->encrypt(
                $attributes['id'],
                $attributes['tokenable_id'],
                Carbon::parse($attributes['created_at']),
                Carbon::parse($attributes['expires_at']),
                Carbon::parse($attributes['can_be_used_after'])
            )
        );
    }
}
