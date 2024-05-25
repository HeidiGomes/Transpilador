import ply.lex as lex
from ply import yacc
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Análise Léxica
reserved = {
   'SE': 'SE',
   'ELSE': 'ELSE',
   'ENQUANTO': 'ENQUANTO',
   'PARA': 'PARA',
   'ESCREVA': 'ESCREVA',
   'LEIA': 'LEIA',
   'EM' : 'EM',
   'RANGE' : 'RANGE',
}

tokens = [
    'INTEIRO',
    'DOUBLE',
    'STRING',
    'INT',
    'VARIAVEL',
    'OP_MAT_ADICAO',
    'OP_MAT_SUB',
    'OP_MAT_MULT',
    'OP_MAT_POT',
    'OP_MAT_DIV',
    'OP_EXEC_VIRGULA',
    'OP_ATRIB_IGUAL',
    'OP_ATRIB_MAIS_IGUAL',
    'OP_REL_DUPLO_IGUAL',
    'OP_REL_MENOR',
    'OP_REL_MAIOR',
    'OP_FINAL_LINHA_PONTO_VIRGULA', 
    'OP_PRIO_ABRE_PARENTESES',
    'OP_PRIO_FECHA_PARENTESES',
    #'OP_PRIO_ABRE_COLCHETES',
    #'OP_PRIO_FECHA_COLCHETES',
    'OP_PRIO_ABRE_CHAVES',
    'OP_PRIO_FECHA_CHAVES',
] + list(reserved.values())  # Concatenando com as palavras reservadas para verificação

# Regras de expressão regular (RegEx) para tokens simples
t_ENQUANTO = r'ENQUANTO'
t_SE = r'SE'
t_ELSE = r'ELSE'
t_PARA = r'PARA'
t_ESCREVA = r'ESCREVA'
t_LEIA = r'LEIA'
t_EM = r'EM'
t_RANGE = r'RANGE'
t_OP_MAT_ADICAO = r'\+'
t_OP_MAT_SUB = r'-'
t_OP_MAT_MULT = r'\*'
t_OP_MAT_POT = r'\*\*'
t_OP_MAT_DIV = r'/'
t_OP_FINAL_LINHA_PONTO_VIRGULA = r'\;'
t_OP_EXEC_VIRGULA = r'\,'
t_OP_ATRIB_IGUAL = r'\='
t_OP_ATRIB_MAIS_IGUAL = r'\+\='
t_OP_REL_DUPLO_IGUAL = r'\=\='
t_OP_REL_MENOR = r'\<'
t_OP_REL_MAIOR = r'\>'
t_OP_PRIO_ABRE_PARENTESES = r'\('
t_OP_PRIO_FECHA_PARENTESES = r'\)'
#t_OP_PRIO_ABRE_COLCHETES = r'\['
#t_OP_PRIO_FECHA_COLCHETES = r'\]'
t_OP_PRIO_ABRE_CHAVES = r'\{'
t_OP_PRIO_FECHA_CHAVES = r'\}'

t_ignore = ' \t'  # Ignora espaço e tabulação

# Regras de expressão regular (RegEx) para tokens mais "complexos"


def t_STRING(t):
    r'("[^"]*")'
    return t

def t_DOUBLE(t):
    r'([0-9]+\.[0-9]+)|([0-9]+\.[0-9]+)'
    return t

def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIAVEL(t):
    r'[a-z][a-z_0-9]*'
    return t

def t_INT(t):
    r'INT'
    return t

# Define uma regra para que seja possível rastrear o números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra de tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append(t)
    t.lexer.skip(1)

# Análise Sintática

def p_declaracoes_single(p):
    '''
    declaracoes : declaracao
    '''

def p_declaracoes_mult(p):
    '''
    declaracoes :  declaracao bloco
    '''

def p_bloco(p):
    '''
    bloco : OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES declaracao bloco OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES escrita impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES escrita escrita impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES escrita escrita expr impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES impressao param_cond OP_FINAL_LINHA_PONTO_VIRGULA OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES param_cond OP_FINAL_LINHA_PONTO_VIRGULA impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES impressao expr OP_PRIO_FECHA_CHAVES
          
    '''

