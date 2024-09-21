# Dedicated Instance

Dedicated Instance는 Amazon EC2에서 제공하는 인스턴스 배포 옵션 중 하나로, 물리적 서버의 하드웨어를 다른 AWS 고객과 공유하지 않고 단일 고객에게만 할당되는 인스턴스입니다. 이는 보안 및 규정 준수 요구 사항이 높은 워크로드에 적합합니다.

## 주요 특징
- **물리적 격리**: 인스턴스가 물리적 서버의 하드웨어를 다른 AWS 고객과 공유하지 않음
- **보안 강화**: 물리적 격리를 통해 보안 및 규정 준수 요구 사항을 충족
- **전용 하드웨어**: 단일 고객에게만 할당된 전용 하드웨어에서 실행
- **유연한 배포**: 기존의 On-Demand, Reserved, Spot 인스턴스와 동일한 방식으로 배포 가능

## 사용 사례
- **규정 준수**: 특정 규정 준수 요구 사항을 충족해야 하는 경우 (예: 금융, 의료 분야)
- **보안 강화**: 물리적 격리가 필요한 보안 민감한 워크로드
- **고성능 컴퓨팅**: 전용 하드웨어에서 실행해야 하는 고성능 컴퓨팅 작업

## 비용
- **추가 요금**: Dedicated Instance는 물리적 격리를 제공하기 때문에 추가 요금이 발생할 수 있음
- **유연한 결제 옵션**: On-Demand, Reserved, Spot 인스턴스와 동일한 결제 옵션 제공

## 결론
Dedicated Instance는 물리적 격리와 보안을 강화해야 하는 워크로드에 적합한 인스턴스 배포 옵션입니다. 규정 준수 요구 사항이 높은 경우나 보안 민감한 워크로드에 유용합니다.

## 예제
### Dedicated Instance 설정 예제 (AWS CLI)
```bash
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --count 1 \
    --instance-type m5.large \
    --placement Tenancy=dedicated
```