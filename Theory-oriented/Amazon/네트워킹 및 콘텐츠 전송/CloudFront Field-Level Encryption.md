# Field-Level Encryption

- Amazon CloudFront에서 제공하는 기능으로, 애플리케이션 스택 전체에서 민감한 데이터를 보호하기 위해 사용됨
- 특정 필드의 데이터를 암호화하여 전송 중 및 저장 중에 보호함

# 주요 기능
- 특정 필드의 데이터 암호화
  - 민감한 데이터를 포함한 특정 필드를 암호화하여 보호할 수 있음
  - HTTPS를 통해 안전하게 전송됨

- 암호화 키 관리
  - AWS Key Management Service (KMS)를 사용하여 암호화 키를 관리할 수 있음
  - 키의 생성, 회전, 삭제 등을 관리할 수 있음

- 데이터 보호 및 접근 제한
  - 암호화된 데이터는 지정된 수신자만 접근할 수 있음
  - 추가적인 보안 계층을 제공하여 데이터 유출을 방지함

- 서비스 통합
  - AWS Key Management Service (KMS), Amazon S3, AWS Lambda 등 다양한 AWS 서비스와 통합됨
  - 이를 통해 복잡한 보안 및 관리 작업을 자동화할 수 있음

# 작동 방식
1. CloudFront 배포를 생성하거나 기존 배포를 수정함
2. 필드 수준 암호화 프로파일을 생성함
3. 암호화할 필드를 지정하고, 암호화 키를 설정함
4. CloudFront 배포에 필드 수준 암호화 프로파일을 연결함
5. 클라이언트가 요청을 보내면, 지정된 필드의 데이터가 암호화됨
6. 암호화된 데이터는 안전하게 전송되고 저장됨

# 사용 사례
- 금융 애플리케이션에서의 민감한 데이터 보호
  - 예: 신용카드 번호, 계좌 정보 등의 암호화
- 의료 정보 시스템에서의 환자 데이터 보호
  - 예: 환자 기록, 진단 정보 등의 암호화
- 전자 상거래 사이트에서의 결제 정보 보호
  - 예: 결제 정보, 사용자 개인정보 등의 암호화

# 결론
- Field-Level Encryption은 민감한 데이터를 보호하기 위한 강력한 보안 기능임
- 추가적인 보안 계층을 제공하여 데이터 유출을 방지함

# 예제 코드
```json
{
  "Comment": "Example field-level encryption profile",
  "FieldLevelEncryptionConfig": {
    "CallerReference": "unique-string",
    "Comment": "Example field-level encryption profile",
    "QueryArgProfileConfig": {
      "ForwardWhenQueryArgProfileIsUnknown": false,
      "QueryArgProfiles": {
        "Items": [
          {
            "QueryArg": "credit-card-number",
            "ProfileId": "example-profile-id"
          }
        ],
        "Quantity": 1
      }
    },
    "ContentTypeProfileConfig": {
      "ForwardWhenContentTypeIsUnknown": false,
      "ContentTypeProfiles": {
        "Items": [
          {
            "Format": "URLEncoded",
            "ProfileId": "example-profile-id",
            "ContentType": "application/x-www-form-urlencoded"
          }
        ],
        "Quantity": 1
      }
    }
  }
}