import winsound

petla = True

while (petla):

    try:
        masa = float(input("\nPodaj masę ciała (kg): "))
        wzrost = float(input("Podaj wzrost (cm): "))
        if masa <= 0 or wzrost <= 0:
            print("Wzrost i waga muszą być dodatnie!")
            continue
    except ValueError:
        print("Wzrost i waga muszą być liczbami całkowitymi lub zmiennoprzecinkowymi!")
        continue

    bmi = masa / (wzrost / 100 )**2

    print(f"Twoje bmi: {round(bmi, 2)}")

    if bmi < 18.5:
        winsound.Beep(500, 1000)
        print("niedowaga")
    elif bmi >= 30:
        winsound.Beep(700, 1000)
        print("otyłość")
    elif bmi >= 18.5 and bmi <= 24.9:
        winsound.Beep(300, 400)
        print("waga prawidłowa")
    else:
        winsound.Beep(500, 1000)
        print("nadwaga")

    odpowiedz = input("\nWpisz coś żeby kontynuować dla kolejnej osoby (pozostaw puste żeby zakończyć): ")
    petla = odpowiedz or False
