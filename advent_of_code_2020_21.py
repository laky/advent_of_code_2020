def get_possible_alergen_words(ingredients, alergens):
  alergens_to_ingredients = dict()
    
  for i, ings in enumerate(ingredients):
    for al in alergens[i]:
      if al in alergens_to_ingredients:
        alergens_to_ingredients[al] = alergens_to_ingredients[al].intersection(ings)
      else:
        alergens_to_ingredients[al] = set(ings)
  return alergens_to_ingredients
    
  for a, al in enumerate(alergens):
    1+1


test="""mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".split("\n")

with open("input_21.txt", "r") as f:
  foods = [line.strip() for line in f]
  ingredients = [food.split(" (contains ")[0].split(" ") for food in foods]
  alergens = [food.split(" (contains ")[1][:-1].split(", ") for food in foods]

  print(ingredients, alergens)
  alergens_to_ingredients = get_possible_alergen_words(ingredients, alergens)
  print([ (key, len(item)) for key, item in alergens_to_ingredients.items() ])
  alergens_to_unique_ingredients = dict()
  while len(alergens_to_ingredients.items()) > 0:
    for al, ings in alergens_to_ingredients.items():
      if (len(ings) == 1):
        ing = ings.pop()
        alergens_to_unique_ingredients[al] = ing
        for al_2, ings_2 in alergens_to_ingredients.items():
          if ing in ings_2:
            ings_2.remove(ing)
        del alergens_to_ingredients[al]
        break
  print(alergens_to_unique_ingredients)
  
  counter = 0
  for ings in ingredients:
    for ing in ings:
      if ing not in alergens_to_unique_ingredients.values():
        counter += 1
        
  print("Part 1:", counter)
  
  al_ings = [(al, ing) for (al, ing) in alergens_to_unique_ingredients.items()]
  al_ings.sort()
  print(al_ings)
  print("Part 2:", ",".join([ ing for _, ing in al_ings ]))
