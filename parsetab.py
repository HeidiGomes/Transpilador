
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOP_MAT_ADICAOOP_MAT_SUBleftOP_MAT_MULTOP_MAT_DIVDOUBLE ELIF ELSE FOR IF INTEIRO OP_ATRIB_IGUAL OP_EXEC_VIRGULA OP_FINAL_LINHA_PONTO_VIRGULA OP_MAT_ADICAO OP_MAT_DIV OP_MAT_MULT OP_MAT_SUB OP_PRIO_ABRE_CHAVES OP_PRIO_ABRE_COLCHETES OP_PRIO_ABRE_PARENTESES OP_PRIO_FECHA_CHAVES OP_PRIO_FECHA_COLCHETES OP_PRIO_FECHA_PARENTESES OP_REL_MAIOR OP_REL_MENOR PRINTF SCANF STRING VARIAVEL WHILE string_mal_formada\n    declaracoes : declaracao\n    \n    bloco : OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n          \n    \n    declaracao : WHILE OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES bloco\n    \n    declaracao : FOR OP_PRIO_ABRE_PARENTESES VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_EXEC_VIRGULA param_cond OP_EXEC_VIRGULA VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO  OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n               | FOR OP_PRIO_ABRE_PARENTESES VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_EXEC_VIRGULA param_cond OP_EXEC_VIRGULA VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO  OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n               | FOR OP_PRIO_ABRE_PARENTESES VARIAVEL param_cond OP_EXEC_VIRGULA VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO  OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n    \n    declaracao : VARIAVEL OP_ATRIB_IGUAL expr OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL STRING OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL DOUBLE OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL funcao OP_FINAL_LINHA_PONTO_VIRGULA\n            | param VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA\n    \n    declaracao : IF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n            | IF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES senaose\n            | IF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES senaose ELSE OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n            | IF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES ELSE OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n    \n    declaracao : funcao OP_FINAL_LINHA_PONTO_VIRGULA\n               | impressao\n               | escrita\n               | \n    \n    declaracao : funcao OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n    \n    param_cond :  VARIAVEL OP_REL_MENOR INTEIRO\n                | VARIAVEL OP_REL_MENOR DOUBLE\n                | VARIAVEL OP_REL_MENOR VARIAVEL\n                | VARIAVEL OP_REL_MAIOR INTEIRO\n                | VARIAVEL OP_REL_MAIOR DOUBLE\n                | VARIAVEL OP_REL_MAIOR VARIAVEL\n\n    impressao : PRINTF expr OP_FINAL_LINHA_PONTO_VIRGULA\n                 | PRINTF expr OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA\n                 | PRINTF OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA\n                 | PRINTF OP_PRIO_ABRE_PARENTESES  STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA\n    escrita : VARIAVEL OP_ATRIB_IGUAL SCANF OP_PRIO_ABRE_PARENTESES expr OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA\n               | VARIAVEL OP_ATRIB_IGUAL SCANF OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA \n               | VARIAVEL OP_ATRIB_IGUAL SCANF OP_PRIO_ABRE_PARENTESES STRING VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA \n    \n    expr :  VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA\n    \n    expr : expr OP_MAT_ADICAO expr\n        |  expr OP_MAT_SUB expr\n        |  expr OP_MAT_MULT expr\n        |  expr OP_MAT_DIV expr\n    \n    param_vazio :\n    \n    param : INTEIRO\n        | DOUBLE\n        | STRING\n        | VARIAVEL\n    \n    funcao :  OP_PRIO_ABRE_PARENTESES param_vazio OP_PRIO_FECHA_PARENTESES\n        |  OP_PRIO_ABRE_PARENTESES param OP_PRIO_FECHA_PARENTESES\n    \n    senaose : ELIF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n    '
    
