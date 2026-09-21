jogos = []

def inserir():
#FIXME: colocar validação de nome
    jogo = str(input("Digite o nome do jogo: "))
    jogos.append(jogo)
def menu():
    print("Lista de desejos")
    print("=" * 20)
    print("1. Inserir item")
    print("2. Remover item")
    print("3.")
    print("4.")
    print("0. SAIR")

def main():
    while True:
        
        menu()

if __name__ == "__main__":
        main()

        #TODO: colocar validação de entrada
        op = int(input("Escolha uma opção: "))
        match op:
            case 1:
                inserir()
            case 2:
                for jogo in jogos:
                    print(jogo)
            case 0:
                print("Saindo...")
              
