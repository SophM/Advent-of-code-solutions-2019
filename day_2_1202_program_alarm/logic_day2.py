def intcode_program(file):
    f = open(file)
    intcode = [int(i) for i in f.readline().split(",")]
    # other way to get the first line: intcode = f.readlines()[0].split(",")
    f.close()
    # for i in range(0,len(intcode)-1):
    #     if intcode[i] == 99
    print(intcode)


if __name__ == "__main__":
    intcode_program("input_day2.txt")
