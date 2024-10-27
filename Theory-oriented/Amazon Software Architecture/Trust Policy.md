**Trust Policy**는 AWS IAM (Identity and Access Management)에서 사용되는 정책의 일종으로, 특정 IAM Role에 대한 신뢰를 정의합니다. Trust Policy는 해당 역할이 어떤 AWS 계정, 사용자, 또는 서비스에 의해 "가정"될 수 있는지를 명시합니다. 즉, 어떤 엔티티가 이 역할을 사용할 수 있는지를 정의하는 것입니다.

### Trust Policy의 주요 특징

1. **JSON 형식**:
   - Trust Policy는 JSON 형식으로 작성되며, 신뢰 관계를 정의하는 규칙을 포함합니다.

2. **Principal**:
   - Trust Policy의 주요 요소는 `Principal`입니다. 이 부분은 역할을 가정할 수 있는 주체를 정의합니다. 주체는 AWS 사용자, 서비스, 또는 다른 AWS 계정이 될 수 있습니다.

3. **Action**:
   - Trust Policy는 `sts:AssumeRole`과 같은 작업을 지정하여 해당 역할이 어떻게 사용될 수 있는지를 정의합니다. 이 작업은 주체가 역할을 "가정"할 때 실행되는 액션입니다.

4. **Condition**:
   - Trust Policy에는 특정 조건을 추가할 수 있습니다. 예를 들어, 특정 IP 주소에서만 역할을 가정하도록 제한할 수 있습니다.

### Trust Policy의 구조

Trust Policy는 다음과 같은 기본 구조를 가집니다:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT-ID:root" // 주체 (계정, 사용자 등)
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        // 추가적인 조건 (선택적)
      }
    }
  ]
}
```

### 사용 사례

- **서비스 역할**: 특정 AWS 서비스가 IAM Role을 가정해야 할 때, Trust Policy를 설정하여 그 서비스를 허용합니다. 예를 들어, EC2 인스턴스가 S3 버킷에 접근할 수 있도록 역할을 설정할 때 사용됩니다.
  
- **Cross-Account Access**: 한 AWS 계정의 리소스가 다른 AWS 계정의 역할을 사용해야 할 때 Trust Policy를 통해 신뢰 관계를 정의합니다.

- **Federated Users**: 외부 아이덴티티 제공자(예: Google, Facebook 등)가 AWS에 로그인할 수 있도록 역할을 설정할 때, 해당 아이덴티티 제공자를 신뢰할 수 있도록 Trust Policy를 정의합니다.

### 예제

예를 들어, 다음은 EC2 인스턴스가 S3에 접근할 수 있도록 허용하는 Trust Policy의 예입니다:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

이 정책은 EC2 서비스가 이 역할을 가정할 수 있도록 허용합니다.

### 요약

Trust Policy는 AWS IAM Role에 대한 신뢰 관계를 설정하는 데 필수적인 요소로, 특정 주체가 해당 역할을 가정할 수 있는 권한을 정의합니다. 이를 통해 AWS 리소스에 대한 접근을 보다 안전하게 관리할 수 있습니다.