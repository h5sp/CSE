# notes for the odd
# old_number = ['1', '3', '5', '7', '9']
# list_num = list(old_number)
# for index in range(len(old_number)):
# list_num[index] = int(list_num[index])


def valid_card_number(num: str):

    print(valid_card_number("6702036322882470"))


string = 6702036322882470


def remove(string):
    string2 = (string[:-1])
    print(string2)
    print(string2[::-1])


remove("6702036322882470")

odd_number = ['1', '3', '5', '7', '9']
list_num = list(odd_number)
for index in range(len(odd_number)):
    list_num[index] = int(list_num[index])
