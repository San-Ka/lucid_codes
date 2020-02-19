import sys
import getopt
number_of_legs = {"unicorns": 4, "people": 2, "snakes": 0}
animal = input("Leg count for: ")
print(animal.capitalize(), "have", str(number_of_legs[animal]), "legs.")
