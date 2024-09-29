# 가상 프라이빗 게이트웨이(Virtual Private Gateway, VGW)
- AWS의 VPC(Virtual Private Cloud) 네트워크에서 온프레미스 데이터 센터 또는 다른 네트워크와의 안전한 연결을 위해 사용하는 VPN 연결의 엔드포인트
- AWS VPC와 외부 네트워크(온프레미스 또는 다른 클라우드 네트워크)를 연결하는 역할을 하며, 보통 두 가지 주요 방식으로 사용

## 주요 방식
- AWS Direct Connect와 연결
    - AWS Direct Connect는 온프레미스 데이터 센터와 AWS 간에 고속 전용 네트워크 연결을 설정하는 서비스
    - VGW는 Direct Connect와 VPC를 연결하는 데 사용됨

- VPN 연결
    - 온프레미스 네트워크나 다른 클라우드 네트워크와 VPC 간의 IPsec VPN 연결을 설정할 때 사용
    - 이 경우, 가상 프라이빗 게이트웨이는 온프레미스 쪽의 **고객 게이트웨이(Customer Gateway, CGW)**와 연결
    - 이 연결을 통해 온프레미스 네트워크와 AWS VPC 간에 암호화된 터널이 형성됩니다.

## 주요 특징
- 보안: 온프레미스 네트워크와 AWS 간의 트래픽을 암호화하여 안전한 연결을 제공
- 연결 방식: AWS Direct Connect와 VPN 연결 모두 지원
- 다중 연결 지원: 하나의 VGW에 여러 VPN 또는 Direct Connect 연결을 설정할 수 있음
- 고가용성: AWS의 가상 프라이빗 게이트웨이는 이중화되어 고가용성을 제공하며, 장애가 발생해도 자동으로 대체 경로로 연결을 전환할 수 있음

## 사용 예시
- 온프레미스 데이터 센터와 AWS VPC 간에 보안 연결을 설정하고 싶을 때.
- AWS VPC와 외부 네트워크 간에 전용 회선 또는 암호화된 VPN 터널을 통해 통신할 때.