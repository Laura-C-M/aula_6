#evento corridas, pessoas 7 ano n podem competir com 9 ano. criar várias categorias para dividir os atletas pelas categorias.
ano = int(input("Estás em que ano de escolaridade?(Só podes responder 7,8 e 9)"))
if ano == 7:
        print("Estás no escalão: minis")
elif ano == 8:
        print("Estás no escalão: infantis")
elif ano == 9:
        print("Estás no escalão: iniciados")
else:
        print("Os alunos abaixo do 7º ano não podem competir, nem os acima do 9º.")