import math


def fuel_double_checker(file):
    f = open(file, "r")
    fuel_total = 0
    for line in f:
        fuel_module = math.floor(int(line)/3) - 2
        fuel_total = fuel_total + fuel_module
        while (math.floor(fuel_module/3) > 0):
            fuel_module = math.floor(fuel_module/3) - 2
            if (fuel_module > 0):
                fuel_total = fuel_total + fuel_module
    print(fuel_total)


if __name__ == "__main__":
   fuel_double_checker("input_day1.txt")