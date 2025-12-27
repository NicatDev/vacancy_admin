<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class LevelTranslation extends Model
{
    public $timestamps = false;
    protected $fillable = [
        'label'
    ];
}
