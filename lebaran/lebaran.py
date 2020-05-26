corona = input("\napakah corona ada? ")

lebaran = ["mudik", "sholat id di masjid", "takbiran", "merconan"]

if "y" in corona:
    print("\nTETAP DIRUMAH!!!!")
else:
    a = 0
    for a in range(lebaran.__len__()):
        print("\n", lebaran[a])
