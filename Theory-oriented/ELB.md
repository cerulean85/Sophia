# ELB(Elastic Load Balancer)
- 키워드: Load Balancing, Listener, Target Group, Resource
- AWS의 사용자 정의 네트워크인 ```VPC(Virtual Private Network)```에 탑재
- 사용자 요청을 VPC 안의 EC2와 같은 ```Resource```로 부하 분산
- <b>Listener</b>와 <b>Target Group</b>으로 구성
  - Listener: 외부 요청을 받아 분산하여 전달
  - Target Group: 요청을 처리하는 Resource의 그룹
- 여러 개의 Listener와 Target Group을 거느릴 수 있음
- Resource는 Health Check로 끊임없이 상태 확인
- Listener는 외부 요청을 받아 들이는 Service Port 보유
  > Service Port로 들어오는 외부 요청만 처리함
- Listener가 적합한 요청을 Target Group에게 전달할 때는 Port Translation을 실시하므로, Target Group의 Port는 Listener의 Port와 달라도 됨
- L4 스위치와 비교해보면 Listener는 Virtual Server, Target Group은 Pool에 해당
- ELB는 크게 외부 인터넷에서 접속 가능한 공인/사설 IP 모두를 갖는 Internet LB와 내부 접근만을 허용하는 사설 IP만 갖는 Internal LB로 구분
- L4와 L7에 대한 부하 제어가 가능
- 둘 이상의 가용 영역에서 EC2 인스턴스 컨테이너, IP 주소 등 여러 대상에 걸쳐 수신되는 트래픽을 자동으로 분산
- 서버의 기본 주소가 바뀌면 LB를 새로 생성해아 하며, 하나의 주소에는 하나의 Target Group을 보냄
  > 즉, Target Group의 개수에 비례하여 LB의 개수와 비용이 늘어남
- AWS 환경에서는 4가지 유형의 LB를 지원하며, 사용자의 요구 사항과 환경에 맞춰 선택할 수 있음

## Load Balancer Node
- VPC 내 하나의 형태로 존재하는 다수의 NI(Network Interface)
- 공인/사설 IP 모두 보유 가능
- ELB는 실질적으로 사용자의 요청을 받아 Resource로 부하를 분산함
- AWS 콘솔상에서 NI 형태로만 보이므로 EC2의 NI에서 확인 가능
- Load Balancer Node는 AZ마다 하나씩 존재하고, 소속된 AZ 내의 Resource에게 요청을 전달함
- VPC에서 바라보는 ELB는 Load Balancer Node와 EC2의 집합으로 보이며, 각각 Listener(Load Balancer Node), Target Group(EC2 집합)에 해당