from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from meal_plans.models import MealPlan

from recipes.models import Recipe


class MealPlanListView(LoginRequiredMixin, ListView):
  model = MealPlan
  template_name = "meal_plans/list.html"
  context_object_name = "plans"

  def get_queryset(self):
    return MealPlan.objects.filter(owner=self.request.user)


class MealPlanDetailView(LoginRequiredMixin, DetailView):
  model = MealPlan
  template_name = "meal_plans/detail.html"
  context_object_name = "plan"

  def get_queryset(self):
    return MealPlan.objects.filter(owner=self.request.user)

class MealPlanCreateView(LoginRequiredMixin, CreateView):
  model = MealPlan
  template_name = "meal_plans/new.html"
  fields = ["name", "recipes"]

  def form_valid(self, form):
    plan = form.save(commit=False)
    plan.owner = self.request.user
    plan.save()
    form.save_m2m()
    return redirect("meal_plan_details", pk=plan.id)

class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
  model = MealPlan
  template_name = "meal_plans/edit.html"
  fields = ["name", "recipes"]

  def get_queryset(self):
    return MealPlan.objects.filter(owner=self.request.user)

  def get_success_url(self) -> str:
    return reverse_lazy("meal_plan_details", args=[self.object.id])

class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
  model = MealPlan
  template_name = "meal_plans/delete.html"
  success_url = reverse_lazy("show_meal_plans")
  context_object_name = "plan"

  def get_queryset(self):
    return MealPlan.objects.filter(owner=self.request.user)