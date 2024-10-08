
# AWS Key Management Service (KMS)

- Amazon Web Services(AWS)에서 제공하는 관리형 암호화 키 서비스
- AWS KMS를 사용하면 데이터를 암호화하고, 암호화 키를 생성, 관리 및 제어할 수 있음
- 다양한 AWS 서비스와 통합되어 데이터 보안을 강화하는 데 사용

# 주요 특징
## 1. 키 생성 및 관리
- AWS KMS를 사용하여 대칭 및 비대칭 암호화 키를 생성하고 관리할 수 있음
- 고객 관리형 키(CMK)를 생성하여 특정 요구 사항에 맞게 키를 사용자 정의할 수 있음

## 2. 통합 보안
- 다양한 AWS 서비스와 통합되어 데이터 암호화 및 키 관리 기능을 제공
- Amazon S3, Amazon EBS, Amazon RDS, Amazon Redshift 등과 통합되어 데이터를 자동으로 암호화할 수 있음

## 3. 정교한 액세스 제어
- AWS Identity and Access Management(IAM)와 통합되어 세분화된 액세스 제어를 제공
- 키 정책을 설정하여 특정 사용자나 서비스가 키를 사용할 수 있는 권한을 제어할 수 있음

## 4. 감사 및 모니터링
- AWS CloudTrail과 통합되어 키 사용 내역을 기록하고 모니터링할 수 있음
- 키 생성, 사용, 삭제 등의 이벤트를 추적하여 보안 감사 및 규정 준수를 지원


## 5. 고가용성 및 내구성
- AWS의 글로벌 인프라를 기반으로 높은 가용성과 내구성을 제공
- 키는 여러 물리적 위치에 분산 저장되어 데이터 손실 위험을 최소화

# 사용 사례
- 데이터 암호화
    - 데이터를 저장하거나 전송할 때 AWS KMS를 사용하여 데이터를 암호화할 수 있음
    - 예를 들어, Amazon S3 버킷에 저장된 객체를 암호화하거나, Amazon RDS 데이터베이스의 데이터를 암호화할 수 있음

- 애플리케이션 보안
    - 애플리케이션에서 AWS KMS를 사용하여 민감한 데이터를 암호화하고, 암호화 키를 안전하게 관리할 수 있음
    - 예를 들어, 사용자 비밀번호, API 키, 인증 토큰 등을 암호화할 수 있음

- 규정 준수
    - 데이터 보안 및 암호화 요구 사항을 충족하여 규정 준수를 지원
    - 예를 들어, GDPR, HIPAA, PCI-DSS 등의 규정을 준수하기 위해 데이터를 암호화할 수 있음


# 작동 방식
## 1. 키 생성
- AWS Management Console, AWS CLI, AWS SDK를 사용하여 암호화 키를 생성
- 대칭 키 또는 비대칭 키를 선택할 수 있음

## 2. 키 관리
- 생성된 키를 AWS KMS에서 관리하고, 키 정책을 설정하여 액세스를 제어
- 키를 활성화하거나 비활성화할 수 있으며, 키의 사용 내역을 모니터링할 수 있음

## 3. 데이터 암호화 및 복호화
- AWS KMS를 사용하여 데이터를 암호화하고, 암호화된 데이터를 복호화할 수 있음
- AWS 서비스와 통합되어 자동으로 데이터를 암호화할 수 있음

## 4. 감사 및 모니터링
- AWS CloudTrail을 사용하여 키 사용 내역을 기록하고, 보안 이벤트를 모니터링
- 키 생성, 사용, 삭제 등의 이벤트를 추적하여 보안 감사 및 규정 준수를 지원

요약
- 데이터를 암호화하고, 암호화 키를 생성, 관리 및 제어할 수 있는 관리형 암호화 키 서비스 - 다양한 AWS 서비스와 통합되어 데이터 보안을 강화하며, 정교한 액세스 제어, 감사 및 모니터링 기능을 제공
- 데이터 암호화, 애플리케이션 보안, 규정 준수 등의 다양한 사용 사례에 활용될 수 있음


AWS Key Management Service (KMS)는 다양한 유형의 암호화 키를 지원하여 다양한 보안 요구 사항을 충족할 수 있습니다. KMS에서 지원하는 주요 키 유형은 다음과 같습니다:

