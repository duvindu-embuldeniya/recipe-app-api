from django.urls import path, include
from . views import *


from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('profile', UserProfileViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view(), name = 'login'),
]