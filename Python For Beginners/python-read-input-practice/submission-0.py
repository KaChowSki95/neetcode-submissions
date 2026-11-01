def add_two_numbers() -> int:
    user = input().split(",")
    temp = []
    for i in user:
        temp.append(int(i))
    return sum(temp)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
