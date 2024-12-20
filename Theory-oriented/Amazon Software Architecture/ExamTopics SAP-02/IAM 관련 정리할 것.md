AWS IAM Identity Center와 AWS Identity and Access Management  차이는?

AWS IAM Identity Center(구 AWS SSO)와 AWS Identity and Access Management(IAM)는 AWS에서 사용자 및 권한을 관리하는 두 가지 주요 서비스이지만, 목적과 사용 사례에서 차이가 있습니다. 

### 1. **AWS IAM (Identity and Access Management)**  
IAM은 AWS 리소스에 대한 세부적이고 미세한 권한 관리를 제공합니다.  

- **주요 기능**  
  - AWS 리소스(EC2, S3, RDS 등)에 대한 사용자, 그룹, 역할(Role)의 **직접적인 권한 제어**.
  - **정책(Policy)**을 사용해 권한을 JSON 형식으로 정의.
  - **IAM 사용자** 및 **IAM 역할**을 생성해 특정 리소스와 작업에 권한 부여.
  - AWS 서비스와 통합된 **서비스 역할** 및 **교차 계정 액세스** 관리.

- **사용 사례**  
  - AWS 리소스에 대해 **서비스별 세부 권한 제어**가 필요할 때.
  - 특정 애플리케이션이나 서비스가 AWS 리소스에 접근할 수 있도록 **역할(Role)**을 생성할 때.
  - 시스템 간 통신 또는 자동화를 위해 서비스 계정을 사용할 때.

---

### 2. **AWS IAM Identity Center (IAM Identity Center, 구 AWS SSO)**  
IAM Identity Center는 **AWS 계정 전체** 및 **타사 애플리케이션(SaaS)**에 대한 **중앙화된 사용자 인증 및 권한 관리**를 제공합니다.

- **주요 기능**  
  - AWS 계정 및 AWS Organizations와 통합하여 여러 계정에서 **중앙 집중식 사용자 인증 및 권한 관리**.
  - **SSO(Single Sign-On)** 기능으로 AWS Management Console, CLI, 기타 애플리케이션에 원활하게 접근 가능.
  - **외부 IdP(Identity Provider)**와의 통합을 통해 사용자 관리를 간소화 (예: Microsoft Active Directory, Okta, Google Workspace).
  - **사용자 그룹 기반 권한 설정**으로 관리 간소화.
  - SSO를 통해 **IAM 역할**과 매핑 가능.

- **사용 사례**  
  - AWS Organizations 환경에서 여러 AWS 계정을 사용하는 조직에서 **중앙 집중식 권한 관리**를 원하는 경우.
  - **외부 IdP**를 사용하는 기업이 사용자 계정을 AWS와 동기화하고 권한을 통합적으로 관리하고자 할 때.
  - SSO를 통해 사용자의 로그인 경험을 간소화하려는 경우.

---

### 3. **주요 차이점**  

| **특징**                    | **AWS IAM**                                           | **AWS IAM Identity Center**                          |
|-----------------------------|-----------------------------------------------------|-----------------------------------------------------|
| **목적**                    | AWS 리소스에 대한 세부적 권한 관리                      | 여러 AWS 계정 및 애플리케이션에 대한 중앙화된 사용자 관리 및 인증 |
| **사용 대상**               | 리소스 중심 (사용자, 역할, 서비스)                     | 사용자 중심 (SSO 및 IdP 통합)                        |
| **권한 부여 방식**           | 정책(JSON)을 기반으로 상세 제어                         | 그룹 및 역할 매핑을 통해 간소화된 권한 부여             |
| **외부 시스템 연동**         | 제한적 (주로 AWS 내부)                                | 외부 IdP와 쉽게 통합 가능 (SAML, OIDC)                |
| **관리 계정**               | 개별 사용자와 역할                                    | AWS Organizations와 연계한 중앙 집중 관리             |
| **사용자 경험**             | AWS 리소스별 개별 로그인                              | SSO로 단일 로그인 경험 제공                           |

---

### **요약**  
- **IAM**: AWS 리소스 수준에서 세부적으로 권한을 제어해야 할 때 사용.  
- **IAM Identity Center**: 여러 AWS 계정 및 외부 애플리케이션에 대한 중앙 집중식 사용자 인증 및 권한 관리를 원할 때 사용.

이 두 서비스를 함께 사용하여 AWS 환경에서 더 강력하고 유연한 보안 및 사용자 관리 체계를 구축할 수 있습니다.


