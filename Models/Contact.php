<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Contact extends Model
{
    protected $fillable = [
        'fullname',
        'email',
        'question',
        'comment',
        'read_by',
        'read_at',
    ];

    protected $casts = [
        'read_at' => 'datetime',
        'read_by' => 'integer',
    ];

    public function markAsRead(User $user): true
    {
        return $this->update([
            'read_at' => now(),
            'read_by' => $user->getKey()
        ]);
    }


    public function isRead(): bool
    {
        return false === is_null($this->getAttribute('read_at'));
    }

    public function reader(): BelongsTo
    {
        return $this->belongsTo(
            User::class,
            'read_by',
            'id',
        );
    }
}
