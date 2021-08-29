import math
import pyfiglet

# Create a variable of your favorite car brand.
favorite = "chevy"

# Create a list of 5 of their models from cheapest to most expensive.
chevyCars = ["Equinox", "Trailblazer", "Silverado", "Tahoe", "Suburban"]

# Append a 6ht model to the list
chevyCars.append("Spark")

# Create list of 5 standard colors for all models.
standardColors = ["Green", "Blue", "Red", "Black", "Silver"]

# Replace your last color with a different color.
standardColors[4] = "Purple"

# Create a variable of the current new year models
currentYear = 2021

# Create MSRP constant number of each of the models
priceEquinox = 23_000
priceTrailblazer = 19_000
priceSilverado = 29_300
priceTahoe = 49_600
priceSuburban = 52_000
priceSpark = 13_600

# Create a constant number (not string) for total months in 4yr, 5yr, and 6yr loans.
loansFour = 48
loansFive = 60
loansSix = 72

# Create a variable for the Guest's name. Be courteous in your upcoming messages :)
customerName = input("Please enter your name: ")

# Create a message variable (with f-string) welcoming customer to your new car dealership.
greetingMessage = f"Welcome to The Shady Oaks car dealership Mr/Mrs {customerName}"

# Create an awesome Banner with your dealership however you want to welcome customers
asciiBanner = pyfiglet.figlet_format("Shady Oaks Dealership")

print(asciiBanner)
print(greetingMessage)
