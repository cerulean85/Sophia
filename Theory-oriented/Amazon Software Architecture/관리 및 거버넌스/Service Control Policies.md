# Service Control Policies

- AWS Organizations에서 제공하는 기능으로, 조직 내 계정의 서비스 사용을 제어하기 위해 사용됨
- 조직의 루트, 조직 단위(OU), 또는 개별 계정에 적용할 수 있음

## 주요 기능 및 특징
- 서비스 사용 제어
  - 특정 AWS 서비스 또는 API 작업에 대한 접근을 허용하거나 차단할 수 있음
  - 조직 내 모든 계정에 일관된 정책을 적용할 수 있음

- 계층적 정책 적용
  - 조직의 루트, OU, 계정에 계층적으로 정책을 적용할 수 있음
  - 상위 레벨의 정책은 하위 레벨에 자동으로 상속됨

- 정책 관리
  - JSON 형식으로 정책을 작성하고 관리할 수 있음
  - AWS Management Console, AWS CLI, AWS SDK를 통해 정책을 생성, 수정, 삭제할 수 있음

- 보안 강화
  - 조직 내 계정의 보안 설정을 중앙에서 관리하고 강화할 수 있음
  - 특정 리소스에 대한 접근을 제한하여 보안 사고를 예방할 수 있음

## 구성
- 조직의 루트, OU, 계정에 정책을 적용할 수 있음
- 정책은 JSON 형식으로 작성됨
- 정책은 허용(Allow) 또는 거부(Deny) 문을 포함할 수 있음

## 작동 방식
1. AWS Organizations에서 조직을 생성하고 계정을 추가함
2. 조직의 루트, OU, 또는 계정에 적용할 SCP를 작성함
3. SCP를 적용할 엔터티(루트, OU, 계정)를 선택함
4. SCP를 적용하여 해당 엔터티의 서비스 사용을 제어함
5. SCP는 상위 레벨에서 하위 레벨로 상속됨

## 다른 서비스와의 연관성
- AWS Identity and Access Management (IAM): IAM 정책과 함께 사용하여 세부적인 접근 제어를 구현할 수 있음
- AWS CloudTrail: SCP 적용 결과를 모니터링하고 감사할 수 있음

## 사용 사례
- 특정 서비스 사용 제한
  - 예: 개발 계정에서 비용이 많이 드는 서비스 사용을 제한함
- 보안 정책 적용
  - 예: 모든 계정에서 특정 리전의 리소스 생성 제한
- 규정 준수
  - 예: 특정 규정 준수를 위해 특정 서비스 사용을 강제함

## 결론
- Service Control Policies는 조직 내 계정의 서비스 사용을 중앙에서 제어하고 관리할 수 있는 강력한 도구임
- 보안 강화, 비용 관리, 규정 준수 등을 위해 유용하게 사용될 수 있음

## 예제 코드
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ec2:RunInstances",
        "s3:CreateBucket"
      ],
      "Resource": "*"
    }
  ]
}
```


## SCP를 통한 간접적인 인터넷 연결 차단 방법
- 퍼블릭 IP 할당 차단
  - SCP를 사용해 ```ec2:AssignPublicIpAddress``` API를 차단하면, EC2 인스턴스가 퍼블릭 IP 할당받는 것을 막을 수 있음
  - 퍼블릭 IP가 없다면 해당 인스턴스는 인터넷과 연결할 수 없음

- 인터넷 게이트웨이 생성 차단:
  - ```ec2:CreateInternetGateway``` 및 ```ec2:AttacthInternetGateway``` API 호출을 차단하여 VPC가 인터넷과 연결되지 않도록 만들 수 있음

- 네트워크 보안 설정 제한
  - ```ec2:AuthorizeSecurityGroupIngress``` 또는 ```ec2:AuthorizeSecurityGroupEgress```와 같은 보안 그룹의 인바운드/아웃바운드 규칙을 제한하여 인터넷을 통한 트래픽이 허용되지 않도록 만들 수 있음