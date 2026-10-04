temp = float(input("qual a temperatura de hoje em celsius?"))

if temp < 10:
    print ("Está muito frio! Use roupas quentes.")
elif temp < 20:
    print ("Frio. Vista-se bem!")
elif temp < 25:
    print ("Temperatura agradável.")
elif temp < 30:
    print ("Está ficando quente!")
elif temp > 30: 
    print ("Está muito quente! Fique hidratado.")