import re

# Definição dos padrões regulares para os tokens
patterns = [
    ('PROGRAMA', r'programa'),
    ('FIMPROG', r'fimprog'),
    ('TIPO', r'(inteiro|decimal|caractere)'),
    ('LEIA', r'leia'),
    ('ESCREVA', r'escreva'),
    ('ABRE_CHAVE', r'\{'),
    ('FECHA_CHAVE', r'\}'),
    ('OPERADOR', r'\+|-|\*|/|>|>=|<|<=|==|!='),
    ('ABRE_PAR', r'\('),
    ('FECHA_PAR', r'\)'),
    ('VIRGULA', r','),
    ('IGUAL', r':='),
    ('PONTO_VIRGULA', r';'),
    ('IDENTIFICADOR', r'[a-zA-Z][a-zA-Z0-9]*'),
    ('NUMERO', r'\d+(\.\d+)?'),
    ('TEXTO', r'"[^"]*"'),
    ('COMENTARIO', r'//.*'),
    ('ESPACO', r'\s+'),
    ('NOVA_LINHA', r'\n')
]

# Função para identificar o próximo token no código fonte
def lexer(code):
    tokens = []
    while code:
        match = None
        for token_type, pattern in patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                if token_type != 'ESPACO' and token_type != 'NOVA_LINHA' and token_type != 'COMENTARIO':
                    tokens.append((token_type, value))
                code = code[match.end():]
                break
        if not match:
            print('Caractere inválido:', code[0])
            raise ValueError('Caractere inválido: ' + code[0])
    return tokens

# Função para gerar código equivalente em Python
def gerar_codigo_python(tokens):
    codigo_python = ""

    # Função para consumir o próximo token
    def consumir(tipo_esperado):
        nonlocal tokens
        if tokens[0][0] == tipo_esperado:
            return tokens.pop(0)[1]
        else:
            raise SyntaxError(f'Erro de sintaxe: esperado {tipo_esperado}, encontrado {tokens[0][0]}')

    # Função para a regra do programa
    def programa():
        nonlocal codigo_python
        print("Iniciando a análise do programa...")
        consumir('PROGRAMA')
        declaracoes()
        bloco()
        consumir('FIMPROG')

    # Função para a regra das declarações
    def declaracoes():
        nonlocal codigo_python
        print("Iniciando a análise das declarações...")
        while tokens[0][0] == 'TIPO':
            consumir('TIPO')
            variaveis = []
            while tokens[0][0] == 'IDENTIFICADOR':
                variavel = consumir('IDENTIFICADOR')
                variaveis.append(variavel)
                if tokens[0][0] == 'VIRGULA':
                    consumir('VIRGULA')
            consumir('PONTO_VIRGULA')
            for variavel in variaveis:
                codigo_python += f'{variavel} = 0\n'

    # Função para a regra do bloco
    def bloco():
        nonlocal codigo_python
        print("Iniciando a análise do bloco...")
        consumir('ABRE_CHAVE')
        comandos()
        consumir('FECHA_CHAVE')

    # Função para a regra dos comandos
    def comandos():
        nonlocal codigo_python
        print("Iniciando a análise dos comandos...")
        while tokens[0][0] != 'FECHA_CHAVE':
            comando()

    def comando():
        nonlocal codigo_python
        print("Iniciando a análise do comando...")
        if tokens[0][0] == 'LEIA':
            consumir('LEIA')
            consumir('ABRE_PAR')
            identificador = consumir('IDENTIFICADOR')
            consumir('FECHA_PAR')
            consumir('PONTO_VIRGULA')
            codigo_python += f'{identificador} = int(input("Digite o valor de {identificador}: "))\n'
        elif tokens[0][0] == 'ESCREVA':
            consumir('ESCREVA')
            consumir('ABRE_PAR')
            if tokens[0][0] == 'TEXTO':
                texto = consumir('TEXTO')
                consumir('FECHA_PAR')
                consumir('PONTO_VIRGULA')
                codigo_python += f'print({texto})\n'
            elif tokens[0][0] == 'IDENTIFICADOR':
                identificador = consumir('IDENTIFICADOR')
                consumir('FECHA_PAR')
                consumir('PONTO_VIRGULA')
                codigo_python += f'print("{identificador} =", {identificador})\n'
        else:
            atribuicao()

    # Função para a regra da atribuição
    def atribuicao():
        nonlocal codigo_python
        identificador = consumir('IDENTIFICADOR')
        operador = consumir('IGUAL')
        valor = expressao()
        consumir('PONTO_VIRGULA')
        codigo_python += f'{identificador} = {valor}\n'

    # Função para a regra da expressão
    def expressao():
        nonlocal codigo_python
        valor = termo()
        while tokens[0][0] in ['OPERADOR', 'IDENTIFICADOR', 'NUMERO', 'ABRE_PAR']:
            operador = consumir('OPERADOR')
            proximo_valor = termo()
            valor = f'({valor} {operador} {proximo_valor})'
        return valor

    # Função para a regra do termo
    def termo():
        nonlocal codigo_python
        valor = fator()
        while tokens[0][0] in ['OPERADOR', 'IDENTIFICADOR', 'NUMERO', 'ABRE_PAR']:
            operador = consumir('OPERADOR')
            proximo_valor = fator()
            valor = f'({valor} {operador} {proximo_valor})'
        return valor

    # Função para a regra do fator
    def fator():
        nonlocal codigo_python
        if tokens[0][0] == 'IDENTIFICADOR':
            return consumir('IDENTIFICADOR')
        elif tokens[0][0] == 'NUMERO':
            return consumir('NUMERO')
        elif tokens[0][0] == 'ABRE_PAR':
            consumir('ABRE_PAR')
            valor = expressao()
            consumir('FECHA_PAR')
            return valor
        else:
            raise SyntaxError(f'Erro de sintaxe: fator inesperado {tokens[0][0]}')

    # Chamada da regra inicial
    programa()

    return codigo_python

# Ler o código fonte
with open('codigo_fonte.txt', 'r') as file:
    codigo_fonte = file.read()

# Realizar a análise léxica
tokens = lexer(codigo_fonte)
print(tokens)

# Tentar fazer a análise sintática
try:
    codigo_python = gerar_codigo_python(tokens)
    print('Análise sintática concluída sem erros.')

    # Verificar se há código Python gerado
    if codigo_python:
        # Se a análise sintática estiver correta e houver código Python gerado,
        # salve-o no arquivo "codigo_python.txt"
        with open('codigo_python.txt', 'w') as file:
            file.write(codigo_python)

        print('Código Python gerado com sucesso e salvo no arquivo "codigo_python.txt".')
    else:
        print('Nenhum código Python foi gerado.')

except SyntaxError as e:
    print('Erro de sintaxe:', e)
