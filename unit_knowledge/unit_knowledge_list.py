from unit_knowledge.unit_knowledge import *
from unit_knowledge.equation import *
from unit_knowledge.expression import *
from unit_knowledge.number import *
from unit_knowledge.term import *
from unit_knowledge.action_unit_knowledge import *
from unit_knowledge.side import *

# TODO: ValueOfAlgebraicTerm -> ValueOfAlgebraicExpreesion
# TODO: IdentityTerm -> IdentityEquation
uk_list = {
	"UnitKnowledge" : UnitKnowledge(),
	"Equation": Equation(),
	"Expression": Expression(),
	"LinearExpression":LinearExpression(),
	"Monomial":Monomial(),
	"Polynomial":Polynomial(),
	"Substitution": Substitution(),
	"Number": Number(),
	"AlgebraicTerm":AlgebraicTerm(),
	"LikeTerm":LikeTerm(),
	"Degree" : Degree(),
	"ConstantTerm":ConstantTerm(),
	"Coefficient":Coefficient(),
	"ValueOfAlgebraicExpreesion":ValueOfAlgebraicExpreesion(),
	"SimilarTerm":SimilarTerm(),
	"LeftHandSide":LeftHandSide(),
	"RightHandSide":RightHandSide(),
	"BothSide":BothSide(),
	"IdentityEquation":IdentityEquation(),
	"Transposition":Transposition(),
	"LinearEquation":LinearEquation()

}


def test():
	print("UnitKnowledgeList test")
