from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('case/',  include('case.urls')),
    path('caseworker/', include('caseworker.urls')),

    path('', RedirectView.as_view(url='/caseworker/')),
    path('accounts/login/', RedirectView.as_view(url='/caseworker/')),
    path('admin/login/', RedirectView.as_view(url='/caseworker/')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
