def multiplication_table(base_number):
    # Lista para armazenar os resultados da tabuada
    results_list = []

    # Função interna para calcular a tabuada até o número especificado
    def calculate_table(up_to):
        print(f'TABLE OF {base_number} / TABUADA DE {base_number}'.center(50).upper())  # Exibe o título da tabuada
        for i in range(1, up_to + 1):
            result = base_number * i
            results_list.append(f"{i} x {base_number} = {result}")
        return results_list

    return calculate_table

# Solicita ao usuário o número base para a tabuada
user_base_number = input('Enter a number to multiply / Digite um número para multiplicar: ')
user_base_number = int(user_base_number)

# Chama a função para criar a tabuada
table_calculator = multiplication_table(user_base_number)

# Solicita até qual número o usuário deseja calcular a tabuada
user_limit = input('Up to which number? / Até qual número? ')
user_limit = int(user_limit)

# Calcula e exibe os resultados da tabuada
final_results = table_calculator(user_limit)
for result in final_results:
    print(result)
print('END / FIM'.center(50).upper())