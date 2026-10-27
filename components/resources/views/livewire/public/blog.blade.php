<div class="row">
  @foreach ($pageTrans as $pageTran)
    <div class="col-lg-4 col-sm-6 mb-4">
      <div class="card h-100 shadow-sm border-0 overflow-hidden" style="transition: transform 0.2s ease, box-shadow 0.2s ease;">
        <div class="card-image position-relative overflow-hidden">
          <a href="{{ route('home') . '/blog/' . $pageTran->slug }}">
            <img class="w-100 {{ ($general->lazy_loading) ? 'lazyload' : '' }}" style="height: 200px; object-fit: cover;" {{ ($general->lazy_loading ) ? 'data-' : '' }}src="{{ ($pageTran->featured_image) ? $pageTran->featured_image : asset('assets/img/no-thumb.svg') }}" alt="{{ $pageTran->title }}">
          </a>
        </div>
        <div class="card-body d-flex flex-column p-4">
          <div class="mb-2">
            <span class="badge bg-primary text-white px-2 py-1 rounded-pill" style="font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Tech Guide</span>
          </div>
          <div class="text-muted small mb-2 d-flex align-items-center flex-wrap gap-2" style="font-size: 0.8rem;">
            <span><i class="far fa-calendar-alt me-1 text-primary"></i>{{ \Carbon\Carbon::parse($pageTran->updated_at ?? $pageTran->created_at)->format('M d, Y') }}</span>
            <span>•</span>
            <span><i class="far fa-user me-1 text-primary"></i>Editorial Team</span>
            <span>•</span>
            <span><i class="far fa-clock me-1 text-primary"></i>5 min read</span>
          </div>
          <h3 class="title h5 mb-2 flex-grow-0">
            <a href="{{ route('home') . '/blog/' . $pageTran->slug }}" class="fw-bold text-dark text-decoration-none" title="{{ $pageTran->title }}" target="{{ $pageTran->target }}">{{ $pageTran->title }}</a>
          </h3>
          <p class="text-secondary small flex-grow-1 mb-3" style="line-height: 1.6;">{{ \Illuminate\Support\Str::limit($pageTran->short_description, 130) }}</p>

          <div class="mt-auto pt-2 border-top">
            <a href="{{ route('home') . '/blog/' . $pageTran->slug }}" class="btn btn-sm btn-outline-primary rounded-pill px-3 py-1 fw-medium" title="{{ $pageTran->title }}" target="{{ $pageTran->target }}">
              {{ __('Read Article') }} <i class="ti ti-chevron-right text-xs ms-1" aria-hidden="true"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  @endforeach

  <div class="d-flex justify-content-center mt-3">
    {{ $pageTrans->links() }}
  </div>
</div>