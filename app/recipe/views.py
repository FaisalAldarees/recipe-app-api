
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from core.models import (
    Tag,
    Ingredient,
    Recipe,
)

from recipe import serializers


class TagListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self,):
        return self.queryset.filter(user=self.request.user).order_by("-name")

    def perform_create(
        self, serializer,
    ):
        serializer.save(user=self.request.user)


class IngredientListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

    def get_queryset(self,):
        return self.queryset.filter(user=self.request.user).order_by("-name")

    def perform_create(
        self, serializer,
    ):
        serializer.save(user=self.request.user)


class RecipeListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self,):
        tags = self.request.query_params.get('tags')
        ingredients = self.request.query_params.get('ingredients')
        queryset = self.queryset
        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)

        if ingredients:
            ingredients_id = self._params_to_ints(ingredients)
            queryset = queryset.filter(ingredients__id__in=ingredients_id)

        return queryset.filter(user=self.request.user)

    def perform_create(
        self, serializer,
    ):
        serializer.save(user=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    # lookup_field = 'name'
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self,):
        return self.queryset.filter(user=self.request.user)
