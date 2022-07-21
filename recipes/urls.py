from django.urls import path

from recipes.views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    log_rating,
    RecipeDetailView,
    RecipeListView,
    UserListView,
    ShoppingCartCreateView,
    ShoppingCartDeleteView,
    ShoppingCartListView
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    path("users/", UserListView.as_view(), name="recipe_users"),
    path("shopping_items/create/", ShoppingCartCreateView.as_view() ,name="shopping_items_create"),
    path("shopping_items/", ShoppingCartListView.as_view() ,name="shopping_items"),
    path("shopping_items/delete/", ShoppingCartDeleteView.as_view() ,name="shopping_items_delete"),
]
