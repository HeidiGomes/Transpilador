
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOP_MAT_ADICAOOP_MAT_SUBleftOP_MAT_MULTOP_MAT_DIVOP_MAT_POTDOUBLE ELSE EM ENQUANTO ESCREVA INT INTEIRO LEIA OP_ATRIB_IGUAL OP_ATRIB_MAIS_IGUAL OP_EXEC_VIRGULA OP_FINAL_LINHA_PONTO_VIRGULA OP_MAT_ADICAO OP_MAT_DIV OP_MAT_MULT OP_MAT_POT OP_MAT_SUB OP_PRIO_ABRE_CHAVES OP_PRIO_ABRE_PARENTESES OP_PRIO_FECHA_CHAVES OP_PRIO_FECHA_PARENTESES OP_REL_DUPLO_IGUAL OP_REL_MAIOR OP_REL_MENOR PARA RANGE SE STRING VARIAVEL\n    declaracoes : declaracao\n    \n    declaracoes :  declaracao bloco\n    \n    bloco : OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n          | OP_PRIO_ABRE_CHAVES declaracao bloco OP_PRIO_FECHA_CHAVES\n          | OP_PRIO_ABRE_CHAVES impressao OP_PRIO_FECHA_CHAVES\n          | OP_PRIO_ABRE_CHAVES escrita impressao OP_PRIO_FECHA_CHAVES\n          | OP_PRIO_ABRE_CHAVES escrita escrita impressao OP_PRIO_FECHA_CHAVES\n          | OP_PRIO_ABRE_CHAVES escrita escrita expr impressao OP_PRIO_FECHA_CHAVES\n          | OP_PRIO_ABRE_CHAVES impressao param_cond OP_FINAL_LINHA_PONTO_VIRGULA OP_PRIO_FECHA_CHAVES\n          | OP_PRIO_ABRE_CHAVES param_cond OP_FINAL_LINHA_PONTO_VIRGULA impressao OP_PRIO_FECHA_CHAVES\n          | OP_PRIO_ABRE_CHAVES impressao expr OP_PRIO_FECHA_CHAVES\n          \n    \n    declaracao : ENQUANTO param_cond bloco\n               | declaracao ENQUANTO param_cond bloco\n    \n    declaracao : PARA VARIAVEL EM RANGE OP_PRIO_ABRE_PARENTESES INTEIRO OP_EXEC_VIRGULA INTEIRO OP_PRIO_FECHA_PARENTESES bloco\n               | PARA VARIAVEL EM RANGE OP_PRIO_ABRE_PARENTESES DOUBLE OP_EXEC_VIRGULA DOUBLE OP_PRIO_FECHA_PARENTESES bloco\n    \n    declaracao : VARIAVEL OP_ATRIB_IGUAL expr OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL STRING OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL DOUBLE OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_IGUAL funcao OP_FINAL_LINHA_PONTO_VIRGULA\n            | param VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA\n            | VARIAVEL OP_ATRIB_MAIS_IGUAL INTEIRO\n            | VARIAVEL OP_ATRIB_MAIS_IGUAL DOUBLE\n            | VARIAVEL OP_ATRIB_MAIS_IGUAL VARIAVEL\n    \n    declaracao : SE param_cond bloco\n               | declaracao SE param_cond bloco\n               | declaracao SE param_cond bloco senao\n               | SE param_cond bloco senao\n    \n    declaracao : funcao OP_FINAL_LINHA_PONTO_VIRGULA\n               | impressao\n               | escrita\n    \n    declaracao : funcao OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES\n    \n    param_cond :  VARIAVEL OP_REL_MENOR INTEIRO\n                | VARIAVEL OP_REL_MENOR DOUBLE\n                | VARIAVEL OP_REL_MENOR VARIAVEL\n                | VARIAVEL OP_REL_MAIOR INTEIRO\n                | VARIAVEL OP_REL_MAIOR DOUBLE\n                | VARIAVEL OP_REL_MAIOR VARIAVEL\n                | VARIAVEL OP_ATRIB_MAIS_IGUAL INTEIRO\n                | VARIAVEL OP_ATRIB_MAIS_IGUAL DOUBLE\n                | VARIAVEL OP_ATRIB_MAIS_IGUAL VARIAVEL\n                | VARIAVEL OP_REL_DUPLO_IGUAL INTEIRO\n                | VARIAVEL OP_REL_DUPLO_IGUAL DOUBLE\n                | VARIAVEL OP_REL_DUPLO_IGUAL VARIAVEL\n\n    impressao : ESCREVA expr OP_FINAL_LINHA_PONTO_VIRGULA\n                 | ESCREVA expr OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA\n                 | ESCREVA OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA\n                 | ESCREVA OP_PRIO_ABRE_PARENTESES  STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA\n    escrita : VARIAVEL OP_ATRIB_IGUAL LEIA OP_PRIO_ABRE_PARENTESES expr OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA\n               | VARIAVEL OP_ATRIB_IGUAL param OP_PRIO_ABRE_PARENTESES LEIA OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA\n               | VARIAVEL OP_ATRIB_IGUAL LEIA OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA \n               | VARIAVEL OP_ATRIB_IGUAL LEIA OP_PRIO_ABRE_PARENTESES STRING VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA \n    \n    expr :  VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_SUB INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_SUB VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_MULT INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_MULT VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_DIV INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_DIV VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_POT INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA\n         |  VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_POT VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA\n    \n    expr : expr OP_MAT_ADICAO expr\n        |  expr OP_MAT_SUB expr\n        |  expr OP_MAT_MULT expr\n        |  expr OP_MAT_DIV expr\n        |  expr OP_MAT_POT expr\n    \n    param_vazio :\n    \n    param : INTEIRO\n        | INT\n        | DOUBLE\n        | STRING\n        | VARIAVEL\n    \n    funcao :  OP_PRIO_ABRE_PARENTESES param_vazio OP_PRIO_FECHA_PARENTESES\n        |  OP_PRIO_ABRE_PARENTESES param OP_PRIO_FECHA_PARENTESES\n    \n    senao : ELSE bloco\n    '
    
