# test_code.py


# Exemplo de código que precisa de formatação
def some_function(param1, param2):
    if param1 and param2:
        print("Condition met!")
    else:
        print("Condition not met!")


# Exemplo de função que tem uma linha longa para testar a configuração max-line-length
def long_line_example():
    very_long_string = """This is an example of a very long string that should exceed the max line
    length and thus trigger
    formatting or linting issues in order to test the pre-commit hooks properly."""
    print(very_long_string)


# Função com variáveis não utilizadas para testar o linting
def unused_variables():
    a = 10
    b = 20
    return a + b


# Comentário de linha muito longa para testar o max-line-length
# Este é um comentário muito longo que deve ultrapassar o comprimento máximo de linha definido
# pelo Flake8, que está configurado para 120 caracteres neste exemplo de arquivo.
