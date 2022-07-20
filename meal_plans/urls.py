from django.urls import path

from meal_plans.views import MealPlanListView, MealPlanDetailView, MealPlanUpdateView, MealPlanCreateView, MealPlanDeleteView

urlpatterns = [
  path('', MealPlanListView.as_view(), name="show_meal_plans"),
  path('<int:pk>/', MealPlanDetailView.as_view(), name="meal_plan_details"),
  path('<int:pk>/edit', MealPlanUpdateView.as_view(), name="meal_plan_edit"),
  path('create/', MealPlanCreateView.as_view(), name="meal_plan_create"),
  path('<int:pk>/delete', MealPlanDeleteView.as_view(), name="meal_plan_delete")
]
