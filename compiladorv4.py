import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog as fd
from tkinter import messagebox
import ply.lex as lex
import ply.yacc as yacc

# Palavras reservadas
reserved = {
    'IF': 'IF',
    'ELSE': 'ELSE',
    'WHILE': 'WHILE',
    'FOR': 'FOR',
    'BOOLEAN': 'BOOLEAN',
    'PRINTF': 'PRINTF',
    'SCANF': 'SCANF',
    'RETURN': 'RETURN',
}

# Lista de tokens
tokens = [
    'ID',
    'OP_PRIO_ABRE_PARENTESES',  # (
    'OP_PRIO_FECHA_PARENTESES',  # )
    'OP_PRIO_ABRE_CHAVES',  # {
    'OP_PRIO_FECHA_CHAVES',  # }
    'OP_ATRIBUICAO',  # =
    'OP_MAT_MAIS',  # +
    'OP_MAT_MENOS',  # -
    'OP_MAT_VEZES',  # *
    'OP_MAT_DIVIDE',  # /
    'OP_EXEC_PONTO_VIRGULA',  # ;
    'OP_EXEC_VIRGULA',  # ,
    'OP_REL_MENOR',  # <
    'OP_REL_MAIOR',  # >
    'INTEIRO',
    'DOUBLE',
    'STRING',

] + list(reserved.values())

# Expressões regulares para tokens simples

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_IF = r'IF'
t_ELSE = r'ELSE'
t_WHILE = r'WHILE'
t_FOR = r'FOR'
t_BOOLEAN = r'BOOLEAN'
t_PRINTF = r'PRINTF'
t_SCANF = r'SCANF'
t_RETURN = r'RETURN'

t_OP_PRIO_ABRE_PARENTESES = r'\('
t_OP_PRIO_FECHA_PARENTESES = r'\)'
t_OP_PRIO_ABRE_CHAVES = r'\{'
t_OP_PRIO_FECHA_CHAVES = r'\}'
t_OP_ATRIBUICAO = r'\='

t_OP_MAT_MAIS = r'\+'
t_OP_MAT_MENOS = r'-'
t_OP_MAT_VEZES = r'\*'
t_OP_MAT_DIVIDE = r'/'
t_OP_EXEC_PONTO_VIRGULA = r'\;'
t_OP_EXEC_VIRGULA = r'\,'

t_OP_REL_MENOR = r'\<'
t_OP_REL_MAIOR = r'\>'

# Ignorar caracteres em branco
t_ignore = ' \t'

# Tratar quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratar números inteiros
def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Tratar strings delimitadas por aspas duplas
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Remove as aspas duplas
    return t

# Tratar números double
def t_DOUBLE(t):
    r'([0-9]+\.[0-9]+)|([0-9]+\.[0-9]+)'
    return t

# Tratar erros léxicos
erroslexicos = []
def t_error(t):
    erroslexicos.append(t)
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Definição das regras de parsing
def p_programa(p):
    '''programa : declaracoes comandos
                | comandos'''

    # Um programa pode conter apenas declarações ou declarações seguidas de comandos
    print("Tokens ou comandos encontrados:")
    for item in p[1:]:
        print(item)

def p_declaracoes(p):
    '''declaracoes : declaracao OP_EXEC_PONTO_VIRGULA
                   | declaracoes declaracao OP_EXEC_PONTO_VIRGULA'''

    # Uma lista de declarações.

def p_declaracao(p):
    '''declaracao : tipo lista_variaveis declaracao_aux
                  | tipo ID declaracao_aux'''

    # Declaração de variáveis com um tipo e uma lista de variáveis.
    
def p_declaracao_aux(p):
    '''declaracao_aux : OP_ATRIBUICAO expressao
                      | empty'''
    
def p_lista_variaveis(p):
    '''lista_variaveis : ID
                       | lista_variaveis OP_EXEC_VIRGULA ID'''
    # Lista de variáveis separadas por vírgula.


def p_tipo(p):
    '''tipo : DOUBLE
            | BOOLEAN
            | INTEIRO
            | STRING'''
    # Tipos de dados possíveis para variáveis.

def p_comandos(p):
    '''comandos : comando
                | comandos comando'''
    # Lista de comandos.

def p_comando(p):
    '''comando : condicional
               | iterativo
               | atribuicao
               | expressao OP_EXEC_PONTO_VIRGULA
               | leia
               | escreva
               | retorna'''
    # Diferentes tipos de comandos que podem ocorrer no programa.

def p_condicional(p):
    '''condicional : IF OP_PRIO_ABRE_PARENTESES expressao OP_PRIO_FECHA_PARENTESES bloco
                   | IF OP_PRIO_ABRE_PARENTESES expressao OP_PRIO_FECHA_PARENTESES bloco ELSE bloco'''
    # Estrutura condicional (if-else).

