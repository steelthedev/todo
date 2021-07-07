from django.urls import path
from django.urls.conf import include
from . import views 
from rest_framework import routers


router = routers.DefaultRouter()
router.register('heroes', views.HeroViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]