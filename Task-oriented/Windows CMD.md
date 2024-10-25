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