_lr_action_items = {'WHILE':([0,23,75,88,124,129,140,142,151,152,],[3,3,3,3,3,3,3,3,3,3,]),'FOR':([0,23,75,88,124,129,140,142,151,152,],[5,5,5,5,5,5,5,5,5,5,]),'VARIAVEL':([0,4,6,7,8,9,11,15,16,20,21,23,25,33,46,47,48,49,53,54,55,63,73,75,84,86,88,89,93,94,105,112,113,124,125,126,127,129,140,142,151,152,],[6,19,-45,-42,-44,-43,24,28,30,33,34,6,30,30,28,28,28,28,76,79,82,28,91,6,95,97,6,100,30,30,114,120,121,6,30,132,133,6,6,6,6,6,]),'IF':([0,23,75,88,124,129,140,142,151,152,],[12,12,12,12,12,12,12,12,12,12,]),'$end':([0,1,2,13,14,22,44,57,58,59,60,61,62,64,74,87,90,102,106,108,109,111,115,116,119,136,141,149,150,155,156,],[-21,0,-1,-19,-20,-18,-29,-9,-7,-8,-10,-11,-12,-22,-3,-13,-31,-2,-33,-34,-14,-32,-35,-15,-30,-17,-16,-6,-48,-5,-4,]),'INTEIRO':([0,4,21,23,42,53,54,55,75,88,122,124,129,138,139,140,142,151,152,],[7,7,37,7,65,77,80,83,7,7,128,7,7,143,144,7,7,7,7,]),'DOUBLE':([0,4,21,23,53,54,75,88,124,129,140,142,151,152,],[9,9,38,9,78,81,9,9,9,9,9,9,9,9,]),'STRING':([0,4,21,23,27,45,63,75,88,124,129,140,142,151,152,],[8,8,36,8,50,67,86,8,8,8,8,8,8,8,8,]),'OP_PRIO_ABRE_PARENTESES':([0,3,5,12,15,21,23,26,40,51,68,69,70,71,75,88,118,124,129,140,142,151,152,],[4,16,20,25,27,4,4,45,63,-36,-37,-38,-39,-40,4,4,125,4,4,4,4,4,4,]),'PRINTF':([0,23,75,88,124,129,140,142,151,152,],[15,15,15,15,15,15,15,15,15,15,]),'OP_PRIO_FECHA_CHAVES':([2,13,14,22,23,41,44,57,58,59,60,61,62,64,74,75,87,88,90,92,99,102,106,108,109,111,115,116,119,124,129,130,135,136,140,141,142,145,146,149,150,151,152,153,154,155,156,],[-1,-19,-20,-18,-21,64,-29,-9,-7,-8,-10,-11,-12,-22,-3,-21,-13,-21,-31,102,109,-2,-33,-34,-14,-32,-35,-15,-30,-21,-21,136,141,-17,-21,-16,-21,149,150,-6,-48,-21,-21,155,156,-5,-4,]),'OP_PRIO_FECHA_PARENTESES':([4,7,8,9,17,18,19,29,43,50,51,68,69,70,71,76,77,78,79,80,81,85,86,91,97,100,128,131,143,144,],[-41,-42,-44,-43,31,32,-45,52,66,72,-36,-37,-38,-39,-40,-25,-23,-24,-28,-26,-27,96,98,101,107,110,134,137,147,148,]),'OP_ATRIB_IGUAL':([6,24,33,95,120,121,],[21,42,55,105,126,127,]),'OP_FINAL_LINHA_PONTO_VIRGULA':([10,26,28,31,32,34,35,36,37,38,39,51,57,65,68,69,70,71,72,96,98,101,107,110,],[22,44,51,-46,-47,57,58,59,60,61,62,-36,-36,87,-37,-38,-39,-40,90,106,108,111,115,119,]),'OP_PRIO_ABRE_CHAVES':([10,31,32,52,66,117,123,134,137,147,148,],[23,-46,-47,75,88,124,129,140,142,151,152,]),'SCANF':([21,],[40,]),'OP_MAT_ADICAO':([26,35,51,57,68,69,70,71,85,114,132,133,],[46,46,-36,-36,-37,-38,-39,-40,46,122,138,139,]),'OP_MAT_SUB':([26,35,51,57,68,69,70,71,85,],[47,47,-36,-36,-37,-38,-39,-40,47,]),'OP_MAT_MULT':([26,35,51,57,68,69,70,71,85,],[48,48,-36,-36,48,48,-39,-40,48,]),'OP_MAT_DIV':([26,35,51,57,68,69,70,71,85,],[49,49,-36,-36,49,49,-39,-40,49,]),'OP_REL_MENOR':([30,],[53,]),'OP_REL_MAIOR':([30,],[54,]),'OP_EXEC_VIRGULA':([50,56,67,76,77,78,79,80,81,82,83,103,104,],[73,84,89,-25,-23,-24,-28,-26,-27,93,94,112,113,]),'ELSE':([109,116,150,],[117,123,-48,]),'ELIF':([109,],[118,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracoes':([0,23,75,88,124,129,140,142,151,152,],[1,41,92,99,130,135,145,146,153,154,]),'declaracao':([0,23,75,88,124,129,140,142,151,152,],[2,2,2,2,2,2,2,2,2,2,]),'funcao':([0,21,23,75,88,124,129,140,142,151,152,],[10,39,10,10,10,10,10,10,10,10,10,]),'param':([0,4,23,75,88,124,129,140,142,151,152,],[11,18,11,11,11,11,11,11,11,11,11,]),'impressao':([0,23,75,88,124,129,140,142,151,152,],[13,13,13,13,13,13,13,13,13,13,]),'escrita':([0,23,75,88,124,129,140,142,151,152,],[14,14,14,14,14,14,14,14,14,14,]),'param_vazio':([4,],[17,]),'expr':([15,21,46,47,48,49,63,],[26,35,68,69,70,71,85,]),'param_cond':([16,25,33,93,94,125,],[29,43,56,103,104,131,]),'bloco':([52,],[74,]),'senaose':([109,],[116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracoes","S'",1,None,None,None),
  ('declaracoes -> declaracao','declaracoes',1,'p_declaracoes','main.py',107),
  ('bloco -> OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','bloco',3,'p_bloco','main.py',112),
  ('declaracao -> WHILE OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES bloco','declaracao',5,'p_declaracao_while','main.py',118),
  ('declaracao -> FOR OP_PRIO_ABRE_PARENTESES VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_EXEC_VIRGULA param_cond OP_EXEC_VIRGULA VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','declaracao',17,'p_declaracao_para','main.py',123),
  ('declaracao -> FOR OP_PRIO_ABRE_PARENTESES VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_EXEC_VIRGULA param_cond OP_EXEC_VIRGULA VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','declaracao',17,'p_declaracao_para','main.py',124),
  ('declaracao -> FOR OP_PRIO_ABRE_PARENTESES VARIAVEL param_cond OP_EXEC_VIRGULA VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','declaracao',14,'p_declaracao_para','main.py',125),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL expr OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',130),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL STRING OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',131),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',132),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',133),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL DOUBLE OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',134),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL funcao OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',135),
  ('declaracao -> param VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',5,'p_declaracao_atribuicaoValorVariavel','main.py',136),
  ('declaracao -> IF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','declaracao',7,'p_declaracao_condicionais','main.py',141),
  ('declaracao -> IF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES senaose','declaracao',8,'p_declaracao_condicionais','main.py',142),
  ('declaracao -> IF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES senaose ELSE OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','declaracao',12,'p_declaracao_condicionais','main.py',143),
  ('declaracao -> IF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES ELSE OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','declaracao',11,'p_declaracao_condicionais','main.py',144),
  ('declaracao -> funcao OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',2,'p_declaracao_funcao_invocada','main.py',149),
  ('declaracao -> impressao','declaracao',1,'p_declaracao_funcao_invocada','main.py',150),
  ('declaracao -> escrita','declaracao',1,'p_declaracao_funcao_invocada','main.py',151),
  ('declaracao -> <empty>','declaracao',0,'p_declaracao_funcao_invocada','main.py',152),
  ('declaracao -> funcao OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','declaracao',4,'p_declaracao_definir_funcao','main.py',157),
  ('param_cond -> VARIAVEL OP_REL_MENOR INTEIRO','param_cond',3,'p_parametro_condicional','main.py',162),
  ('param_cond -> VARIAVEL OP_REL_MENOR DOUBLE','param_cond',3,'p_parametro_condicional','main.py',163),
  ('param_cond -> VARIAVEL OP_REL_MENOR VARIAVEL','param_cond',3,'p_parametro_condicional','main.py',164),
  ('param_cond -> VARIAVEL OP_REL_MAIOR INTEIRO','param_cond',3,'p_parametro_condicional','main.py',165),
  ('param_cond -> VARIAVEL OP_REL_MAIOR DOUBLE','param_cond',3,'p_parametro_condicional','main.py',166),
  ('param_cond -> VARIAVEL OP_REL_MAIOR VARIAVEL','param_cond',3,'p_parametro_condicional','main.py',167),
  ('impressao -> PRINTF expr OP_FINAL_LINHA_PONTO_VIRGULA','impressao',3,'p_impressao','main.py',172),
  ('impressao -> PRINTF expr OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','impressao',8,'p_impressao','main.py',173),
  ('impressao -> PRINTF OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','impressao',5,'p_impressao','main.py',174),
  ('impressao -> PRINTF OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','impressao',7,'p_impressao','main.py',175),
  ('escrita -> VARIAVEL OP_ATRIB_IGUAL SCANF OP_PRIO_ABRE_PARENTESES expr OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','escrita',7,'p_escrita','main.py',179),
  ('escrita -> VARIAVEL OP_ATRIB_IGUAL SCANF OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','escrita',7,'p_escrita','main.py',180),
  ('escrita -> VARIAVEL OP_ATRIB_IGUAL SCANF OP_PRIO_ABRE_PARENTESES STRING VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','escrita',8,'p_escrita','main.py',181),
  ('expr -> VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA','expr',2,'p_expressao_variavel','main.py',187),
  ('expr -> expr OP_MAT_ADICAO expr','expr',3,'p_expressao_operacao','main.py',192),
  ('expr -> expr OP_MAT_SUB expr','expr',3,'p_expressao_operacao','main.py',193),
  ('expr -> expr OP_MAT_MULT expr','expr',3,'p_expressao_operacao','main.py',194),
  ('expr -> expr OP_MAT_DIV expr','expr',3,'p_expressao_operacao','main.py',195),
  ('param_vazio -> <empty>','param_vazio',0,'p_parametro_vazio','main.py',200),
  ('param -> INTEIRO','param',1,'p_parametro','main.py',205),
  ('param -> DOUBLE','param',1,'p_parametro','main.py',206),
  ('param -> STRING','param',1,'p_parametro','main.py',207),
  ('param -> VARIAVEL','param',1,'p_parametro','main.py',208),
  ('funcao -> OP_PRIO_ABRE_PARENTESES param_vazio OP_PRIO_FECHA_PARENTESES','funcao',3,'p_regra_funcao','main.py',213),
  ('funcao -> OP_PRIO_ABRE_PARENTESES param OP_PRIO_FECHA_PARENTESES','funcao',3,'p_regra_funcao','main.py',214),
  ('senaose -> ELIF OP_PRIO_ABRE_PARENTESES param_cond OP_PRIO_FECHA_PARENTESES OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','senaose',7,'p_senao_se','main.py',219),
]
