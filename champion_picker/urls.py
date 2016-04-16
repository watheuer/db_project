from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'api/champions', views.ChampionViewSet)
router.register(r'api/roles', views.RoleViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^api/champions/(?P<champion_id>[0-9]+)$', views.detail, name='detail'),
    # url(r'^api/champions$', views.all, name='all'),
    # url(r'^api/roles/(?P<role_id>[0-9]+)$', views.role, name='role'),
    # url(r'^api/roles/(?P<role_id>[0-9]+)/matchups$', views.matchups, name='matchups'),
    # url(r'^api/roles/(?P<role_id>[0-9]+)/builds$', views.builds, name='builds'),
    # url(r'^api/items$', views.items, name='items')
]

urlpatterns += router.urls
