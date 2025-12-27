<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Spatie\Permission\Models\Permission;

/**
 * @property int $id
 * @property string $name
 * @property string|null $alias
 * @property \Illuminate\Support\Carbon|null $created_at
 * @property \Illuminate\Support\Carbon|null $updated_at
 * @property-read \Illuminate\Database\Eloquent\Collection<int, Permission> $permissions
 * @property-read int|null $permissions_count
 *
 * @method static \Illuminate\Database\Eloquent\Builder<static>|ModelInfo newModelQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|ModelInfo newQuery()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|ModelInfo query()
 * @method static \Illuminate\Database\Eloquent\Builder<static>|ModelInfo whereAlias($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|ModelInfo whereCreatedAt($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|ModelInfo whereId($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|ModelInfo whereName($value)
 * @method static \Illuminate\Database\Eloquent\Builder<static>|ModelInfo whereUpdatedAt($value)
 *
 * @mixin \Eloquent
 */
class ModelInfo extends Model
{
    protected $fillable = [
        'name',
        'alias',
    ];

    public function permissions(): BelongsToMany
    {
        return $this->belongsToMany(Permission::class);
    }
}
