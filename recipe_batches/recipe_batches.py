#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # result = 100
  # for rkey,rval in recipe.items():
  #   for ikey,ival in ingredients.items():
  #     if rval/ival <= 1:
  #       # We have enough
  #       if math.floor(ival/rval) < result:
  #         result = math.floor(ival/rval)
  #       pass
  #     elif rval/ival > 1:
  #       # We dont have enough
  #       result = 0
  # return result
  min_ratio = math.inf
  for ingredient, amount in recipe.items():
    if ingredient not in ingredients:
      return 0
    ratio = ingredients[ingredient] // amount
    if ratio == 0:
      return 0
    if ratio < min_ratio:
      min_ratio = ratio

  return min_ratio

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))