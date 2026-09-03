import math

def menu_circulo():
    print("""
    -------------------------------------------------
                       CÍRCULO
    -------------------------------------------------
    """)
    raio = float(input("Digite o raio do círculo: "))
    circunferencia = 2 * math.pi * raio
    area = math.pi * (raio ** 2)

    print(f"""
    Circunferência: {circunferencia:.2f}
    Área: {area:.2f}
    """)

def menu_quadrado():
    print("""
    -------------------------------------------------
                       QUADRADO
    -------------------------------------------------
    """)
    lado = float(input("Digite o lado do quadrado: "))
    perimetro = 4 * lado
    area = lado ** 2

    print(f"""
    Perímetro: {perimetro:.2f}
    Área: {area:.2f}
    """)

def menu_vetor():
    print("""
    -------------------------------------------------
                       VETOR
    -------------------------------------------------
    """)
    qtd = int(input("Quantos elementos terá o vetor? "))
    if qtd <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    vetor = []
    for i in range(qtd):
        num = float(input(f"Digite o elemento {i + 1}: "))
        vetor.append(num)

    menor = min(vetor)
    maior = max(vetor)

    print(f"""
    Dados do vetor: {vetor}
    Menor elemento: {menor}
    Maior elemento: {maior}
    """)

def main():
    while True:
        print("""
        -------------------------------------------------
                             MENU
        -------------------------------------------------

        [1] Círculo: Cálculo de Circunferência e Área
        [2] Quadrado: Cálculo de Perímetro e Área
        [3] Vetor: Leitura, exibição, menor e maior elemento
        [4] Sair
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_circulo()
        elif opcao == '2':
            menu_quadrado()
        elif opcao == '3':
            menu_vetor()
        elif opcao == '4':
            print("Encerrando programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")