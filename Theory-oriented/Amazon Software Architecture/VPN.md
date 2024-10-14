# AWS VPN

## 요약
- AWS VPN은 AWS 클라우드와 온프레미스 네트워크 간의 안전한 연결을 제공하는 서비스입니다.

## 개요
- AWS VPN은 두 가지 주요 서비스로 구성됩니다: AWS Site-to-Site VPN과 AWS Client VPN
- AWS Site-to-Site VPN은 온프레미스 네트워크와 AWS VPC 간의 안전한 IPsec 연결을 제공합니다.
- AWS Client VPN은 원격 사용자들이 AWS와 온프레미스 네트워크에 안전하게 접속할 수 있도록 지원합니다.

## 주요 기능 및 특징
### AWS Site-to-Site VPN
- **IPsec 터널**: 안전한 IPsec 터널을 통해 온프레미스 네트워크와 AWS VPC를 연결
- **고가용성**: 두 개의 VPN 터널을 통해 고가용성 제공
- **자동 라우팅**: 동적 라우팅 프로토콜(BGP)을 사용하여 라우팅 자동화
- **통합**: AWS Direct Connect와 통합 가능

### AWS Client VPN
- **OpenVPN 기반**: OpenVPN 프로토콜을 사용하여 원격 사용자 연결 지원
- **확장성**: 수천 명의 원격 사용자 지원
- **통합 인증**: Active Directory, RADIUS, SAML 등과 통합된 인증
- **관리형 서비스**: AWS에서 완전 관리형으로 제공

## 사용 사례
- **온프레미스와 클라우드 통합**: 온프레미스 데이터 센터와 AWS 클라우드 간의 안전한 연결
- **원격 근무 지원**: 원격 사용자들이 안전하게 AWS 리소스에 접근할 수 있도록 지원
- **데이터 전송 보안**: 민감한 데이터를 안전하게 전송

## 작동 방식
### AWS Site-to-Site VPN 설정
1. AWS Management Console에서 VPN 게이트웨이 생성
2. 온프레미스 라우터와 AWS VPN 게이트웨이 간의 IPsec 터널 설정
3. 터널 설정 완료 후, 라우팅 테이블 구성

### AWS Client VPN 설정
1. AWS Management Console에서 Client VPN 엔드포인트 생성
2. 인증 및 인증서 설정
3. 클라이언트 구성 파일 다운로드 및 배포
4. 원격 사용자가 클라이언트 소프트웨어를 통해 VPN에 연결

## 예제 코드
### AWS CLI를 사용한 Site-to-Site VPN 설정 예제
```bash
# 가상 프라이빗 게이트웨이 생성
aws ec2 create-vpn-gateway --type ipsec.1 --amazon-side-asn 65000

# 고객 게이트웨이 생성
aws ec2 create-customer-gateway --type ipsec.1 --public-ip <CustomerGatewayIP> --bgp-asn 65001

# VPN 연결 생성
aws ec2 create-vpn-connection --type ipsec.1 --customer-gateway-id <CustomerGatewayId> --vpn-gateway-id <VpnGatewayId>