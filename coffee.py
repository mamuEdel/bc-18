""" Make Tea 
1. Took a cup
2. Placed tea bag in cup
3. Poured milk into cup
4. Added sugar
5. Stirred
6. Ready to serve
"""
 #Make a cup coffee
def coffee_maker(coffe_type):
    if coffe_type == milk:
      print("These are the steps to make coffee")
      print("1. Take a cup")
      print("2. Place a coffee in cup")
      print("3. Pour milk in the cup")
      print("4. Add sugar")
      print("5. Stir")
    elif coffe_type == water:
      print("These are the steps to make coffee")
      print("1. Take a cup")
      print("2. Place a coffee in cup")
      print("3. Pour water in the cup")
      print("4. Add sugar")
      print("5. Stir")
    coffee="Tasty coffee"
    return coffee
def serve_coffee(coffee, person_name):
    serve = "Here's your tasty coffee"
    return serve + person_name