_lr_action_items = {'ENQUANTO':([0,2,13,14,20,29,30,39,40,41,44,58,59,60,65,66,76,77,78,80,102,103,104,105,106,107,110,112,123,124,126,129,132,133,134,139,140,142,149,150,152,171,174,176,179,192,194,198,199,200,],[3,18,-31,-32,3,-30,3,18,-31,-32,-12,-25,-23,-24,-26,-46,-13,-27,-3,-5,-18,-16,-17,-19,-20,-21,-33,-29,-28,-4,-11,-6,-25,-23,-24,-22,-78,-48,-9,-7,-10,-8,-50,-52,-49,-53,-47,-14,-15,-51,]),'PARA':([0,20,30,],[4,4,4,]),'VARIAVEL':([0,3,4,5,6,7,8,9,11,12,15,16,18,19,20,24,25,30,40,41,43,45,46,47,48,66,68,69,70,71,72,75,84,88,108,121,130,137,141,142,144,145,146,147,148,174,176,179,192,194,200,],[5,22,23,-75,28,-71,-73,-74,31,22,-72,35,22,22,43,50,58,5,83,86,-75,89,92,95,98,-46,35,35,35,35,35,122,35,132,35,143,28,156,159,-48,161,163,165,167,169,-50,-52,-49,-53,-47,-51,]),'SE':([0,2,13,14,20,29,30,39,40,41,44,58,59,60,65,66,76,77,78,80,102,103,104,105,106,107,110,112,123,124,126,129,132,133,134,139,140,142,149,150,152,171,174,176,179,192,194,198,199,200,],[12,19,-31,-32,12,-30,12,19,-31,-32,-12,-25,-23,-24,-26,-46,-13,-27,-3,-5,-18,-16,-17,-19,-20,-21,-33,-29,-28,-4,-11,-6,-25,-23,-24,-22,-78,-48,-9,-7,-10,-8,-50,-52,-49,-53,-47,-14,-15,-51,]),'INTEIRO':([0,6,20,24,25,30,45,46,47,48,64,88,130,135,144,145,146,147,148,172,],[7,7,7,53,59,7,90,93,96,99,111,133,7,153,162,164,166,168,170,190,]),'INT':([0,6,20,24,30,130,],[15,15,15,15,15,15,]),'DOUBLE':([0,6,20,24,25,30,45,46,47,48,88,130,135,173,],[8,8,8,54,60,8,91,94,97,100,134,8,154,191,]),'STRING':([0,6,20,24,30,34,67,108,130,158,],[9,9,9,52,9,73,114,137,9,177,]),'OP_PRIO_ABRE_PARENTESES':([0,7,8,9,15,16,20,24,28,30,33,50,52,53,54,56,57,74,101,115,116,117,118,119,138,180,181,182,183,184,185,186,187,188,189,],[6,-71,-73,-74,-72,34,6,6,-75,6,67,-75,-74,-71,-73,108,109,-54,135,-65,-66,-67,-68,-69,158,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,]),'ESCREVA':([0,20,30,41,74,84,87,115,116,117,118,119,128,174,176,180,181,182,183,184,185,186,187,188,189,192,200,],[16,16,16,16,-54,16,16,-65,-66,-67,-68,-69,16,-50,-52,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,-53,-51,]),'$end':([1,2,13,14,17,29,44,58,59,60,65,66,76,77,78,80,102,103,104,105,106,107,110,112,123,124,126,129,139,140,142,149,150,152,171,174,176,179,192,194,198,199,200,],[0,-1,-31,-32,-2,-30,-12,-25,-23,-24,-26,-46,-13,-27,-3,-5,-18,-16,-17,-19,-20,-21,-33,-29,-28,-4,-11,-6,-22,-78,-48,-9,-7,-10,-8,-50,-52,-49,-53,-47,-14,-15,-51,]),'OP_PRIO_FECHA_CHAVES':([2,13,14,17,29,38,39,40,41,44,58,59,60,63,65,66,74,76,77,78,79,80,82,85,102,103,104,105,106,107,110,112,115,116,117,118,119,123,124,125,126,127,129,131,132,133,134,139,140,142,149,150,151,152,171,174,176,179,180,181,182,183,184,185,186,187,188,189,192,194,198,199,200,],[-1,-31,-32,-2,-30,78,-1,80,-32,-12,-25,-23,-24,110,-26,-46,-54,-13,-27,-3,124,-5,126,129,-18,-16,-17,-19,-20,-21,-33,-29,-65,-66,-67,-68,-69,-28,-4,149,-11,150,-6,152,-25,-23,-24,-22,-78,-48,-9,-7,171,-10,-8,-50,-52,-49,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,-53,-47,-14,-15,-51,]),'OP_PRIO_ABRE_CHAVES':([2,10,13,14,21,29,32,36,37,39,40,41,44,58,59,60,61,62,65,66,76,77,78,80,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,106,107,110,112,113,123,124,126,129,132,133,134,139,140,142,149,150,152,171,174,176,179,192,194,195,196,198,199,200,],[20,30,-31,-32,20,-30,20,20,20,20,-31,-32,-12,-25,-23,-24,-76,-77,-26,-46,-13,-27,-3,-5,-36,-34,-35,-39,-37,-38,-42,-40,-41,-45,-43,-44,-18,-16,-17,-19,-20,-21,-33,-29,20,-28,-4,-11,-6,-25,-23,-24,-22,-78,-48,-9,-7,-10,-8,-50,-52,-49,-53,-47,20,20,-14,-15,-51,]),'OP_ATRIB_IGUAL':([5,31,35,43,50,83,86,],[24,64,75,24,75,75,130,]),'OP_ATRIB_MAIS_IGUAL':([5,22,43,83,],[25,47,88,47,]),'OP_PRIO_FECHA_PARENTESES':([6,7,8,9,15,26,27,28,73,74,115,116,117,118,119,136,137,143,156,159,177,180,181,182,183,184,185,186,187,188,189,190,191,193,],[-70,-71,-73,-74,-72,61,62,-75,120,-54,-65,-66,-67,-68,-69,155,157,160,175,178,193,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,195,196,197,]),'OP_FINAL_LINHA_PONTO_VIRGULA':([10,33,35,42,50,51,52,53,54,55,61,62,74,81,83,89,90,91,92,93,94,95,96,97,98,99,100,102,111,115,116,117,118,119,120,132,133,134,155,157,160,161,162,163,164,165,166,167,168,169,170,175,178,180,181,182,183,184,185,186,187,188,189,197,],[29,66,74,87,102,103,104,105,106,107,-76,-77,-54,125,74,-36,-34,-35,-39,-37,-38,-42,-40,-41,-45,-43,-44,-54,139,-65,-66,-67,-68,-69,142,-42,-40,-41,174,176,179,180,181,182,183,184,185,186,187,188,189,192,194,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,200,]),'OP_REL_MENOR':([22,43,83,],[45,45,45,]),'OP_REL_MAIOR':([22,43,83,],[46,46,46,]),'OP_REL_DUPLO_IGUAL':([22,43,83,],[48,48,48,]),'EM':([23,],[49,]),'LEIA':([24,109,130,],[56,138,56,]),'OP_MAT_ADICAO':([33,51,74,82,102,115,116,117,118,119,122,128,136,180,181,182,183,184,185,186,187,188,189,],[68,68,-54,68,-54,-65,-66,-67,-68,-69,144,68,68,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,]),'OP_MAT_SUB':([33,51,74,82,102,115,116,117,118,119,122,128,136,180,181,182,183,184,185,186,187,188,189,],[69,69,-54,69,-54,-65,-66,-67,-68,-69,145,69,69,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,]),'OP_MAT_MULT':([33,51,74,82,102,115,116,117,118,119,122,128,136,180,181,182,183,184,185,186,187,188,189,],[70,70,-54,70,-54,70,70,-67,-68,-69,146,70,70,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,]),'OP_MAT_DIV':([33,51,74,82,102,115,116,117,118,119,122,128,136,180,181,182,183,184,185,186,187,188,189,],[71,71,-54,71,-54,71,71,-67,-68,-69,147,71,71,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,]),'OP_MAT_POT':([33,51,74,82,102,115,116,117,118,119,122,128,136,180,181,182,183,184,185,186,187,188,189,],[72,72,-54,72,-54,72,72,-67,-68,-69,148,72,72,-56,-55,-58,-57,-60,-59,-62,-61,-64,-63,]),'RANGE':([49,],[101,]),'ELSE':([65,77,78,80,124,126,129,149,150,152,171,],[113,113,-3,-5,-4,-11,-6,-9,-7,-10,-8,]),'OP_EXEC_VIRGULA':([73,114,153,154,],[121,141,172,173,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracoes':([0,20,30,],[1,38,63,]),'declaracao':([0,20,30,],[2,39,2,]),'funcao':([0,20,24,30,],[10,10,55,10,]),'param':([0,6,20,24,30,130,],[11,27,11,57,11,57,]),'impressao':([0,20,30,41,84,87,128,],[13,40,13,85,127,131,151,]),'escrita':([0,20,30,41,],[14,41,14,84,]),'bloco':([2,21,32,36,37,39,113,195,196,],[17,44,65,76,77,79,140,198,199,]),'param_cond':([3,12,18,19,20,40,],[21,32,36,37,42,81,]),'param_vazio':([6,],[26,]),'expr':([16,24,40,68,69,70,71,72,84,108,],[33,51,82,115,116,117,118,119,128,136,]),'senao':([65,77,],[112,123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracoes","S'",1,None,None,None),
  ('declaracoes -> declaracao','declaracoes',1,'p_declaracoes_single','main.py',115),
  ('declaracoes -> declaracao bloco','declaracoes',2,'p_declaracoes_mult','main.py',120),
  ('bloco -> OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','bloco',3,'p_bloco','main.py',125),
  ('bloco -> OP_PRIO_ABRE_CHAVES declaracao bloco OP_PRIO_FECHA_CHAVES','bloco',4,'p_bloco','main.py',126),
  ('bloco -> OP_PRIO_ABRE_CHAVES impressao OP_PRIO_FECHA_CHAVES','bloco',3,'p_bloco','main.py',127),
  ('bloco -> OP_PRIO_ABRE_CHAVES escrita impressao OP_PRIO_FECHA_CHAVES','bloco',4,'p_bloco','main.py',128),
  ('bloco -> OP_PRIO_ABRE_CHAVES escrita escrita impressao OP_PRIO_FECHA_CHAVES','bloco',5,'p_bloco','main.py',129),
  ('bloco -> OP_PRIO_ABRE_CHAVES escrita escrita expr impressao OP_PRIO_FECHA_CHAVES','bloco',6,'p_bloco','main.py',130),
  ('bloco -> OP_PRIO_ABRE_CHAVES impressao param_cond OP_FINAL_LINHA_PONTO_VIRGULA OP_PRIO_FECHA_CHAVES','bloco',5,'p_bloco','main.py',131),
  ('bloco -> OP_PRIO_ABRE_CHAVES param_cond OP_FINAL_LINHA_PONTO_VIRGULA impressao OP_PRIO_FECHA_CHAVES','bloco',5,'p_bloco','main.py',132),
  ('bloco -> OP_PRIO_ABRE_CHAVES impressao expr OP_PRIO_FECHA_CHAVES','bloco',4,'p_bloco','main.py',133),
  ('declaracao -> ENQUANTO param_cond bloco','declaracao',3,'p_declaracao_ENQUANTO','main.py',139),
  ('declaracao -> declaracao ENQUANTO param_cond bloco','declaracao',4,'p_declaracao_ENQUANTO','main.py',140),
  ('declaracao -> PARA VARIAVEL EM RANGE OP_PRIO_ABRE_PARENTESES INTEIRO OP_EXEC_VIRGULA INTEIRO OP_PRIO_FECHA_PARENTESES bloco','declaracao',10,'p_declaracao_para','main.py',145),
  ('declaracao -> PARA VARIAVEL EM RANGE OP_PRIO_ABRE_PARENTESES DOUBLE OP_EXEC_VIRGULA DOUBLE OP_PRIO_FECHA_PARENTESES bloco','declaracao',10,'p_declaracao_para','main.py',146),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL expr OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',151),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL STRING OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',152),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',153),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',154),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL DOUBLE OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',155),
  ('declaracao -> VARIAVEL OP_ATRIB_IGUAL funcao OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',4,'p_declaracao_atribuicaoValorVariavel','main.py',156),
  ('declaracao -> param VARIAVEL OP_ATRIB_IGUAL INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',5,'p_declaracao_atribuicaoValorVariavel','main.py',157),
  ('declaracao -> VARIAVEL OP_ATRIB_MAIS_IGUAL INTEIRO','declaracao',3,'p_declaracao_atribuicaoValorVariavel','main.py',158),
  ('declaracao -> VARIAVEL OP_ATRIB_MAIS_IGUAL DOUBLE','declaracao',3,'p_declaracao_atribuicaoValorVariavel','main.py',159),
  ('declaracao -> VARIAVEL OP_ATRIB_MAIS_IGUAL VARIAVEL','declaracao',3,'p_declaracao_atribuicaoValorVariavel','main.py',160),
  ('declaracao -> SE param_cond bloco','declaracao',3,'p_declaracao_condicionais','main.py',165),
  ('declaracao -> declaracao SE param_cond bloco','declaracao',4,'p_declaracao_condicionais','main.py',166),
  ('declaracao -> declaracao SE param_cond bloco senao','declaracao',5,'p_declaracao_condicionais','main.py',167),
  ('declaracao -> SE param_cond bloco senao','declaracao',4,'p_declaracao_condicionais','main.py',168),
  ('declaracao -> funcao OP_FINAL_LINHA_PONTO_VIRGULA','declaracao',2,'p_declaracao_funcao_invocada','main.py',173),
  ('declaracao -> impressao','declaracao',1,'p_declaracao_funcao_invocada','main.py',174),
  ('declaracao -> escrita','declaracao',1,'p_declaracao_funcao_invocada','main.py',175),
  ('declaracao -> funcao OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES','declaracao',4,'p_declaracao_definir_funcao','main.py',180),
  ('param_cond -> VARIAVEL OP_REL_MENOR INTEIRO','param_cond',3,'p_parametro_condicional','main.py',185),
  ('param_cond -> VARIAVEL OP_REL_MENOR DOUBLE','param_cond',3,'p_parametro_condicional','main.py',186),
  ('param_cond -> VARIAVEL OP_REL_MENOR VARIAVEL','param_cond',3,'p_parametro_condicional','main.py',187),
  ('param_cond -> VARIAVEL OP_REL_MAIOR INTEIRO','param_cond',3,'p_parametro_condicional','main.py',188),
  ('param_cond -> VARIAVEL OP_REL_MAIOR DOUBLE','param_cond',3,'p_parametro_condicional','main.py',189),
  ('param_cond -> VARIAVEL OP_REL_MAIOR VARIAVEL','param_cond',3,'p_parametro_condicional','main.py',190),
  ('param_cond -> VARIAVEL OP_ATRIB_MAIS_IGUAL INTEIRO','param_cond',3,'p_parametro_condicional','main.py',191),
  ('param_cond -> VARIAVEL OP_ATRIB_MAIS_IGUAL DOUBLE','param_cond',3,'p_parametro_condicional','main.py',192),
  ('param_cond -> VARIAVEL OP_ATRIB_MAIS_IGUAL VARIAVEL','param_cond',3,'p_parametro_condicional','main.py',193),
  ('param_cond -> VARIAVEL OP_REL_DUPLO_IGUAL INTEIRO','param_cond',3,'p_parametro_condicional','main.py',194),
  ('param_cond -> VARIAVEL OP_REL_DUPLO_IGUAL DOUBLE','param_cond',3,'p_parametro_condicional','main.py',195),
  ('param_cond -> VARIAVEL OP_REL_DUPLO_IGUAL VARIAVEL','param_cond',3,'p_parametro_condicional','main.py',196),
  ('impressao -> ESCREVA expr OP_FINAL_LINHA_PONTO_VIRGULA','impressao',3,'p_impressao','main.py',201),
  ('impressao -> ESCREVA expr OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','impressao',8,'p_impressao','main.py',202),
  ('impressao -> ESCREVA OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','impressao',5,'p_impressao','main.py',203),
  ('impressao -> ESCREVA OP_PRIO_ABRE_PARENTESES STRING OP_EXEC_VIRGULA VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','impressao',7,'p_impressao','main.py',204),
  ('escrita -> VARIAVEL OP_ATRIB_IGUAL LEIA OP_PRIO_ABRE_PARENTESES expr OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','escrita',7,'p_escrita','main.py',208),
  ('escrita -> VARIAVEL OP_ATRIB_IGUAL param OP_PRIO_ABRE_PARENTESES LEIA OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','escrita',10,'p_escrita','main.py',209),
  ('escrita -> VARIAVEL OP_ATRIB_IGUAL LEIA OP_PRIO_ABRE_PARENTESES STRING OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','escrita',7,'p_escrita','main.py',210),
  ('escrita -> VARIAVEL OP_ATRIB_IGUAL LEIA OP_PRIO_ABRE_PARENTESES STRING VARIAVEL OP_PRIO_FECHA_PARENTESES OP_FINAL_LINHA_PONTO_VIRGULA','escrita',8,'p_escrita','main.py',211),
  ('expr -> VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA','expr',2,'p_expressao_variavel','main.py',217),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',218),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_ADICAO VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',219),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_SUB INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',220),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_SUB VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',221),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_MULT INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',222),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_MULT VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',223),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_DIV INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',224),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_DIV VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',225),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_POT INTEIRO OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',226),
  ('expr -> VARIAVEL OP_ATRIB_IGUAL VARIAVEL OP_MAT_POT VARIAVEL OP_FINAL_LINHA_PONTO_VIRGULA','expr',6,'p_expressao_variavel','main.py',227),
  ('expr -> expr OP_MAT_ADICAO expr','expr',3,'p_expressao_operacao','main.py',233),
  ('expr -> expr OP_MAT_SUB expr','expr',3,'p_expressao_operacao','main.py',234),
  ('expr -> expr OP_MAT_MULT expr','expr',3,'p_expressao_operacao','main.py',235),
  ('expr -> expr OP_MAT_DIV expr','expr',3,'p_expressao_operacao','main.py',236),
  ('expr -> expr OP_MAT_POT expr','expr',3,'p_expressao_operacao','main.py',237),
  ('param_vazio -> <empty>','param_vazio',0,'p_parametro_vazio','main.py',242),
  ('param -> INTEIRO','param',1,'p_parametro','main.py',248),
  ('param -> INT','param',1,'p_parametro','main.py',249),
  ('param -> DOUBLE','param',1,'p_parametro','main.py',250),
  ('param -> STRING','param',1,'p_parametro','main.py',251),
  ('param -> VARIAVEL','param',1,'p_parametro','main.py',252),
  ('funcao -> OP_PRIO_ABRE_PARENTESES param_vazio OP_PRIO_FECHA_PARENTESES','funcao',3,'p_regra_funcao','main.py',257),
  ('funcao -> OP_PRIO_ABRE_PARENTESES param OP_PRIO_FECHA_PARENTESES','funcao',3,'p_regra_funcao','main.py',258),
  ('senao -> ELSE bloco','senao',2,'p_senao_se','main.py',263),
]