! AWS IAM으로 IAM User에 IAM Role을 위임하는 예제를 몇 개 알려줘.
AWS IAM에서 IAM User가 특정 작업을 수행하기 위해 **IAM Role**을 사용할 수 있도록 위임하려면 다음의 구성 요소가 필요합니다.  

1. **IAM Role 생성**: 역할(Role)은 사용자(User)와 다르게 AWS 리소스에 대해 작업을 수행할 수 있는 권한을 정의한 개체입니다. 역할은 **AssumeRole 정책**을 사용해 특정 사용자 또는 엔터티에 위임됩니다.  

2. **IAM Role 위임 정책 설정**: 역할의 **신뢰 정책(Trust Policy)**에서 역할을 사용할 수 있는 주체(Principal, 예: IAM User)를 정의해야 합니다.  

3. **IAM User에 역할 사용 권한 부여**: 사용자가 역할을 사용할 수 있도록 필요한 권한을 추가합니다.  

다음은 몇 가지 예제입니다.  

---

### **1. S3 Bucket에 대한 액세스 위임**  
IAM User가 특정 IAM Role을 Assume하여 S3 버킷에 액세스하도록 설정합니다.  

#### (1) **IAM Role 생성 및 신뢰 정책 설정**  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/ExampleUser"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

- `Principal`: 이 역할을 사용할 수 있는 IAM User를 지정합니다.  
- `Action`: `sts:AssumeRole`은 역할 전환을 허용합니다.  

#### (2) **IAM Role의 권한 정책 설정**  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::example-bucket/*"
    }
  ]
}
```

- 이 정책은 `example-bucket`에 대한 모든 S3 작업을 허용합니다.  

#### (3) **IAM User에 Role 사용 권한 부여**  
IAM User에 다음 정책을 추가합니다.  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::123456789012:role/ExampleRole"
    }
  ]
}
```

---

### **2. Cross-Account Access 위임**  
IAM User가 다른 AWS 계정의 리소스에 접근할 수 있도록 IAM Role을 사용합니다.  

#### (1) **Role의 신뢰 정책 설정 (계정 간 권한 부여)**  
다른 계정(예: 계정 ID `987654321098`)의 User가 Assume할 수 있도록 역할의 신뢰 정책을 설정합니다.  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::987654321098:user/ExampleUser"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

#### (2) **IAM Role의 권한 정책 설정**  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*"
    }
  ]
}
```

#### (3) **Cross-Account IAM User 권한 추가**  
IAM User에 다음 정책을 추가하여 역할 Assume을 허용합니다.  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::123456789012:role/CrossAccountRole"
    }
  ]
}
```

---

### **3. Lambda 실행 권한 위임**  
IAM User가 Lambda를 실행할 수 있는 역할을 Assume하도록 설정합니다.  

#### (1) **IAM Role 생성 및 신뢰 정책**  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/ExampleUser"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

#### (2) **IAM Role의 권한 정책**  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-west-2:123456789012:function:MyFunction"
    }
  ]
}
```

#### (3) **IAM User에 Role Assume 권한 추가**  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::123456789012:role/LambdaInvokeRole"
    }
  ]
}
```

---

### **IAM Role Assume 방법**  
IAM User가 역할을 Assume할 때는 AWS CLI나 SDK를 사용할 수 있습니다.

#### AWS CLI 예제
```bash
aws sts assume-role \
  --role-arn "arn:aws:iam::123456789012:role/ExampleRole" \
  --role-session-name "ExampleSession"
```

- 결과로 반환되는 `AccessKeyId`, `SecretAccessKey`, `SessionToken`을 사용하여 임시 자격 증명을 설정합니다.  

이 예제들을 참고하여 IAM User가 IAM Role을 효과적으로 사용할 수 있도록 설정할 수 있습니다! 😊



!! IAM User에 정책을 부여하는 예제를 보여줘.
IAM User에 정책을 부여하는 방법은 크게 두 가지입니다:  

1. **AWS 관리형 정책**을 사용하는 방법.  
2. **사용자 지정 정책(JSON 포맷)**을 사용하는 방법.  

IAM User에 정책을 부여하려면 AWS Management Console, CLI, SDK 중 하나를 사용할 수 있습니다. 아래는 각각의 예제입니다.  

---

