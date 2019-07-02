print("Hello world")

name = input("What's your name? ")
print("Hello, %s!" %(name)) # percent is also a format specifier

animal = input("Dogs or Cats? ")

if animal == "Dogs" or animal == "dogs":
    print("Yay!" , name, ", I agree, dogs are the best.")
else:
    print("Dogs are better.")
