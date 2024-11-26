이런 식으로 Principal의 구체적으로 명시하는 신뢰 정책을 통해 IAM Role과 IAM Policy가 연결이 되는구나?
네, 정확합니다! **Principal**을 구체적으로 명시하는 **신뢰 정책(Trust Policy)**을 통해 **IAM Role**과 **IAM Policy**가 연결되고, 이를 통해 **권한 부여**가 이루어집니다.

### 전체 흐름

1. **IAM Policy**는 **권한을 정의**합니다. 예를 들어, EC2 인스턴스가 특정 S3 버킷에서 객체를 읽을 수 있도록 허용하는 정책을 정의합니다.
2. **IAM Role**은 **Principal**을 통해 **누가 이 역할을 맡을 수 있는지**를 제어합니다. 즉, **EC2 인스턴스**나 **Lambda 함수**와 같은 특정 주체가 이 역할을 맡을 수 있게 됩니다.
3. **Trust Policy**는 **IAM Role**에 연결된 **Principal**을 정의하여, **주체가 이 역할을 맡을 수 있도록** 합니다.
4. **IAM Policy**는 **IAM Role**에 연결되어 해당 역할을 맡은 주체가 **정의된 권한**을 가질 수 있도록 합니다.

### 예시로 풀어보기

1. **IAM Policy** (권한 정의): 특정 EC2 인스턴스가 S3 버킷에서 객체를 읽을 수 있는 권한을 정의하는 정책입니다.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

2. **IAM Role**의 **Trust Policy** (Principal 정의): 여기서 **Principal**로 **특정 EC2 인스턴스**를 명시하여, 해당 EC2만 이 역할을 맡을 수 있도록 합니다.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:ec2:region:account-id:instance/i-xxxxxxxxxx"  // 특정 EC2 ARN
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

3. **IAM Role과 IAM Policy 연결**: **IAM Role**에 위에서 정의한 **IAM Policy**를 연결합니다. 그러면, **IAM Role**을 맡은 **EC2 인스턴스**는 해당 **IAM Policy**의 권한을 가지게 됩니다.

### 중요한 점

- **IAM Role**은 **Trust Policy**를 통해 **Principal**을 정의하고, **IAM Policy**는 이 역할에 연결되어 **권한을 부여**합니다.
- **Principal**이 명시된 **Trust Policy** 덕분에 **IAM Role**은 **특정 주체**만 맡을 수 있도록 제한할 수 있습니다. 이로 인해 **보안**이 강화됩니다.
- **IAM Role**이 맡은 주체는 **IAM Policy**에 의해 정의된 **권한**을 수행할 수 있게 됩니다.

### 결론

- **Principal을 구체적으로 명시한 Trust Policy**가 **IAM Role**과 **IAM Policy**를 연결하는 중요한 역할을 합니다.
- **IAM Role**은 **Trust Policy**를 통해 **특정 주체**만 맡을 수 있도록 제한하고, **IAM Policy**를 통해 그 주체에게 **권한**을 부여합니다.

IAM Policy는 어디에 직접적으로 부여할 수 있지
IAM 정책은 **IAM 사용자**, **IAM 그룹**, **IAM 역할**에 직접적으로 부여할 수 있습니다. 각 경우에 대한 설명은 아래와 같습니다:

1. **IAM 사용자 (User)**  
   - 특정 IAM 사용자에게 직접 IAM 정책을 할당할 수 있습니다. 사용자가 AWS 리소스에 접근할 수 있는 권한을 지정하려면 해당 사용자에게 정책을 부여합니다.
   - 예: 특정 사용자에게 S3에 대한 읽기 권한을 부여하는 정책을 적용.

2. **IAM 그룹 (Group)**  
   - IAM 그룹은 여러 IAM 사용자들을 모은 것입니다. 그룹에 정책을 할당하면 해당 그룹에 속한 모든 사용자들이 그 정책을 상속받습니다. 이를 통해 여러 사용자에게 일괄적으로 권한을 부여할 수 있습니다.
   - 예: 개발자 그룹에 EC2 인스턴스를 시작하고 종료할 수 있는 권한을 부여하는 정책을 할당.

