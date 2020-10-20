# QnA파트의 수학질의 추론엔진

## **Abstract**
### **What we do?**
+ 학생들의 수학 질문에 답변해 주는 **질의응답시스템**을 구축합니다. 
### **Why we do?**
+ 수학이라는 도메인이 주는 **엄밀함** 때문에 적절하고 효율 높은 질의응답 시스템을 구축하기 위해서는 도메인에 Specific한 접근이 필요합니다.
+ **수학지식DB와 논리식 설계**를 담당하는 팀에 내에서 유연하고 상세한 설계가 가능합니다.
+ 수학지식DB의 **사용자 입장**에서 DB개발의 필요사항을 파악할 수 있습니다. 
+ 그리하여!! 2-1팀에 수학QNA파트를 설립하여 개발하여 되었습니다.
### **How we do?**
+ 추론엔진은 아래의 모듈로 구성되어 있습니다. 

	+ **Entity extractor module**
		+ UK, Component, Attribute, Expression, Keyword 를 추출
	+ **Intent classifier** 
		+ 추출된 Entity기반 Intent 파악
	+ **Inference module**
		+ 실제로 답변 생성을 위한 추론
	+ **Query Generator module**
		+ Entity, Intent 기반 외부 모듈 호출 쿼리 생성
	+ **NLG module**
		+ 추론 결과를 자연어로 변환
	+ **Feedback module**
		+ 각각의 모듈에서 예외 상황 발생시 사용자에게 재질문
	+ **Dummy external module**
		+ PoC 진행을 위한 Dummy CAS와 Dummy DB 모듈  

+ 위 모듈이 [Flow chart](artwork/poc1.png)와 같이 구성되어 있습니다.   

### **How to use?**

현재 지원되는 봇 서버는 Discord와 Http기반 서버입니다. 
```shell 
$ cd python_qna_inferenceengine
$ pip install -r requirements.txt
$ vi config.json # Set your bot token, url and port
$ python main.py --client_type="admin_page" # Or "discord"
```

---
## **Example**
+ Input은 사전에 정의된 intent_entity 문법으로 변환됩니다.
	+ Intent Type은 [component, implication, logic, action] 으로 구성됩니다.
	+ Intent 기반으로 추론을 진행하여 답변을 생성합니다. 
	+ 입력 예시
		+ [등식의 성질은 뭐뭐가 있는지 알려주세요!](io_example/intent_entity_output_example1.json)
		+ [방정식도 등식이라고 할 수 있나요??](io_example/intent_entity_output_example2.json)
		+ [$0$은 상수항이라고 할 수 없나요?](io_example/intent_entity_output_example3.json)
		+ [$2x-y-4$에서 $x$의 계수가 뭔가요?](io_example/intent_entity_output_example4.json)
		+ [$2x-y-4$에서 $x$에 $3$을 대입해주세요.](io_example/intent_entity_output_example6.json)
+ Output은 질의에 대한 자연어 응답입니다.
	+ 출력 예시 
		+ 등식의 성질: 등식에서 등호가 성립할 때 참, 성립하지 않을 때 거짓이라 한다. 1. 등식의 양변에 같은 수를 더하여도 등식은 성립한다. $A=B$이면 $A+C=B+C$ 2. 등식의 양변에 같은 수를 빼어도 등식은 성립한다. $A=B$이면 $A-C=B-C$ 3. 등식의 양변에 같은 수를 곱하여도 등식은 성립한다. $A=B$이면 $AC=BC$ 4. 등식의 양변을 0이 아닌 같은 수로 나누어도 등식은 성립한다. $C\neq 0$이고 $A=B$이면 $\frac{A}{C}=\frac{B}{C}$
		+ 방정식은 등식이 맞습니다
		+ $0$는 상수항이 아닙니다
		+ $2$ 입니다
		+ $2 - y$ 입니다

---

## **Etc**
### **개발 계획**
+ [1차 PoC](doc/poc1.md)(~7.08)
+ [2차 PoC](doc/poc2.md)(7.10~7.31)
+ 3차 PoC(8.01~?)
### **Issue**
+ 디스코드 패키지는 최신버전을 써야합니다. 
### **Module 사용법** 
+ Discord bot 설정법
+ http bot 설정법
### **Dev rule**
+ 별도의 모듈을 개발시 테스트는 ~
+ 디버깅을 위한 로그는 ~
+ Branching 기법
+ Commit message
### **필요한 패키지 (requirements.txt)**
+ Python 3.6.9 버전에서 개발하였습니다.
+ pip 9.0.1 버전을 사용하였습니다.
```
sympy==1.6
mpmath==1.1.0
discord>=1.0.1
antlr4-python3-runtime==4.7.1
flask==1.1.2
flask-restful==0.3.8
mecab-python3==1.0.0
```
### **How repo construct?**
```
 Folder hierarchy please
```
---