### **1. AWS Management Console에서 정책 부여**
1. **IAM 콘솔로 이동** → [IAM 콘솔](https://console.aws.amazon.com/iam/).
2. 왼쪽 메뉴에서 **사용자(Users)**를 선택.
3. 정책을 추가하려는 사용자 선택.
4. **권한(Permissions)** 탭에서 **권한 추가(Add permissions)** 클릭.
5. **정책 연결(Attach policies)** 옵션 선택.
6. 원하는 AWS 관리형 정책(예: `AmazonS3FullAccess`)을 검색 및 선택.
7. **권한 추가(Add permissions)**를 클릭해 저장.

---

### **2. 사용자 지정 정책(JSON) 예제**  
#### (1) **IAM User에 S3 읽기 전용 권한 부여**  
IAM User가 특정 S3 버킷에서 객체를 읽을 수 있도록 설정하는 JSON 정책입니다.  

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-bucket/*"
    }
  ]
}
```

- **`Effect`**: 권한 허용(`Allow`) 또는 거부(`Deny`) 여부 지정.  
- **`Action`**: 허용된 작업(`s3:GetObject`) 지정.  
- **`Resource`**: 작업이 적용될 AWS 리소스를 정의.

#### (2) **EC2 인스턴스 시작 권한 부여**
IAM User가 EC2 인스턴스를 시작할 수 있도록 설정하는 정책입니다.  

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:RunInstances",
      "Resource": "*"
    }
  ]
}
```

- 모든 리소스(`*`)에 대해 EC2 인스턴스를 시작할 수 있는 권한을 부여.

---

### **3. AWS CLI를 사용한 정책 부여**  
IAM User에 정책을 연결하려면 `aws iam attach-user-policy` 명령어를 사용합니다.

#### (1) **AWS 관리형 정책 연결**
```bash
aws iam attach-user-policy \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess \
    --user-name ExampleUser
```

- `--policy-arn`: 연결할 관리형 정책의 ARN (AmazonS3FullAccess 정책).  
- `--user-name`: 정책을 부여할 IAM User 이름.

#### (2) **사용자 지정 정책 생성 및 연결**
1. JSON 파일(`s3-read-policy.json`)에 사용자 지정 정책 작성:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-bucket/*"
    }
  ]
}
```

2. 정책을 생성:
```bash
aws iam create-policy \
    --policy-name S3ReadOnlyPolicy \
    --policy-document file://s3-read-policy.json
```

3. 정책 ARN 확인 후 사용자에 연결:
```bash
aws iam attach-user-policy \
    --policy-arn arn:aws:iam::123456789012:policy/S3ReadOnlyPolicy \
    --user-name ExampleUser
```

---

### **4. 사용자에 인라인 정책 추가**
IAM User에 직접 정책을 삽입하는 인라인 정책 방식도 가능합니다.

#### CLI를 사용한 인라인 정책 추가
```bash
aws iam put-user-policy \
    --user-name ExampleUser \
    --policy-name InlineS3Policy \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:ListBucket",
                "Resource": "arn:aws:s3:::example-bucket"
            },
            {
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::example-bucket/*"
            }
        ]
    }'
```

- **`put-user-policy`**는 인라인 정책을 직접 User에 추가합니다.

---

### **5. JSON 예제 조합**
#### **S3와 DynamoDB에 대한 복합 권한**
IAM User가 S3 버킷에서 읽기와 DynamoDB에서 읽기/쓰기를 할 수 있는 정책입니다.
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::example-bucket",
        "arn:aws:s3:::example-bucket/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem"
      ],
      "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/ExampleTable"
    }
  ]
}
```

이 정책을 사용하면 S3 버킷 및 DynamoDB 테이블에 대한 복합 작업을 수행할 수 있습니다.

---

### **요약**
- AWS 관리형 정책은 빠르고 간단한 권한 부여 방법.  
- 사용자 지정 정책은 세부 제어가 필요한 경우 사용.  
- AWS CLI를 활용하면 정책 생성 및 부여 작업을 자동화할 수 있음.  

필요에 따라 정책을 적절히 조합해 IAM User에 권한을 부여하세요! 😊



!!!IAM User에 IAM Role을 부여하는 예제
IAM User에 **IAM Role을 부여한다**는 것은 직접적으로 Role을 사용자에게 연결하는 것이 아니라, IAM User가 특정 Role을 **Assume**할 수 있도록 설정하는 것을 의미합니다. 이를 통해 사용자는 `sts:AssumeRole` API를 호출하여 해당 Role의 권한을 임시로 사용할 수 있습니다.

다음은 IAM User가 IAM Role을 Assume할 수 있도록 설정하는 방법과 예제입니다.

---

### **1. IAM Role 생성**
IAM Role은 신뢰 정책(Trust Policy)을 통해 특정 주체(Principal)가 Role을 Assume할 수 있도록 허용합니다.

#### **신뢰 정책 (Trust Policy)**
IAM Role 생성 시 다음과 같은 신뢰 정책을 설정합니다:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/ExampleUser"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

- **Principal**: Role을 Assume할 수 있는 주체를 정의 (여기서는 특정 IAM User).  
- **Action**: `sts:AssumeRole`은 역할 전환을 허용하는 API 호출 권한.

---

### **2. IAM Role의 권한 정책**
IAM Role에 부여된 권한 정책은 Role을 Assume한 주체가 수행할 수 있는 작업을 정의합니다.

#### 예제: S3 읽기 권한 정책
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-bucket/*"
    }
  ]
}
```

---

### **3. IAM User에 Role Assume 권한 부여**
IAM User가 특정 Role을 Assume할 수 있도록 정책을 부여해야 합니다. 이를 위해 IAM User에 다음 JSON 정책을 추가합니다:

#### 사용자 권한 정책
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::123456789012:role/ExampleRole"
    }
  ]
}
```

- **Action**: `sts:AssumeRole`은 사용자가 Role을 Assume할 수 있도록 허용.  
- **Resource**: Assume할 수 있는 Role의 ARN.

---

### **4. AWS CLI를 사용한 Role Assume**
IAM User는 AWS CLI 또는 SDK를 사용하여 Role을 Assume할 수 있습니다.

#### CLI 명령어
```bash
aws sts assume-role \
  --role-arn "arn:aws:iam::123456789012:role/ExampleRole" \
  --role-session-name "ExampleSession"
```

- **`--role-arn`**: Assume할 IAM Role의 ARN.  
- **`--role-session-name`**: Assume된 역할 세션에 대한 이름.

#### 출력 예시
```json
{
    "Credentials": {
        "AccessKeyId": "ASIA...",
        "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY",
        "SessionToken": "IQoJ...",
        "Expiration": "2024-12-20T15:00:00Z"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "ARO...",
        "Arn": "arn:aws:sts::123456789012:assumed-role/ExampleRole/ExampleSession"
    }
}
```

- **Credentials**: Role Assume 후 반환된 임시 보안 자격 증명.  
- **Expiration**: 임시 자격 증명의 만료 시간.

#### 임시 자격 증명 사용
```bash
export AWS_ACCESS_KEY_ID="ASIA..."
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY"
export AWS_SESSION_TOKEN="IQoJ..."
```

---

### **5. 완전한 예제 시나리오**

#### **Step 1: IAM Role 생성**
```bash
aws iam create-role \
  --role-name ExampleRole \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam::123456789012:user/ExampleUser"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  }'
```

#### **Step 2: Role에 권한 정책 연결**
```bash
aws iam put-role-policy \




!!!정책과 IAM Role의 권한 정책은 무슨 차이?
**IAM 정책(IAM Policy)**과 **IAM Role의 권한 정책(Role Policy)**는 모두 AWS 리소스에 대한 접근 권한을 제어하는 데 사용되지만, 사용하는 목적과 동작 방식에서 차이가 있습니다.  

---

### **1. IAM 정책 (IAM Policy)**

#### **정의**  
IAM 정책은 IAM 엔터티(사용자, 그룹, 역할)에 부여하여 AWS 리소스에 대한 권한을 정의하는 JSON 형식의 문서입니다.

#### **사용 대상**  
IAM 사용자(User), IAM 그룹(Group), 또는 IAM 역할(Role)에 직접 연결됩니다.

#### **특징**  
- 정책은 AWS 리소스에 대한 **허용(Allow)** 또는 **거부(Deny)**를 정의합니다.  
- AWS에서 제공하는 **AWS 관리형 정책**과 사용자가 정의하는 **사용자 지정 정책(Custom Policy)**이 있습니다.  
- 권한 정책은 일반적으로 **사용자**, **그룹** 또는 **역할**이 수행할 수 있는 작업을 정의합니다.

#### **예제**:  
IAM 사용자에게 특정 S3 버킷 읽기 권한을 부여하는 정책.  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-bucket/*"
    }
  ]
}
```

- 이 정책은 사용자(User) 또는 역할(Role)에 부여되어 AWS S3 버킷에서 객체를 읽을 수 있도록 허용합니다.

---

### **2. IAM Role의 권한 정책 (Role Policy)**

#### **정의**  
IAM 역할(Role)에 연결된 정책으로, **역할을 Assume한 주체**(IAM 사용자, 서비스, 또는 AWS 계정)가 수행할 수 있는 작업과 접근 가능한 리소스를 정의합니다.

#### **사용 대상**  
IAM 역할(Role)에만 연결되며, 역할(Role)이 허용하는 작업과 리소스를 제한합니다.

#### **특징**  
- **IAM 역할을 Assume한 주체**가 사용할 수 있는 권한을 정의합니다.  
- 권한 정책 외에 **신뢰 정책(Trust Policy)**를 통해 역할을 사용할 수 있는 주체를 별도로 정의해야 합니다.  
- 역할(Role)은 다른 AWS 서비스나 계정에 권한을 위임할 때 주로 사용됩니다.

#### **예제**:  
IAM 역할에 연결된 S3 읽기/쓰기 권한 정책.  
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::example-bucket/*"
    }
  ]
}
```

---

### **3. 차이점 비교**

| 특징                     | **IAM 정책 (IAM Policy)**                                              | **IAM Role의 권한 정책 (Role Policy)**                          |
|--------------------------|------------------------------------------------------------------------|----------------------------------------------------------------|
| **적용 대상**            | 사용자(User), 그룹(Group), 역할(Role)                                 | 역할(Role) 전용                                               |
| **연결 주체**            | 사용자 또는 그룹에 직접 연결                                           | Assume한 주체가 수행할 수 있는 작업 정의                       |
| **주체 제한**            | 별도의 주체 제한 없음 (사용자/그룹에 직접 부여됨)                      | **신뢰 정책(Trust Policy)**로 역할을 사용할 수 있는 주체 정의 |
| **주요 목적**            | 직접 권한 부여 (IAM 엔터티에 할당됨)                                  | 역할을 통해 간접적으로 권한 부여                               |
| **예시 사용 사례**       | IAM 사용자에게 EC2 시작 권한 부여                                     | 다른 계정의 서비스가 역할을 Assume하여 S3 작업 수행           |

---

### **4. IAM 역할의 신뢰 정책(Trust Policy)**와의 관계
- **권한 정책(Role Policy)**: 역할(Role)을 Assume한 주체가 AWS 리소스에 대해 수행할 수 있는 작업을 정의.  
- **신뢰 정책(Trust Policy)**: 누가(Role을 Assume할 주체)가 역할을 사용할 수 있는지를 정의.

#### 예제: IAM 역할 설정
- **신뢰 정책 (누가 Assume 가능한가?):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/ExampleUser"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

- **권한 정책 (Assume 후 어떤 작업을 할 수 있는가?):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*"
    }
  ]
}
```

---

### **5. 요약**
- **IAM 정책**은 사용자(User)나 그룹(Group)에 직접 권한을 부여하는 데 사용됩니다.  
- **IAM Role의 권한 정책**은 **역할(Role)**에 연결되어 역할을 Assume한 주체가 수행할 수 있는 작업을 정의합니다.  
- IAM Role에는 **신뢰 정책**과 **권한 정책**이 함께 설정되어야 역할을 완전히 활용할 수 있습니다.  

이 차이를 이해하면 IAM 역할과 정책을 효율적으로 설정할 수 있습니다! 😊


!!!만들어둔 IAM Policy를 IAM Role 권한 정책에 추가 가능?
네, 이미 만들어둔 **IAM Policy**를 **IAM Role 권한 정책(Role Policy)**으로 추가할 수 있습니다. 다만, **IAM Policy**는 두 가지 형태로 IAM Role에 연결될 수 있습니다:  

1. **관리형 정책(Managed Policy)**로 연결  
2. **인라인 정책(Inline Policy)**으로 추가  

---

### **1. IAM Role에 관리형 정책 연결**

#### **설명**  
- 이미 생성된 관리형 정책(사용자 정의 또는 AWS 관리형)을 IAM Role에 연결할 수 있습니다.  
- 관리형 정책은 여러 엔터티(User, Group, Role)에 재사용 가능.  

#### **방법**: AWS Management Console 또는 CLI를 사용

##### (1) AWS Management Console
1. **IAM 콘솔로 이동** → [IAM 콘솔](https://console.aws.amazon.com/iam/).
2. **역할(Roles)** 메뉴에서 수정할 IAM Role 선택.
3. **권한(Permissions)** 탭에서 **정책 추가(Attach policies)** 클릭.
4. 기존 관리형 정책을 검색 후 선택.
5. **Attach policy**를 클릭해 저장.

##### (2) AWS CLI
IAM Role에 관리형 정책 연결:
```bash
aws iam attach-role-policy \
    --role-name ExampleRole \
    --policy-arn arn:aws:iam::123456789012:policy/CustomPolicyName
```

- `--role-name`: 정책을 연결할 IAM Role 이름.
- `--policy-arn`: 연결할 관리형 정책의 ARN.

---

### **2. IAM Role에 인라인 정책 추가**

#### **설명**  
- 인라인 정책은 특정 IAM Role에만 연결되는 정책입니다.  
- 재사용할 수 없고, 역할(Role)이 삭제되면 정책도 함께 삭제됩니다.  
- 인라인 정책은 더 세부적이고 제한적인 권한을 설정해야 할 때 사용합니다.

#### **방법**: AWS Management Console 또는 CLI를 사용

##### (1) AWS Management Console
1. **IAM 콘솔로 이동** → [IAM 콘솔](https://console.aws.amazon.com/iam/).
2. **역할(Roles)** 메뉴에서 수정할 IAM Role 선택.
3. **권한(Permissions)** 탭에서 **정책 추가(Add inline policy)** 클릭.
4. 정책 작성기를 사용하거나 JSON 형식으로 정책 추가 후 저장.

##### (2) AWS CLI
IAM Role에 인라인 정책 추가:
```bash
aws iam put-role-policy \
    --role-name ExampleRole \
    --policy-name InlinePolicyName \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::example-bucket/*"
            }
        ]
    }'
```

- `--role-name`: 정책을 추가할 IAM Role 이름.
- `--policy-name`: 인라인 정책 이름.
- `--policy-document`: 정책 내용(JSON 형식).

---

### **3. 관리형 정책 vs 인라인 정책**

| **특징**                | **관리형 정책(Managed Policy)**                         | **인라인 정책(Inline Policy)**              |
|-------------------------|--------------------------------------------------------|---------------------------------------------|
| **연결 가능 대상**       | 여러 IAM 엔터티(User, Group, Role)에 연결 가능          | 특정 IAM Role에만 연결                      |
| **재사용 여부**          | 재사용 가능                                            | 재사용 불가능                               |
| **삭제 시 영향**         | 정책 삭제 시 연결된 권한도 제거                         | 역할(Role)이 삭제되면 정책도 함께 삭제       |
| **사용 사례**            | 여러 역할에 동일한 권한을 부여해야 하는 경우            | 특정 역할에만 맞춤 권한을 설정해야 하는 경우 |

---

### **4. 완전한 예제**

#### **1) 관리형 정책 생성 후 Role에 연결**
1. 사용자 정의 정책 생성:
```bash
aws iam create-policy \
    --policy-name CustomS3Policy \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::example-bucket/*"
            }
        ]
    }'
```

2. Role에 정책 연결:
```bash
aws iam attach-role-policy \
    --role-name ExampleRole \
    --policy-arn arn:aws:iam::123456789012:policy/CustomS3Policy
```

#### **2) 인라인 정책으로 직접 추가**
```bash
aws iam put-role-policy \
    --role-name ExampleRole \
    --policy-name InlineS3Policy \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::example-bucket/*"
            }
        ]
    }'
```

---

### **5. 요약**
- 이미 만들어둔 IAM Policy를 관리형 정책으로 Role에 연결하려면 `attach-role-policy`를 사용하세요.
- 특정 Role에만 사용할 정책이라면 인라인 정책으로 추가하세요.
- 관리형 정책은 재사용성이 높아 일반적으로 권장되며, 인라인 정책은 특수한 경우에 사용됩니다.




그럼 IAM Role 권한 정책은 Inline Policy라고 봐도 됨?
IAM Role의 권한 정책이 항상 **Inline Policy(인라인 정책)**이라고 단정할 수는 없습니다. **IAM Role 권한 정책(Role Policy)**은 **관리형 정책(Managed Policy)**와 **인라인 정책(Inline Policy)** 둘 다 포함할 수 있기 때문입니다.

### **IAM Role 권한 정책의 구성**

IAM Role에 부여된 권한 정책은 두 가지 방식으로 존재할 수 있습니다:

---

### **1. 관리형 정책 (Managed Policy)**

- **AWS 관리형 정책(AWS Managed Policy)**  
  AWS에서 제공하는 미리 정의된 정책으로, 역할(Role)에 연결하여 사용할 수 있습니다.  

- **사용자 정의 관리형 정책(Customer Managed Policy)**  
  사용자가 정의한 정책으로, 여러 IAM 엔터티(User, Group, Role)에서 재사용 가능합니다.

#### **특징**
- 여러 역할(Role)에 공유 가능.  
- 정책을 수정하면 연결된 모든 역할(Role)에 변경 사항이 적용됩니다.

#### **예시**: AWS CLI로 IAM Role에 관리형 정책 연결
```bash
aws iam attach-role-policy \
    --role-name ExampleRole \
    --policy-arn arn:aws:iam::123456789012:policy/CustomPolicyName
```

---

### **2. 인라인 정책 (Inline Policy)**

- 특정 IAM Role에만 직접 연결된 정책입니다.  
- 역할(Role)이 삭제되면 인라인 정책도 삭제됩니다.  

#### **특징**
- 정책이 해당 역할(Role)에만 고유하게 적용됩니다.  
- 재사용 불가능하며, 더 세밀하게 제어해야 하는 권한에 적합합니다.

#### **예시**: AWS CLI로 IAM Role에 인라인 정책 추가
```bash
aws iam put-role-policy \
    --role-name ExampleRole \
    --policy-name InlinePolicyName \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::example-bucket/*"
            }
        ]
    }'
```

---

### **IAM Role 권한 정책과 Inline Policy의 관계**

| **항목**                     | **IAM Role 권한 정책**                         | **Inline Policy**                              |
|-----------------------------|-----------------------------------------------|-----------------------------------------------|
| **정의**                     | Role에 부여된 권한을 정의하는 정책의 총칭       | Role에만 연결되는 고유한 정책                 |
| **관리형 정책 포함 여부**     | 포함 가능                                      | 포함되지 않음                                 |
| **재사용성**                 | 관리형 정책은 재사용 가능                       | 인라인 정책은 재사용 불가능                   |
| **삭제 시 정책 유지 여부**    | 관리형 정책은 유지                              | Role 삭제 시 인라인 정책도 삭제               |

---

### **정리**

IAM Role의 권한 정책은 **관리형 정책**과 **인라인 정책**을 모두 포함할 수 있습니다.  
- **Inline Policy**는 특정 IAM Role에만 직접 연결된 정책으로, 역할 삭제 시 함께 삭제되는 고유한 정책입니다.
- IAM Role 권한 정책 전체를 **Inline Policy**라고 볼 수는 없으며, 관리형 정책도 포함될 수 있습니다.  

권한을 관리할 때는 **관리형 정책**을 선호하며, 특수한 요구 사항이나 단일 역할에만 적용할 권한이 필요할 경우 **인라인 정책**을 사용합니다.


!!!IAM User에 IAM Role을 위임하여 어떤 Policy를 부여한다면, 관리형 정책이든 인라인 정책이든 IAM Role에 정책을 부여하는 건 맞지?
네, **IAM User**가 **IAM Role**을 Assume(역할 수임)하여 권한을 부여받는 경우, 결국 **IAM Role에 연결된 정책**이 권한을 정의하는 역할을 합니다. 이 정책은 **관리형 정책**이든 **인라인 정책**이든 상관없습니다. **IAM Role**은 실제 작업을 수행하는 주체의 권한을 결정합니다.

---

### **전체 흐름**
1. **IAM User가 IAM Role을 Assume**  
   - IAM User는 `sts:AssumeRole` 권한이 필요합니다.
   - IAM Role의 **신뢰 정책(Trust Policy)**에 IAM User가 Role을 Assume할 수 있도록 설정해야 합니다.

2. **IAM Role에 부여된 권한 정책(Role Policy)**  
   - IAM Role에 연결된 권한 정책이 실제로 AWS 리소스에 접근할 수 있는 권한을 결정합니다.
   - 이 권한 정책은 **관리형 정책** 또는 **인라인 정책**일 수 있습니다.

---

### **예제: IAM User가 IAM Role을 Assume하여 S3 권한을 부여받는 경우**

#### **1. IAM Role의 신뢰 정책 (Trust Policy)**
IAM Role이 IAM User의 Assume 요청을 신뢰하도록 구성:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/ExampleUser"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

#### **2. IAM Role의 권한 정책 (Role Policy)**  
IAM Role이 Assume된 후, 부여된 권한 정책에 따라 작업을 수행:
- **관리형 정책 연결**
```bash
aws iam attach-role-policy \
    --role-name ExampleRole \
    --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

- **인라인 정책 추가**
```bash
aws iam put-role-policy \
    --role-name ExampleRole \
    --policy-name InlineS3Policy \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:PutObject",
                "Resource": "arn:aws:s3:::example-bucket/*"
            }
        ]
    }'
```

#### **3. IAM User에 권한 추가**  
IAM User가 `sts:AssumeRole` API를 호출할 수 있도록 정책을 부여:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::123456789012:role/ExampleRole"
    }
  ]
}
```

---

### **결론**
- IAM User가 IAM Role을 Assume하면, 그 이후의 권한은 **IAM Role의 권한 정책(Role Policy)**에 의해 결정됩니다.
- IAM Role에 연결된 정책은 **관리형 정책**이든 **인라인 정책**이든 상관없이 역할을 Assume한 주체(IAM User)가 AWS 리소스에 대해 수행할 수 있는 작업을 정의합니다.
- 따라서 **IAM User가 직접 IAM Role의 정책을 사용하지 않고, IAM Role을 통해 위임된 정책을 사용한다**고 이해하면 됩니다. 

이 방식은 권한 관리를 더 체계적으로 유지하고, 원칙에 따라 최소 권한을 할당할 수 있는 효율적인 방법입니다.



!!!IAM User, IAM Role에는 Inline Policy를 부여할 수 있찌?
네, **IAM User**와 **IAM Role** 모두 **인라인 정책(Inline Policy)**를 부여할 수 있습니다. 그러나 **IAM Group**에도 인라인 정책을 부여할 수 있다는 점을 추가로 기억하면 좋습니다. 아래는 각 엔터티에 인라인 정책을 부여할 수 있는 방법과 주요 특징을 정리한 내용입니다.

---

### **1. IAM User에 인라인 정책 추가**
**IAM User**에 특정 권한을 부여하기 위해 인라인 정책을 추가할 수 있습니다.

#### **방법**: AWS CLI 예제
```bash
aws iam put-user-policy \
    --user-name ExampleUser \
    --policy-name InlinePolicyForUser \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:ListBucket",
                "Resource": "arn:aws:s3:::example-bucket"
            }
        ]
    }'
```

---

### **2. IAM Role에 인라인 정책 추가**
**IAM Role**에도 특정 권한을 부여하기 위해 인라인 정책을 추가할 수 있습니다.

#### **방법**: AWS CLI 예제
```bash
aws iam put-role-policy \
    --role-name ExampleRole \
    --policy-name InlinePolicyForRole \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "dynamodb:PutItem",
                "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/ExampleTable"
            }
        ]
    }'
```

---

### **3. IAM Group에 인라인 정책 추가**
**IAM Group**에도 인라인 정책을 추가할 수 있습니다. Group에 속한 모든 User가 이 정책의 영향을 받습니다.

#### **방법**: AWS CLI 예제
```bash
aws iam put-group-policy \
    --group-name ExampleGroup \
    --policy-name InlinePolicyForGroup \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "ec2:DescribeInstances",
                "Resource": "*"
            }
        ]
    }'
```

---

### **인라인 정책의 주요 특징**
1. **특정 엔터티에만 연결**  
   - 인라인 정책은 오직 연결된 IAM User, Role, Group에만 적용됩니다.
   - 정책을 다른 엔터티에 재사용할 수 없습니다.

2. **삭제와 연동**  
   - 엔터티(User, Role, Group)가 삭제되면 해당 인라인 정책도 함께 삭제됩니다.

3. **유연성**  
   - 특정 엔터티에 제한된 권한을 부여해야 할 때 유용합니다.
   - 하지만 관리형 정책(Managed Policy)에 비해 재사용성과 관리 측면에서 비효율적일 수 있습니다.

---

### **비교: 인라인 정책 vs 관리형 정책**

| **특징**               | **인라인 정책(Inline Policy)**                | **관리형 정책(Managed Policy)**              |
|-----------------------|-------------------------------------------|-------------------------------------------|
| **재사용성**            | 단일 엔터티(User, Role, Group)에만 적용       | 여러 엔터티에서 재사용 가능                  |
| **삭제 시 정책 유지 여부**| 엔터티(User, Role, Group) 삭제 시 함께 삭제됨 | 별도로 관리되며 엔터티 삭제 시 유지됨         |
| **관리 편의성**          | 특정 엔터티에만 적용할 때 유용               | 여러 엔터티에 동일한 권한을 부여할 때 유용     |
| **사용 사례**            | 개별 엔터티에 고유한 권한을 정의해야 할 때    | 표준화된 권한 관리 및 여러 엔터티에 적용할 때 |

---

### **결론**
- **IAM User**, **IAM Role**, **IAM Group** 모두 인라인 정책을 부여할 수 있습니다.
- 인라인 정책은 특정 엔터티에만 적용되는 맞춤형 권한 설정에 적합하지만, 재사용성과 관리 편의성을 고려할 때는 **관리형 정책(Managed Policy)**를 선호하는 것이 좋습니다.