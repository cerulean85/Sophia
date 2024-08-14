# AWS Config
- 계정 내 AWS 리소스 구성의 상세한 뷰를 제공
    - 리소스 간 연관성, 리소스 구성 및 관계의 변화 확인 가능

## 고려사항
- AWS account: 활성화된 AWS 계정 필요
- Amazon S3 Bucket: 구성 스냅샷과 히스토리를 받기 위해 S3 버킷 필요
- Amazon SNS Topic: 구성 스냅샷과 히스토리가 변하면 알림을 받기 위해 Amazon SNS가 필요
- IAM Role: AWS Config에 접근하기 위해 필요한 권한을 가진 IAM role이 필요
- Resource types: AWS Config가 기록할 리소스 유형을 결정할 수 있음

# References
- [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)