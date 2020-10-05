if __name__ == '__main__':
    import random

    huruf = ['a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']


    def Clearscreen():
        import os
        os.system("clear")


    def jawaban():
        print("""
a b c d e f g h i j  k  l  m  n  o  p
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
q  r  s  t  u  f  w  x  y  z
17 18 19 20 21 22 23 24 25 26
        """)


    def lagi_bro():
        lagi = input("\nMau maen lagi? (y/n)")

        while not lagi.__eq__('y') and not lagi.__eq__('n'):
            print("\npilih 'y' atau 'n'")
            lagi = input("\nMau maen lagi? (y/n)")

        return lagi.__eq__('y')


    def logic_game():
        soal = huruf[random.randint(0, 25)]

        print(f"\ntentukan urutan abjad dari huruf {soal}\n")

        jawaban_user = int(input("Masukan jawabanmu: "))

        if jawaban_user <= 26:
            if huruf[jawaban_user-1].__eq__(soal):
                print("\nanda benar")
            else:
                print("\nanda salah")
            jawaban()
        else:
            print("\nhuruf abjad cuma ada 26")


    def main():
        Clearscreen()
        print("\t\tmenentukan urutan abjad")

        print("""
peraturan: 
anda akan diberi huruf abjad secara acak 
lalu anda harus menebak urutan abjad tersebut
jika siap tekan enter""")

        input()
        
        play = True
        while play:
            Clearscreen()
            logic_game()
            play = lagi_bro()


    main()