def p_iterativo(p):
    '''iterativo : WHILE OP_PRIO_ABRE_PARENTESES expressao OP_PRIO_FECHA_PARENTESES bloco
                 | FOR OP_PRIO_ABRE_PARENTESES atribuicao OP_EXEC_PONTO_VIRGULA expressao OP_EXEC_PONTO_VIRGULA atribuicao OP_PRIO_FECHA_PARENTESES bloco'''
    # Estruturas de repetição (while, for).

def p_bloco(p):
    '''bloco : OP_PRIO_ABRE_CHAVES comandos OP_PRIO_FECHA_CHAVES'''
    # Bloco de código delimitado por chaves.

def p_atribuicao(p):
    '''atribuicao : ID OP_ATRIBUICAO expressao'''
    # Atribuição de valor a uma variável.

def p_expressao(p):
    '''expressao : expressao OP_MAT_MAIS expressao
                 | expressao OP_MAT_MENOS expressao
                 | expressao OP_MAT_VEZES expressao
                 | expressao OP_MAT_DIVIDE expressao
                 | OP_PRIO_ABRE_PARENTESES expressao OP_PRIO_FECHA_PARENTESES
                 | expressao OP_REL_MAIOR expressao
                 | expressao OP_REL_MENOR expressao
                 | INTEIRO
                 | DOUBLE
                 | BOOLEAN
                 | STRING'''
    # Expressões matemáticas e literais.


def p_leia(p):
    '''leia : SCANF OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA ID OP_PRIO_FECHA_PARENTESES OP_EXEC_PONTO_VIRGULA'''
    # Comando de leitura de entrada.

def p_escreva(p):
    '''escreva : PRINTF OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA expressao OP_PRIO_FECHA_PARENTESES OP_EXEC_PONTO_VIRGULA'''
    # Comando de saída.

def p_empty(p):
    'empty :'
    pass

def p_retorna(p):
    '''retorna : RETURN expressao OP_EXEC_PONTO_VIRGULA'''
    # Comando de retorno.

#determina a precedência e associatividade dos operadores na linguagem
precedence = (
    ('left', 'OP_MAT_MAIS', 'OP_MAT_MENOS'),
    ('left', 'OP_MAT_VEZES', 'OP_MAT_DIVIDE'),
)

# Construir o lexer
lexer = lex.lex()

# Construir o parser
parser = yacc.yacc()

