# Definição dos tipos de exceção para erros sintáticos
class SyntaxError(Exception):
    pass

# Função para ler os tokens de um arquivo .txt
def ler_tokens(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        tokens = [tuple(linha.strip().split(',')) for linha in arquivo.readlines()]
    return tokens

# Definição da função para o analisador sintático
def parser(tokens):
    index = 0

    # Função para consumir o próximo token
    def consume(expected_token_type):
        nonlocal index
        if index < len(tokens) and tokens[index][0] == expected_token_type:
            index += 1
        else:
            raise SyntaxError(f'Erro de sintaxe: esperado {expected_token_type}, encontrado {tokens[index][0]}')

    # Função para a regra do programa
    def programa():
        consume('PROGRAMA')
        declaracoes()
        bloco()
        consume('FIMPROG')

    # Função para a regra das declarações
    def declaracoes():
        consume('INTEIRO')
        consume('IDENTIFICADOR')
        while tokens[index][0] == 'VIRGULA':
            consume('VIRGULA')
            consume('IDENTIFICADOR')
        consume('PONTO_VIRGULA')

    # Função para a regra do bloco
    def bloco():
        consume('ABRE_CHAVE')
        comandos()
        consume('FECHA_CHAVE')

    # Função para a regra dos comandos
    def comandos():
        while tokens[index][0] != 'FECHA_CHAVE':
            comando()

    # Função para a regra do comando
    def comando():
        if tokens[index][0] == 'LEIA':
            consume('LEIA')
            consume('ABRE_PAR')
            consume('IDENTIFICADOR')
            consume('FECHA_PAR')
            consume('PONTO_VIRGULA')
        elif tokens[index][0] == 'ESCREVA':
            consume('ESCREVA')
            consume('ABRE_PAR')
            consume('IDENTIFICADOR')
            consume('FECHA_PAR')
            consume('PONTO_VIRGULA')
        elif tokens[index][0] == 'IF':
            consume('IF')
            consume('ABRE_PAR')
            expressao()
            consume('FECHA_PAR')
            bloco()
            if tokens[index][0] == 'ELSE':
                consume('ELSE')
                bloco()
        elif tokens[index][0] in ['WHILE', 'DO', 'FOR']:
            repeticao()
        else:
            atribuicao()

    # Função para a regra da repetição
    def repeticao():
        if tokens[index][0] == 'WHILE':
            consume('WHILE')
            consume('ABRE_PAR')
            expressao()
            consume('FECHA_PAR')
            bloco()
        elif tokens[index][0] == 'DO':
            consume('DO')
            bloco()
            consume('WHILE')
            consume('ABRE_PAR')
            expressao()
            consume('FECHA_PAR')
            consume('PONTO_VIRGULA')
        elif tokens[index][0] == 'FOR':
            consume('FOR')
            consume('ABRE_PAR')
            atribuicao()
            consume('PONTO_VIRGULA')
            expressao()
            consume('PONTO_VIRGULA')
            atribuicao()
            consume('FECHA_PAR')
            bloco()

    # Função para a regra da atribuição
    def atribuicao():
        consume('IDENTIFICADOR')
        consume('IGUAL')
        expressao()
        consume('PONTO_VIRGULA')

    # Função para a regra da expressão
    def expressao():
        termo()
        while tokens[index][0] in ['OPERADOR', 'IDENTIFICADOR', 'NUMERO', 'ABRE_PAR']:
            consume('OPERADOR')
            termo()

    # Função para a regra do termo
    def termo():
        fator()
        while tokens[index][0] in ['OPERADOR', 'IDENTIFICADOR', 'NUMERO', 'ABRE_PAR']:
            consume('OPERADOR')
            fator()

    # Função para a regra do fator
    def fator():
        if tokens[index][0] == 'IDENTIFICADOR':
            consume('IDENTIFICADOR')
        elif tokens[index][0] == 'NUMERO':
            consume('NUMERO')
        elif tokens[index][0] == 'ABRE_PAR':
            consume('ABRE_PAR')
            expressao()
            consume('FECHA_PAR')
        else:
            raise SyntaxError(f'Erro de sintaxe: fator inesperado {tokens[index][0]}')

    # Chamada da regra inicial
    programa()

# Ler os tokens do arquivo .txt
nome_arquivo = 'tokens.txt'
tokens = ler_tokens(nome_arquivo)

# Tentar fazer a análise sintática
try:
    parser(tokens)
    print('Análise sintática concluída sem erros.')
except SyntaxError as e:
    print(e)
