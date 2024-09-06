# Access Control List (ACL)

- AWS에서 특정 리소스에 대한 접근 권한을 제어한느 방법 중 하나
- 주로 Amazon S3와 Amazon VPC에서 사용
- 특정 IP 주소나 CIDR 블록에 대해 접근을 허용하거나 거부할 수 있음

# 주요 기능
- Amazon S3 ACL
    - S3 버킷과 객체에 대한 접근 권한을 제어
    - 각 객체와 버킷에 대해 읽기, 쓰기, 읽기 ACL, 쓰기 ACL 권한을 설정할 수 있음
    - 주로 간단한 권한 설정에 사용되며, 복잡한 권한 설정에는 버킷 정책이나 IAM 정책을 사용하는 것이 좋음

- Amazon VPC 네트워크 ACL
    - VPC 서브넷에 대한 인바운드 및 아웃바운드 트래픽을 제어
    - 각 서브넷에 대해 여러 네트워크 ACL을 설정할 수 있으며, 각 ACL은 여러 규칙을 가질 수 있음
    - 규칙은 번호 순서대로 평가되며, 첫 번재 일치하는 규칙이 적용됨
    - 기본적으로 모든 인바운드 및 아웃바운드 트래픽을 허용하거나 거부할 수 있음


# 예시
- 버킷 ACL
    - 버킷 소유자에게 모든 권한을 부여하고, 특정 사용자에게 읽기 권한을 부여할 수 있음

```js
{
  "Owner": {
    "ID": "bucket-owner-id"
  },
  "Grants": [
    {
      "Grantee": {
        "Type": "CanonicalUser",
        "ID": "user-id"
      },
      "Permission": "READ"
    }
  ]
}
```

- Amazon VPC 네트워크 ACL 예시
    - 인바운드 규칙
        - 특정 IP 주소에서 오는 HTTP 트래픽을 허용하는 규칙 추가
```js
[
  {
    "RuleNumber": 100,
    "Protocol": "TCP",
    "RuleAction": "ALLOW",
    "Egress": false,
    "CidrBlock": "0.0.0.0/0",
    "PortRange": {
      "From": 80,
      "To": 80
    }
  }
]
```        