
from django import template

register = template.Library()


# def resize_to(value, arg):
#     print("value:", value)
#     print("arg:", arg)
#     print(type(value.recipe.servings))
#     print(type(arg))
#     return "resize done"


def resize_to(ingredient, target):
  servings = ingredient.recipe.servings
  if servings != None and target != None:
    ratio = int(target) / int(servings)
    return ratio * ingredient.amount
  return ingredient


register.filter(resize_to)