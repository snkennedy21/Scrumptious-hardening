from django.urls import path

from meal_plans.views import MealPlanListView, MealPlanDetailView

urlpatterns = [
  path('', MealPlanListView.as_view(), name="show_meal_plans"),
  path('<int:pk>/', MealPlanDetailView.as_view(), name="meal_details")
]
