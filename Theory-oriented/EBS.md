# EBS (Elastic Block Store)
- EBS는 SSD나 HDD처럼 데이터를 저정하는 역할을 담당
- 하나의 AZ 서버 자원을 모아 생성하므로, 99.9999% 가용성 제공
- EC2와 같은 AZ에 존재 해야 하며, 다르다면 오류 발생
- 동일한 AZ에 생성된 EC2 장치에 탈부착 가능하고, 데이터를 잃지 않고 보관 가능
- 빠르게 사용량을 확장할 수 있으며, 프로비저닝한 부분에 대해 저렴한 비용으로 사용 가능
- 네트워크를 통해 연결되므로 EC2 인스턴스가 종료되어도 별개로 작동
- 인스턴스를 정지해도 독립적으로 살아있으므로, 스토리지 기능만 이용시 인스턴스에 대한 추가 요금을 내지 않아도 됨
- EC2 인스턴스에 여러 가지 EBS 부착이 가능하며, 반대도 가능

# EBS 볼륨 유형

|타입|범용|Provisioned IOPS|쓰루풋 최적화 HDD| Cold HDD| 마그네틱|
|:---:|:---:|:---:|:---:|:---:|:---:|
|이름|GP3|IO2|ST1|SC1|Standard|
|용량|1GB~16TB|4GB~16TB|500GB~16TB|500GB~16TB|1GB~1TB|
|사용|일반 범용|IOPS가 중요한 App/DB|쓰루풋이 중요한 App/Hadoop/OLAP DB 등|파일 저장소|백업/비주기적 데이터 액세스|
|MAX IOPS|16,000|64,000|500|250|40~200|

- 하드 성능은 용량과 MAX OPOS 수치를 보면 됨
- IOPS 수치가 높을수록 데이터 통신이 빠르며, 따라서 프로비전된 IOPS(64,000)이 가장 빠르고 좋음
- 일반적으로 범용타입은 GP3를 선택하지만, 요금을 극도로 아끼고 싶다면 마그네틱 사용
- Provisioned: 서버의 CPU, Memory 등의 자원을 할당 또는 적절히 배치하여 운영이 가능하도록 준비
- 

# 참고사이트
- [인파 EBS 링크](https://inpa.tistory.com/entry/AWS-%F0%9F%93%9A-EBS-%EA%B0%9C%EB%85%90-%EC%82%AC%EC%9A%A9%EB%B2%95-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC-EBS-Volume-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0)

- [EC2 인스턴스 최대 절전 모드](https://www.megazone.com/techblog_181214_ec2-instances/)