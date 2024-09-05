# AWS Shield

AWS Shield는 Amazon Web Services(AWS)에서 제공하는 관리형 DDoS(Distributed Denial of Service) 보호 서비스입니다. AWS Shield는 애플리케이션을 DDoS 공격으로부터 보호하여 가용성을 유지하고, 성능 저하를 방지합니다. AWS Shield는 두 가지 수준의 보호를 제공합니다: AWS Shield Standard와 AWS Shield Advanced.

주요 특징
AWS Shield Standard
기본 보호:

모든 AWS 고객에게 추가 비용 없이 제공됩니다.
AWS 인프라를 대상으로 하는 대부분의 일반적인 네트워크 및 전송 계층 DDoS 공격을 자동으로 탐지하고 완화합니다.
자동화된 보호:

AWS Shield Standard는 자동으로 DDoS 공격을 탐지하고 대응합니다.
AWS CloudFront, AWS Route 53, AWS Global Accelerator와 같은 AWS 서비스와 통합되어 보호 기능을 제공합니다.
AWS Shield Advanced
향상된 보호:

AWS Shield Standard의 모든 기능을 포함하며, 추가 비용으로 제공됩니다.
더 큰 규모의 공격과 애플리케이션 계층 공격에 대한 보호를 제공합니다.
24/7 DDoS 대응 팀(DRT):

AWS 보안 전문가로 구성된 DDoS 대응 팀이 24시간 연중무휴로 지원을 제공합니다.
공격 발생 시 실시간으로 대응하고, 복구를 지원합니다.
실시간 가시성 및 분석:

AWS WAF(Web Application Firewall)와 통합되어 실시간으로 공격을 모니터링하고 분석할 수 있습니다.
AWS CloudWatch를 통해 공격 이벤트와 메트릭을 모니터링할 수 있습니다.
비용 보호:

DDoS 공격으로 인해 발생한 AWS 리소스 사용량 증가에 대한 비용 보호를 제공합니다.
공격으로 인한 비용 증가를 AWS가 보상합니다.
애플리케이션 계층 보호:

AWS WAF와 통합하여 애플리케이션 계층 공격을 탐지하고 완화할 수 있습니다.
사용자 정의 규칙을 설정하여 특정 유형의 공격을 차단할 수 있습니다.
사용 사례
웹 애플리케이션 보호:

웹사이트와 웹 애플리케이션을 DDoS 공격으로부터 보호하여 가용성을 유지합니다.
AWS CloudFront와 AWS WAF를 사용하여 웹 애플리케이션 계층 공격을 완화합니다.
DNS 보호:

AWS Route 53을 사용하여 DNS 인프라를 DDoS 공격으로부터 보호합니다.
DNS 쿼리의 가용성을 유지하고, 성능 저하를 방지합니다.
API 보호:

AWS API Gateway와 통합하여 API 엔드포인트를 DDoS 공격으로부터 보호합니다.
API 호출의 가용성을 유지하고, 성능 저하를 방지합니다.
작동 방식
자동 탐지 및 완화:

AWS Shield는 네트워크 트래픽을 지속적으로 모니터링하여 DDoS 공격을 자동으로 탐지합니다.
공격이 탐지되면, AWS Shield는 자동으로 공격을 완화하여 애플리케이션의 가용성을 유지합니다.
실시간 모니터링 및 경고:

AWS CloudWatch를 통해 실시간으로 공격 이벤트와 메트릭을 모니터링할 수 있습니다.
공격 발생 시 경고를 받아 즉시 대응할 수 있습니다.
DDoS 대응 팀 지원:

AWS Shield Advanced 고객은 DDoS 대응 팀의 지원을 받아 공격에 실시간으로 대응할 수 있습니다.
DDoS 대응 팀은 공격 분석, 완화 전략 제안, 복구 지원 등을 제공합니다.
요약
AWS Shield는 AWS에서 제공하는 관리형 DDoS 보호 서비스로, AWS Shield Standard와 AWS Shield Advanced 두 가지 수준의 보호를 제공합니다. AWS Shield Standard는 모든 AWS 고객에게 기본적인 DDoS 보호를 제공하며, AWS Shield Advanced는 더 큰 규모의 공격과 애플리케이션 계층 공격에 대한 향상된 보호를 제공합니다. AWS Shield는 웹 애플리케이션, DNS, API 등을 DDoS 공격으로부터 보호하여 가용성을 유지하고, 성능 저하를 방지합니다.


# AWS Shield Standard
- 네트워크 및 전송 계층 DDoS 공격으로부터 보호
- Amazon CloudFront 및 Amazon Route 53과 함께 사용하면 알려진 모든 인프라(3,4계층)에 대한 포괄적인 가용성 보호 가능

# AWS Shield Advanced
- EC2, ELB, CloudFront, AWS Global Accelerator, Route53 리소스에서 실행되는 애플리케이션에 대한 더 높은 수준의 보호 구현
- 정교한 대규모 DDoS 공격에 대한 추가 보호 및 완화
- 실시간에 가까운 공격에 대한 가시성
- 웹 애플리케이션 방화벽 AWS WAF와 통합 제공


## References
- [AWS Shield 기능](https://aws.amazon.com/ko/shield/features/)
- [AWS Shield, WAF](https://www.notion.so/AWS-Shield-WAF-9635d94d3efe43be9fd9b051b4f38dc4)