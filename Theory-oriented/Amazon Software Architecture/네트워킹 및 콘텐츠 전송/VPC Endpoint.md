# VPC Endpoint
- Amazon Virtual Private Cloud(VPC) 내에서 AWS서비스에 대한 프라이빗 연결을 제공하는 서비스
- 인터넷 게이트웨이, NAT 디바이스, VPN 연결 또는 AWS Direct Connect를 사용하지 않고도 VPC 내에서 AWS 서비스에 안전하게 접근 가능

# 주요 기능
- 프라이빗 연결
  - VPC와 AWS 서비스 간의 트래픽이 인터넷을 통하지 않고 AWS 네트워크 내에서 안전하게 전송됨
  - 보안 그룹 및 VPC 엔드포인트 정책을 사용하여 접근 제어를 설정할 수 있음

- 유형
  - 인터페이스 엔드포인트: AWS PrivateLink를 사용하여 VPC 내의 특정 서비스에 대한 프라이빗 IP 주소를 제공
  - 게이트웨이 엔드포인트: S3 및 DynamoDB와 같은 특정 AWS 서비스에 대한 프라이빗 경로를 제공

- 비용 효율성
  - 데이터 전송 비용을 절감할 수 있으며, 인터넷 게이트웨이 또는 NAT 디바이스를 사용하지 않으므로 추가 비용이 발생하지 않음

- 확장성 및 가용성
  - VPC 엔드포인트는 자동으로 확장되며, 고가용성을 제곰

# 사용 사례
- 보안 강화: 인터넷을 통하지 않고 AWS 서비스에 접근하여 보안을 강화할 수 있음
- 비용 절감: 데이터 전송 비용을 절감하고, NAT 게이트웨이 비용을 줄일 수 있음
- 규정 준수: 데이터가 인터넷을 통하지 않으므로 규정 준수 요구사항을 충족할 수 있음




# VPC Endpoint

- Endpoint는 요청을 보낼 때 필요한 목적지라 할 수 있음
  - 어떤 서비스나 리소스로 접근할 수 있는 특정 URL이나 네트워크 주소가 될 수 있음
- VPC Endpoint는 Endpoint 유형 중 하나로, VPC Endpoint를 사용하면 VPC 내부 또는 외부에 있는 AWS 서비스들과 통신할 때 인터넷 통신이 되지 않아도 Private한 통신 환경을 통해 서비스에 접근할 수 있도록 함

## VPC Endpoint 종류

1. Gateway Endpoint
- NAT 디바이스가 없어도 VPC에 연결된 라우팅 테이블을 참조하여 S3 또는 DynamoDB로 전달되는 트래픽에 사용
- AWS PrivateLink를 활성화하지 않음

![alt text](../../images/cloud/vpc_endpoint_exam.png)

- 1번: V1이 참조하는 라우팅 테이블은 10.0.0.0/16 대역의 IP는 Local로, 그외의 모든 IP대역은 igw로 향함. 인터넷을 통해 S3로 접근
- 2번: 반면, V2가 참조하는 라우팅 테이블은 동일하게 10.0.0.0/16 대역의 IP는 Local로 가지만, S3에 대한 Endpoint IP대역은 모두 VPC Endpoint로 향하게 됨


2. Interface Endpoint
- AWS PrivateLink 기술을 사용하여 구성
- VPC 내부 전용 라우팅 테이블이 생성
- Interface Endpoint를 생성하게 되면 AWS 서비스에 대한 ENI가 일반적으로 한개 생성
  - VPC 내부에서 전용 IP를 사용하여 AWS 서비스와 통신하는 인터페이스



## 참고사이트
- [[소개] VPC Endpoint란?](https://tech.cloud.nongshim.co.kr/2023/03/16/%EC%86%8C%EA%B0%9C-vpc-endpoint%EB%9E%80/)

- [AWS PrivateLink를 통한 새로운 SaaS 전략](https://www.megazone.com/techblog_191113_aws-privatelink/)