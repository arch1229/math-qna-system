# Expression to Sympy

## 개요
- LaTeX 형태의 수식(math expression)을 Sympy로 변형

## 구조 (`util/latex2sympy.py`)
- `class LatexConverter`
  - `latex2sympy(LaTex_Expression)`
    - `string` 형태의 LaTeX expression을 입력으로 받아서 Sympy로 변환
    - LaTeX expression이 아닌 경우 에러 발생 및 `False` 반환
  - `sympy2latex(sympy_expression)`
    - Sympy expression을 LaTeX expression으로 변환
  - `sympytype(sympy_expression)`
    - Sympy expression의 type을 반환

## 사용법
```python
>>> from util/latex2sympy import *
>>> latex_converter = LatexConverter()
>>> sympy_expr = latex_converter.latex2sympy('$LaTeX_expression_string$')
```

## BNF 표현과의 변경점, 차이점
- 1차 PoC까지
  - `util/type_checker.py` 및 `unit_knowledge/term.py`는 입력으로 BNF 및 dict 자료형을 가정
  - `util/type_checker.py` 및 `unit_knowledge/term.py`는 BNF dict에서 expr에 해당하는 key값의 value로 expression의 type을 확인했음
- 2차 PoC부터
  - `util/type_checker.py`의 `ExprType class`의 `ExprType` 함수는 `check`로 이름 변경
    - BNF dict로 표현된 expression(`doc/expr2bnf`)의 type check을 하고 싶다면, 다음과 같은 입력을
        ```python
        from util/type_checker import *
        expr_type_checker = ExprType()
        list_exprtype = expr_type_checker.ExprType(expr_dict)
        ```
       아래와 같이 변경하면 작동한다.
        ```python
        from util/type_checker import *
        expr_type_checker = ExprType()
        list_exprtype = expr_type_checker.check(expr_dict["expr"])
        ```
  - 또한 해당 `check` 함수는 expression이 Number 형태일 경우 수의 범위도 확인하게끔 `latex_exprtype_check` 함수로 확장되었고, 아래와 같이 사용하면 된다.
      ```python
      from util/type_checker import *
      list_exprtype = latex_expr_type_check('$LaTeX_expression_string$')
      ```
