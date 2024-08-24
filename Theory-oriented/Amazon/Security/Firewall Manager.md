- 여러 AWS 계정 및 리소스에 걸쳐 보안 젇책을 중앙에서 관리하고 적용하기 위한 서비스
- 보안 정책 중앙 관리: 여러 계정과 리소스에 대한 방화벽 규칙 및 보안 정책을 중앙에서 관리
- AWS WAF 관리: 여러 계정에 걸쳐 AWS WAF(Web Application Firewall) 규칙을 일관되게 적용
- AWS Shield Advanced 관리: AWS Shield Advanced를 통해 DDoS 방어 정책을 중앙에서 관리
- AWS Network Firewall 통합: AWS Network Firewall 정책을 여러 VPC에 일관되게 적용
- Config Rules 관리: AWS Config 규칙을 여러 계정과 리소스에 적용하여 규정 준수 상태를 모니터링
- 보안 그룹 관리: 보안 그룹 정책을 중앙에서 관리하고 일관되게 적용



## Network Firewall
- VPC 내의 네트워크 트래픽을 직접적으로 제어하고 보호하는 데 중점
- 개별 VPC 내의 네트워크 트래픽 보호
- 네트워크 트래픽 필터링 및 보호에 특화된 기능 제공

## Firewall Manager
- 여러 AWS 계정과 리소스에 걸쳐 보안 정책을 중앙에서 관리하고 일관되게 적용하는 데 중점
- 조직 전체의 AWS 계정과 리소스에 대한 보안 정책 관리
- AWS WAF, AWS Shield, AWS Network Firewall, 보안 그룹 등 다양한 보안 서비스를 통합 관리

- 즉, Network Firewall은 네트워크 레벨의 보안에 집중하고, AWS Firewall Manager는 조직 전체의 보안 정책 관리에 중점을 둠


## 참고사이트
- ChatGPT Firewall Manager과 Network Firewall의 차이