<section id="tools-box">
  @if ( !empty($tool_with_categories) )
      @foreach ($tool_with_categories as $key => $value)

        @if ( $page->ads_status && $advertisement->area3_status && $advertisement->area3 != null )
          <x-public.advertisement.area3 :advertisement="$advertisement" />
        @endif

        <div class="card mb-3">
            <div class="d-block card-header category-box text-{{ $value['align'] }} {{ ($value['background'] !== 'bg-white') ? $value['background'] . ' text-white' : 'bg-transparent' }}">
                <h3 class="card-title" id="{{ \Illuminate\Support\Str::slug($value['title'], '-') }}">
                  <a href="#{{ \Illuminate\Support\Str::slug($value['title'], '-') }}" title="{{ __($value['title']) }}">{{ __($value['title']) }}</a>
                </h3>
                <span>{{ __($value['description']) }}</span>
            </div>
            <div class="card-body pb-0">
                <div class="row">
                    @foreach ($value['pages'] as $key2 => $value2)
                    <div class="col-12 col-md-6 col-lg-4 mb-3">
                        <a class="card text-decoration-none cursor-pointer item-box" href="{{ (empty($value2['custom_tool_link'])) ? route('home') . '/' . $value2['slug'] : $value2['custom_tool_link'] }}" target="{{ $value2['target'] }}">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                      @if ( $general->icon_before_tool_name_status )
                                        <img class="avatar me-3 bg-transparent {{ ($general->lazy_loading) ? 'lazyload' : '' }}" data-src="{{ ($value2['icon_image']) ? $value2['icon_image'] : asset('assets/img/no-thumb.svg') }}" @if (!$general->lazy_loading) src="{{ ($value2['icon_image']) ? $value2['icon_image'] : asset('assets/img/no-thumb.svg') }}" @endif alt="{{ $value2['title'] }}">
                                      @endif
                                      <div class="fw-medium">{{ $value2['title'] }}</div>
                                </div>
                            </div>
                        </a>
                    </div>
                    @endforeach
                </div>
            </div>
        </div>
      @endforeach

  @else

    @if ( $page->ads_status && $advertisement->area3_status && $advertisement->area3 != null )
      <x-public.advertisement.area3 :advertisement="$advertisement" />
    @endif
    
    <div class="row">
        @foreach ($tools as $key => $value)
        <div class="col-12 col-md-6 col-lg-4 mb-3">
            <a class="card text-decoration-none cursor-pointer item-box" href="{{ ( empty( $value['custom_tool_link'] ) ) ? route('home') . '/' . $value['slug'] : $value['custom_tool_link'] }}" target="{{ $value['target'] }}">
                <div class="card-body">
                    <div class="d-flex align-items-center">
                        <img class="avatar me-3 bg-transparent {{ ($general->lazy_loading) ? 'lazyload' : '' }}" data-src="{{ ($value['icon_image']) ? $value['icon_image'] : asset('assets/img/no-thumb.svg') }}" @if (!$general->lazy_loading) src="{{ ($value['icon_image']) ? $value['icon_image'] : asset('assets/img/no-thumb.svg') }}" @endif alt="{{ $value['title'] }}">
                        <div>
                            <div class="fw-medium">{{ $value['title'] }}</div>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        @endforeach
    </div>
  @endif
</section>


