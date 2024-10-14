# AWS Firewall Manager

## 요약
- AWS Firewall Manager는 여러 AWS 계정과 리소스에 걸쳐 방화벽 규칙을 중앙에서 관리할 수 있는 서비스

## 개요
- AWS Organizations와 통합되어 여러 계정에 일관된 보안 정책 적용
- 네트워크 보안 규칙을 중앙에서 관리하고 모니터링

## 주요 기능 및 특징
- 중앙 집중식 규칙 관리
- AWS WAF, AWS Shield, AWS Network Firewall과 통합
- 자동 규칙 적용
- 규정 준수 모니터링
- 보안 이벤트 알림

## 구성
- 보안 정책: 여러 계정에 적용할 규칙 정의
- 규칙 그룹: 특정 보안 요구 사항을 충족하는 규칙 모음
- 대상 리소스: 규칙이 적용될 AWS 리소스

## 작동 방식
1. AWS Management Console에서 AWS Firewall Manager 설정
2. 보안 정책을 생성하고 규칙 그룹 정의
3. 대상 리소스를 선택하여 규칙 적용
4. 규칙이 자동으로 여러 계정과 리소스에 배포
5. 보안 이벤트와 규정 준수 상태를 모니터링

## 다른 서비스와의 연관성
- AWS Organizations: 여러 계정에 일관된 보안 정책 적용
- AWS WAF: 웹 애플리케이션 방화벽 규칙 관리
- AWS Shield: DDoS 보호 규칙 관리
- AWS Network Firewall: 네트워크 트래픽 필터링 규칙 관리

## 사용 사례
- 여러 계정에 걸친 일관된 보안 정책 적용
- 규정 준수 요구 사항 충족
- 중앙 집중식 보안 관리

## 결론
- AWS Firewall Manager는 여러 계정과 리소스에 걸쳐 일관된 보안 정책을 적용하고 관리하는 데 중요한 역할
- 다른 AWS 보안 서비스와 통합되어 종합적인 보안 솔루션 제공

## 예제 코드
```json
{
  "Policy": {
    "PolicyName": "ExamplePolicy",
    "SecurityServicePolicyData": {
      "Type": "WAF",
      "ManagedServiceData": "{\"type\":\"waf\",\"preProcessRuleGroups\":[],\"postProcessRuleGroups\":[],\"defaultAction\":{\"type\":\"ALLOW\"}}"
    },
    "ResourceType": "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "ResourceTags": [],
    "ExcludeResourceTags": false,
    "RemediationEnabled": true,
    "IncludeMap": {
      "ACCOUNT": ["123456789012"]
    }
  }
}

---


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