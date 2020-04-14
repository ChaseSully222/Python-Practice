# Create an empty set named showroom.

showroom = set()


# Add four of your favorite car model names to the set.

showroom.add("Ferrari")
showroom.add("Lamborghini")
showroom.add("Evo")
showroom.add("Impreza")


# Print the length of your set.

print(len(showroom))

# Pick one of the items in your show room and add it to the set again.

showroom.add("Evo")

# Print your showroom. Notice how there's still only one instance of that model in there.

print(showroom)

# Using update(), add two more car models to your showroom with another set.

showroom.update({"Nissan", "Honda"})
print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.

showroom.discard("Evo")
print(showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"Nissan", "Honda", "Toyota", "Ford", "Tesla"}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.

print(junkyard.intersection(showroom))

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.

showroom = showroom.union(junkyard)
print(showroom)

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
showroom.discard("Ford")
showroom.discard("Tesla")
showroom.discard("Toyota")

print(showroom)