<!-- Section: Latest Editorial Guides & Tech Insights -->
@if ( !empty($home_recent_posts) && count($home_recent_posts) > 0 )
<section id="latest-guides" class="mt-5 mb-4">
    <div class="d-flex align-items-center justify-content-between mb-4 flex-wrap gap-2">
        <div>
            <span class="badge bg-primary text-white px-3 py-1 rounded-pill mb-2" style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px;">Editorial Insights</span>
            <h2 class="h3 fw-bold mb-1">Latest Tech & Web Development Guides</h2>
            <p class="text-muted small mb-0">Expert articles, pillar guides, and tutorials from the LinkeFly Editorial Team.</p>
        </div>
        <a href="{{ route('home') }}/blog" class="btn btn-outline-primary rounded-pill px-4">
            {{ __('View All Guides') }} <i class="ti ti-arrow-right ms-1"></i>
        </a>
    </div>

    <div class="row">
        @foreach (array_slice($home_recent_posts, 0, 6) as $post)
        <div class="col-lg-4 col-md-6 mb-4">
            <div class="card h-100 shadow-sm border-0 overflow-hidden" style="transition: transform 0.2s ease;">
                <div class="position-relative overflow-hidden" style="height: 180px;">
                    <a href="{{ route('home') . '/blog/' . ($post['slug'] ?? '') }}">
                        <img class="w-100 h-100 {{ ($general->lazy_loading) ? 'lazyload' : '' }}" style="object-fit: cover;" {{ ($general->lazy_loading ) ? 'data-' : '' }}src="{{ !empty($post['featured_image']) ? $post['featured_image'] : asset('assets/img/no-thumb.svg') }}" alt="{{ $post['title'] ?? '' }}">
                    </a>
                </div>
                <div class="card-body d-flex flex-column p-4">
                    <div class="text-muted small mb-2 d-flex align-items-center gap-2" style="font-size: 0.78rem;">
                        <span><i class="far fa-calendar-alt me-1 text-primary"></i>{{ !empty($post['updated_at']) ? \Carbon\Carbon::parse($post['updated_at'])->format('M d, Y') : 'Recent' }}</span>
                        <span>•</span>
                        <span><i class="far fa-clock me-1 text-primary"></i>5 min read</span>
                    </div>
                    <h3 class="h6 fw-bold mb-2 flex-grow-0">
                        <a href="{{ route('home') . '/blog/' . ($post['slug'] ?? '') }}" class="text-dark text-decoration-none">
                            {{ \Illuminate\Support\Str::limit($post['title'] ?? '', 65) }}
                        </a>
                    </h3>
                    <p class="text-secondary small flex-grow-1 mb-3" style="line-height: 1.5;">
                        {{ \Illuminate\Support\Str::limit($post['short_description'] ?? '', 100) }}
                    </p>
                    <div class="mt-auto pt-2 border-top">
                        <a href="{{ route('home') . '/blog/' . ($post['slug'] ?? '') }}" class="btn btn-sm btn-link text-primary p-0 fw-semibold text-decoration-none">
                            {{ __('Read Full Guide') }} <i class="ti ti-chevron-right text-xs"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        @endforeach
    </div>
</section>
@endif

<!-- Section: Why Choose LinkeFly / Platform Features -->
<section id="why-choose-us" class="card shadow-sm border-0 mb-4 p-4 p-md-5">
    <div class="text-center mb-5">
        <span class="badge bg-primary text-white px-3 py-1 rounded-pill mb-2" style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px;">Why LinkeFly</span>
        <h2 class="h3 fw-bold mb-2">Designed for Speed, Security & Simplicity</h2>
        <p class="text-muted mx-auto" style="max-width: 650px;">LinkeFly is built from the ground up to offer the most reliable, client-side, and privacy-focused suite of online developer and productivity tools.</p>
    </div>

    <div class="row g-4">
        <div class="col-md-6 col-lg-3">
            <div class="p-3 text-center rounded bg-light h-100">
                <div class="avatar avatar-md bg-primary text-white rounded-circle mb-3 mx-auto d-flex align-items-center justify-content-center">
                    <i class="fas fa-bolt fa-lg"></i>
                </div>
                <h3 class="h6 fw-bold mb-2">100% Free Forever</h3>
                <p class="text-muted small mb-0">All 150+ web utilities, encoders, converters, and calculators are accessible free with zero hidden limits or subscriptions.</p>
            </div>
        </div>

        <div class="col-md-6 col-lg-3">
            <div class="p-3 text-center rounded bg-light h-100">
                <div class="avatar avatar-md bg-success text-white rounded-circle mb-3 mx-auto d-flex align-items-center justify-content-center">
                    <i class="fas fa-shield-alt fa-lg"></i>
                </div>
                <h3 class="h6 fw-bold mb-2">Zero-Logging Privacy</h3>
                <p class="text-muted small mb-0">Your sensitive data, strings, codes, and files are processed strictly in your browser or through ephemeral memory. No data is stored.</p>
            </div>
        </div>

        <div class="col-md-6 col-lg-3">
            <div class="p-3 text-center rounded bg-light h-100">
                <div class="avatar avatar-md bg-info text-white rounded-circle mb-3 mx-auto d-flex align-items-center justify-content-center">
                    <i class="fas fa-tachometer-alt fa-lg"></i>
                </div>
                <h3 class="h6 fw-bold mb-2">Instant Results</h3>
                <p class="text-muted small mb-0">Engineered with modern algorithms and minified execution to guarantee lightning-fast conversions in under 50 milliseconds.</p>
            </div>
        </div>

        <div class="col-md-6 col-lg-3">
            <div class="p-3 text-center rounded bg-light h-100">
                <div class="avatar avatar-md bg-warning text-white rounded-circle mb-3 mx-auto d-flex align-items-center justify-content-center">
                    <i class="fas fa-mobile-alt fa-lg"></i>
                </div>
                <h3 class="h6 fw-bold mb-2">Cross-Platform Ready</h3>
                <p class="text-muted small mb-0">Flawlessly responsive on desktops, tablets, and smartphones. Works directly in any standard browser without extensions.</p>
            </div>
        </div>
    </div>
