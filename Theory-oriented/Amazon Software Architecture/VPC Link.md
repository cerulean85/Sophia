# VPC Link

## 요약
VPC Link는 AWS API Gateway와 VPC 내의 리소스를 연결하는 서비스임.

## 개요
- VPC Link는 API Gateway를 통해 VPC 내의 리소스에 안전하게 접근할 수 있도록 함
- 주로 프라이빗 서브넷에 위치한 리소스와의 통신을 위해 사용됨

## 주요 기능 및 특징
- API Gateway와 VPC 내 리소스를 연결함
- 프라이빗 서브넷의 리소스에 대한 안전한 접근을 제공함
- 네트워크 트래픽을 VPC 내에서 유지하여 보안성을 높임
- 여러 API Gateway 엔드포인트에서 동일한 VPC Link를 공유 가능함

## 구성
- VPC Link는 API Gateway와 VPC 내의 Network Load Balancer(NLB)를 연결함
- NLB는 VPC 내의 리소스로 트래픽을 라우팅함

## 작동 방식
1. VPC Link 생성
2. API Gateway에서 VPC Link를 사용하여 엔드포인트 설정
3. NLB를 통해 VPC 내의 리소스로 트래픽 전달

## 다른 서비스와의 연관성
- API Gateway와 연동하여 VPC 내 리소스에 접근함
- Network Load Balancer와 함께 사용됨

## 사용 사례
- 프라이빗 서브넷에 위치한 데이터베이스에 접근
- 내부 애플리케이션 서버와의 통신

## 결론
VPC Link는 API Gateway와 VPC 내 리소스를 안전하게 연결하는 데 유용함.

## 예제 코드
```json
{
  "VpcLink": {
    "Name": "MyVpcLink",
    "TargetArns": [
      "arn:aws:elasticloadbalancing:region:account-id:loadbalancer/net/my-nlb/1234567890abcdef"
    ]
  }
}