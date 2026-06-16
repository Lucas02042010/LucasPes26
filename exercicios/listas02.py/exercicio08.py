fatura = 1000
meses = int(input("A quantidade de meses em que você deve está devendo é: "))
contagem = 0

while contagem < meses: 
    fatura = fatura + fatura/100*(15.3)
    contagem += 1
print (fatura)
