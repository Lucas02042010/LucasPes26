def volume(altura, raio):
    volume = 3.14 * (raio ** 2) * altura
    return volume


a = float(input("Digite a altura do cilindro em metros: "))
r = float(input("Digite o raio do cilindro em metros: "))

resultado = volume(a, r)

print("O volume do cilindro é:", resultado, "m³")
