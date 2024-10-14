# Transit VPC에 대해 알려줘

## 요약
- Transit VPC는 여러 VPC와 온프레미스 네트워크 간의 트래픽을 중앙에서 관리하고 라우팅하기 위한 아키텍처 패턴

## 개요
- 네트워크 관리의 복잡성을 줄이고, 확장성을 높이며, 보안을 강화
- 여러 VPC와 온프레미스 네트워크를 연결하는 중앙 허브 역할

## 주요 기능 및 특징
- 중앙 집중식 관리: 모든 VPC와 온프레미스 네트워크 간의 트래픽을 중앙에서 관리
- 확장성: 새로운 VPC나 온프레미스 네트워크를 쉽게 추가 가능
- 보안: 중앙 집중식 보안 정책 적용 가능
- 비용 효율성: 여러 VPC 간의 트래픽을 직접 연결하는 것보다 비용 절감

## 구성
- Transit Gateway: 여러 VPC와 온프레미스 네트워크를 연결하는 중앙 허브
- VPN 연결: 온프레미스 네트워크와 Transit VPC 간의 보안 연결 제공
- 라우팅 테이블: 트래픽이 올바른 대상에 도달하도록 라우팅 규칙 정의
- 보안 그룹 및 네트워크 ACL: 트래픽을 제어하고 보안을 강화

## 작동 방식
1. Transit Gateway 생성
2. Transit Gateway에 VPC 연결
3. 라우팅 테이블 업데이트
4. 보안 그룹 설정

## 다른 서비스와의 연관성
- AWS Direct Connect와 연동하여 온프레미스 네트워크와의 고속 연결 제공
- AWS CloudWatch와 연동하여 네트워크 트래픽 모니터링 가능

## 사용 사례
- 대규모 엔터프라이즈 네트워크에서 여러 VPC와 온프레미스 네트워크 간의 트래픽 관리
- 멀티 리전 아키텍처에서 중앙 집중식 네트워크 관리

## 결론
- Transit VPC는 네트워크 관리의 복잡성을 줄이고, 확장성을 높이며, 보안을 강화하는 데 매우 유용한 아키텍처 패턴

## 예제 코드
```bash
# Transit Gateway 생성
aws ec2 create-transit-gateway --description "My Transit Gateway"

# Transit Gateway에 VPC 연결
aws ec2 create-transit-gateway-vpc-attachment --transit-gateway-id tgw-12345678 --vpc-id vpc-12345678 --subnet-ids subnet-12345678

# 라우팅 테이블 업데이트
aws ec2 create-route --route-table-id rtb-12345678 --destination-cidr-block 10.0.0.0/16 --transit-gateway-id tgw-12345678

# 보안 그룹 설정
aws ec2 authorize-security-group-ingress --group-id sg-12345678 --protocol tcp --port 6379 --source-group sg-87654321