def p_declaracao_ENQUANTO(p):
    '''
    declaracao : ENQUANTO param_cond bloco
               | declaracao ENQUANTO param_cond bloco
    '''

def p_declaracao_para(p):
    '''
    declaracao : PARA VARIAVEL EM RANGE OP_PRIO_ABRE_PARENTESES INTEIRO OP_EXEC_VIRGULA INTEIRO OP_PRIO_FECHA_PARENTESES bloco
               | PARA VARIAVEL EM RANGE OP_PRIO_ABRE_PARENTESES DOUBLE OP_EXEC_VIRGULA DOUBLE OP_PRIO_FECHA_PARENTESES bloco
    '''

def p_declaracao_atribuicaoValorVariavel(p):
    '''
    declaracao : VARIAVEL OP_ATRIB_IGUAL expr OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL STRING OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL DOUBLE OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_IGUAL funcao OP_FINAL_LINHA_PONTO_VIRGULA
            | param VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
            | VARIAVEL OP_ATRIB_MAIS_IGUAL INTEIRO
            | VARIAVEL OP_ATRIB_MAIS_IGUAL DOUBLE
            | VARIAVEL OP_ATRIB_MAIS_IGUAL VARIAVEL
    '''

def p_declaracao_condicionais(p):
    '''
    declaracao : SE param_cond bloco
               | declaracao SE param_cond bloco
               | declaracao SE param_cond bloco senao
               | SE param_cond bloco senao
    '''

def p_declaracao_funcao_invocada(p):
    '''
    declaracao : funcao OP_FINAL_LINHA_PONTO_VIRGULA
               | impressao
               | escrita
    '''

def p_declaracao_definir_funcao(p):
    '''
    declaracao : funcao OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES
    '''

def p_parametro_condicional(p):
    '''
    param_cond :  VARIAVEL OP_REL_MENOR INTEIRO
                | VARIAVEL OP_REL_MENOR DOUBLE
                | VARIAVEL OP_REL_MENOR VARIAVEL
                | VARIAVEL OP_REL_MAIOR INTEIRO
                | VARIAVEL OP_REL_MAIOR DOUBLE
                | VARIAVEL OP_REL_MAIOR VARIAVEL
                | VARIAVEL OP_ATRIB_MAIS_IGUAL INTEIRO
                | VARIAVEL OP_ATRIB_MAIS_IGUAL DOUBLE
                | VARIAVEL OP_ATRIB_MAIS_IGUAL VARIAVEL
                | VARIAVEL OP_REL_DUPLO_IGUAL INTEIRO
                | VARIAVEL OP_REL_DUPLO_IGUAL DOUBLE
                | VARIAVEL OP_REL_DUPLO_IGUAL VARIAVEL

    '''

def p_impressao(p):
    '''impressao : ESCREVA expr OP_FINAL_LINHA_PONTO_VIRGULA
                 | ESCREVA expr OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
                 | ESCREVA OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
                 | ESCREVA OP_PRIO_ABRE_PARENTESES  STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
    '''

def p_escrita(p):
    '''escrita : VARIAVEL OP_ATRIB_IGUAL LEIA OP_PRIO_ABRE_PARENTESES expr OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
               | VARIAVEL OP_ATRIB_IGUAL param OP_PRIO_ABRE_PARENTESES LEIA OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA
               | VARIAVEL OP_ATRIB_IGUAL LEIA OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA 
               | VARIAVEL OP_ATRIB_IGUAL LEIA OP_PRIO_ABRE_PARENTESES STRING VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA 
    '''


def p_expressao_variavel(p):
    '''
    expr :  VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_SUB INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_SUB VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_MULT INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_MULT VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_DIV INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_DIV VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_POT INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA
         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_POT VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA
    '''


def p_expressao_operacao(p):
    '''
    expr : expr OP_MAT_ADICAO expr
        |  expr OP_MAT_SUB expr
        |  expr OP_MAT_MULT expr
        |  expr OP_MAT_DIV expr
        |  expr OP_MAT_POT expr
    '''

