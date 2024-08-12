# AWS Traffic Mirroring
- 유형이 ```interface```인 ENI의 네트워크 트래픽을 복사하는 데 사용할 수 있는 Amazon VPC의 특징
- 트래픽을 ```Out-of-band``` Security와 Content Inspection, Threat Monitoring, Trouble Shooting 등의 모니터링 어플라이언스로 보낼 수 있음
- 보안과 모니터링 어플라이언스는 개별 인스턴스로 혹은 NLB나 UDP 리스너를 가진 Gateway Load Balancing 뒤의 인스터스 무리로 배포될 수 있음
- 트래픽 미러링은 filters와 packet truncation을 지원하여 사용자가 선택한 모니터링 툴을 이용하여 관심있는 트래픽만 추출할 수 있게 함