1. 대칭 키 (Symmetric Keys)
설명: 대칭 키는 동일한 키를 사용하여 데이터를 암호화하고 복호화합니다.
사용 사례: 대부분의 데이터 암호화 작업에 사용됩니다. 예를 들어, S3 객체 암호화, EBS 볼륨 암호화, RDS 데이터베이스 암호화 등.
관리: AWS KMS는 대칭 키의 생성, 관리, 회전, 삭제를 지원합니다.
암호화 알고리즘: AWS KMS는 AES-256 알고리즘을 사용하여 대칭 키를 생성합니다.
2. 비대칭 키 (Asymmetric Keys)
설명: 비대칭 키는 공개 키와 개인 키의 쌍으로 구성됩니다. 공개 키는 데이터를 암호화하는 데 사용되고, 개인 키는 데이터를 복호화하는 데 사용됩니다.
사용 사례: 디지털 서명, 데이터 무결성 검증, 비대칭 암호화가 필요한 경우에 사용됩니다.
관리: AWS KMS는 비대칭 키의 생성, 관리, 회전, 삭제를 지원합니다.
암호화 알고리즘: RSA 및 ECC 알고리즘을 사용하여 비대칭 키를 생성합니다.
3. 고객 관리 키 (Customer Managed Keys, CMKs)
설명: 고객이 생성하고 관리하는 키로, 키 정책을 통해 액세스 제어를 설정할 수 있습니다.
사용 사례: 특정 보안 요구 사항을 충족하기 위해 고객이 직접 키를 관리하고자 할 때 사용됩니다.
관리: 고객은 CMK의 생성, 관리, 회전, 삭제를 제어할 수 있습니다.
추적 및 감사: AWS CloudTrail을 통해 CMK의 사용 내역을 추적하고 감사할 수 있습니다.
4. AWS 관리 키 (AWS Managed Keys)
설명: AWS 서비스가 자동으로 생성하고 관리하는 키로, 특정 AWS 서비스와 통합되어 사용됩니다.
사용 사례: S3, EBS, RDS 등과 같은 AWS 서비스에서 기본적으로 제공하는 암호화 기능을 사용할 때 사용됩니다.
관리: AWS가 키의 생성, 관리, 회전을 자동으로 처리합니다.
추적 및 감사: AWS CloudTrail을 통해 AWS 관리 키의 사용 내역을 추적할 수 있습니다.
5. 고객 제공 키 (Customer Provided Keys, CPKs)
설명: 고객이 직접 생성한 키를 AWS KMS에 가져와 사용하는 키입니다.
사용 사례: 고객이 자체적으로 생성한 키를 사용하여 AWS 리소스를 암호화하고자 할 때 사용됩니다.
관리: 고객은 키의 생성, 관리, 회전을 직접 처리해야 합니다.
추적 및 감사: AWS CloudTrail을 통해 CPK의 사용 내역을 추적할 수 있습니다.
요약
AWS KMS는 다양한 유형의 암호화 키를 지원하여 다양한 보안 요구 사항을 충족할 수 있습니다. 대칭 키와 비대칭 키를 포함하여, 고객 관리 키, AWS 관리 키, 고객 제공 키 등의 키 유형을 통해 데이터 암호화, 디지털 서명, 데이터 무결성 검증 등의 다양한 사용 사례에 활용될 수 있습니다. 각 키 유형의 관리 및 사용 방법을 이해하면, 특정 보안 요구 사항에 맞는 적절한 암호화 키를 선택하고 사용할 수 있습니다.



--- 
- AWS KMS는 데이터 보호를 위한 암호화 키를 쉽게 만들고 통제할 수 있는 관리형 서비스
- 대부분의 AWS 서비스와 통합되는데, 감사, 규제, 규정 준수 요구 사항에 따른 AWS 키 사용을 AWS CloudTrail로 기록
- AWS KMS API를 사용하여 KMS 키와 특수 기능을 생성 및 관리할 수 있음

- AWS KMS가 통합된 AWS 서비스나 사용자 애플리켕션에 직접적으로 키관리를 넣고 암호화 가능함
- 암호화된 데이터에 대해 접근 통제 가능
- AWS CloudTrail과 통합하여 KMS가 언제, 어떻게, 누가 사용하였는지 모니터링 및 조사

## References
- [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html)
- [S3 암호화](https://velog.io/@hwaya2828/S3-%EC%95%94%ED%98%B8%ED%99%94)
- [Using server-side encryption with Amazon S3 managed keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html)