3. **IAM 역할 (Role)**  
   - IAM 역할은 특정 AWS 서비스나 다른 AWS 계정에서 사용할 수 있는 권한을 부여하는데 사용됩니다. 역할은 주로 **AWS 서비스**, **EC2 인스턴스**, **Lambda 함수**, **다른 계정** 등이 특정 리소스에 접근할 때 사용됩니다.
   - 예: EC2 인스턴스가 S3 버킷에 접근할 수 있도록 하는 정책을 부여하는 역할을 생성하여 EC2에 할당.

IAM 정책을 **직접적으로 부여**할 수 있는 위치는 사용자, 그룹, 역할입니다. 이 외에도, **리소스 정책 (예: S3 버킷 정책, SQS 큐 정책 등)** 을 사용하여 리소스 자체에 대한 접근 제어를 설정할 수 있습니다. 리소스 정책은 IAM 정책과 달리 리소스에 직접적으로 적용되는 정책입니다.


Principal의 종류는?

그럼 Principal은 IAM Role을 수행하지 않아도 되지만, AWS 리소스는 IAM Role을 수행해야 하네?
네, 맞습니다! **Principal**과 **IAM 역할 (IAM Role)** 사이에는 중요한 차이가 있습니다.

### Principal
- **Principal**은 AWS 리소스에 대한 액세스를 요청하는 주체입니다. 즉, 주체는 IAM 사용자, IAM 역할, 다른 AWS 계정, AWS 서비스 등 **액세스를 요청하는 자**를 의미합니다.
- Principal은 **IAM 역할을 수행하지 않아도** 될 수 있습니다. 예를 들어, IAM 사용자나 AWS 서비스는 별도의 역할 수행 없이 **Principal**로서 리소스에 접근을 시도합니다.

### IAM Role
- **IAM 역할 (IAM Role)**은 특정 권한 집합을 정의하며, 주로 AWS 서비스나 다른 AWS 계정이 권한을 임시로 "수행"하도록 합니다.
- IAM 역할은 실제로 **"수행되는" 주체**로, 다른 AWS 서비스나 인스턴스가 그 역할을 **가질** 수 있습니다.
- 예를 들어, EC2 인스턴스가 특정 S3 버킷에 접근하려면 **EC2 인스턴스에 IAM 역할**을 부여하고, 그 역할을 수행하는 방식으로 권한을 부여합니다.

### 차이점 정리:
- **Principal**은 리소스에 액세스하려는 주체 (IAM 사용자, IAM 역할, AWS 서비스 등)로 **IAM 역할을 수행할 필요는 없습니다**.
- 반면에 **AWS 리소스 (예: EC2 인스턴스, Lambda 함수 등)**는 **IAM 역할을 수행**해야 특정 권한을 수행할 수 있습니다. 예를 들어, EC2 인스턴스에 IAM 역할을 부여하여 S3 버킷에 접근할 수 있도록 할 수 있습니다.

