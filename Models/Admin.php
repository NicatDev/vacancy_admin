<?php

namespace App\Models;

use App\Interfaces\ProfileInterface;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

/**
 * @property int $id
 * @property int $user_id
 * @property string $phone
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property-read \App\Models\User $user
 *
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Admin newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Admin newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Admin query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Admin whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Admin whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Admin wherePhone($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Admin whereUpdatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Admin whereUserId($value)
 *
 * @mixin \Eloquent
 */
class Admin extends Model implements ProfileInterface
{
    use HasFactory;

    protected $fillable = [
        'phone',
        'user_id',
    ];

    protected $with = [
        'user'
    ];

    protected static function booted(): void
    {
        parent::booted();

        static::addGlobalScope('onlyAdminRole', function ($builder) {
            $builder->whereHas('user.roles', function ($query) {
                $query->where('name', \App\Enums\Role::ADMIN);
            });
        });
    }

    public function user(): \Illuminate\Database\Eloquent\Relations\BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function profile(): static
    {
        return $this;
    }
}
