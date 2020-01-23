def intcode_program(file):
    f = open(file)
    intcode = f.readline().split(",")
    # other way to get the first line: intcode = f.readlines()[0].split(",")
    f.close()
    print(intcode)


if __name__ == "__main__":
    intcode_program("input_day2.txt")
