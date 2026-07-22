#Data type
print("*****Data Types in Python*****")
print(type("Hello, World!"))
print(type(42))

#Multi-line variable.
print("*****Multi-line variable*****")
cooking_instructions = """Store the multi-line cooking instructions
Step 1: Boil water in a large pot
Step 2: Add pasta and cook for 10 minutes
Step 3: Drain and serve with sauce"""

print(cooking_instructions)

#Replace and lower.
print("*****Replace and Lower*****")
pasta_type = "pasta"
pasta_type = pasta_type.replace("pasta", "fusilli pasta")

ingredient_one = "BASIL"
ingredient_one = ingredient_one.lower()

#List
print("*****List*****")
ingredients = ["tomatoes", "garlic", "olive oil", "basil", "parmesan cheese"]
print(ingredients)
print(ingredients[2])
print(ingredients[-1]) #Last item in the list
print(ingredients[1:4]) #Slicing the list
print(len(ingredients)) #Length of the list
print(ingredients[3:]) #Slicing the list from index 3 to the end
print(ingredients[:3]) #Slicing the list from the start to index 3
print(ingredients[::2]) #Slicing the list with a step of 2
print(ingredients[1::2]) #Slicing the list with a step of 2 starting from index 1

#Dictionary
print("*****Dictionary*****")
recipe = {
    "name": "Pasta Primavera",
    "ingredients": ingredients,
    "prep_time": 20
}
print(recipe)
print(recipe["name"])
print(recipe.values()) # Print all values in the dictionary
print(recipe.keys()) # Print all keys in the dictionary
print(recipe.items()) # Print all key-value pairs in the dictionary
recipe["name"] = "Pasta alla Carbonara" #Add a new key-value pair to the dictionary
print(recipe)
#Add a new key-value pair to the dictionary
recipe["cooking_time"] = 15
print(recipe)

#Sets - A set is a collection of unique elements. It is unordered and does not allow duplicate values.
print("*****Sets*****")
unique_ingredients = {"tomatoes", "garlic", "olive oil", "basil", "parmesan cheese"} 
print(sorted(unique_ingredients)) # Print the set in sorted order
unique_ingredients.add("salt") # Add a new element to the set
unique_ingredients = set(ingredients) # Convert the list to a set to remove duplicates
print(unique_ingredients)

#Tuples - Cannot be changed after creation, unlike lists.
print("*****Tuples*****")
pasta_types = ("fusilli", "penne", "spaghetti")
print(pasta_types[2])

#Loops
print("*****Loops*****")
for x in ingredients:
    print(x)

for item, value in recipe.items():
    print(item, ":", value, ".")

for i in range(1, 6):
    print(i)

#Whie loop
print("*****While Loop*****")
ingredients_to_add = 5
items_added = 0
while items_added < ingredients_to_add:
    items_added += 1
    remaining_items = ingredients_to_add - items_added
    print(remaining_items, "items remaining to add.")

#In
print("*****In*****")
if "basil" in ingredients:
    print("Basil is in the ingredients list.")

#Appending
print("*****Appending*****")
shopping_list = []
for ingredient, qty_needed in recipe.items():
     if ingredient not in ["name", "prep_time"]:
        shopping_list.append(ingredient)
print("Shopping List:", shopping_list)