# AWS Network Firewall

## 요약
- AWS 클라우드 환경에서 네트워크 트래픽을 보호하기 위한 관리형 방화벽 서비스

## 개요
- AWS VPC 내에서 트래픽을 모니터링하고 제어
- 네트워크 보안을 강화하고 규정 준수를 지원

## 주요 기능 및 특징
- 상태 저장 방화벽
- 침입 탐지 및 방지 시스템 (IDS/IPS)
- 중앙 집중식 관리
- 확장성 및 고가용성
- AWS 서비스와의 통합

## 구성
- 방화벽 정책: 트래픽 필터링 규칙 정의
- 방화벽 엔드포인트: VPC 서브넷에 배포
- 로그 및 모니터링: Amazon CloudWatch 및 S3와 통합

## 작동 방식
1. AWS Management Console에서 AWS Network Firewall 설정
2. 방화벽 정책 생성 및 트래픽 필터링 규칙 정의
3. 방화벽 엔드포인트를 VPC 서브넷에 배포
4. 트래픽이 방화벽을 통과할 때 규칙에 따라 필터링
5. 로그와 모니터링 데이터를 CloudWatch 및 S3로 전송

## 다른 서비스와의 연관성
- AWS VPC: VPC 내에서 네트워크 트래픽 보호
- Amazon CloudWatch: 로그 및 모니터링 데이터 수집
- AWS IAM: 액세스 제어 및 정책 관리 지원

## 사용 사례
- 클라우드 네트워크 보안 강화
- 규정 준수 요구 사항 충족
- 침입 탐지 및 방지

## 결론
- AWS Network Firewall은 AWS 환경에서 네트워크 보안을 강화하는 데 중요한 역할
- 확장성과 고가용성을 제공하며, 다른 AWS 서비스와 원활하게 통합

## 예제 코드
```json
{
  "FirewallPolicy": {
    "StatelessRuleGroupReferences": [
      {
        "ResourceArn": "arn:aws:network-firewall:us-west-2:123456789012:stateless-rulegroup/example",
        "Priority": 1
      }
    ],
    "StatefulRuleGroupReferences": [
      {
        "ResourceArn": "arn:aws:network-firewall:us-west-2:123456789012:stateful-rulegroup/example"
      }
    ]
  }
}



---

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


## 참고사이트
- ChatGPT Firewall Manager과 Network Firewall의 차이