
import random

def sceglipm(lista):
    scelta = random.choice(lista)
    return scelta

def main():
    print("Hello, I'm the Lazy Decider, also known as the Script That Saved You From Staying In Bed For Hours Just To Decide What To Do. But I'm humble, so Lazy Decider is fine.")
    testo = input("Type what you want to do, eat, build, blow up... I don't care. Split them with a comma (,): ")

    lista_s = testo.split(",")
    
    lista_p = []

    for elemento in lista_s:
        if elemento.strip() !="":
            lista_p.append(elemento.strip())

    if len(lista_p) == 0:
        print("Bro, you gave ne nothing. I can't decide nothing. ")
        return

    risultato = sceglipm(lista_p)
    print(f"I've chosen {risultato}! Don't argue with the Decider.")    

main()