def p_parametro_vazio(p):
    '''
    param_vazio :
    '''


def p_parametro(p):
    '''
    param : INTEIRO
        | INT
        | DOUBLE
        | STRING
        | VARIAVEL
    '''

def p_regra_funcao(p):
    '''
    funcao :  OP_PRIO_ABRE_PARENTESES param_vazio OP_PRIO_FECHA_PARENTESES
        |  OP_PRIO_ABRE_PARENTESES param OP_PRIO_FECHA_PARENTESES
    '''

def p_senao_se(p):
    '''
    senao : ELSE bloco
    '''

# Define a precedência e associação dos operadores matemáticos
precedence = (
    ('left', 'OP_MAT_ADICAO', 'OP_MAT_SUB'),
    ('left', 'OP_MAT_MULT', 'OP_MAT_DIV','OP_MAT_POT'),
)

errossintaticos = []
def p_error(p):
    errossintaticos.append(p)
    if p:
        print("ERRO SINTÁTICO: ", p)
    else:
        print("ERRO SINTÁTICO: erro de sintaxe desconhecido")

parser = yacc.yacc()

erros = 0

# função padrão para adicionar as classificações dos tokens para ser impressa pelo compilador
def add_lista_saida(t, notificacao):
    saidas.append(( t.type, t.value, notificacao))

saidas = []


