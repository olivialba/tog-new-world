from adventure import startAdventureScript

if __name__ == '__main__':
    choiche = input("1 - Auto Adventure\nPlease input your choiche: ")
    
    match choiche:
        case '1':
            startAdventureScript(input("Phone window's title?"))
        case _:
            print("Wrong selection, please input a number from the list above.\n")
            pass