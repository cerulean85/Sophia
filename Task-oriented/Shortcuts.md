# VSCode
- 줄 번호로 이동: Ctrl + G
- 파일 찾기: Ctrl + P
- 디버깅
  - 디버깅 실행: F5
  - 디버깅 종료: Shfit + F5
  - 디버깅 재실행: Ctrl + Shift + F5
  - Step Over: F10 
    > **Step Over**? 현재 라인의 코드를 실행하되, 그 라인에 함수 호출이 포함되어 있으면 그 함수의 내부로 들어가지 않고 함수 호출을 완료한 후 다음 라인으로 넘어감
  - Step Into: F11
    > **Step Into**? 현재 실행 중인 코드 라인의 함수 호출이 있을 때, 그 함수 내부로 들어가서 한 줄씩 디버깅을 진행
  - Step Out: Shfit + F11
  - Toggle Breakpoint: F9
    - Remove All Breakpoint (Custom): Ctrl + Shift + F9
  - 브레이크 포인트 따라가기(Continue): F5

# VSCode Node.js Debugging 설정
- Ctrl + Shift + D를 눌러 ```RUN AND DEBUG```를 열어줌
- launch.json을 만들어주기 위해 좌측에서의 콤보박스에서 [Node.js...] 선택
- 다음과 같이 json 입력
```js
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}/app.js"
        }
    ]
}
```


# PyCharm 단축키
