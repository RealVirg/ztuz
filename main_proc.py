import field

print("enter_size_1")

size_1 = int(input())

print("enter_size_2")

size_2 = int(input())

f = field.Field(size_1, size_2)

print(f)

while f.count_empty > 0 or not f.end or f.create_puzzle:
    command = input()
    if command == "clear":
        arg = input().split(" ")
        f.clear_value(int(arg[0]), int(arg[1]))
    elif command == "put":
        arg = input().split(" ")
        f.put_value(int(arg[0]), int(arg[1]), int(arg[2]))
    elif command == "start puzzle":
        f.start_puzzle()
    f.check_end()
    print(f)

