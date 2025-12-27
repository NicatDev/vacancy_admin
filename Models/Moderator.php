<?php

namespace App\Models;

use App\Interfaces\ProfileInterface;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

/**
 * @property int $id
 * @property int $user_id
 * @property string $full_name
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property-read \App\Models\User $user
 *
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Moderator newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Moderator newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Moderator query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Moderator whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Moderator whereFullName($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Moderator whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Moderator whereUpdatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|Moderator whereUserId($value)
 * @method static \Database\Factories\ModeratorFactory factory($count = null, $state = [])
 *
 * @mixin \Eloquent
 */
class Moderator extends Model implements ProfileInterface
{
    use HasFactory;

    protected $fillable = [
        'full_name',
        'user_id',
    ];

    public function user(): \Illuminate\Database\Eloquent\Relations\BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function profile(): static
    {
        return $this;
    }
}
