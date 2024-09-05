# AWS PrivateLink
- Amazon Web Services(AWS)에서 제공하는 서비스
- VPC(Virtual Private Cloud) 내에서 AWS 서비스 및 타사 서비스에 대한 프라이빗 연결을 설정할 수 있도록 지원
- PrivateLink를 사용하면 인터넷을 통해 데이터를 전송하지 않고도 안전하게 서비스에 액세스할 수 있음

# 주요 특징
## 1. 프라이빗 연결
- 인터넷을 거치지 않고 VPC 내에서 AWS 서비스 및 타사 서비스에 직접 연결할 수 있음
- 서비스 엔드포인트를 통해 프라이빗 IP 주소를 사용하여 연결을 설정

## 2. 보안
- 데이터가 인터넷을 통과하지 않기 때문에 보안이 강화
- VPC 보안 그룹 및 네트워크 ACL을 사용하여 액세스를 제어할 수 있음

## 3. 간편한 설정
- AWS Management Console, AWS CLI, AWS SDK를 사용하여 쉽게 설정할 수 있음
- 서비스 엔드포인트와 엔드포인트 서비스 간의 연결을 간편하게 구성할 수 있음

## 4. 확장성 및 가용성
- AWS의 글로벌 인프라를 활용하여 높은 가용성과 확장성을 제공
- 여러 가용 영역(AZ)에 걸쳐 엔드포인트를 배포할 수 있음

# 사용 사례
- 프라이빗 SaaS 연결
    - 타사 SaaS 애플리케이션에 대한 프라이빗 연결을 설정하여 보안을 강화할 수 있음
    - 예를 들어, 데이터베이스 서비스, 모니터링 서비스 등에 프라이빗 연결을 설정할 수 있음

- 내부 서비스 연결
    - 여러 VPC 간에 내부 서비스 연결을 설정하여 데이터 전송을 안전하게 할 수 있음
    - 예를 들어, 마이크로서비스 아키텍처에서 서비스 간 통신을 프라이빗하게 설정할 수 있음

- 하이브리드 클라우드 아키텍처
    - 온프레미스 데이터 센터와 AWS 간의 프라이빗 연결을 설정하여 하이브리드 클라우드 아키텍처를 구현할 수 있음
    - AWS Direct Connect와 함께 사용하여 온프레미스 네트워크와 AWS 간의 프라이빗 연결을 설정할 수 있음

# 작동 방식
## 1. 엔드포인트 서비스 생성
- 서비스 제공자가 VPC 내에서 엔드포인트 서비스를 생성
- 엔드포인트 서비스는 하나 이상의 네트워크 로드 밸런서를 통해 트래픽을 수신

## 2. 엔드포인트 생성
- 서비스 소비자가 자신의 VPC 내에서 엔드포인트를 생성
- 엔드포인트는 서비스 제공자의 엔드포인트 서비스와 연결

## 3. 트래픽 라우팅
- 서비스 소비자의 VPC에서 발생하는 트래픽은 엔드포인트를 통해 서비스 제공자의 엔드포인트 서비스로 라우팅
- 트래픽은 인터넷을 통과하지 않고 AWS 네트워크 내에서 안전하게 전송

# 예제 코드
- 다음은 AWS CLI를 사용하여 AWS PrivateLink를 설정하는 예제
- 엔드포인트 서비스 생성
```sh
aws ec2 create-vpc-endpoint-service-configuration \
    --network-load-balancer-arns arnawselasticloadbalancingregionaccount-idloadbalancer/net/my-nlb \
    --acceptance-required
```
- 엔드포인트 생성
```sh
aws ec2 create-vpc-endpoint \
    --vpc-id vpc-abc123 \
    --service-name com.amazonaws.vpce.region.vpce-svc-abc123 \
    --vpc-endpoint-type Interface \
    --subnet-ids subnet-abc123 \
    --security-group-ids sg-abc123
```

요약
AWS PrivateLink는 VPC 내에서 AWS 서비스 및 타사 서비스에 대한 프라이빗 연결을 설정할 수 있는 서비스입니다. 인터넷을 통하지 않고 안전하게 서비스에 액세스할 수 있으며, 보안, 간편한 설정, 확장성 및 가용성 등의 이점을 제공 프라이빗 SaaS 연결, 내부 서비스 연결, 하이브리드 클라우드 아키텍처 등의 다양한 사용 사례에 활용할 수 있음


---
- 가용성 높고 확장 유연한, 프라빗하게 VPC를 서비스가 마치 VPC에 있는 것처럼 서비스를 연결함
- VPC로부터 도달하는 기술된 API 엔드포인트, 사이트, 서비스 통제 가능
- igw가 불필요 하고, NAT Device, Public IP 주소, AWS Direct Connect dusruf, Site-to-Site VPN 연결을 Private 서브넷에서 서브로의 연결 허용

## Use cases
- VPC 엔드포인트를 생성하여 AWS PrivateLink와 통합되는 VPC의 리소스를 VPC 엔드포인트를 만들 수 있음
- 사용자 고유의 VPC 엔드포인트 서비스를 만들 수 있고, 이 서비스는 다른 AWS 고객이 이용할 수 있음
- 다음 다이어그램에서 좌측 VPC는 프라이빗 서브넷 내에 몇 개의 EC2 인스턴스와 세 가지 인터페이스 VPC 엔드포인트를 가짐
- 가장 상단의 VPC 엔드포인트는 AWS 서비스와 연결됨
- 중앙의 VPC 엔드포인트는 또 다른 AWS 계정(VPC 엔드포인트 서비스)에 의해 호스트된 서비스에 연결됨
- 하단의 VPC 엔드포인트는 AWS 마켓플레이스 파트너 서비스에 연결됨

## Concepts
- VPC를 정의하기 위해 Amazon VPC를 사용하는데, 이것은 지역적으로 격리된 가상 네트워크임
- AWS 리소스를 VPC에서 런치할 수 있는데, VPC 내의 리소스가 VPC 바깥의 리소스에 연결할 수 있도록 함
- 예를 들어, VPC가 인터넷에 접근 할 수 있도록 인터넷 게이트웨이를 추가하면 되고, 온프레미스 네트워크에 접근할 수 있도록 VPN 연결을 추가하면 됨
- 대안으로 사용자의 VPC 내의 리소스가 프라이빗 IP 주소를 사용하는 다른 VPC의 서비스에 연결할 수 있도록 AWS PrivateLink를 사용하면 됨

![alt text](../../images/cloud/privatelink.png)