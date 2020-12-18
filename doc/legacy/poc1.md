- 1차 PoC Plan(~7.03)
	- 목표 : 하기의 질문을 응답할 수 있다. 
	- 질문 List 
		1. 등식의 성질이 뭔가요?
		2. 항등식은 방정식인가요?
		3. $0$은 상수항인가요?
		4. $3x + 4y -5$에서 $x$의 계수는 뭐죠?
	- 진행 사항(세부 파트별)
		- [자연어2쿼리](doc/nl2query.md)(여기서, 쿼리는 우리파트만의 자체 규약 우리만 사용, [예시](http://gitlab.tmaxwork.shop/hyperstudy/qna/python_qna_inferenceengine/-/blob/feature/inference/query_example2.json)) : 기능 구현 완료, 성능 업그레이드 중
		- [Expression2BNF_JSON](expr2bnf.md)(Latex string 수식을 [BNF](https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%BB%A4%EC%8A%A4-%EB%82%98%EC%9A%B0%EB%A5%B4_%ED%91%9C%EA%B8%B0%EB%B2%95)형태 기반 JSON으로 예쁘게 변환) : 기능 구현 완료, 성능 업그레이드 중
		- 추론(쿼리+BNF_JSON으로 이루어진 질문을 응답하기 위한 추론 진행) : 기능 구현 중...
		- 추론 기반 자연어 응답 생성 : 상기 질문에 대해서만 간단히 구현 예정.
	- 경과 보고 
		1. DB json 구축하기 (문자와식)
		2. 문자와식 keyword_corpus 집합 만들기
		3. keyword는 문자와식 단원의 keyword_corpus 집합의 index값으로 저장
		4. expression_type_checker
		5. dummy CAS 만들기 (계수, 대입 등) -> 3팀 CAS io 표본 만들기
		6. Discord EndtoEnd 구현