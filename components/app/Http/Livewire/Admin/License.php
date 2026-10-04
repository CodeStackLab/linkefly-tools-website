<?php

namespace App\Http\Livewire\Admin;

use Artesaos\SEOTools\Facades\SEOMeta;
use Livewire\Component;

class License extends Component
{
    public function render()
    {
        $title = __('License') . ' ' . env('APP_SEPARATOR') . ' ' . env('APP_NAME');
        SEOMeta::setTitle($title);

        return view('livewire.admin.license')->layout('layouts.admin', [
            'breadcrumbs' => [
                ['title' => __( 'Admin' ), 'url' => route('admin.dashboard.index')],
                ['title' => __( 'License' ), 'url' => null]
            ]
        ]);
    }
}
