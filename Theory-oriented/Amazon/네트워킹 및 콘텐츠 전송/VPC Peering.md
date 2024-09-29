# VPC Peering

## 요약
- VPC Peering은 두 개의 VPC 간에 네트워크 트래픽을 직접 전송할 수 있게 하는 서비스임

## 개요
- VPC Peering은 AWS 내의 두 VPC 간에 프라이빗 IP 주소를 사용하여 트래픽을 전송할 수 있게 함
- 동일한 AWS 계정 내 또는 다른 AWS 계정 간의 VPC 간에도 연결 가능함

## 주요 기능 및 특징
- **프라이빗 연결**: 인터넷을 거치지 않고 프라이빗 IP 주소를 사용하여 VPC 간 트래픽 전송 가능
- **보안**: 트래픽이 AWS 네트워크 내에서만 이동하므로 보안성이 높음
- **유연성**: 동일한 리전 내 또는 다른 리전 간에도 VPC Peering 설정 가능
- **확장성**: 여러 VPC 간의 피어링 연결을 설정하여 네트워크를 확장 가능
- **비용 효율성**: 데이터 전송 비용이 낮음
- **간편한 설정**: AWS Management Console, AWS CLI, AWS SDK를 통해 쉽게 설정 가능

## 구성
- AWS Management Console, AWS CLI, AWS SDK를 통해 설정 및 관리 가능
- 피어링 연결 요청 및 수락
- 라우팅 테이블 업데이트
- 보안 그룹 및 네트워크 ACL 설정

## 작동 방식
1. AWS Management Console에 로그인
2. VPC 서비스 선택
3. VPC Peering 연결 생성
4. 피어 VPC ID 및 계정 ID 입력
5. 피어링 연결 요청 전송
6. 피어링 연결 수락
7. 각 VPC의 라우팅 테이블 업데이트
8. 보안 그룹 및 네트워크 ACL 설정

## 다른 서비스와의 연관성
- Amazon EC2 인스턴스 간의 통신 가능
- Amazon RDS와 같은 AWS 서비스와 통합 가능
- AWS Direct Connect와 함께 사용하여 온프레미스 네트워크와 통합 가능

## 사용 사례
- 여러 VPC 간의 데이터 전송
- 멀티 계정 환경에서의 네트워크 통합
- 리전 간 데이터 전송
- 마이크로서비스 아키텍처에서의 서비스 간 통신

## 결론
- VPC Peering은 두 개의 VPC 간에 안전하고 효율적인 네트워크 트래픽 전송을 가능하게 하여 다양한 비즈니스 요구를 충족시킴

## 예제 코드
```python
import boto3

client = boto3.client('ec2')

response = client.create_vpc_peering_connection(
    VpcId='vpc-12345678',
    PeerVpcId='vpc-87654321',
    PeerOwnerId='123456789012'
)

print(response)
```