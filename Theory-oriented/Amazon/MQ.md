# Amazon MQ
- Apache ActiveMQ 및 RabbitMQ와 같은 오픈 소스 메시지 브로커를 관리형 서비스로 제공하는 AWS 서비스
- 메시지 브로코는 분산 시스템에서 서로 다른 애플리케이션, 시스템, 서비스 간의 메시지를 송수신하는 데 사용

# 주요 기능
- 관리형 서비스
    - 메시지 브로커의 설치, 설정, 유지 관리, 확장 등을 자동으로 처리하여 관리 부담을 줄여줌
    - AWS Management Console, CLI, SDK를 통해 브로커를 쉽게 생성하고 관리할 수 있음

- 고가용성
    - 다중 가용 영역(Multi-AZ) 배포를 지원하여 고가용성을 제공
    - 자동 장애 조치(Failover) 기능을 통해 브로커의 가용성을 보장

- 보안
    - VPC 내에서 브로커를 실행하여 네트워크 격리를 제공
    - TLS를 사용한 데이터 전송 암호화, AWS IAM을 통한 접근 제어, Amazon VPC 보안 그룹을 통한 네트워크 보안을 지원

- 호환성
    - Apache ActiveMQ 및 RabbitMQ와 호환되므로, 기존 애플리케이션을 최소한의 변경으로 Amazon MQ로 마이그레이션할 수 있음
    - 다양한 메시징 프로토콜을 지원(예: MQTT, AMQP, STOMP, OpenWire, WSS)

- 모니터링 및 로깅
    - Amazon CloudWatch를 통해 브로커의 성능 및 상태를 모니터링할 수 있음
    - AWS CloudTrail을 통해 API 호출을 로깅하여 보안 및 규정 준수 요구사항을 충족할 수 있음

# 사용 사례
- 애플리케이션 통합: 서로 다른 애플리케이션 간의 메시지 송수신을 통해 통합을 용히하게 함
- 마이크로서비스 아키텍처: 마이크로서비스 간의 비동기 통신을 지원하여 시스템의 확장성과 유연성을 높임
- 이벤트 드리븐 아키텍처: 이벤트 기반 시스템에서 이벤트를 전달하고 처리하는 데 사용
