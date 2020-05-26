from random import randint

def gbk():
    clearScreen()

    print("Welcome to the game")

    jeda()

    nama = input("siapa nama anda: ")

    jeda()
    clearScreen()

    pilihan = ["1.gunting", "2.batu", "3.kertas"]

    scorePemain = 0
    scoreKomputer = 0

    user = True
    while user:
        clearScreen()

        tampilkanPilihan(pilihan)
        print("0.score")

        komputer = pilihan[randint(0,2)]

        pemain = input("\npilihanmu: ")

        print("\n")

        if pemain in komputer:
            pemain = komputer
            print(pemain, " vs ", komputer)
            print("\nSeri")
            pass
        elif pemain == "1":
            pemain = pilihan[0]
            if "3" in komputer:
                print(pemain, " vs ", komputer)
                print("\n",nama, " menang")
                scorePemain += 1
            elif "2" in komputer:
                print(pemain, " vs ", komputer)
                print("\n",nama, " kalah")
                scoreKomputer += 1
            pass
        elif pemain == "2":
            pemain = pilihan[1]
            if "1" in komputer:
                print(pemain, " vs ", komputer)
                print("\n",nama, " menang")
                scorePemain += 1
            elif "3" in komputer:
                print(pemain, " vs ", komputer)
                print("\n",nama, " kalah")
                scoreKomputer += 1
            pass
        elif pemain == "3":
            pemain = pilihan[2]
            if "2" in komputer:
                print(pemain, " vs ", komputer)
                print("\n",nama, " menang")
                scorePemain += 1
            elif "1" in komputer:
                print(pemain, " vs ", komputer)
                print("\n",nama, " kalah")
                scoreKomputer += 1
            pass
        elif pemain == "0":
            score(nama,scorePemain,scoreKomputer)
            pass
        else:
            print("\nBukan itu woy pilihannya")
            jeda()
            continue

        komputer = pilihan[randint(0,2)]
        user = getYesOrNo()



    
def clearScreen():
    import os
    os.system("clear")


def jeda():
    input("")


def getYesOrNo():
    isLanjutkan = input("\napakah anda ingin melanjutkan? (y/t) ")

    while not isLanjutkan.__contains__("y") and not isLanjutkan.__contains__("t"):
        print("\npilihlah 'y' / 't'")
        isLanjutkan = input("\napakah anda ingin melanjutkan? (y/t) ")

    return isLanjutkan.__contains__("y")


def tampilkanPilihan(pilihan = []):

    i = 0
    for i in range(pilihan.__len__()):
        print(pilihan[i])


def score(nama, scorePemain, scoreKomputer):
    print("Score")
    print(nama, " = ", scorePemain)
    print("komputer = ", scoreKomputer)



gbk()