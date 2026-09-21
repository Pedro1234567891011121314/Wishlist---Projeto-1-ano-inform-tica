jogos = [""] #FIXME: (garcia vai cuidar disso dps ent rlx) mesmo q vc insira (ou faça qualquer coisa) um item, ele n realmente insere pq n ta conectado num .json, ent n salva

def inserir():
#FIXME: colocar validação de nome
    jogo = str(input("Digite o nome do jogo: "))
    jogos.append(jogo)
def menu():
    print("Lista de desejos")
    print("=" * 20)
    print("1. Inserir item")
    print("2. Remover item")
    print("3. Ver lista")
    print("4. Limpar lista")
    print("0. Sair")


def main():
    while True:
        
        menu()
        break


if __name__ == "__main__":
        main()

        #TODO: colocar validação de entrada
        op = int(input("Escolha uma opção: "))
        match op:
            case 1:
                inserir()

            case 2:
                jogo = str(input("Digite o nome do jogo a ser removido: "))
                if jogo in jogos:
                    jogos.remove(jogo)
                    print("Jogo removido com sucesso!")
                else:
                    print("Jogo não encontrado na lista.")

            case 3: #FIXME: consertar (nao fala q ta vazia quanto ta vazia)
                if jogos:
                    print("Lista de desejos: ")
                    for jogo in jogos:
                        print(jogo)
                else:
                    print("A lista de desejos está vazia.")

            case 4: #FIXME: consertar (nao fala q ta vazia quanto ta vazia)
                if jogos:
                    jogos.clear()
                    print("Lista limpa com sucesso!")
                else:
                    print("A lista de desejos já está vazia.")

            case 0:
                while True: 
                    print("Saindo...")
                    break
              
