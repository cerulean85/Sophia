- AWS Virtual Private Cloud(VPC) 환경 내에서 네트워크 트래픽을 제어하고 보호하기 위한 서비스
- 상태 기반 방화벽 기능: 네트워크 트래픽 상태를 추적하여 인바운드 및 아웃바운드 트래픽 제어
- 네트워크 트래픽 필터링: IP, 포트, 프로토콜 등의 기준으로 트래픽을 필터링
- 애플리케이션 프로토콜 필터링: HTTP/S 및 DNS 트래픽에 대한 필터링 기능 제공
- 침입 탐지 및 방지 시스템(IDS/IPS): 네트워크 내의 악성 트래픽 탐지하고 차단
- 로깅 및 모니터링: 트래픽 로그를 Amazon S3, Amazon CLoudWatch 및 Amazon Kinesis Data Firehose에 통합하여 모니터링


## Network Firewall
- VPC 내의 네트워크 트래픽을 직접적으로 제어하고 보호하는 데 중점
- 개별 VPC 내의 네트워크 트래픽 보호
- 네트워크 트래픽 필터링 및 보호에 특화된 기능 제공

## Firewall Manager
- 여러 AWS 계정과 리소스에 걸쳐 보안 정책을 중앙에서 관리하고 일관되게 적용하는 데 중점
- 조직 전체의 AWS 계정과 리소스에 대한 보안 정책 관리
- AWS WAF, AWS Shield, AWS Network Firewall, 보안 그룹 등 다양한 보안 서비스를 통합 관리

- 즉, Network Firewall은 네트워크 레벨의 보안에 집중하고, AWS Firewall Manager는 조직 전체의 보안 정책 관리에 중점을 둠
