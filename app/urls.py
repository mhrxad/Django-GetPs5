import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from app import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views

from app.sitemap import StaticsPage

sitemaps = {
    "StaticsPage": StaticsPage,
    # "ProductList": ProductList,
    # "PostList": PostList,
}

urlpatterns = [

    path('', include("home_app.urls")),
    path('', include("account_app.urls")),
    path('', include("aboutus_app.urls")),
    path('', include("privacy_app.urls")),
    path('', include("contactus_app.urls")),
    path('', include("faq_app.urls")),


    path('admin/', admin.site.urls),
    path('ckeditor', include("ckeditor_uploader.urls")),

    path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('__debug__/', include(debug_toolbar.urls)),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