root = tk.Tk()  # cria a janela


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.Menus()
        self.dark_mode = False  # Modo claro inicial
        self.toggle_dark_mode()  # Ajusta a aparência de acordo com o modo
        self.root.mainloop()

    def limpa_telaentrada(self):
        self.codigo_entry.delete(1.0, tk.END)
        for i in self.saida.get_children():
            self.saida.delete(i)
        saidas.clear()
        erroslexicos.clear()
        errossintaticos.clear()
        global erros
        erros = 0
        self.frame_1.update()
        self.frame_2.update()
        self.frame_3.update()
        root.update()

    def tela(self):
        self.root.title("Transpilador")
        self.root.configure(background="white")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        self.root.minsize(width=700, height=500)

    def frames_da_tela(self):
        # Label Código Fonte
        self.lb_codigo = tk.Label(text="Código Fonte", bg="white", font=('', 12))
        self.lb_codigo.place(relx=0.001, rely=0.02, relwidth=0.2, relheight=0.05)

        # Frame Código Fonte
        self.frame_1 = tk.Frame(self.root, bd=4, bg="#DCDCDC", highlightbackground="white", highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.07, relwidth=0.46, relheight=0.55)

        # Frame Código Python
        self.frame_3 = tk.Frame(self.root, bd=4, bg="#DCDCDC", highlightbackground="grey", highlightthickness=3)
        self.frame_3.place(relx=0.52, rely=0.07, relwidth=0.46, relheight=0.55)

        # Label Código Python
        self.lb_codigo_python = tk.Label(text="Código Python", bg="white", font=('', 12))
        self.lb_codigo_python.place(relx=0.51, rely=0.02, relwidth=0.2, relheight=0.05)

        # Código Python Entry
        self.codigo_python_entry = tk.Text(self.frame_3)
        self.codigo_python_entry.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)

        # Label Análise Léxica e Sintática
        self.lb_analise = tk.Label(text="Análise Léxica e Sintática", bg="white", font=('', 12))
        self.lb_analise.place(relx=0.05, rely=0.63, relwidth=0.2, relheight=0.05)

        # Frame do Analisador lexico e sintatico
        self.frame_2 = tk.Frame(self.root, bd=4, bg="#DCDCDC", highlightbackground="grey", highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.70, relwidth=0.96, relheight=0.20)

    def chama_analisador(self):
        columns = ('token', 'lexema', 'notificacao')
        self.saida = ttk.Treeview(self.frame_2, height=5, columns=columns, show='headings')
        self.saida.heading("token", text='Token')
        self.saida.heading("lexema", text='Lexema')
        self.saida.heading("notificacao", text='Notificacao')

        # Adicionar barra de rolagem vertical
        scrollbar = ttk.Scrollbar(self.frame_2, orient='vertical', command=self.saida.yview)
        scrollbar.place(relx=0.975, rely=0, relheight=0.96)
        self.saida.configure(yscrollcommand=scrollbar.set)

        data = self.codigo_entry.get(1.0, "end-1c")
        lexer = lex.lex()
        lexer.input(data)

        print("Análise Léxica:")
        # Tokenizar a entrada para passar para o analisador léxico
        for tok in lexer:
            print("Token:", tok.type)
            print("Valor:", tok.value)
            global erros
            if tok.type == "INTEIRO":
                max = (len(str(tok.value)))
                if max > 15:
                    erros += 1
                    add_lista_saida(tok, f"entrada maior que a suportada")
                else:
                    add_lista_saida(tok, f" ")
            elif tok.type == "SE" or tok.type == "ELSE" or tok.type == "ENQUANTO" or tok.type == "PARA" or tok.type == "ESCREVA" or tok.type == "IN" or tok.type == "RANGE" or tok.type == "LEIA":
                max = len(tok.value)
                if max < 20:
                    if tok.value in reserved:
                        tok.type = reserved[tok.value]
                        add_lista_saida(tok, f"palavra reservada")
                    else:
                        add_lista_saida(tok, f" ")
            else:
                add_lista_saida(tok, f" ")

        for tok in erroslexicos:
            add_lista_saida(tok, f"Caracter Inválido na linguagem")

        tamerroslex = len(erroslexicos)
        if tamerroslex == 0 and erros == 0:
            self.saida.insert('', tk.END, values="Análise Léxica Concluída sem Erros")
            parser.parse(data)
            tamerrosin = len(errossintaticos)
            if tamerrosin == 0:
                self.saida.insert('', tk.END, values="Análise Sintática Concluída sem Erros")
            else:
                self.saida.insert('', tk.END, values="Erro Sintático")
        else:
            self.saida.insert('', tk.END, values="Erro Léxico")

        for retorno in saidas:
            self.saida.insert('', tk.END, values=retorno)

        self.saida.place(relx=0.001, rely=0.01, relwidth=0.97, relheight=0.95)

    def transpilar_codigo(self):
        codigo_fonte = self.codigo_entry.get(1.0, tk.END)
        codigo_transpilado = self.transpilar_para_python(codigo_fonte)
        self.mostrar_codigo_transpilado(codigo_transpilado)

    def transpilar_para_python(self, codigo_fonte):
        # Remover o ponto e vírgula no final da linha e espaços em branco subsequentes
        codigo_fonte = codigo_fonte.replace(';', '').rstrip()

        # Substituir PARA por for
        codigo_fonte = codigo_fonte.replace('PARA', 'for')

        codigo_fonte = codigo_fonte.replace('ELSE', 'else')

        # Substituir LEIA por input
        codigo_fonte = codigo_fonte.replace('LEIA', 'input')

        # Substituir SE por if e ELSE por else
        codigo_fonte = codigo_fonte.replace('SE', 'if')

        # Substituir ESCREVA por print
        codigo_fonte = codigo_fonte.replace('ESCREVA', 'print')

        # Substituir chaves por indentação
        codigo_fonte = codigo_fonte.replace('{', '').replace('}', '')

        # Remover ':' após a linha 'x = 11'
        codigo_fonte = codigo_fonte.replace('x = 11\n:', 'x = 11\n')

        # Substituir acentos
        codigo_fonte = codigo_fonte.replace('eh', 'é')

        # Corrigir formatação da string dentro da função ESCREVA
        in_string = False
        temp = ''
        word = ''
        for char in codigo_fonte:
            if char == '"':
                in_string = not in_string
            if not in_string:
                if char.isalpha():
                    word += char
                else:
                    if word == 'RANGE':
                        temp += 'range'
                    elif word == 'EM':
                        temp += 'in'
                    elif word == 'INT':
                        temp += 'int'
                    else:
                        temp += word
                    word = ''
                    temp += char
            else:
                temp += char
        codigo_fonte = temp

        # transpilar a estrutura ENQUANTO
        codigo_fonte = codigo_fonte.replace('ENQUANTO', 'while')

        # Transpilar atribuição de valor a uma variável
        codigo_fonte = codigo_fonte.replace('OP_ATRIB_IGUAL', '=')

        # Corrigir indentação
        linhas = codigo_fonte.split('\n')
        for i in range(len(linhas)):
            linha = linhas[i].strip()
            if linha.startswith(('if', 'else', 'while', 'for')):
                # Adicionar ':' se ainda não estiver presente
                if not linha.endswith(':'):
                    linhas[i] = linha + ':'
            # Corrigir indentação do bloco else
            elif linha.startswith('else'):
                if i > 0 and linhas[i-1].strip().endswith(':'):
                    linhas[i] = ' ' + linha
                else:
                    if i+1 < len(linhas) and not linhas[i+1].strip().startswith('print'):
                        linhas[i+1] = '    ' + linhas[i+1]
                        linhas[i] = ' ' + linha

        codigo_fonte = '\n'.join(linhas)

        return codigo_fonte

    
    
    def mostrar_codigo_transpilado(self, codigo_transpilado):
        # Limpar a área de visualização do código Python
        self.codigo_python_entry.delete(1.0, tk.END)
        # Exibir o código Python transpilado na área de visualização
        self.codigo_python_entry.insert(tk.END, codigo_transpilado)

    def botoes(self):
        self.bt_limpar = tk.Button(text="Limpar", bd=2, bg="#FF6347", font=('', 11), command=self.limpa_telaentrada)
        self.bt_limpar.place(relx=0.74, rely=0.92, relwidth=0.1, relheight=0.05)

        self.bt_transpilar = tk.Button(text="Transpilar", bd=2, bg="#87CEEB", font=('', 11),
                                       command=lambda: [self.chama_analisador(), self.transpilar_codigo()])
        self.bt_transpilar.place(relx=0.63, rely=0.92, relwidth=0.1, relheight=0.05)

        self.bt_toggle_mode = tk.Button(text="Modo Escuro", bd=2, bg="#FFFF00", font=('', 11),
                                        command=self.toggle_dark_mode)
        self.bt_toggle_mode.place(relx=0.85, rely=0.92, relwidth=0.1, relheight=0.05)

        self.codigo_entry = tk.Text(self.frame_1)
        self.codigo_entry.place(relx=0.001, rely=0.001, relwidth=0.995, relheight=0.995)

        self.scroll_bar = ttk.Scrollbar(self.frame_1, orient='vertical', command=self.codigo_entry.yview)
        self.scroll_bar.place(relx=0.982, rely=0.0019, relwidth=0.015, relheight=0.99)
        self.codigo_entry['yscrollcommand'] = self.scroll_bar


    def Menus(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar)

        def Quit(): self.root.destroy()

        def onOpen():
            tf = filedialog.askopenfilename(
                initialdir="C:/Users/MainFrame/Desktop/",
                title="Open Text file",
                filetypes=(("Text Files", "*.txt"),)
            )
            tf = open(tf, 'r')
            entrada = tf.read()
            self.codigo_entry.insert(tk.END, entrada)
            tf.close()

        def onSave():
            files = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            t = self.codigo_python_entry.get(1.0, tk.END)
            files.write(t.rstrip())

        menubar.add_cascade(label="Menu", menu=filemenu,)
        filemenu.add_command(label="Abrir", command=onOpen)
        filemenu.add_command(label="Salvar", command=onSave)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=Quit)


            # Função para alternar entre modos claro e escuro
    def toggle_dark_mode(self):
        if self.dark_mode:
            # Mudar para modo claro
            self.root.configure(background="white")
            self.bt_toggle_mode.configure(text="Modo Escuro", bg="#FFFF00")
        else:
            # Mudar para modo escuro
            self.root.configure(background="black")
            self.bt_toggle_mode.configure(text="Modo Claro", bg="#FFD700")

        # Inverter o valor do modo
        self.dark_mode = not self.dark_mode

app = Application()