from pyparsing import *

def rearrange(tks):
       T=tks[0]
       T[0],T[1] = T[1],T[0]
       return tks

expr = Forward()
arithOp = Word( "+-*/", max=1 )
terminal = ( Word(alphas, alphanums)
              | Word(nums)
              | Suppress("(") + expr + Suppress(")") )
expr << Group(terminal + arithOp + terminal).setParseAction(rearrange)

parseTree = expr.parseString("x+(y*z)")
print(parseTree)
