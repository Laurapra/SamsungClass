def menu():
    print("""
    Welcome to Yummy Restaurant, this is the menu:
    1- Burguer (Enter b)
    2- Chicken (Enter c)
    3- Pizza (Enter p)
    """)

    opcion = input("Chose the menu: ")
    if opcion =="B" or opcion=="b": print("You chose burguer")
    else:
        if opcion =="C" or opcion=="c": print("You chose chicken")
        else:
            if opcion =="P" or opcion=="p": print("You chose pizza")
            else:
                menu()

    return

menu()