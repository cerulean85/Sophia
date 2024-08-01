# RabbitMQ 사용하기

- 리소스 리스트  RabbitMQ 리파지토리를 추가 
```shell
sudo vi /etc/apt/sources.list

deb http://www.rabbitmq.com/debian/ testing main 
RabbitMQ의 public key를 ubuntu가 신뢰할 수 있도록 key 등록
 
wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo apt-key add rabbitmq-signing-key-public.asc
```

- RabbitMQ 설치
```shell
sudo apt-get install rabbitmq-server 
```
 
- Management Plugin 설치
  - Management Plugin도 활성화 통해 GUI환경 제공 (https://www.rabbitmq.com/management.html)

```shell
sudo rabbitmq-plugins enable rabbitmq_management
sudo service rabbitmq-server restart 
```

- 플러그인 설치 후 restart하면 반영된다.
- 웹브라우저로 http://serverip:15672/ 접속


- 관리자 계정  추가
```shell
sudo rabbitmqctl add_user rabbitmq password
sudo rabbitmqctl set_user_tags rabbitmq administrator 
```

- 사용자의 비번 변경
```shell
$ rabbitmqctl change_password <사용자> <신규비번>
```

- 사용자 권한 부여하기
```shell
rabbitmqctl set_permissions -p / "rabbitmq" ".*" ".*" ".*"
rabbitmqctl list_permissions
```

- cmd로 queue 삭제하기
  - RabbitMQ Management를 실행하였다면 브라우저를 통해 다음 경로로 접속하여 rabbitmqadmin 다운로드
  - 경로: http://localhost:15672/cli/rabbitmqadmin
  - 다운로드 받은 파일을 원하는 위치로 옮긴 후 다음 명령어로 실습

```shell

# CMD 실행 후 rabbitmqadmin을 옮긴 경로로 이동
cd C:\Program Files\RabbitMQ Server\rabbitmq_server-3.13.4\escript

# guest 계정으로, / 호스트의 celery 큐 삭제
python rabbitmqadmin -u guest -p guest -V / delete queue name=celery

# tos_admin 계정으로, / 호스트의 celery 큐 삭제
python rabbitmqadmin -u tos_admin -p <Any Pass> -V /TOS_SYSTEM delete queue name=celery

# tos_admin 계정으로, / 호스트의 TOS 큐 삭제
python rabbitmqadmin -u tos_admin -p <Any Pass> -V /TOS_SYSTEM delete queue name=TOS

```
- rabbitmqadmin은 파이썬으로 실행해야 함

## References
- [출처1](https://experiences.tistory.com/2)
- [출처2](https://sarc.io/index.php/miscellaneous/1632-ubuntu-rabbitmq-apt)
- [사용자 비번 변경](https://bangcfactory.tistory.com/entry/rabbitmq-%EC%82%AC%EC%9A%A9%EC%9E%90-%EA%B4%80%EB%A6%AC)
- [사용자 권한 변경](https://heodolf.tistory.com/50)
- [RabbitMQ Mamangement-cli](https://www.rabbitmq.com/docs/management-cli)