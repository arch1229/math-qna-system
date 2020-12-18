# **Python Logging 모듈을 사용하여 Log 남기기** 
## **Why?** 

- 우리는 때때로 디버깅을 위해 print등을 통해 콘솔에 원하는 것들을 출력해 봅니다. 하지만, Ops 버전을 배포하기 위해서는 디버깅에 사용한 print를 지워야 하는데 여간 귀찮은 일이 아닙니다. 
- Ops버전이 아니고 Dev 버전이라고 할지라도 공동 개발자가 소스를 실행해보고 무의미한 수많은 print들에 놀랄지도 모릅니다.  
- 그래서 Logging 모듈을 활용하여 Log의 레벨을 변경하며 때에 따라 적절한 Log를  띄울 수 있도록 해봅시다.  

## **How?**

### **Loging Level** 
---
Logging 모듈은 이벤트의 수준 또는 심각도를 따라 Logging Level을 정하도록 권장합니다. 

| 수준 | 사용할 때 |
|---|:------------------------:|
| `DEBUG` |상세한 정보. 보통 문제를 진단할 때만 필요합니다. |
| `INFO` |예상대로 작동하는지에 대한 확인. |
| `WARNING` |예상치 못한 일이 발생했거나 가까운 미래에 발생할 문제(예를 들어 〈디스크 공간 부족〉)에 대한 표시. 소프트웨어는 여전히 예상대로 작동합니다. |
| `ERROR` | 더욱 심각한 문제로 인해, 소프트웨어가 일부 기능을 수행하지 못했습니다. |
| `CRITICAL`|심각한 에러. 프로그램 자체가 계속 실행되지 않을 수 있음을 나타냅니다.|
---

기본 수준은 `WARNING` 입니다. 프로그램의 배포 수준에 따라서 Logging 레벨을 다르게 설정하여야 합니다. 



### **여러 모듈에서 Logging**
---
우리는 서비스를 기능별로 쪼개어 개발하기로 합니다. 여러 모듈에서 Logging을 사용해야하는 일은 피할 수 없습니다. 아래의 예시로 사용법을 쉽게 익혀 봅시다. 

```python 
#main.py

import logging
from inference import infer

def main():
    logging.debug("without logger name")
    # 로거이름을 설정하지 않고 로깅을 하면 root로 표기됩니다.
    # 위와 같은 사용은 지양합니다.!
    main_logger = logging.getLogger("main/main")
    var = "to log"
    main_logger.error("how %s %s", var, "variable")
    # %s를 활용하여 variable을 로그에 삽입 할 수 있습니다. 
    infer()

if __name__ == "__main__" :
	logging.basicConfig(level=logging.DEBUG, \
        format='[%(levelname)s:%(name)s:%(asctime)s] %(message)s', \
        datefmt='%m/%d/%Y %I:%M:%S %p')
    # 위의 로깅 Config은 글로벌하게 한번만 하기를 기대합니다. 

    main()
```

```python
#inference.py
import logging

def infer():
    infer_logger = logging.getLogger("inference/infer")
    # 다른 모듈에서도 logging을 import한 후 logger 이름을 설정하여 사용합니다. 
    infer_logger.error("inference good")
```
실행결과 
```shell
$ python main.py
[DEBUG:root:09/14/2020 02:53:21 PM] without logger name
[ERROR:main/main:09/14/2020 02:53:21 PM] how to log variable
[ERROR:inferernce/infer:09/14/2020 02:53:21 PM] inference good
```

## **Conclusion**

-  print 대신 Logging을 사용합시다.
- ```main_logger = logging.getLogger("main/main")``` 와 같이 로거 이름을 설정하여 전체 시스템 실행시 어디서 로그가 발생했는지 알수 있게 합시다. 
- 적절한 Logging level 설정으로 배포시 간단하게 불필요한 Log를 안보이게 할 수 있게 합시다. 


## **Reference**

- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)