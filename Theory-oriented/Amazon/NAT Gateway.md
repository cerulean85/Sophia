# NAT (Network Address Translation)
- 한정된 IP자원 때문에 대부분의 네트워크는 호스트 중 일부만 인터넷 통신을 수행
- 따라서 대부분의 호스트는 외부에 노출하는 IP 수를 줄이기 위해 인터넷 통신에만 Public IP를 사용 
- Private IP에서 인터넷으로 요청을 보내면 NAT 라우터에서 주소 변환 테이블에 따라 Public IP로 변환
- 이때 변환된 내용은 NAT 변환 테이블에 기록되는데, 인터넷으로부터 응답이 라우터에 도착하면 이 테이블을 참조하여 Private IP를 가진 호스트에게 전달

# AWS NAT Gateway
- NAT Gateway는 AWS에서 제공하는 NAT 서비스
- Private Subnet의 인스턴스가 인터넷과 같은 VPC 외부 서비스에 연결할 수 있도록 함
- NAT Gateway는 외부 서비스에서 Private Subnet 내의 인스턴스와 연결할 수 없도록 함
- 즉, Private Subnet 내의 EC2가 인터넷, AWS 서비스 등의 외부 서비스에 접근 가능하도록 하고, 외부 서비스에서 해당 EC2로의 접근을 막기 위해 사용
- NAT Gateway는 VPC 내의 Public Subnet 내에 생성해야 함

# NAT Gateway 설정 순서
1. NAT Gateway가 속할 Public Subnet 지정
2. NAT Gateway와 연결할 Elastic IP 주소 지정
    > NAT Gateway 연결 후에는 탄력적 IP 주소를 변경할 수 없음
3. NAT Gateway 만든 뒤 한 개 이상의 Private Subnet과 연결된 라우팅 테이블을 업데이트하여 인터넷 바운드 트래픽이 NAT Gateway를 가리키도록 함

# NAT Gateway 기본 사항
- 기본 라우팅 테이블은 Prviate Subnet의 인스턴스에서 NAT Gateway로 인터넷 트래픽을 보냄
- NAT Gateway는 Internet Gateway로 트래픽을 보낼 때 NAT Gateway의 Source IP를 Elastic IP 주소로 사용

![VPC NAT](../images/cloud/vpc_nat.png)

# NAT Gateway 규칙 및 제한
- 하나의 Elastic IP만 NAT Gateway에 연결할 수 있으며, 연결 후 NAT Gateway에서 Elastic IP 주소의 연결을 끊을 수 없음
- 보안 그룹을 NAT Gateway와 연결할 수 없으며, Private Subnet의 인스턴스에 대한 보안 그룹을 사용하여 해당 인스턴스에서 주고 받는 트래픽을 제어할 수 있음
- Network ACL(Access Control List)을 사용하여 NAT Gateway가 위치한 Subnet에서 주고 받는 트래픽을 제어할 수 있음
- Network ACL은 NAT Gateway의 트래픽에 적용되며, NAT Gateway는 포트 1024 ~ 65535를 사용
- NAT Gateway가 생성되면 Subnet의 IP 범위에 속하는 Private IP가 자동으로 할당된 네트워크 인터페이스(Network Interface, NI)를 받음
- Amazon EC2 콘솔에서 NAT Gateway의 NI를 볼 수 있으며, NI의 속성을 수정할 수는 없음

# NAT Gateway vs. NAT Instance
- NAT Gateway는 AWS가 관리 하므로 관리 부담이 적고, 고가용성이며, 비싸며, 사용량 기반 비용 지불. 그리고 Bastion 서버 불가능하며, 보안그룹도 적용할 수 없음

- NAT Instance는 사용자가 관리하므로 관리부담이 크고, 가용성 부족. 스케일링을 수동으로 해야 하며, Bastion 서버 사용 가능. 보안그룹 적용 가능하며 NAT Gateway 보다는 저렴하며, EC2 인스턴스 유형과 시간에 따라 비용 결정


# 참조/링크
- [NAT GATEWAY](https://hyeyeon13.tistory.com/20)
- [[AWS] NAT Gateway와 NAT Instance의 차이점 정리](https://jibinary.tistory.com/356#google_vignette)
