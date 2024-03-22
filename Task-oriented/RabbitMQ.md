RabbitMQ 명령어 메모

리소스 리스트  RabbitMQ 리파지토리를 추가 
sudo vi /etc/apt/sources.list

deb http://www.rabbitmq.com/debian/ testing main 
RabbitMQ의 public key를 ubuntu가 신뢰할 수 있도록 key 등록
 
wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo apt-key add rabbitmq-signing-key-public.asc
 
RabbitMQ 설치
 
sudo apt-get install rabbitmq-server 
 

Management Plugin 설치
Management Plugin도 활성화 통해 GUI환경 제공 (https://www.rabbitmq.com/management.html)
sudo rabbitmq-plugins enable rabbitmq_managementsudo service rabbitmq-server restart 
플러그인 설치 후에는 RabbitMQ를 restart 후 반영 된다.

3. 관리자 계정  추가
sudo rabbitmqctl add_user rabbitmq passwordsudo rabbitmqctl set_user_tags rabbitmq administrator 

4. Management Plugin 접속웹브라우저로 http://serverip:15672/  접속
출처
https://experiences.tistory.com/2
https://sarc.io/index.php/miscellaneous/1632-ubuntu-rabbitmq-apt


사용자의 비번 변경
$ rabbitmqctl change_password <사용자> <신규비번>
https://bangcfactory.tistory.com/entry/rabbitmq-%EC%82%AC%EC%9A%A9%EC%9E%90-%EA%B4%80%EB%A6%AC


사용자 권한 부여하기
rabbitmqctl set_permissions -p / "rabbitmq" ".*" ".*" ".*"
rabbitmqctl list_permissions
https://heodolf.tistory.com/50
