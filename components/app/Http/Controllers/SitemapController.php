<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Admin\Page;

class SitemapController extends Controller
{
    public function index()
    {
        $pages = Page::translated()
            ->where('custom_tool_link', null)
            ->where(function($q) {
                $q->where(function($sub) {
                    $sub->where('type', 'tool')->where('tool_status', true);
                })->orWhere(function($sub) {
                    $sub->where('type', 'post')->where('post_status', true);
                })->orWhere(function($sub) {
                    $sub->whereIn('type', ['page', 'home', 'contact', 'report'])->where('page_status', true);
                });
            })
            ->orderBy('id', 'DESC')
            ->get()
            ->toArray();

        return response()->view('sitemap', [
            'pages' => $pages
        ], 200)->header('Content-Type', 'text/xml');
    }
}
