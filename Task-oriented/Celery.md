# Celery 개요
- 이메일 발송이나 주문 내역 엑셀 다운로드 등과 같이 처리나 쿼리 실행이 오래 걸리는 작업을 비동기적으로 수행할 때 활용
- 메시지를 전달하는 Publisher와 Message Broker에서 메시지 가져와 작업을 수행하는 Worker로 구성
- Message Borker로는 대표적으로 RabbitMQ를 활용


## Example
```python
# main.py
app = Celery(
    'my_tasks'
    , broker='amqp://admin:admin1234eo@localhost:5672//'
    , backend='rpc://' # 결과 반환
    , include=['tasks.calc']  # 등록 안 해야 함
)
```

```python
# tasks/calc.py

import time
 
from main import app
 
@app.task
def add( num1, num2 ):
    time.sleep(1)    
    print( "{} + {} = {}".format( num1, num2, num1+num2 ) )    
    return num1 + num2
 
@app.task
def callback( results ):
    return results
```

```python
# run.py
from tasks import calc
 
# delay와 apply_async
task_1 = calc.add.delay( 1, 2 )
task_2 = calc.add.apply_async( args=[3, 4], ignore_result=True )
task_3 = calc.add.apply_async( args=[5, 6], kwargs={} )
 
print( "# 1. Task ID 확인" )
print( "task_1 is {}".format( task_1.id ) )
print( "task_2 is {}".format( task_2.id ) )
print( "task_3 is {}".format( task_3.id ) )
 
print( "\n# 2. Task 상태" )
print( "task_1 is ready? {}".format( task_1.ready() ) ) # False
print( "task_2 is ready? {}".format( task_2.ready() ) ) # False
print( "task_3 is ready? {}".format( task_3.ready() ) ) # False
 
print( "\n# 3. 실행결과 확인" )
print( "task_1 is {}".format( task_1.get() ) ) # 3
print( "task_2 is {}".format( task_2.get() ) ) # None → ignore_result에 의해 실행 결과 알 수 없음
print( "task_3 is {}".format( task_3.get() ) ) # 11
 
print( "\n# 4. Task 상태" )
print( "task_1 is ready? {}".format( task_1.ready() ) )
print( "task_2 is ready? {}".format( task_2.ready() ) )
print( "task_3 is ready? {}".format( task_3.ready() ) )
```

## 실행
```sh
# 둘 중 하나 선택
celery -A main worker -l INFO -P Soloi -c 10
celery worker --app=main --loglevel=INFO --pool=solo --concurrency=10
```
- [A | --app]: Celery App의 파일명
- [worker]: Worker 실행 명령어
- [-l | --loglevel]: Logging 레벨 설정, DEBUG, INFO, WARNING, ERROR, CRITICAL, or FATAL
- [-P | --pool]: 프로세스 처리 방식
- [-c | --concurrency]: 동시에 병행처리 할 수 있는 Task 수

## References
- [[Celery] 무작정 시작하기 (2) - Task](https://heodolf.tistory.com/63)