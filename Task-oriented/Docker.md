# Dockerfile 명령어

## FROM
- 도커 이미지의 바탕이 되는 베이스 이미지 지정
- Dockerfile로 이미지를 빌드할 때 먼저 FROM 명령에 지정된 이미지를 내려 받음
## RUN
- 도커 이미지를 실행할 때 컨테이너 안에서 실행할 명령어 정의
## COPY
- 도커 동작 중 호스트 머신의 파일이나 디렉터리를 도커 컨테이너로 복사
## CMD
- 도커 컨테이너 실행 시 컨테이너 안에서 실행할 프로세스 지정
## ENTRYPONT
- CMD와 마찬가지로 컨테이너 안에서 실행할 프로세스 지정


# DockerFile 실행
1. Dockerfile 경로 이동
2. docker build –t [tag_name] .

# Docker 이미지 검색
- 호스트 cmd에서 아래처럼 명령어 입력하여 검색
  - docker search nodejs  # Node.js 이미지 검색
  - docker search openjdk  # OpenJDK 이미지 검색
  - docker search kafka  # Apache Kafka
  - docer search mysql --limit 5 # MySQL

# Error : Cannot perform an interactive login from a non TTY device
- 호스트 cmd에서 도커 명령어 실행 시 위의 오류가 발생하면 맨 앞에 winpty 입력
- winpty docker container run –p 5000:3000 –it zhwan85/goodwill
- winpty docker container run –p 5000:3000 zhwan85/goodwill

# Docker 이미지 목록 확인
- docker image ls

# Docker 이미지 생성
- docker image build –t zhwan85/goodwill:latest .

