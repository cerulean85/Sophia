# Amazon AppFlow
- Amazon Web Services(AWS)에서 제공하는 완전 관리형 데이터 통합 서비스
- AppFlow를 사용하면 다양한 SaaS(Software as a Service) 애플리케이션과 AWS 서비스 간에 데이터를 안전하게 전송하고 통합할 수 있음
- 이를 통해 데이터 이동을 자동화하고, 데이터 통합 작업을 간소화할 수 있음

# 주요 특징
## 1. 다양한 데이터 소스 지원
- Salesforce, ServiceNow, Slack, Google Analytics, Zendesk 등 다양한 SaaS 애플리케이션과의 데이터 통합을 지원
- Amazon S3, Amazon Redshift, Amazon EventBridge 등 AWS 서비스와의 데이터 통합도 가능

## 2. 보안 및 규정 준수
- 데이터 전송 중 및 저장 중 암호화를 지원하여 데이터 보안을 보장
- AWS Identity and Access Management(IAM)와 통합되어 세분화된 액세스 제어를 제공

## 3. 자동화된 데이터 이동
- 정기적인 데이터 전송을 자동화할 수 있으며, 이벤트 기반 트리거를 설정하여 특정 조건이 충족될 때 데이터를 전송할 수 있음

## 4. 데이터 변환 및 필터링
- 데이터 전송 중에 데이터 변환 및 필터링을 수행할 수 있음
- 예를 들어, 특정 필드를 변환하거나 필터링하여 필요한 데이터만 전송할 수 있음

## 5. 사용자 친화적인 인터페이스
- AWS Management Console을 통해 직관적인 사용자 인터페이스를 제공하여, 코드 작성 없이 데이터 통합 작업을 설정하고 관리할 수 있음


# 사용 사례
## 1. 데이터 통합
- 다양한 SaaS 애플리케이션에서 데이터를 수집하여 AWS 데이터 레이크나 데이터 웨어하우스에 통합할 수 있음

## 2. 데이터 분석
- SaaS 애플리케이션의 데이터를 Amazon Redshift나 Amazon S3로 전송하여 데이터 분석을 수행할 수 있음

## 3. 데이터 동기화
- 여러 애플리케이션 간에 데이터를 동기화하여 일관된 데이터 상태를 유지할 수 있음

## 4. 이벤트 기반 데이터 이동
- 특정 이벤트가 발생할 때 데이터를 자동으로 전송하여 실시간 데이터 처리를 가능하게 함


# 작동 방식
## 1. 연결 설정
- AWS Management Console에서 Amazon AppFlow를 사용하여 데이터 소스와 대상 간의 연결을 설정

## 2. 데이터 흐름 생성
- 데이터 흐름을 생성하고, 데이터 소스와 대상, 전송할 데이터 필드, 데이터 변환 및 필터링 규칙을 정의

## 3. 전송 트리거 설정
- 데이터 전송을 트리거할 조건을 설정
- 정기적인 일정, 이벤트 기반 트리거, 또는 수동 트리거를 선택할 수 있음

## 4. 데이터 전송 및 모니터링
- 설정된 조건에 따라 데이터를 전송하고, AWS Management Console에서 데이터 전송 상태를 모니터링할 수 있음


요약
- 다양한 SaaS 애플리케이션과 AWS 서비스 간에 데이터를 안전하게 전송하고 통합할 수 있는 완전 관리형 데이터 통합 서비스

- 데이터 이동을 자동화하고, 데이터 변환 및 필터링 기능을 제공하여 데이터 통합 작업을 간소화
- 다양한 사용 사례에 적용할 수 있으며, 사용자 친화적인 인터페이스를 통해 쉽게 설정하고 관리할 수 있


---

- 클릭 몇 번으로 Salesforce, Marketo, Slack 및 ServiceNow와 같은 SaaS 애플리케이션과  Amazon S3 및 Amazon Redshift와 같은 AWS 서비스 간에 데이터를 안전하게 전송할 수 있게 해주는 완전관리형 통합 서비스

- 규모에 거의 상관 없이 원하는 빈도로 일정과 비즈니스 이벤트에 대한 응답으로 또는 온디맨드로 데이터 플로우를 실행할 수 있음

- 매핑, 병합, 마스킹, 필터링 및 검증과 같은 강력한 데이터 변환 기능을 포함하므로, 추가 단계 없이 플로우 자체의 일부로 바로 사용 가능한 풍부한 데이터를 생성할 수 있음

- 이동 중의 데이털르 자동으로 암호화하며 사용자가 AWS PrivateLink와 통합된 SaaS 애플리케이션을 위해 퍼블릭 인터넷상의 데이터 흘므을 제어할 수 있게 해주므로 보안 위협에 대한 노출이 감소

- a fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications such as Salesforce, and AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon Redshift.
- you can ingest contact records from Salesforce to Amazon Redshift or pull support tickets from Zendesk to an Amazon S3 bucket. The following diagram illustrates how it works:

## References
- [Amazon AppFlow 소개](https://aws.amazon.com/ko/about-aws/whats-new/2020/04/introducing-amazon-appflow/)
- [What is Amazon AppFlow?](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html)