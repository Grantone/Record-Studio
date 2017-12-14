from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import tags


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^studio/(\d+)', views.studio, name='studio'),
    url(r'^image/$', views.images, name='image'),
    url(r'^tags/$', views.tag, name='tags'),
    url(r'^categories/(\d+)', views.categories, name='categories'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
