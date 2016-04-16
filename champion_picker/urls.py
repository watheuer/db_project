from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'api/champions', views.ChampionViewSet)
router.register(r'api/roles', views.RoleViewSet)
router.register(r'api/items', views.ItemViewSet)
router.register(r'api/builds', views.BuildViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns += router.urls
