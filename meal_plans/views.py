from django.shortcuts import render
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