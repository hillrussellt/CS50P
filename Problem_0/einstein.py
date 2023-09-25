def main():
    prompt = str("Please give me a value for mass in Kilograms ")
    mass = int(input(prompt))
    energytotal = mass * (300000000**2)
    print("An object with mass of", mass, "has",
          energytotal, "joules of energy")


main()