# Docker 이미지 배포
- docker image push zhwan85/goodwill:latest
- docker commit c33c299a3bd4 zhwan85/goodwill:lastest
- docker image tag [이미지명:현재태그] [이미지명:변경태그]
- docker image tag zhwan85/goodwill:latest zhwan85/goodwill:0.0.1
- docker push zhwan85/goodwill:0.0.1
- [참고사이트](https://nicewoong.github.io/development/2018/03/06/docker-commit-container/)

# Docker 이미지 삭제
- docker rmi [이미지아이디]

# Docker 컨테이너 목록 확인
- docker ps –a
- docker container ls –a

# Docker 컨테이너 생성
- winpty docker container run -it –p 5000:3000 zhwan85/goodwill
포트포워딩: [호스트포트번호:컨테이너포트번호]
- -it: Windows에서 커맨드창으로 컨테이너 실행 시 -it를 안 붙이면 실행 안됨  
- 포트 포워딩은 run에서만 가능하므로, 컨테이너를 commit 후 컨테이너를 재생성하여 포트포워딩 해야 함

- docker container run -it –p 5000:3000 –p 4000:2000 zhwan85/goodwill
- 포트포워딩은 여러 개 가능

- winpty docker container run -it –p 5000:3000 –p 3308:3306 —privileged zhwan85/goodwill

- docker container run -it  -v C:\Users\JHKIM\Desktop\GoodWill:/home/app -d -p 5000:3000 -p 5030:3030 -p 5306:3306 -p 5084:8084 -p 5181:2181 -p 5092:9092 --name goodwill  --privileged zhwan85/goodwill:0.0.2 init

# Docker 컨테이너 시작/재시작/정지
- docker start/restart/stop [컨테이너명or아이디]
- [참고사이트](https://snowdeer.github.io/docker/2018/01/03/docker-launch-container-from-image/)


# Docker 컨테이너 접속
- docker attach [컨테이너명or아이디]

# Docker 컨테이너 백그라운드 실행 시 접속
- docker exec -it [컨테이너명or아이디] bash

# Docker 컨테이너 외부에서 명령 실행
- docker exec [컨테이너명or아이디] [커맨드]
- docker exec zhwan85:goodwill:0.0.1 echo “Hello!!”

# Docker 컨테이너 삭제
- docker rm [컨테이너명or아이디]
 
# Docker 컨테이너 재시작
- docker container restart silly_heyrovsky

# Docker 이미지 최초 배포
- docker login –u zhwan85 –p 비밀번호
- docker image push zhwan85/goodwill:latest

# Docker 컨테이너 커밋
- docker commit [컨테이너ID] [이미지명]

# Docker 이미지 태그 달기
- docker image tag [이미지명:현재태그] [이미지명:변경태그]
- docker image tag zhwan85/goodwill:latest zhwan85/goodwill:0.0.1

# Docker Node.js 설정 참고
- [참고사이트](https://www.daleseo.com/docker-nodejs/)


# Docker 파라미터 

## -i
- 컨테이너 실행 시 컨테이너 쪽 표준 입력과의 연결을 그대로 유지
- 컨테이너 쉘에 들어가 명령 실행 가능 하며 –t 옵션과 함께 사용
## -t
- 유사 터미널 기능 활성화
- -i 옵션을 사용하지 않으면 유사 터미널을 실행해도 여기에 입력할 수 없으므로 –i와 –t옵션을 같이 사용하거나 이드옵션을 축약한 –it 옵션 사용
## --rm
- 컨테이너 종료 시 컨테이너 파기 옵션
- 한 번 실행 후 유지 않아도 되는 명령행 도구 컨테이너 실행할 때 유용
## -v
- 호스트와 컨테이너 간에 디렉터리나 파일 공유
## -d
- -i 옵션의 반대로 컨테이너를 백그라운드 실행
## -p
- 포트포워딩 [외부포트]:[내부포트]
- 여러 개 열려면 –p [외부포트]:[내부포트] -p [외부포트]:[내부포트] ... 형태로 반복 해주면 됨
## -c
- CPU 자원 분배 설정
## -m
- 메모리 한계 설정
## /bin/bash
- 리눅스의 경우 컨테이너에 bash 쉘 이용
## --privileged
- 기본적으로 실행되는 unprivileged모드에서는 시스템 자원에 대한 접근이 제한적이므로 거의 모든 커널 기능을 사용하기 위하여 privileged모드로 실행해야 함
- 아래는 발생 가능한 에러
- Failed to get D-Bus connection [관련글 참고](https://lsjsj92.tistory.com/415)
  - --privileged와 init 명령어를 사용하여 컨테이너를 생성해야 함

  - docker container run -it -d -p 5000:3000 -p 3308:3306 --privileged –d zhwan85/goodwill:0.0.1 init
    - I: 표준입력 연결, t: tty 활성화, d: 백그라운드 실행
    - p: 포트포워딩, privileged: 가용 시스템 자원 확장

  - docker container run -it -d -p 5000:3000 -p 3308:3306 --privileged  zhwan85/goodwill:0.0.1 init


# 데이터 볼륨
- 컨테이너에서 실행된 애플리케이션이 stateful 유형이라면 새로운 컨테이너가 배포되어도 사용 중인 파일이나 디렉터리의 상태가 유지되어야 된다. 데이터 볼륨은 호스트와 컨테이너 사이의 디렉터리 공유 및 재사용 기능을 제공하여 애플리케이션이 사용하는 파일이나 디렉터리를 보존한다.


# 엔트리포인트(Entrypoint)
- 도커 컨테이너가 실행할 때 고정적으로 실행되는 스크립트 혹은 명령어
- 생략 가능하며 생략 시 커맨드에 지정된 명령어로 수행
- docker run --entrypoint echo ubuntu:focal hello world

# 커맨드(Command)
- 도커 컨테이너가 실행할 때 수행할 명령어 혹은 엔트리포인트에 지정된 명령어에 대한 인자값

# 환경변수
- docker run -i -t -e MY_HOST=fastcampus.com ubuntu:focal bash
- -e, --env, --env-file 
- nginx, grafana 등 컨테이너의 환경변수 확인

# docker exec
- 실행 중인 컨테이너에 명령어 실행
- docker exec [container] [command]
- docker exec -i -t my-nginx bash: my-nginx 컨테이너에 Bash 셀로 접속
- docker exec my-nginx env: my-nginx 컨테이너에 환경변수 확인
docker run -d --name my-nginx nginx
docker exec my-nginx env
docker exec -i -t my-nginx bash
  

# docker network

# docker volume

# docker build
