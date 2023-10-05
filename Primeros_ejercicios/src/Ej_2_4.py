def conv_a_Fahrenheit(celsius):
    return f"{celsius}ºC son {celsius * 1.8 + 32}ºF"


if __name__ == "__main__":
    print(conv_a_Fahrenheit(float(input("Dime una temperatura en ºC: "))))
