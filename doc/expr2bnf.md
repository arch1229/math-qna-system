# Expr2BNF

## **!! 필독 !!**
- 아래 내용은 1차 PoC에서 expression을 bnf 및 `python dict` 형태로 나타내던 방법에 대한 설명입니다.
- 2차 PoC부터는 `sympy` 형태로 표현하기에, `doc/expr2sympy.md`를 참고 바랍니다.   

## 개요
- LaTeX 형태의 수식(math expression)을 BNF(Backus–Naur form) 형태로 파싱 및 변환
- 필요에 따라 BNF를 Python dict 또는 json 파일로 반환

## 구조
- expression2bnf : LaTeX 수식을 재귀적 BNF 형태로 변환하는 부속 모듈
	- input : LaTeX 수식
	- output : BNF 형태의 수식
- expression2json : LaTeX 수식을 BNF형태로 변환하여 ```Python <dict>```로 반환
	- input : LaTeX 수식
	- output : LaTex 수식의 BNF 형태, 자료형은 ```Python <dict>```

## BNF 형태 (Expression Type)
Expression | 설명 | LaTeX 예시
----- | ----- | -----
constant | 모든 형태의 수 | "0" "0.2" "-5"
variable | 모든 형태의 변수 | "x" "y" "z"
finite addition | 항(term)의 유한합 | "a+b" "x+2" "5-pq"
finite product | 항(term)의 유한곱 | "abc" "-xy"
exponential | 제곱 | "x^2" "5^y"
fraction | 분수 | "\frac{a}{b}"
algebraic relation type | 관계 연산자 | “eq” “leq” “lt” “geq” “gt”

## 사용 방법
    expression2json('입력 LaTeX 수식')
    expression2json("입력 LaTeX 수식")

## 입출력 예시
```python
>>> expression2json("$2x-y-4$")
```
```json
{
    "expr": "2*x+-1*y+-4",
    "expr_type": "finite_addition",
    "expr_n": 3,
    "expr_elem": [
        {
            "expr": "2*x",
            "expr_type": "finite_product",
            "expr_n": 2,
            "expr_elem": [
                {
                    "expr": "2",
                    "expr_type": "constant",
                    "expr_n": 1,
                    "expr_elem": []
                },
                {
                    "expr": "x",
                    "expr_type": "variable",
                    "expr_n": 1,
                    "expr_elem": []
                }
            ]
        },
        {
            "expr": "-1*y",
            "expr_type": "finite_product",
            "expr_n": 2,
            "expr_elem": [
                {
                    "expr": "-1",
                    "expr_type": "constant",
                    "expr_n": 1,
                    "expr_elem": []
                },
                {
                    "expr": "y",
                    "expr_type": "variable",
                    "expr_n": 1,
                    "expr_elem": []
                }
            ]
        },
        {
            "expr": "-4",
            "expr_type": "constant",
            "expr_n": 1,
            "expr_elem": []
        }
    ]
}
```
---
```python
>>> expression2json("$x$")
```
```json
{
    "expr": "x",
    "expr_type": "variable",
    "expr_n": 1,
    "expr_elem": []
}
```
---
```python
>>> expression2json("$-y$")
```
```json
{
    "expr": "-1*y",
    "expr_type": "finite_product",
    "expr_n": 2,
    "expr_elem": [
        {
            "expr": "-1",
            "expr_type": "constant",
            "expr_n": 1,
            "expr_elem": []
        },
        {
            "expr": "y",
            "expr_type": "variable",
            "expr_n": 1,
            "expr_elem": []
        }
    ]
}
```
---
```python
>>> expression2json("$3$")
```
```json
{
    "expr": "3",
    "expr_type": "constant",
    "expr_n": 1,
    "expr_elem": []
}
```
---
