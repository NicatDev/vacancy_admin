<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\SoftDeletes;

class Phone extends Model
{
    use HasFactory;
    use SoftDeletes;

    protected $table = 'company_phone_numbers';

    protected $fillable = [
        'company_id',
        'number',
        'label',
    ];

    public function company(): BelongsTo
    {
        return $this->belongsTo(Company::class);
    }
}
