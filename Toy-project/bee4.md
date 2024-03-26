# bee4 (beeFour) 정의 및 목표

## bee4 정의
- 꿀벌과 Net의 조합
- 꿀벌은 영어로 bee이고, Network의 Net은 한글발음이 넷인데, 숫자 4도 넷이라고 발음함
- 꿀벌은 한 마리의 여왕을 필두로 집단을 이루고 있음
- Network는 상호협력을 최우선으로 여김
- 즉, bee4은 우두머리(매니저)에 의한 협력이 강조되는 네트워크 시스템을 의미함

## bee4 목표

# bee4 설계

## 구성

## 매니저
### 역할
- DB와 Worker 사이의 Broker로써, DB에서 Task를 조회하여 Worker에게 전달
- Worker에게 Task를 균등하게 분배하여 병목을 해소
### 기능
- **조회(Selection)**: 주기적으로 DB를 조회하여 Task를 조회
- **스케쥴링(Scheduling)**: Worker의 유휴 상태를 확인하여 Worker들의 처리 순서 결정
- **전달(Delivery)**: 메시지큐에 Worker가 처리해야 할 Task를 전달
- **Health Check**: 클러스터상에서 Working-Manager의 Health를 StandBy-Manager가 확인
- **Fall Out(???용어 뭐드라)**: 고장 시 Stand-by Manager가 이어 받아 계속 진행

## 참고
- 아래 파일 참고하여 설계
  - E:\Study\References\유출금지_정리중\(참고)텍스톰 수집  네트워크 설계 v0.6.pptx
  - E:\Study\Toy-project\PROJECT_Earthling.pptx
  - E:\Study\Toy-project\스마트메모 시스템 구성도.pptx