# for i in range(5):
#     for j in range(5):
#         print(f"({i}, {j})", end="")
#         print()

for i in range(1, 6, 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()