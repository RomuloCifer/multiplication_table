import unicodedata
import json
with open("alunos.json", "r", encoding="utf-8") as arquivo:
    alunos = json.load(arquivo)

materias_disponiveis = {
    "1": "Matemática",
    "12": "Português",
    "123": "História",
    "1234": "Geografia",
    "12345": "Ciências",
    "123456": "Inglês",
    "1234567": "Educação Física",
    "12345678": "Artes"
}


# Função para perguntar qual série o usuário deseja verificar.
def selecionar_serie(lista_alunos):
    while True:
        serie_usuario = input('Deseja verificar de qual série? ')
        if serie_usuario.isdigit() and len(serie_usuario) == 1:
            for aluno, dados in lista_alunos.items():
                serie = dados['série']
                materias = dados['matérias']
                if serie.startswith(serie_usuario):  # ex: '7' == '7º ano'
                    for materia, nota in materias.items():
                        if materia == materia_professor:
                            print(f"{aluno:<8} - {materia:<15} - Nota: {nota if nota is not None else 'Sem nota'}")
            break
        else:
            print('Por favor, digite o ano em números. EXEMPLO: 6, 7, 8...')
            continue
    return serie_usuario

# Função para imprimir os alunos da série que o usuário pedir.
def exibir_alunos_por_serie(lista_alunos, serie_usuario):
    for aluno, dados in lista_alunos.items():
        serie = dados['série']
        materias = dados['matérias']
        if serie.startswith(serie_usuario):  # ex: '7' == '7º ano'
            for materia, nota in materias.items():
                print(aluno, materia, nota)

# Função para transformar a nota do professor para float.
def obter_nota_professor():
    while True:
        nota_input = input('Qual nota? ').replace(',', '.')
        try:
            return float(nota_input)
        except ValueError:
            print('Digite uma nota válida (ex: 7.5 ou 6,0)')

# Função para remover caracteres especiais e acentos de uma string.
def normalizar_texto(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

# Função para lançar nota para um aluno.
def lancar_nota(lista_alunos, materia_professor):
    while True:
        nome_aluno = input('Qual nome do aluno que deseja lançar nota? \n')
        nome_aluno_normalizado = normalizar_texto(nome_aluno)
        for aluno, dados in lista_alunos.items():
            if normalizar_texto(aluno) == nome_aluno_normalizado:
                materias = dados['matérias']
                for materia, nota in materias.items():
                    if materia == materia_professor:
                        materias[materia] = obter_nota_professor()
        with open("alunos.json", "w", encoding="utf-8") as arquivo:
            json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

        sair = input('Deseja sair? [s] ')
        if sair.lower() in ['s', 'sair']:
            break

# Função para verificar todas as notas.
def verificar_notas(lista_alunos, materia_professor):
    for aluno, dados in lista_alunos.items():
        serie = dados["série"]
        materias = dados["matérias"]
        for materia, nota in materias.items():
            if materia == materia_professor:
                print(f"{aluno:<8} - {materia:<15} - {serie:<8} - Nota: {nota if nota is not None else 'Sem nota'}")

# Função para o painel do professor.
def painel_professor(opcao):
    if opcao == 1:
        selecionar_serie(alunos)
    elif opcao == 2:
        lancar_nota(alunos, materia_professor)
    elif opcao == 3:
        verificar_notas(alunos, materia_professor)

# Função para o login do professor.
def login_professor():
    senha_professor = input('Coloque sua senha: ')
    for senha, materia in materias_disponiveis.items():
        if senha == senha_professor:
            print(f"Bem-vindo, sua matéria é {materia}")
            return materia

materia_professor = login_professor()

# Loop principal do programa.
while True:
    opcao_usuario = input("Digite '1' para verificar por série \nDigite '2' para lançar notas\n" \
                          "Digite '3' para verificar notas\nDigite '4' para sair. ")
    if opcao_usuario.isdigit() and len(opcao_usuario) == 1 and opcao_usuario in ['1', '2', '3', '4']:
        opcao_usuario = int(opcao_usuario)
        if opcao_usuario == 4:
            print('Obrigado por utilizar o programa.')
            break
        else:
            painel_professor(opcao_usuario)
    else:
        print('Digite uma opção válida.')


