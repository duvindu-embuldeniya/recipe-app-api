from django.urls import path, include
from . views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('recipe', RecipeViewSet)
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)


urlpatterns = [
    path('', include(router.urls)),
]