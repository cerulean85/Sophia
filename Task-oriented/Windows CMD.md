## Task 검색
```sh
tasklist | findstr [구문]

## 예시
tasklist | findstr "celery"
```

## Task 종료
```sh
taskkill /PID [프로세스ID] /F
```

## Port 검색
```sh
netstat -ano | find "[포트번호]"
# 예시: netstat -ano | find "8080"
```

## OpenSSH Server 활성화
1) 시작메뉴 > 찾기 > 선택적 기능 > 기능 추가 > OpenSSH Server 추가

2) 관리자 권한으로 Powershell 열기

2) 설치 상태 확인
```sh
 $ Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
 ```

 3) OpenSSH Server 실행 상태 확인
 ```sh
 $ Get-Service sshd
 ```

 4) OpenSSH Server 시작
 ```sh
 $ Start-Service sshd

 # 부팅 때마다 실행시키려면 아래 명령어 입력
 $ Set-Service -Name sshd -StartupType 'Automatic'
 ```
 
## SSH 기반 파일 전송
```sh
# scp C:\path\to\local\file username@remote_host:/path/to/remote/directory
scp C:\Users\John\Documents\example.txt username@remote_host:/home/username/

# 예시
# scp C:/Users/ZHKim/Desktop/any_file.txt zhkim@123.23.23.14:/C:/Users/RemoteZHKim/Desktop
# scp "C:/Users/ZHKim/Desktop/어떤 파일.pptx" zhkim@123.23.23.14:/C:/Users/RemoteZHKim/Desktop
# scp C:/Users/Hanwha/Desktop/20241029_1.md swdev.common1@172.22.104.226:/C:/Users/swdev.common1/Desktop/20241029_1.md
```