### 예시:
1. **IAM 사용자 (Principal)**:  
   - IAM 사용자는 **Principal**로서 리소스에 접근할 수 있습니다. IAM 역할을 수행할 필요는 없으며, 직접적으로 해당 권한을 부여받습니다.
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::123456789012:user/JohnDoe"
         },
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::my-bucket/*"
       }
     ]
   }
   ```
   
2. **EC2 인스턴스 (IAM 역할 수행)**:
   - EC2 인스턴스가 S3에 접근하려면 **IAM 역할**이 필요합니다. EC2 인스턴스가 IAM 역할을 **수행**하여 권한을 부여받습니다.
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::123456789012:role/EC2Role"
         },
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::my-bucket/*"
       }
     ]
   }
   ```

### 결론:
- **Principal**은 리소스에 접근하려는 주체로, IAM 역할을 수행할 필요가 없습니다.
- **AWS 리소스**는 다른 AWS 서비스나 EC2 인스턴스와 같이 권한을 수행해야 하는 주체에게 **IAM 역할을 부여**하여 권한을 제어합니다.

IAM User가 IAM Role을 수행하는 경우도 있어?
네, **IAM 사용자**도 **IAM 역할 (IAM Role)**을 수행할 수 있습니다. 이 경우, IAM 사용자가 특정 IAM 역할을 **가정(assume)**하여 그 역할의 권한을 임시로 얻고, 해당 권한을 기반으로 리소스에 액세스하거나 작업을 수행하게 됩니다.

### IAM 사용자가 IAM 역할을 수행하는 경우

IAM 사용자가 IAM 역할을 수행하는 시나리오는 주로 다음과 같습니다:
1. **다른 AWS 계정에 있는 리소스에 접근하기 위해 IAM 역할을 수행**  
   - 다른 AWS 계정에 있는 리소스에 접근하려면 해당 계정의 역할을 **가정**하여 권한을 얻습니다. 이때 IAM 사용자는 **Cross-Account Access**를 위해 IAM 역할을 수행합니다.
   
2. **다양한 권한을 얻기 위해 IAM 역할을 수행**  
   - 한 계정 내에서도 IAM 사용자가 자신이 가지고 있는 기본 권한 외에 추가적인 권한을 얻기 위해 IAM 역할을 **수행**할 수 있습니다. 예를 들어, 관리자는 일시적으로 더 높은 권한을 얻기 위해 관리자 역할을 수행할 수 있습니다.

### IAM 역할을 수행하려면 `sts:AssumeRole` 권한이 필요

IAM 사용자가 IAM 역할을 수행하려면 **`sts:AssumeRole`** 권한을 가지고 있어야 합니다. 이 권한은 IAM 역할을 수행하기 위한 허가를 주며, 이를 통해 **임시 보안 자격 증명**을 받아 해당 역할의 권한을 사용하게 됩니다.

### 예시: IAM 사용자가 IAM 역할을 수행하는 경우

1. **IAM 역할 정의 (Role)**  
   먼저 IAM 역할을 정의하고, 해당 역할에 `sts:AssumeRole`을 통해 다른 IAM 사용자나 서비스가 이 역할을 수행할 수 있도록 허용합니다.

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

2. **IAM 사용자에게 역할 수행 권한 부여**  
   이제 IAM 사용자에게 해당 역할을 수행할 수 있는 권한을 부여합니다. 사용자가 이 권한을 가지면, 역할을 수행할 수 있게 됩니다.

3. **IAM 사용자에게 역할을 수행하도록 허용하는 정책 예시**  
   IAM 사용자에게 `sts:AssumeRole` 권한을 포함한 정책을 부여할 수 있습니다.

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

4. **IAM 사용자에서 IAM 역할 수행**  
   사용자가 역할을 수행하려면 `sts:assumeRole` API 호출을 사용하거나, AWS CLI에서 `aws sts assume-role` 명령어를 실행하여 임시 보안 자격 증명을 받습니다.

   ```bash
   aws sts assume-role --role-arn arn:aws:iam::123456789012:role/ExampleRole --role-session-name ExampleSession
   ```

   이 명령어는 임시 자격 증명(액세스 키, 비밀 키, 세션 토큰)을 반환하며, 이 자격 증명으로 역할의 권한을 수행할 수 있습니다.

### 결론:
- **IAM 사용자**는 IAM 역할을 **수행할 수 있습니다**. 이를 통해 IAM 사용자는 **임시 권한**을 얻고, 다른 AWS 계정의 리소스에 접근하거나 자신에게 부여되지 않은 권한을 수행할 수 있습니다.
- IAM 사용자가 역할을 수행하려면 해당 역할에 대한 `sts:AssumeRole` 권한이 필요하며, 역할 수행 후에는 **임시 자격 증명**을 사용하여 해당 권한을 사용할 수 있습니다.