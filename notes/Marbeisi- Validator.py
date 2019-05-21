def validate(num: str):
    print(validate("6702036322882470"))


string = 6702036322882470


def remove(string):
    print("1.")
    string2 = (string[:-1])
    print(string2)
    print("-----------")
    print("2.")

    print(string2[::-1])


remove("6702036322882470")

print("-----------")

print("3.")


def multiply(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False
