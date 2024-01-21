def print_pattern(num_rows):
    if(num_rows>0):
        for i in range(1, num_rows + 1):
            for j in range(1, i + 1):
                if i % 2 == 0:
                    print("#", end=' ')
                else:
                    print("*", end=' ')
            print()
    else:
        print("Invalid input")
num_rows = int(input("Enter no. of rows:"))
print_pattern(num_rows)