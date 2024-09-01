# Origin Access Identity (OAI)
- Amazon CloudFront와 Amazon S3 버킨 간 보안 연결 설정에 사용되는 기능
- S3 버킷에 대한 직접적인 공개 접근을 차단하고, CloudFront를 통해서만 S3 버킷의 콘텐츠에 접근할 수 있도록 설정할 수 있음
- S3 버킷의 콘텐츠를 보호하고, CloudFront를 통해서만 안전하게 콘텐츠를 제공할 수 있음

# 주요 기능
- 보안 강화
    - S3 버킷에 대한 직접적인 공개 접근을 차단하여 보안을 강화
    - CloudFont를 통해서만 S3 버킷의 콘텐츠에 접근할 수 있음

- 간편한 설정
    - AWS Management Console, AWS CLI, 또는 AWS SDK를 사용하여 OAI를 쉽게 생성하고 설정할 수 있음

- 액세스 제어
    - OAI를 사용하여 S3 버킷 정책을 설정하면, CloudFront 배포를 통해서만 콘텐츠를 제공할 수 있음
    - S3 버킷 정책을 통해 특정 CloudFront 배포에만 접근을 허용할 수 있음