class Application():
    def __init__(self, root):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.menus()

    def tela(self):
        self.root.title("Analisador Léxico e Sintático")
        self.root.configure(background="white")
        self.root.geometry("900x600")  # Alterando a geometria da janela principal
        self.root.resizable(True, True)
        self.root.minsize(width=700, height=500)

    def frames_da_tela(self):
        self.frame_codigo_fonte = tk.Frame(self.root, bd=4, bg="#DCDCDC", highlightbackground="grey", highlightthickness=3)
        self.frame_codigo_fonte.place(relx=0.02, rely=0.02, relwidth=0.46, relheight=0.45)

        self.frame_analise = tk.Frame(self.root, bd=4, bg="#DCDCDC", highlightbackground="grey", highlightthickness=3)
        self.frame_analise.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.2)  # Reduzindo altura e aumentando largura

        self.frame_codigo_python = tk.Frame(self.root, bd=4, bg="#DCDCDC", highlightbackground="grey", highlightthickness=3)
        self.frame_codigo_python.place(relx=0.52, rely=0.02, relwidth=0.46, relheight=0.45)

        # Adicionando títulos
        self.lb_codigo_fonte = tk.Label(self.root, text="Código Fonte", bg="white", font=('', 12))
        self.lb_codigo_fonte.place(relx=0.02, rely=0.01)

        self.lb_analise = tk.Label(self.root, text="Análise Léxica e Sintática", bg="white", font=('', 12))
        self.lb_analise.place(relx=0.02, rely=0.49)

        self.lb_codigo_python = tk.Label(self.root, text="Código Transpilado", bg="white", font=('', 12))
        self.lb_codigo_python.place(relx=0.52, rely=0.01)

        self.codigo_entry = tk.Text(self.frame_codigo_fonte)
        self.codigo_entry.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)

        self.scroll_bar = ttk.Scrollbar(self.frame_codigo_fonte, orient='vertical', command=self.codigo_entry.yview)
        self.scroll_bar.place(relx=0.982, rely=0.0019, relwidth=0.015, relheight=0.99)
        self.codigo_entry['yscrollcommand'] = self.scroll_bar

        self.tree = ttk.Treeview(self.frame_analise, height=3, columns=('col0', 'col1', 'col2', 'col3'))
        self.tree.heading("#0", text='Tokens')
        self.tree.heading("#1", text='Lexemas')
        self.tree.heading("#2", text='Expressão Regular')
        self.tree.heading("#3", text='Descrição')
        self.tree.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)

        self.codigo_python_entry = tk.Text(self.frame_codigo_python)
        self.codigo_python_entry.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)
        self.codigo_python_entry.config(state=tk.DISABLED)

        self.scroll_bar_python = ttk.Scrollbar(self.frame_codigo_python, orient='vertical', command=self.codigo_python_entry.yview)
        self.scroll_bar_python.place(relx=0.982, rely=0.0019, relwidth=0.015, relheight=0.99)
        self.codigo_python_entry['yscrollcommand'] = self.scroll_bar_python

    def limpa_telaentrada(self):
        self.codigo_entry.delete(1.0, tk.END)

    def botoes(self):
        self.bt_limpar = tk.Button(text="Limpar", bd=2, bg="#FF6347", font=('', 11), command=self.limpa_telaentrada)
        self.bt_limpar.place(relx=0.3, rely=0.92, relwidth=0.1, relheight=0.05)

        self.bt_converter_python = tk.Button(text="Converter para Python", bd=2, bg="lightblue", font=('', 11), command=self.converter_para_python)
        self.bt_converter_python.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.05)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)

        def Quit(): self.root.destroy()

        def onOpen():
            tf = fd.askopenfilename(
                initialdir="C:/Users/MainFrame/Desktop/",
                title="Open Text file",
                filetypes=(("Text Files", "*.txt"),)
            )
            tf = open(tf, 'r')
            entrada = tf.read()
            self.codigo_entry.insert(tk.END, entrada)
            tf.close()

        def onSave():
            files = fd.asksaveasfile(mode='w', defaultextension=".txt")
            t = self.codigo_entry.get(1.0, tk.END)
            files.write(t.rstrip())

        def mostrar_tabela_tokens():
            new_window = tk.Toplevel(self.root)
            new_window.title("Tabela de Tokens")
            new_window.geometry("600x400")

            tree = ttk.Treeview(new_window, height=20, columns=('col1', 'col2', 'col3', 'col4'))
            tree.heading("#0", text='Token')
            tree.heading("#1", text='Lexema')
            tree.heading("#2", text='Expressão Regular')
            tree.heading("#3", text='Descrição')

            # Adicionando os tokens à Treeview
            tokens = [
                ("IF", "if", "if", "Palavra reservada if"),
                ("ELSE", "else", "else", "Palavra reservada else"),
                ("WHILE", "while", "while", "Palavra reservada while"),
                # Adicionar os outros tokens
            ]

            for idx, token in enumerate(tokens, start=1):
                tree.insert('', idx, text='', values=token)

            tree.pack(expand=True, fill='both')

        menubar.add_cascade(label="Arquivos", menu=filemenu)
        filemenu.add_command(label="Abrir Código Fonte", command=onOpen)
        filemenu.add_command(label="Salvar como", command=onSave)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=Quit)

        tabela_tokens_menu = Menu(menubar)
        menubar.add_cascade(label="Tabela de Tokens", menu=tabela_tokens_menu)
        tabela_tokens_menu.add_command(label="Mostrar Tabela", command=mostrar_tabela_tokens)

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

        self.mostrar_tokens(parser)

    def mostrar_tokens(self, parser):
        # Limpar a Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Adicionar tokens ao Treeview
        for token in parser._token_list:
            self.tree.insert('', tk.END, values=(token.type, token.value, '', ''))

    def converter_para_python(self):
        data = self.codigo_entry.get(1.0, "end-1c")
        codigo_python = ""

        lexer = lex.lex()
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            # perguntar ao professor se preciso adicionar lógica para converter tokens

        parser = yacc.yacc()
        parser.parse(data)

        # Traduzindo para Python
        for line in data.split('\n'):
            if line.startswith('se'):
                codigo_python += f"if {line[2:]}:\n"
            elif line.startswith('senao'):
                codigo_python += f"else:\n"
            elif line.startswith('enquanto'):
                codigo_python += f"while {line[8:]}:\n"
            elif line.startswith('para'):
                # Implementação do for em Python pode variar dependendo da estrutura da sua linguagem
                # Aqui está um exemplo simples, você pode precisar adaptar conforme necessário
                partes = line[5:].split(' ')
                codigo_python += f"for {partes[0]} in range({partes[2]}):\n"
            elif line.startswith('leia'):
                codigo_python += f"{line[4:]} = input()\n"
            elif line.startswith('escreva'):
                codigo_python += f"print({line[7:]})\n"
            elif line.startswith('retorna'):
                codigo_python += f"return {line[8:]}\n"
            else:
                codigo_python += f"{line}\n"

        # Atualizando o campo de texto com o código Python resultante
        self.codigo_python_entry.config(state=tk.NORMAL)
        self.codigo_python_entry.delete(1.0, tk.END)
        self.codigo_python_entry.insert(tk.END, codigo_python)
        self.codigo_python_entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
