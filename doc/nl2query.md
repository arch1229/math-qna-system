# Python_QnA_NL2Query


Overview
---

Window10환경에서 MeCab을 사용하여 Python으로 구현됩니다.

#### Input
$LaTeX$ 형태를 동반한 자연어 질의입니다.

자연어 질의 예시

 1. [등식의 성질은 뭐뭐가 있는지 알려주세요!](query_example1.json)
 2. [항등식도 방정식이라고 볼 수 있나요?](query_example2.json)
 3. [$0$은 상수항이라고 할 수 없나요?](query_example3.json)
 4. [$2x-y-4$에서 $x$의 계수가 뭔가요?](query_example4.json)

#### Output
추론엔진에 들어갈 json형식의 Query입니다. 위 예시들의 링크를 참조

How to Set up
---
1. Window용 MeCab은 다음 [링크](https://cleancode-ws.tistory.com/97)를 참고하여 다운받습니다.
2. MeCab에서 정의되지 않은 Unit Knowledge(ex. 이차방정식)은 사용자 정의사전을 추가하도록 합니다. [사용자 사전 추가](#사용자-사전-추가)

Implementation
---
```{.python}
from util/nl2query import *

query = query_generator("$LaTeX$ 형태를 포함할 수 있는 자연어 질의")
```
## 사용자 사전 추가

## 준비
[mecab-ko-msvc](https://github.com/Pusnow/mecab-ko-msvco)와 [mecab-ko-dic-msvc](https://github.com/Pusnow/mecab-ko-dic-msvc) 을 다운받아 설치합니다. 
반드시 `C:\mecab` 경로에 설치하셔야 사전 추가가 가능합니다.

## 사전 추가
`C:\mecab\user-dic` 디렉토리 안에 csv 확장자로 사전 파일을 추가합니다.


    user-dic/
    ├── nnp.csv
    ├── person.csv
    └── place.csv

* 일반적인 고유명사 추가
    
        대우,,,,NNP,*,F,대우,*,*,*,*
        구글,,,,NNP,*,T,구글,*,*,*,*

* 인명 추가

        까비,,,,NNP,인명,F,까비,*,*,*,*

* 지명 추가

        세종,,,,NNP,지명,T,세종,*,*,*,*
        세종시,,,,NNP,지명,F,세종시,Compound,*,*,세종/NNP/지명+시/NNG/*

그 외의 품사 추가가 필요한 경우에는 [품사태그표](https://docs.google.com/spreadsheet/ccc?key=0ApcJghR6UMXxdEdURGY2YzIwb3dSZ290RFpSaUkzZ0E&usp=sharing#gid=4) 를 참고하세요.

## 사전 컴파일

Powershell을 이용하여 작업하셔야 합니다. 단축키 `(윈도우키) + R` 을 누르고 `powershell` 을 입력하면 실행 가능합니다.

* `C:\mecab` 경로로 이동합니다.

        PS C:\Users> cd C:\mecab
        PS C:\mecab>
* `tools\add-userdic-win.ps1` 스크립트를 실행합니다.

        PS C:\mecab> tools\add-userdic-win.ps1
        generating userdic...
        C:\mecab\mecab-ko-dic\model.def is not a binary model. reopen it as text mode...
        reading C:\mecab\user-dic\nnp.csv ...
        done!
        ...생략

    
아래와 같이 user-xxx.csv 사전이 추가된 모습을 볼 수 있습니다. 사실 아래 파일은 컴파일 되기 직전의 파일이며, 실제로 sys.dic 파일에 바이너리로 컴파일 되어 들어가게 됩니다.

    mecab-ko-dic
    ├── ....
    ├── user-nnp.csv
    ├── user-person.csv
    ├── user-place.csv
    └── ...

## 설치
설치 과정은 따로 필요 없습니다. 바로 사용하시면 됩니다.
