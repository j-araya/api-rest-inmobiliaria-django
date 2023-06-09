from django.urls import include, path
from rest_framework import routers
from api.views import PropertyViewSet

router = routers.DefaultRouter()
router.register(r'property', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]