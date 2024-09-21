# EC2 Instance Savings Plan

EC2 Instance Savings Plan은 AWS에서 제공하는 비용 절감 옵션으로, 특정 EC2 인스턴스 패밀리와 리전에 대해 일정 시간 동안 사용을 약정함으로써 할인된 요금으로 인스턴스를 사용할 수 있는 계획입니다.

## 주요 특징
- **할인 요금**: 특정 EC2 인스턴스 패밀리와 리전에 대해 할인된 요금을 제공
- **유연성**: 동일한 인스턴스 패밀리 내에서 인스턴스 유형, 운영 체제, 테넌시, 결제 옵션을 변경할 수 있음
- **약정 기간**: 1년 또는 3년 약정 기간 선택 가능
- **결제 옵션**: All Upfront, Partial Upfront, No Upfront 결제 옵션 제공

## 작동 방식
1. **약정**: 특정 EC2 인스턴스 패밀리와 리전에 대해 일정 시간 동안 사용을 약정
2. **할인 적용**: 약정한 시간 동안 해당 인스턴스 패밀리와 리전에 대해 할인된 요금이 자동으로 적용
3. **유연성**: 동일한 인스턴스 패밀리 내에서 인스턴스 유형, 운영 체제, 테넌시, 결제 옵션을 변경할 수 있음

## 사용 사례
- **예측 가능한 워크로드**: 일정한 사용 패턴이 있는 워크로드에 대해 비용 절감 가능
- **장기 사용 계획**: 장기적으로 특정 인스턴스 패밀리와 리전을 사용할 계획이 있는 경우
- **비용 최적화**: EC2 인스턴스 사용 비용을 최적화하고자 하는 경우

## 결론
EC2 Instance Savings Plan은 특정 EC2 인스턴스 패밀리와 리전에 대해 일정 시간 동안 사용을 약정함으로써 할인된 요금으로 인스턴스를 사용할 수 있는 비용 절감 옵션입니다. 예측 가능한 워크로드와 장기 사용 계획이 있는 경우 비용을 최적화하는 데 유용합니다.

## 예제
### EC2 Instance Savings Plan 구매 예제 (AWS CLI)
```bash
aws savingsplans purchase-savings-plan \
    --savings-plan-offering-id <offering-id> \
    --commitment <commitment-amount> \
    --savings-plan-type EC2Instance \
    --term 1-year \
    --payment-option AllUpfront
```

# Compute Savings Plan

Compute Savings Plan은 AWS에서 제공하는 비용 절감 옵션으로, 특정 인스턴스 유형이나 리전에 구애받지 않고 모든 AWS 컴퓨팅 서비스에 대해 할인된 요금을 제공하는 계획입니다. 이는 EC2 인스턴스, AWS Fargate, AWS Lambda 등 다양한 컴퓨팅 서비스에 적용됩니다.

## 주요 특징
- **유연성**: 특정 인스턴스 유형, 리전, 운영 체제, 테넌시 등에 구애받지 않고 모든 AWS 컴퓨팅 서비스에 적용 가능
- **할인 요금**: 약정한 사용량에 대해 할인된 요금을 제공
- **약정 기간**: 1년 또는 3년 약정 기간 선택 가능
- **결제 옵션**: All Upfront, Partial Upfront, No Upfront 결제 옵션 제공

## 작동 방식
1. **약정**: 일정 시간 동안 특정 금액의 컴퓨팅 사용을 약정
2. **할인 적용**: 약정한 시간 동안 모든 AWS 컴퓨팅 서비스에 대해 할인된 요금이 자동으로 적용
3. **유연성**: 다양한 컴퓨팅 서비스와 인스턴스 유형에 대해 유연하게 적용 가능

## 사용 사례
- **다양한 컴퓨팅 서비스 사용**: EC2 인스턴스, AWS Fargate, AWS Lambda 등 다양한 컴퓨팅 서비스를 사용하는 경우
- **예측 가능한 워크로드**: 일정한 사용 패턴이 있는 워크로드에 대해 비용 절감 가능
- **비용 최적화**: 컴퓨팅 사용 비용을 최적화하고자 하는 경우

## 결론
Compute Savings Plan은 특정 인스턴스 유형이나 리전에 구애받지 않고 모든 AWS 컴퓨팅 서비스에 대해 할인된 요금을 제공하는 비용 절감 옵션입니다. 다양한 컴퓨팅 서비스를 사용하는 경우와 예측 가능한 워크로드에 대해 비용을 최적화하는 데 유용합니다.

## 예제
### Compute Savings Plan 구매 예제 (AWS CLI)
```bash
aws savingsplans purchase-savings-plan \
    --savings-plan-offering-id <offering-id> \
    --commitment <commitment-amount> \
    --savings-plan-type Compute \
    --term 1-year \
    --payment-option AllUpfront
```