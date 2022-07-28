def enter_pencil(count=""):
    while True:
        pencil = input()
        if count == "":
            if not pencil.isnumeric():
                print("The number of pencils should be numeric")
            else:
                pencil = int(pencil)
                if pencil == 0:
                    print("The number of pencils should be positive")
                else:
                    if count == "":
                        return pencil
        else:

            if pencil not in ['1', '2', '3']:
                print("Possible values: '1', '2' or '3'")
            else:
                pencil = int(pencil)
                if pencil > count:
                    print("Too many pencils were taken")
                else:
                    return pencil


def enter_first(name_list):
    while True:
        name = input()
        if name in name_list:
            return name
        else:
            print(f"Choose between {name_list[0]} and {name_list[1]}")


def bot_turn(pencils):
    if pencils == 1:
        return 1
    rem = pencils % 4
    x = 1
    if rem == 0:
        x = 3
    elif rem == 3:
        x = 2
    elif rem == 2:
        x = 1
    return x



print('How many pencils will you like to use?')
pencil = enter_pencil()
names = ['John', 'Jack']
print(f'Who will be the first ({names[0]}, {names[1]}):')
first = enter_first(names)
second = names[1] if first == names[0] else names[0]
nextTurn = first

while pencil > 0:
    print("|" * pencil)
    print(f"{nextTurn}'s turn!")
    turn = nextTurn
    if nextTurn == names[0]:
        move = enter_pencil(pencil)
        pencil -= move
    else:
        move = bot_turn(pencil)
        print(move)
        pencil -= move

    nextTurn = second if nextTurn == first else first

print(f"{nextTurn} won!")
