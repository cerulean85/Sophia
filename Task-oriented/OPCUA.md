# OPCUA

## OPCUA란?

## KepServer 설치

## KepServer Simulator 설정

## 주의사항

- KepServer에서 Project > 우클릭 > Property Editor > OPC UA > Allow anonymous login > YES 변경 후,
  - KepServer > Runtime > Reinitialize 해줘야 반영이 됨
- UaExpert에서 OPCUA 연결 설정할 때 Localhost는 127.0.0.1로 IP를 입력해야 함
- Security Polices 끄려면, 
  - 시작표시줄의 메뉴 > KepServer 우클릭 > OPC UA Configuration > Server Endpoints > Basic256Sha256 체크 해제


## 참고 사이트
- [OPC UA 서버 설정](https://oppr123.tistory.com/35)
- [이 페이지 뒤에 OPC UA 서버 설정 내용 추가](https://swsolution.atlassian.net/wiki/spaces/QA/pages/422510653/02.+OPCUA+Kepserver+KEPServerEX+6+Configuration)