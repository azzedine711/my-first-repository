# List of recipes
recipes = [
    {
        "name": "Pasta Carbonara",
        "ingredients": ["pasta", "eggs", "bacon", "cheese"],
        "steps": "Boil pasta, cook bacon, mix with eggs and cheese."
    },
    {
        "name": "Omelette",
        "ingredients": ["eggs", "cheese", "onion"],
        "steps": "Beat eggs, cook in pan, add cheese and onion."
    },
    {
        "name": "Salad",
        "ingredients": ["lettuce", "tomato", "cucumber", "olive oil"],
        "steps": "Chop vegetables, mix in a bowl, add olive oil."
    }
]

# Ask the user what ingredients they have
available = input("Enter your available ingredients (comma separated): ").lower().split(",")

# Clean spaces
available = [item.strip() for item in available]

found = False

# Check each recipe
for recipe in recipes:
    if all(item in available for item in recipe["ingredients"]):
        print("\n✅ You can make:", recipe["name"])
        print("Steps:", recipe["steps"])
        found = True

if not found:
    print("\n❌ Sorry, you don't have enough ingredients for a full recipe.")