</section>

<!-- Section: Frequently Asked Questions (FAQ) -->
<section id="faq-section" class="card shadow-sm border-0 mb-4 p-4 p-md-5">
    <div class="mb-4">
        <span class="badge bg-primary text-white px-3 py-1 rounded-pill mb-2" style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px;">Help & FAQs</span>
        <h2 class="h3 fw-bold mb-1">Frequently Asked Questions</h2>
        <p class="text-muted small mb-0">Everything you need to know about using LinkeFly tools and resources.</p>
    </div>

    <div class="accordion" id="linkeflyFAQ">
        <div class="accordion-item border-0 mb-3 bg-light rounded overflow-hidden">
            <h2 class="accordion-header" id="faqHeadingOne">
                <button class="accordion-button bg-light fw-bold text-dark shadow-none" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapseOne" aria-expanded="true" aria-controls="faqCollapseOne">
                    What is LinkeFly and who is it designed for?
                </button>
            </h2>
            <div id="faqCollapseOne" class="accordion-collapse collapse show" aria-labelledby="faqHeadingOne" data-bs-parent="#linkeflyFAQ">
                <div class="accordion-body text-secondary small pt-0" style="line-height: 1.6;">
                    LinkeFly is an open-access digital utility platform featuring over 150 dedicated online tools for web developers, software engineers, content creators, digital marketers, and everyday web users. Our utilities range from code minifiers, formatters, and cryptographic hash generators to image converters, SEO slug generators, and financial calculators.
                </div>
            </div>
        </div>

        <div class="accordion-item border-0 mb-3 bg-light rounded overflow-hidden">
            <h2 class="accordion-header" id="faqHeadingTwo">
                <button class="accordion-button collapsed bg-light fw-bold text-dark shadow-none" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapseTwo" aria-expanded="false" aria-controls="faqCollapseTwo">
                    Are the tools on LinkeFly completely free to use?
                </button>
            </h2>
            <div id="faqCollapseTwo" class="accordion-collapse collapse" aria-labelledby="faqHeadingTwo" data-bs-parent="#linkeflyFAQ">
                <div class="accordion-body text-secondary small pt-0" style="line-height: 1.6;">
                    Yes, 100% of the tools and guides on LinkeFly are completely free to use. There are no paid tiers, hidden subscriptions, or premium paywalls. You can use any tool as many times as you need without providing any credit card or registration details.
                </div>
            </div>
        </div>

        <div class="accordion-item border-0 mb-3 bg-light rounded overflow-hidden">
            <h2 class="accordion-header" id="faqHeadingThree">
                <button class="accordion-button collapsed bg-light fw-bold text-dark shadow-none" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapseThree" aria-expanded="false" aria-controls="faqCollapseThree">
                    Is my data and code secure when using LinkeFly?
                </button>
            </h2>
            <div id="faqCollapseThree" class="accordion-collapse collapse" aria-labelledby="faqHeadingThree" data-bs-parent="#linkeflyFAQ">
                <div class="accordion-body text-secondary small pt-0" style="line-height: 1.6;">
                    Security and user privacy are fundamental pillars of LinkeFly. Most of our tools execute directly inside your browser using client-side JavaScript, meaning your data never even touches our servers. For operations requiring server-side rendering, data is processed in ephemeral memory and discarded immediately with zero logs retained.
                </div>
            </div>
        </div>

        <div class="accordion-item border-0 bg-light rounded overflow-hidden">
            <h2 class="accordion-header" id="faqHeadingFour">
                <button class="accordion-button collapsed bg-light fw-bold text-dark shadow-none" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapseFour" aria-expanded="false" aria-controls="faqCollapseFour">
                    Do I need to install any software or browser extensions?
                </button>
            </h2>
            <div id="faqCollapseFour" class="accordion-collapse collapse" aria-labelledby="faqHeadingFour" data-bs-parent="#linkeflyFAQ">
                <div class="accordion-body text-secondary small pt-0" style="line-height: 1.6;">
                    No installation or browser extension is required. LinkeFly operates entirely through standard web protocols across modern browsers like Chrome, Firefox, Safari, Edge, and mobile browsers. Simply bookmark the website or specific tool page to access it instantly anytime.
                </div>
            </div>
        </div>
    </div>
</section>
