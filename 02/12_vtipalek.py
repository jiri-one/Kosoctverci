from random import choice

def zkousim_byt_vtipny():
    while user_input := input("Cheš říct vtip? Buď dáš 'ano', nebo to neukončíš."):
        if user_input == "ano":
            break
    input(choice(["Kolik vážíš? ",
                  "Už ses někdy milovaL s mužem? ",
                  "Umíš programovat? ",
                  "Jaké máš IQ? ",
                  "Používáš Python? "]))
    print("To rozhodně nebyla správná a ani pravdivá odpověď.")
    print("Správná odpověď, kterou jsi určitě chtěl napsat, je:")
    print(choice(["Jasně!",
                  "Jako ďas!",
                  "to fakt ano",
                  "pozitivní",
                  "negativní"]))
    
zkousim_byt_vtipny()