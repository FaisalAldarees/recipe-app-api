from django.urls import path

from recipe import views


app_name = "recipe"


urlpatterns = [
    path("tags/", views.TagListCreate.as_view(), name="tag"),
    path(
        "ingredients/", views.IngredientListCreate.as_view(), name="ingredient"
    ),
    path(
        "recipes/", views.RecipeListCreate.as_view(), name="recipe_list_create"
    ),
    path(
        "recipes/<int:pk>", views.RecipeDetail.as_view(), name="recipe_detail"
    ),
]
