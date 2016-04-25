from db_project import settings
from django.conf.urls import url, patterns
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'api/champions', views.ChampionViewSet)
router.register(r'api/roles', views.RoleViewSet)
router.register(r'api/items', views.ItemViewSet)
router.register(r'api/builds', views.BuildViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'builder$', views.builder, name='builder')
]

urlpatterns += router.urls


urlpatterns += patterns('',url(r'^(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT,
}))
