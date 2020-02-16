def intcode_program(file):
    f = open(file)
    intcode = [int(i) for i in f.readline().split(",")]
    # other way to transform the first line into an array of integers
    # intcode = f.readlines()[0].split(",")
    f.close()
    for i in range(0,99):
        intcode[1] = i
        for j in range(0,99):
            intcode[2] = j
            for k in range(0,len(intcode)-1, 4):
                if intcode[k] == 99:
                    break
                elif intcode[k] == 1:
                    intcode[intcode[k+3]] = intcode[intcode[k+1]] + intcode[intcode[k+2]]
                elif intcode[k] == 2:
                    intcode[intcode[k+3]] = intcode[intcode[k+1]] * intcode[intcode[k+2]]
            
            if intcode[0] == 19690720:
                print(intcode[0])
                total = 100 * i + j
                print("total = ", total)

            f = open(file)
            intcode = [int(i) for i in f.readline().split(",")]
            f.close()
            intcode[1] = i
    


if __name__ == "__main__":
    intcode_program("input_day2.txt")