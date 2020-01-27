def intcode_program(file):
    f = open(file)
    intcode = [int(i) for i in f.readline().split(",")]
    # other way to transform the first line into an array of integers
    # intcode = f.readlines()[0].split(",")
    f.close()
    for i in range(0,len(intcode)-1, 4):
        if intcode[i] == 99:
            break
        elif intcode[i] == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        elif intcode[i] == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
    print(intcode[0])


if __name__ == "__main__":
    intcode_program("input_day2.txt")
