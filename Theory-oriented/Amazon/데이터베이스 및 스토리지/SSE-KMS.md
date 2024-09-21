# SSE-KMS (Server-Side Encryption with AWS Key Management Service)

- SSE-KMS는 AWS Key Management Service (KMS)를 사용하여 Amazon S3 객체를 서버 측에서 암호화하는 방법
- 데이터 보안을 강화하고, 암호화 키를 중앙에서 관리할 수 있음

## 주요 기능 및 특징
- **데이터 암호화**: S3 객체를 업로드할 때 AWS KMS 키를 사용하여 데이터를 암호화
- **중앙 관리**: AWS KMS를 통해 암호화 키를 중앙에서 관리하고, 키의 생성, 회전, 삭제 등을 수행
- **접근 제어**: IAM 정책, KMS 정책, S3 버킷 정책을 통해 암호화된 데이터에 대한 접근을 제어
- **감사 및 로깅**: AWS CloudTrail을 사용하여 KMS 키 사용 내역을 로깅하고 감사 가능

## 구성
- **KMS 키 생성**: AWS KMS 콘솔, CLI, SDK를 사용하여 KMS 키를 생성
- **S3 버킷 설정**: S3 버킷에 SSE-KMS를 사용하도록 설정
- **IAM 정책 설정**: KMS 키와 S3 버킷에 대한 접근 권한을 설정

## 작동 방식
1. **KMS 키 생성**: AWS KMS에서 암호화 키를 생성
2. **객체 업로드**: S3 버킷에 객체를 업로드할 때 SSE-KMS를 사용하여 암호화
3. **암호화 키 사용**: AWS KMS 키를 사용하여 데이터를 암호화하고, 암호화된 데이터를 S3에 저장
4. **데이터 접근**: 암호화된 데이터에 접근할 때 AWS KMS 키를 사용하여 데이터를 복호화

## 다른 서비스와의 연관성
- **AWS Key Management Service (KMS)**: 암호화 키 생성 및 관리
- **Amazon S3**: 데이터를 저장하고 암호화
- **AWS CloudTrail**: KMS 키 사용 내역 로깅 및 감사

## 사용 사례
- **민감한 데이터 보호**: 금융 데이터, 의료 기록 등의 민감한 데이터를 암호화하여 보호
- **규정 준수**: 데이터 보호 규정을 준수하기 위해 데이터 암호화
- **데이터 유출 방지**: 무단 접근으로부터 데이터를 보호하여 데이터 유출 방지

## 결론
- SSE-KMS는 AWS KMS를 사용하여 S3 객체를 서버 측에서 암호화하는 강력한 방법
- 데이터 보안을 강화하고, 암호화 키를 중앙에서 관리할 수 있음

## 예제 코드
### S3 버킷에 SSE-KMS 설정 예제
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::example-bucket/*",
      "Condition": {
        "StringEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms",
          "s3:x-amz-server-side-encryption-aws-kms-key-id": "arn:aws:kms:us-west-2:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd56ef"
        }
      }
    }
  ]
}
```