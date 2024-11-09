ordenado = float(input("Quanto recebe de salário?"))
if ordenado <= 500 :
    print("O teu reajuste é de 15% vais passar a receber" , ordenado*1.15, "€.")
elif ordenado > 500 and ordenado < 1000:
    print("O teu reajuste é de 10% vais passar a receber" , ordenado*1.10, "€.")
elif ordenado >= 1000:
    print("O teu reajuste é de 5% vais passar a receber", ordenado * 1.05, "€.")