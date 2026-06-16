from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth
from django.views.static import serve
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('', RedirectView.as_view(url='/blog/'), name='home'),
    #path('blog/login/', user_view.Login, name='login'),
    #path('blog/logout/', auth.LogoutView.as_view(template_name='blog/Main_Page/index.html'), name='logout'),
    #path('blog/register/', user_view.registr, name='registr'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)