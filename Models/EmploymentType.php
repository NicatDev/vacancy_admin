<?php

namespace App\Models;

use Astrotomic\Translatable\Contracts\Translatable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class EmploymentType extends Model implements Translatable
{
    use HasFactory;
    use SoftDeletes;
    use \Astrotomic\Translatable\Translatable;

    protected $fillable = [
    ];

    public $translatedAttributes = [
        'name'
    ];
}
