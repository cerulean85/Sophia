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