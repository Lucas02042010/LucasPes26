temperatura = float(input("Qual a temperatura de hoje?"))

if temperatura < 10:
    print ("Está muito frio! Use roupas quentes.")
elif temperatura <= 20:
    print ("Frio. Vista-se bem!")
elif temperatura <= 25:
    print ("Temperatura agradável.")
elif temperatura <= 30:
    print("Está ficando quente!")
elif temperatura > 30: 
    print("Está muito quente! Fique hidratado.")