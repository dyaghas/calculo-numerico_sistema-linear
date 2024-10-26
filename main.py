# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def execute():
    import csv

    # Interpreta o que está escrito no arquivo csv de input
    def read_csv(input_file):
        try:
            with open(input_file, newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                final_csv = [
                    [float(num) for num in linha] for linha in csv_reader
                ]
        except ValueError:
            print("O arquivo csv possuí valores inválidos")
            exit()
        return final_csv

    # Realiza uma eliminação de gauss para resolver o sistema linear de equações
    def gauss_elimination(csv_input):
        n = len(csv_input)

        # Eliminação que forma uma matriz triangular superior
        for i in range(n):
            # Pivotamento parcial
            max_line = max(range(i, n), key=lambda k: abs(csv_input[k][i]))
            csv_input[i], csv_input[max_line] = csv_input[max_line], csv_input[i]

            # Tornar o pivô como 1 e zerar elementos abaixo
            pivot = csv_input[i][i]
            for j in range(i, n + 1):
                csv_input[i][j] /= pivot
            for k in range(i + 1, n):
                fator = csv_input[k][i]
                for j in range(i, n + 1):
                    csv_input[k][j] -= fator * csv_input[i][j]

        # Substituição reversa para resolver as variáveis
        res = [0] * n
        for i in range(n - 1, -1, -1):
            res[i] = csv_input[i][n] - sum(csv_input[i][j] * res[j] for j in range(i + 1, n))

        return res

    # Exibe a prova real inserindo as variáveis encontradas no sistema linear
    def output_proof(original_system, solution):
        n = len(original_system)
        for i in range(n):
            equation = " + ".join(f"{original_system[i][j]}*{round(solution[j], 2)}" for j in range(n))
            calculated_res = sum(original_system[i][j] * solution[j] for j in range(n))
            print(
                f"Equação {i + 1}:\n{equation} = {round(calculated_res, 2)} \n(resultado esperado: {original_system[i][-1]})\n"
            )

    # Aplica a eliminação de gauss para resolver o sistema de equações e imprime o resultado
    def solve_system(input_csv):
        system = read_csv(input_csv)
        original_system = [line[:] for line in system]  # Faz uma cópia do sistema original para a prova real

        # Resolve o sistema
        solution = gauss_elimination(system)

        # Exibe a solução
        print("Solução:")
        for i, value in enumerate(solution):
            print(f"x{i + 1} = {value}")

        # Prova real
        print("\nProva Real:")
        output_proof(original_system, solution)

    file_name = 'input.csv'
    solve_system(file_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute()
