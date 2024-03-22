# CentOS Firewall 대역 차단/해제

- [CentOS] Firewall IP대역 차단/해제

```bash
$ firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="5.188.62.0/24" reject'
$ firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address="5.188.62.0/24" reject'

$ firewall-cmd --reload
$ firewall-cmd --list-all
```

https://realforce111.tistory.com/87

https://blog.servis.co.kr/index.php/2019/01/31/centos7-firewalld/


# Linux 디렉토리별 용량 확인

- 많은 용량이 쌓인 곳 찾기

```bash
$ du / | sort -n | tail -5
$ du /home | sort -n | tail -5
```

[리눅스 디스크 용량 및 저장 공간 확인, 부족 시 대처법](https://blog.naver.com/PostView.naver?blogId=hongganz&logNo=222437398559&from=search&redirect=Log&widgetTypeCall=true&directAccess=false)

# vim 편집기 명렁어

| h | 왼쪽 |
| --- | --- |
| j | 아래쪽 |
| k | 위쪽 |
| l | 오른쪽 |
| i | 문자입력 |
| a | 커서의 오른쪽에 문자입력 |
| a | 다음 단어의 첫 글자로 이동 |
| W | 공백을 기준으로 다음 단어의 첫 글자로 이동 |
| B | 공백을 기준으로 이전 단어의 첫 글자로 이동 |
| 0 | 행의 시작으로 이동 |
| G | 마지막 행으로 이동 |
| gg | 첫 행으로 이동 |
| 숫자 입력 후 G | 입력한 숫자행으로 이동 |
| $ | 행의 끝으로 이동 |
| d$ | 현재 행의 위치에서 마지막까지 삭제 |
| d0 | 현재 행의 위치에서 시작까지 삭제 |
| x, dl | 문자 한 개씩 삭제 |
| dw | 단어 한 개씩 삭제 |
| dgg | 현재의 위치에서 문자 시작까지 삭제 |
| dG | 현재의 위치에서 문서 끝까지 삭제 |
| dd | 현재 커서가 있는 행 삭제 |
| yy | 현재 커서가 있는 행 복사 |
| y$ | 현재 행의 위치에서 마지막까지 복사 |
| y0 | 현재 행의 위치에서 시작까지 복사 |
| yl | 문자 한 개씩 복사 |
| yw | 단어 한 개씩 복사 |
| ygg | 현재 행의 위치에서 문서 시작까지 복사 |
| yG | 현재 행의 위치에서 문서 끝까지 복사 |
| p | 붙여넣기 |




# [마무리필요] Linux Command 모음

[CentOS] Firewall IP대역 차단/해제

```bash
$ firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="5.188.62.0/24" reject'
$ firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address="5.188.62.0/24" reject'

$ firewall-cmd --reload
$ firewall-cmd --list-all
```

[https://realforce111.tistory.com/87](https://realforce111.tistory.com/87)

[https://blog.servis.co.kr/index.php/2019/01/31/centos7-firewalld/](https://blog.servis.co.kr/index.php/2019/01/31/centos7-firewalld/)

[Ubuntu] 가상환경에서 pip3 명령어 동작하지 않을 때

```bash
$ apt-get install python3-distutils
$ apt install python3-pip
```

[https://stackoverflow.com/questions/61611793/cannot-install-any-packages-with-pip-i-got-this-error-importerror-cannot-import](https://stackoverflow.com/questions/61611793/cannot-install-any-packages-with-pip-i-got-this-error-importerror-cannot-import)

[https://kaen2891.tistory.com/72](https://kaen2891.tistory.com/72)

가장 많은 용량이 쌓인 곳 찾기

```bash
$ du / | sort -n | tail -5
$ du /home | sort -n | tail -5
```

[리눅스 디스크 용량 및 저장 공간 확인, 부족 시 대처법](https://blog.naver.com/PostView.naver?blogId=hongganz&logNo=222437398559&from=search&redirect=Log&widgetTypeCall=true&directAccess=false)

[리눅스 디스크 용량 및 저장 공간 확인, 부족 시 대처법](https://blog.naver.com/PostView.naver?blogId=hongganz&logNo=222437398559&from=search&redirect=Log&widgetTypeCall=true&directAccess=false)

Linux CPU 사용률 확인하기

```bash
$ top -b -n1 | grep -Po '[0-9.]+ id'
$ top -b -n1 | grep -Po '[0-9.]+ id' | awk '{print 100-$1}'
```

Ubuntu SCP 파일 전송

```bash
$ scp [대상 로컬 파일 경로와 파일명] <원격지 사용자ID>@<원격지 주소>:[저장 경로와 파일명]
$ scp /home/banana/test.txt lee@192.168.1.19:/home/lee/test.txt
$ scp /usr/bin/chromedriver root@10.0.0.2:/usr/bin/chromedriver
```

[[Ubuntu] scp 사용법 - 서버간 데이터 전송하기 (file, directory)](https://ourcstory.tistory.com/162)

Ubuntu Chrome Driver 설치

```bash
$ cd /usr/local/local/bin
$ wget https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_linux64.zip
$ apt install unzip
$ unzip chromedriver_linux64.zip
$ rm chromedriver_linux64.zip
```

[ChromeDriver - WebDriver for Chrome - Downloads](https://chromedriver.chromium.org/downloads)

[ChromeDriver - WebDriver for Chrome - Downloads](https://chromedriver.chromium.org/downloads)

IP PORT 접속 확인

```
echo > /dev/tcp/<ip address>/<port
```

[https://itknowledge.co.kr/36](https://itknowledge.co.kr/36)

여긴 내 공인 IP 확인

`curl icanhazip.com`

[리눅스 공인 IP 확인](https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_%EA%B3%B5%EC%9D%B8_IP_%ED%99%95%EC%9D%B8)


# Update-alternatives 패키지 버전 관리

- python3 패키지 버전 등록

```bash
$ update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
$ update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
$ update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 3
```

- python3 패키지 버전 삭제

```bash
$ update-alternatives --remove python3 /usr/bin/python3.5
$ update-alternatives --remove python3 /usr/bin/python3.6
$ update-alternatives --remove python3 /usr/bin/python3.8
```

- python3 패키지 버전 변경

```bash
$ update-alternatives --config python3
```