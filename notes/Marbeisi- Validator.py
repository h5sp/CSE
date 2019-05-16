def valid_card_number(num: str):
    print(valid_card_number("6702036322882470"))


string = 6702036322882470


def remove(string):
    string2 = (string[:-1])
    print(string2)
    print(string2[::-1])


remove("6702036322882470")


def multiply(num: str):
    last_num = int(num[0])
    if last_num % 3 == 0:
        return True
    return False


