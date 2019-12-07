import math


def fuel_counter_upper(file):
    f = open(file, "r")
    fuel_total = 0
    for line in f:
        fuel_total = fuel_total + (math.floor(int(line)/3) - 2)
    f.close()
    print(fuel_total)


if __name__ == "__main__":
   fuel_counter_upper("input_day1.txt")