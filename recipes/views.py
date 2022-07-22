from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from recipes.forms import RatingForm
from recipes.models import Ingredient, Recipe, ShoppingItem


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                rating = form.save(commit=False)
                rating.recipe = recipe
                rating.save()
            except Recipe.DoesNotExist:
                return redirect("recipes_list")
    return redirect("recipe_detail", pk=recipe_id)

def resize(request, recipe_id):
    pass

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    paginate_by = 2


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        shopping_list = []
        for item in self.request.user.shopping_items.all():
            shopping_list.append(item.food_item)

        context["servings"] = self.request.GET.get("servings")

        context["shopping_list"] = shopping_list
        return context



class RecipeCreateView(CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ["name", "description", "image", 'servings']
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "author", "description", "image", 'servings']
    success_url = reverse_lazy("recipes_list")


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")

User = get_user_model()
users = User.objects.all()
class UserListView(ListView):
    model = User
    template_name = "recipes/users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = users
        return context


############## Shopping Cart Views ###################

def create_shopping_item(request):
    ingredient_id = request.POST.get("ingredient_id")
    ingredient = Ingredient.objects.get(id=ingredient_id)
    user = request.user

    try:
        ShoppingItem.objects.create(food_item=ingredient.food, user=user)

    except IntegrityError:
        print("Integrity Error")

    return redirect(
        "recipe_detail", pk=ingredient.recipe.id
    )



def delete_all_shopping_items(request):
    user = request.user
    ShoppingItem.objects.filter(user=user).delete()

    return redirect("shopping_list")



class ShoppingCartListView(ListView):
    model = ShoppingItem
    template_name = "cart/list.html"
    context_object_name = "carts"