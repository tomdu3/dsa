my_menu = {
  'lasagna': 14.75,
  'moussaka': 21.15,
  'sushi': 16.05,
  'paella': 21,
  'samosas': 14
}

# Correct the mistake
for key, value in my_menu.items():
    # Correct the mistake
    print(f"The price of the {key} is {value}.")


# Iterate the elements of the menu
for dish, values in my_menu.items():
    # Print whether the dish must be served cold or hot
    print(f"{dish.title()} is best served {values['best_served']}.")
