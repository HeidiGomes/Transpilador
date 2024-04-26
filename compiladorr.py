import tkinter as tk
from tkinter import ttk
import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = [
    'ID',
    'INTEGER',
    'STRING',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'DOUBLE',
    'READ',
    'WRITE',
    'RETURN',
    'OP_PRIO_ABRE_PARENTESES',
    'OP_PRIO_FECHA_PARENTESES',
    'OP_PRIO_ABRE_CHAVES',
    'OP_PRIO_FECHA_CHAVES',
    'OP_ATRIBUICAO',
    'SEMICOLON',
]

# Palavras reservadas
reserved = {
    'se': 'IF',
    'senao': 'ELSE',
    'enquanto': 'WHILE',
    'para': 'FOR',
    'leia': 'READ',
    'escreva': 'WRITE',
    'retorne': 'RETURN',
    'inteiro': 'INTEGER',
    'double': 'DOUBLE',
    'booleano': 'BOOLEAN'
}

# Expressões regulares para tokens simples
t_OP_PRIO_ABRE_PARENTESES = r'\('
t_OP_PRIO_FECHA_PARENTESES = r'\)'
t_OP_PRIO_ABRE_CHAVES = r'\{'
t_OP_PRIO_FECHA_CHAVES = r'\}'
t_OP_ATRIBUICAO = r'='
t_SEMICOLON = r';'

# Ignorar caracteres em branco
t_ignore = ' \t'

# Tratar quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratar identificadores e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

# Tratar números inteiros
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Tratar strings delimitadas por aspas duplas
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Remove as aspas duplas
    return t

# Tratar erros léxicos
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Definição das regras de parsing

def p_programa(p):
    '''programa : declaracoes funcoes principal'''

def p_declaracoes(p):
    '''declaracoes : declaracoes declaracao
                   |'''

def p_declaracao(p):
    '''declaracao : tipo ID SEMICOLON
                  | tipo ID OP_ATRIBUICAO expressao SEMICOLON'''

def p_tipo(p):
    '''tipo : INTEGER
            | DOUBLE
            | STRING'''

def p_funcoes(p):
    '''funcoes : funcoes funcao
               |'''

def p_funcao(p):
    '''funcao : ID OP_PRIO_ABRE_PARENTESES parametros OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes comandos OP_PRIO_FECHA_CHAVES'''

def p_parametros(p):
    '''parametros : parametro
                  |'''

def p_parametro(p):
    '''parametro : tipo ID'''

def p_principal(p):
    '''principal : ID OP_PRIO_ABRE_PARENTESES parametros OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES comandos OP_PRIO_FECHA_CHAVES'''

def p_comandos(p):
    '''comandos : comandos comando
                |'''

def p_comando(p):
    '''comando : atribuicao
               | condicional
               | repeticao
               | entrada_saida
               | RETURN SEMICOLON'''

def p_atribuicao(p):
    '''atribuicao : ID OP_ATRIBUICAO expressao SEMICOLON'''

def p_condicional(p):
    '''condicional : IF OP_PRIO_ABRE_PARENTESES expressao OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES comandos OP_PRIO_FECHA_CHAVES ELSE OP_PRIO_ABRE_CHAVES comandos OP_PRIO_FECHA_CHAVES'''

def p_repeticao(p):
    '''repeticao : WHILE OP_PRIO_ABRE_PARENTESES expressao OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES comandos OP_PRIO_FECHA_CHAVES
                 | FOR OP_PRIO_ABRE_PARENTESES atribuicao SEMICOLON expressao SEMICOLON atribuicao OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES comandos OP_PRIO_FECHA_CHAVES'''

def p_entrada_saida(p):
    '''entrada_saida : WRITE OP_PRIO_ABRE_PARENTESES expressao OP_PRIO_FECHA_PARENTESES SEMICOLON
                     | READ OP_PRIO_ABRE_PARENTESES ID OP_PRIO_FECHA_PARENTESES SEMICOLON'''

def p_expressao(p):
    '''expressao : termo OP_ATRIBUICAO termo
                 | termo'''

def p_termo(p):
    '''termo : fator'''

def p_fator(p):
    '''fator : ID
             | INTEGER
             | STRING
             | OP_PRIO_ABRE_PARENTESES expressao OP_PRIO_FECHA_PARENTESES'''

# Construir o parser
parser = yacc.yacc()

class Application():
    def __init__(self, root):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        root.mainloop()

    def tela(self):
        self.root.title("Analisador Léxico e Sintático")
        self.root.configure(background="white")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.minsize(width=550, height=350)

    def frames_da_tela(self):
        self.frame_1 = tk.Frame(self.root, bd=4, bg="#DCDCDC", highlightbackground="grey", highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.07, relwidth=0.96, relheight=0.75)

        self.codigo_entry = tk.Text(self.frame_1)
        self.codigo_entry.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)

        self.scroll_bar = ttk.Scrollbar(self.frame_1, orient='vertical', command=self.codigo_entry.yview)
        self.scroll_bar.place(relx=0.982, rely=0.0019, relwidth=0.015, relheight=0.99)
        self.codigo_entry['yscrollcommand'] = self.scroll_bar

    def limpa_telaentrada(self):
        self.codigo_entry.delete(1.0, tk.END)

    def botoes(self):
        self.bt_limpar = tk.Button(text="Limpar", bd=2, bg="#FF6347", font=('', 11), command=self.limpa_telaentrada)
        self.bt_limpar.place(relx=0.74, rely=0.92, relwidth=0.1, relheight=0.05)

        self.bt_executar = tk.Button(text="Executar", bd=2, bg="lightgreen", font=('', 11), command=self.chama_analisador)
        self.bt_executar.place(relx=0.85, rely=0.92, relwidth=0.1, relheight=0.05)

    def chama_analisador(self):
        data = self.codigo_entry.get(1.0, "end-1c")
        lexer = lex.lex()
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)

        parser = yacc.yacc()
        parser.parse(data)


root = tk.Tk()
Application(root)
