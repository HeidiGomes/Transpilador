import re

# Definição dos padrões regulares para os tokens
patterns = [
    ('PROGRAMA', r'programa'),
    ('FIMPROG', r'fimprog'),
    ('INTEIRO', r'inteiro'),
    ('DECIMAL', r'decimal'),
    ('CARACTERE', r'caractere'),
    ('LEIA', r'leia'),
    ('ESCREVA', r'escreva'),
    ('IF', r'if'),
    ('ELSE', r'else'),
    ('WHILE', r'while'),
    ('DO', r'do'),
    ('FOR', r'for'),
    ('OPERADOR', r'\+|-|\*|/|>|>=|<|<=|==|!='),
    ('ABRE_PAR', r'\('),
    ('FECHA_PAR', r'\)'),
    ('ABRE_CHAVE', r'\{'),
    ('FECHA_CHAVE', r'\}'),
    ('VIRGULA', r','),
    ('IGUAL', r':='),
    ('PONTO_VIRGULA', r';'),
    ('IDENTIFICADOR', r'[a-zA-Z][a-zA-Z0-9]*'),
    ('NUMERO', r'\d+(\.\d+)?'),
    ('TEXTO', r'"[^"]*"'),  # Corrigido o padrão para capturar texto entre aspas duplas
    ('PONTO', r'\.'),
    ('COMENTARIO', r'\#.*'),
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
            print('Caractere inválido:', code[0])  # Adição para imprimir o caractere inválido
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
    # Função para a regra das declarações
    def declaracoes():
        nonlocal codigo_python
        print("Iniciando a análise das declarações...")
        consumir('INTEIRO')
        variaveis = []
        while tokens[0][0] == 'IDENTIFICADOR':
            variavel = consumir('IDENTIFICADOR')
            variaveis.append(variavel)
            if tokens[0][0] == 'VIRGULA':
                consumir('VIRGULA')
        consumir('PONTO_VIRGULA')
        for variavel in variaveis:
            # Adiciona a declaração e inicialização das variáveis ao código Python gerado
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
            identificador = consumir('IDENTIFICADOR')  # Captura o identificador
            consumir('FECHA_PAR')
            consumir('PONTO_VIRGULA')
            # Adiciona a leitura de entrada ao código Python gerado
            codigo_python += f'{identificador} = int(input())\n'
        elif tokens[0][0] == 'ESCREVA':
            consumir('ESCREVA')
            consumir('ABRE_PAR')
            if tokens[0][0] == 'IDENTIFICADOR':
                identificador = consumir('IDENTIFICADOR')  # Captura o identificador
                consumir('FECHA_PAR')
                consumir('PONTO_VIRGULA')
                # Adiciona o identificador ao código Python gerado
                codigo_python += f'print({identificador})\n'
            elif tokens[0][0] == 'TEXTO':
                texto = consumir('TEXTO')  # Captura o texto
                consumir('FECHA_PAR')
                consumir('PONTO_VIRGULA')
                # Adiciona o texto ao código Python gerado
                codigo_python += f'print({texto})\n'
            elif tokens[0][0] == 'IDENTIFICADOR':  # Adicionado este bloco para lidar com o caso 'ESCREVA(media);'
                identificador = consumir('IDENTIFICADOR')
                consumir('FECHA_PAR')
                consumir('PONTO_VIRGULA')
                codigo_python += f'print({identificador})\n'
        elif tokens[0][0] == 'IF':
            consumir('IF')
            consumir('ABRE_PAR')
            expressao()
            consumir('FECHA_PAR')
            bloco()
            if tokens[0][0] == 'ELSE':
                consumir('ELSE')
                bloco()
        elif tokens[0][0] in ['WHILE', 'DO', 'FOR']:
            repeticao()
        else:
            atribuicao()

    # Função para a regra da repetição
    def repeticao():
        nonlocal codigo_python
        if tokens[0][0] == 'WHILE':
            consumir('WHILE')
            consumir('ABRE_PAR')
            expressao()
            consumir('FECHA_PAR')
            bloco()
        elif tokens[0][0] == 'DO':
            consumir('DO')
            bloco()
            consumir('WHILE')
            consumir('ABRE_PAR')
            expressao()
            consumir('FECHA_PAR')
            consumir('PONTO_VIRGULA')
        elif tokens[0][0] == 'FOR':
            consumir('FOR')
            consumir('ABRE_PAR')
            atribuicao()
            consumir('PONTO_VIRGULA')
            expressao()
            consumir('PONTO_VIRGULA')
            atribuicao()
            consumir('FECHA_PAR')
            bloco()

    # Função para a regra da atribuição
    def atribuicao():
        nonlocal codigo_python
        consumir('IDENTIFICADOR')
        consumir('IGUAL')
        expressao()
        consumir('PONTO_VIRGULA')

    # Função para a regra da expressão
    def expressao():
        nonlocal codigo_python
        termo()
        while tokens[0][0] in ['OPERADOR', 'IDENTIFICADOR', 'NUMERO', 'ABRE_PAR']:
            consumir('OPERADOR')
            termo()

    # Função para a regra do termo
    def termo():
        nonlocal codigo_python
        fator()
        while tokens[0][0] in ['OPERADOR', 'IDENTIFICADOR', 'NUMERO', 'ABRE_PAR']:
            consumir('OPERADOR')
            fator()

    # Função para a regra do fator
    def fator():
        nonlocal codigo_python
        if tokens[0][0] == 'IDENTIFICADOR':
            return consumir('IDENTIFICADOR')
        elif tokens[0][0] == 'NUMERO':
            return consumir('NUMERO')
        elif tokens[0][0] == 'ABRE_PAR':
            consumir('ABRE_PAR')
            expressao()
            consumir('FECHA_PAR')
        else:
            raise SyntaxError(f'Erro de sintaxe: fator inesperado {tokens[0][0]}')

    # Chamada da regra inicial
    programa()

    return codigo_python  # Garante que a função sempre retorna uma string vazia se nenhum código for gerado

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
