def pedirDados():
    while True:
        nome = input("Digite o nome (Digite 0 para encerrar.): ")
        if nome == "0":
            print("Finalizado.")
            break
        idade = int(input("Digite a idade: "))
        while idade <=0 or idade >= 100:
            idade = int(input("Digite uma idade válida: "))
        sexo = input("Digite o sexo (M/F): ")
        telefone = int(input("Digite o número de telefone: "))
        salvarDados(nome,idade,sexo,telefone)
        respostaBuscarPorSexo = input("Deseja realizar uma busca nos usuários de um sexo em específico (S/N)? ")
        if respostaBuscarPorSexo == "S":
            sexoDesejado = input("Digite o sexo em questão (M/F): ")
            buscarPorSexo(sexoDesejado)
        elif respostaBuscarPorSexo == "N":
            print("Ok.")
        respostaBuscarPorNome = input("Deseja realizar uma busca nos usuários com um nome ou caractéres específico (S/N)? ")
        if respostaBuscarPorNome == "S":
            caracteresDesejados = input("Digite o nome ou os caractéres em questão: ")
            buscarPorNome(caracteresDesejados)
        elif respostaBuscarPorNome == "N":
            print("Ok.")
            continue


def salvarDados(nome,idade,sexo,telefone):
    with open("dados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}|{idade}|{sexo}|{telefone}\n")

def printarDados():
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        for linhas in arquivo.readlines():
            listaUsuarios = linhas.split("|")
            if listaUsuarios[2] == "M":
                listaUsuarios[2] = "Masculino"
            elif listaUsuarios[2] == "F":
                 listaUsuarios[2] = "Feminino"
            print(f"Nome: {listaUsuarios[0]}\Idade: {listaUsuarios[1]}\nSexo: {listaUsuarios[2]}\nTelefone: {listaUsuarios[3]}\n")

def buscarPorSexo(sexoDesejado):
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        for linhas in arquivo.readlines():
            listaUsuarios = linhas.split("|")
            if listaUsuarios[2] == sexoDesejado:
                print(f"Nome: {listaUsuarios[0]}\Idade: {listaUsuarios[1]}\nSexo: {listaUsuarios[2]}\nTelefone: {listaUsuarios[3]}\n")
            else:
                continue

def buscarPorNome(caracteresDesejados):
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        for linhas in arquivo.readlines():
            listaUsuarios = linhas.split("|")
            if caracteresDesejados in listaUsuarios[0]:
                print(f"Nome: {listaUsuarios[0]}\Idade: {listaUsuarios[1]}\nSexo: {listaUsuarios[2]}\nTelefone: {listaUsuarios[3]}\n")
            else:
                continue

if __name__ == "__main__":
    pedirDados()