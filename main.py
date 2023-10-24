from adventure import startAdventureScript

if __name__ == '__main__':
    choiches = input("1 - Auto Adventure\nPlease input your choiche: ")
    
    match choiches:
        case '1':
            startAdventureScript(input("Phone window's title?"))
        case _:
            print("Wrong selection, please input a number from the list above.\n")
            input("...")
            pass