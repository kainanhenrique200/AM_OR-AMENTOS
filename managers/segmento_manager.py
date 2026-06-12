from calculos import Metragem

medidas = []

def adicionar_medida():

    descricao = input("Descrição: ")
    largura = float(input("Largura: "))
    comprimento = float(input("Comprimento: "))

    medida = Metragem(
        descricao,
        largura,
        comprimento
    )

    medidas.append(medida)

    print("Medida cadastrada com sucesso!")

def listar_medidas():

    if len(medidas) == 0:
        print("Nenhuma medida cadastrada.")
        return

    contador = 0

    for medida in medidas:
        print(f"{contador} - {medida}")
        contador += 1

def excluir_medida():

    listar_medidas()

    indice = int(input("Digite o índice: "))

    if 0 <= indice < len(medidas):
        medidas.pop(indice)
        print("Medida excluída!")
    else:
        print("Índice inválido")

def calcular_total():

    total = 0

    for medida in medidas:
        total += medida.calcular_area()

    print(f"Área total: {total:.2f} m²")

def main():

    while True:

        print("\n1 - Adicionar medida")
        print("2 - Listar medidas")
        print("3 - Excluir medida")
        print("4 - Calcular área total")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_medida()

        elif opcao == "2":
            listar_medidas()

        elif opcao == "3":
            excluir_medida()

        elif opcao == "4":
            calcular_total()

        elif opcao == "0":
            break

        else:
            print("Opção inválida")


def menu_metragens():
    menu()


if __name__ == "__main__":
    menu_metragens()