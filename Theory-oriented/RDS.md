# Multi-AZ
- 이름 그대로 여러 개의 AZ에 RDS 분산하는 방식
- DB 가용성 유지하는 데 목적이 있음

![alt text](../images/db_multi_az.png)

- active 상태의 master 인스턴스에 문제 생기면 다른 AZ에 설치된 stanby 인스턴스가 master로 자동 승격되어 서버 운영

- stanby 인스턴스는 평상시 master 인스턴스에 발생하는 데이터 변화를 동기 방식으로 복제(Aurora는 비동기식)하여 동일 데이터를 유지
  - 읽기 전용 복제본으로 사용할 수 없으며, 이것이 목적이라면 Read Replica를 사용해야 함
- RDS는 서비스 도메인이 있는데 평상시엔 master 인스턴스의 IP를 사용하다 active 인스턴스에 문제 발생시 stanby 인스턴스 IP로 변경돼 자동으로 장애를 복구함. 즉, DNS 활용한 Fail-Over

- DNS 질의 결과는 시스템 내부에 특정 시간 주기(TTL: Time To Live) 만큼 캐싱되므로, AWS 이 값을 60초 미만으로 설정할 것을 권고

- 동기식 복제가 지속적으로 발생하기에 Single-AZ 보다 Write/Commit 작업에 지연 생길 수 있음

- Multi-AZ 구성시 RDS 인스턴스 타입을 Provisioned IOPS로 설정하면 좋음


# Read Replica
- DB는 일반적으로 읽기 작업이 쓰기 작업보다 많으므로, READ 트랜잭션은 Read Replica에서 처리하도록 애플리케이션 설계

- 상대적으로 Primary 인스턴스에 부하가 덜 가고 결과적으로 쓰기와 읽기가 분리되어 부하분산. 각각의 트랜잭션 빨라짐

- 같은 AZ 사용하면 Read Replica는 소스 인스턴스와 동일한 기본 스토리지를 공유하므로 비용 절감되는데, 다른 AZ, 심지어 다른 리전에도 설치될 수 있음

- 쓰기/읽기 전용 인스턴스에 문제 생기면 Read Replica는 Primary 인스턴스로 승격

- RDS는 리전 간 복제해도 원본 DB 인스턴스와 읽기 전용 복제본 간에 퍼블릭 키를 암호화 하거나 AWS 보안 구성을 통해 안전한 통신 채널을 설정할 수 있음

- AWS Ke Management Service(KMS)를 통해 저장 중 암호화된 Amazon RDS DB 인스턴스에 대해서도 읽기 전용 복제본을 생성할 수 있음


![alt text](../images/cloud/replica.png.png)


# 참고사이트
[다중 영역(Multi-AZ)& 읽기 전용(Read Replica) 복제](https://velog.io/@amoeba25/%EB%8B%A4%EC%A4%91-%EC%98%81%EC%97%ADMulti-AZ-%EC%9D%BD%EA%B8%B0-%EC%A0%84%EC%9A%A9Read-Replica-%EB%B3%B5%EC%A0%9C)