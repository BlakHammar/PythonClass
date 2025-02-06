for i in range(1, 6):
    for j in range(i, 0, -1):
        if j == i: 
            print(f"# {j}", end=" ")
        else:
            print(j, end=" ")
    print()  # Move to the next line after each row
