from django.shortcuts import render
from rest_framework import viewsets, mixins, status

from core.models import Recipe, Tag, Ingredient
from . serializers import RecipeSerializer, TagSerializer, IngredientSerializer, RecipeImageSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . permissions import UpdateOwnRecipe, UpdateOwnTag, UpdateOwnIngredient

from rest_framework.decorators import action
from rest_framework.response import Response



class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnRecipe, IsAuthenticated]


    def get_serializer_class(self):
        if self.action == 'list':
            return RecipeSerializer
        
        elif self.action == 'upload_image':
            return RecipeImageSerializer
        
        return self.serializer_class


    def perform_create(self, serializer):
        """Sets the user to logged in user"""
        serializer.save(user = self.request.user)
    

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to recipe."""
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class TagViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnTag, IsAuthenticated]


class IngredientViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnIngredient, IsAuthenticated]