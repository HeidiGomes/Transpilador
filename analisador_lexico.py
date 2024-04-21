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
    ('IGUAL', r'='),
    ('PONTO_VIRGULA', r';'),
    ('IDENTIFICADOR', r'[a-zA-Z][a-zA-Z0-9]*'),
    ('NUMERO', r'\d+(\.\d+)?'),
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
            raise ValueError('Caractere inválido: ' + code[0])
    return tokens

# Exemplo de uso
codigo = '''
programa
inteiro a, b, c;
decimal d;
escreva("Programa Teste").
escreva ("Digite A").
leia (a).
escreva ("Digite B").
leia (b).
if (a < b)
{
    c = a + b;
}
else
{
    c = a - b;
}
escreva ("C e igual a ").
escreva (c).
d = c / (a + b).
escreva ("D e igual a ").
escreva (d).
fimprog.
'''

tokens = lexer(codigo)
for token in tokens:
    print(token)
