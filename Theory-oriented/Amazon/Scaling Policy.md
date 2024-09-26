# Simple Scaling Policy

- Simple Scaling Policy는 특정 조건이 충족될 때 단일 스케일링 작업을 수행하는 AWS Auto Scaling 정책
- 조건이 충족되면 인스턴스를 추가하거나 제거하여 애플리케이션의 성능을 유지함

## 주요 기능 및 특징
- 단일 스케일링 작업
  - 특정 조건이 충족될 때 단일 스케일링 작업을 수행
  - 예: CPU 사용률이 70%를 초과하면 인스턴스를 추가

- CloudWatch 경보 기반
  - CloudWatch 경보를 기반으로 스케일링 작업을 트리거
  - 다양한 지표(CPU 사용률, 네트워크 트래픽 등)를 모니터링하여 경보 설정

- 간단한 설정
  - 설정이 간단하여 빠르게 스케일링 정책을 적용할 수 있음
  - 복잡한 조건 없이 단순한 스케일링 작업을 수행

## 구성
- Auto Scaling 그룹 생성
- CloudWatch 경보 설정
- Simple Scaling Policy 설정

## 작동 방식
1. Auto Scaling 그룹을 생성하고 초기 인스턴스 수를 설정함
2. CloudWatch에서 모니터링할 지표와 경보를 설정함
3. Simple Scaling Policy를 설정하여 경보가 트리거될 때 인스턴스를 추가하거나 제거함
4. 조건이 충족되면 Auto Scaling 그룹이 설정된 정책에 따라 인스턴스를 자동으로 조정함

## 다른 서비스와의 연관성
- Amazon EC2: Auto Scaling 그룹에서 관리하는 인스턴스
- Amazon CloudWatch: 모니터링 지표와 경보 설정
- Elastic Load Balancing (ELB): Auto Scaling 그룹과 함께 사용하여 트래픽 분산

## 사용 사례
- 웹 애플리케이션의 트래픽 증가에 대응
  - 예: 트래픽이 증가하면 인스턴스를 추가하여 성능 유지
- 배치 작업의 수요 변화에 대응
  - 예: 배치 작업이 많아지면 인스턴스를 추가하여 작업 시간 단축
- 비용 최적화
  - 예: 수요가 감소하면 인스턴스를 제거하여 비용 절감

## 결론
- Simple Scaling Policy는 특정 조건이 충족될 때 단일 스케일링 작업을 수행하는 간단한 정책
- CloudWatch 경보와 함께 사용하여 애플리케이션의 성능을 유지하고 비용을 최적화할 수 있음

## 예제 코드
### Simple Scaling Policy 설정 예제
```json
{
  "AutoScalingGroupName": "my-auto-scaling-group",
  "PolicyName": "scale-out-policy",
  "PolicyType": "SimpleScaling",
  "AdjustmentType": "ChangeInCapacity",
  "ScalingAdjustment": 1,
  "Cooldown": 300
}
```

# Target Tracking Policy

- Target Tracking Policy는 AWS Auto Scaling에서 제공하는 정책으로, 특정 지표의 목표 값을 설정하고 해당 목표를 유지하기 위해 인스턴스 수를 자동으로 조정하는 기능
- 목표 지표를 설정하면 Auto Scaling이 자동으로 인스턴스 수를 조정하여 목표를 유지함

## 주요 기능 및 특징
- 목표 지표 설정
  - 특정 지표의 목표 값을 설정하여 Auto Scaling이 이를 유지하도록 함
  - 예: 평균 CPU 사용률을 50%로 유지

- 자동 조정
  - 설정된 목표 지표를 유지하기 위해 인스턴스 수를 자동으로 조정
  - 지표가 목표 값을 초과하거나 미달할 때 인스턴스를 추가하거나 제거

- 간단한 설정
  - 설정이 간단하여 빠르게 적용 가능
  - 복잡한 조건 없이 목표 지표만 설정하면 됨

- 다양한 지표 지원
  - CPU 사용률, 네트워크 트래픽, 요청 수 등 다양한 CloudWatch 지표를 지원
  - 사용자 정의 지표도 사용 가능

## 구성
- Auto Scaling 그룹 생성
- CloudWatch 지표 설정
- Target Tracking Policy 설정

## 작동 방식
1. Auto Scaling 그룹을 생성하고 초기 인스턴스 수를 설정함
2. CloudWatch에서 모니터링할 지표를 설정함
3. Target Tracking Policy를 설정하여 목표 지표 값을 정의함
4. Auto Scaling 그룹이 설정된 목표 지표를 유지하기 위해 인스턴스 수를 자동으로 조정함

## 다른 서비스와의 연관성
- Amazon EC2: Auto Scaling 그룹에서 관리하는 인스턴스
- Amazon CloudWatch: 모니터링 지표 설정 및 경보
- Elastic Load Balancing (ELB): Auto Scaling 그룹과 함께 사용하여 트래픽 분산

## 사용 사례
- 웹 애플리케이션의 성능 유지
  - 예: 평균 CPU 사용률을 50%로 유지하여 성능 최적화
- 배치 작업의 수요 변화에 대응
  - 예: 작업 큐의 길이를 일정 수준으로 유지하여 작업 시간 단축
- 비용 최적화
  - 예: 수요가 감소하면 인스턴스를 제거하여 비용 절감

## 결론
- Target Tracking Policy는 특정 지표의 목표 값을 설정하고 이를 유지하기 위해 인스턴스 수를 자동으로 조정하는 강력한 정책
- 간단한 설정과 다양한 지표 지원을 통해 애플리케이션의 성능을 최적화하고 비용을 절감할 수 있음

## 예제 코드
### Target Tracking Policy 설정 예제
```json
{
  "AutoScalingGroupName": "my-auto-scaling-group",
  "PolicyName": "scale-out-policy",
  "PolicyType": "TargetTrackingScaling",
  "TargetTrackingConfiguration": {
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ASGAverageCPUUtilization"
    },
    "TargetValue": 50.0
  }
}
```


# Simple Scaling Policy vs. Target Tracking Policy

## Simple Scaling Policy
- **작동 방식**: 특정 조건이 충족될 때 단일 스케일링 작업을 수행
- **기반**: CloudWatch 경보
- **설정**: 조건이 충족되면 인스턴스를 추가하거나 제거
- **사용 예**: CPU 사용률이 70%를 초과하면 인스턴스를 1개 추가
- **장점**: 설정이 간단하고 특정 조건에 대한 명확한 대응 가능
- **단점**: 복잡한 수요 변화에 대한 대응이 어려움

## Target Tracking Policy
- **작동 방식**: 특정 지표의 목표 값을 설정하고, 해당 목표를 유지하기 위해 인스턴스 수를 자동으로 조정
- **기반**: CloudWatch 지표
- **설정**: 목표 지표 값을 설정하면 Auto Scaling이 이를 유지하기 위해 인스턴스를 추가하거나 제거
- **사용 예**: 평균 CPU 사용률을 50%로 유지
- **장점**: 복잡한 수요 변화에 유연하게 대응 가능, 설정이 간단
- **단점**: 목표 지표 설정이 부정확할 경우 과도한 스케일링 발생 가능




# Step Scaling Policy

## 요약
- Step Scaling Policy는 Amazon EC2 Auto Scaling에서 제공하는 자동 확장 정책 중 하나로, 지표 값이 특정 임계값을 초과하거나 미달할 때 인스턴스 수를 단계적으로 조정하는 기능

## 개요
- Amazon EC2 Auto Scaling의 자동 확장 정책 중 하나
- 지표 값이 특정 임계값을 초과하거나 미달할 때 인스턴스 수를 단계적으로 조정
- 각 단계는 지표 값의 범위와 조정할 인스턴스 수를 정의

## 주요 기능 및 특징
- 단계적 조정: 지표 값의 범위에 따라 인스턴스 수를 단계적으로 조정
- 유연한 설정: 각 단계의 임계값과 조정할 인스턴스 수를 유연하게 설정 가능
- 다양한 지표 지원: CPU 사용률, 네트워크 트래픽, 사용자 정의 지표 등 다양한 지표를 기반으로 확장 가능
- 비용 효율성: 필요에 따라 인스턴스를 자동으로 조정하여 비용 절감
- 고가용성: 애플리케이션의 성능을 유지하면서 고가용성 보장

## 구성
- Auto Scaling 그룹: 인스턴스의 자동 확장을 관리하는 그룹
- 지표: 확장 정책이 모니터링할 지표 (예: CPU 사용률)
- 임계값: 지표 값이 초과하거나 미달할 때의 임계값
- 단계: 각 단계는 지표 값의 범위와 조정할 인스턴스 수를 정의

## 작동 방식
1. Auto Scaling 그룹을 생성하고 인스턴스를 추가함
2. 지표와 임계값을 설정함 (예: CPU 사용률 70% 초과 시)
3. 각 단계의 지표 값 범위와 조정할 인스턴스 수를 설정함
4. 지표 값이 특정 임계값을 초과하거나 미달할 때 인스턴스 수를 단계적으로 조정함

## 다른 서비스와의 연관성
- Amazon CloudWatch와 통합되어 지표 데이터를 모니터링하고 확장 정책을 트리거
- AWS Lambda와 연동하여 사용자 정의 확장 로직을 구현 가능
- Amazon SNS와 통합하여 확장 이벤트에 대한 알림을 받을 수 있음

## 사용 사례
- 웹 애플리케이션의 CPU 사용률을 일정 수준으로 유지하여 성능 최적화
- 네트워크 트래픽에 따라 인스턴스 수를 조정하여 비용 절감
- 사용자 정의 지표를 기반으로 애플리케이션의 확장 정책을 설정

## 결론
- Step Scaling Policy는 지표 값이 특정 임계값을 초과하거나 미달할 때 인스턴스 수를 단계적으로 조정하는 Amazon EC2 Auto Scaling의 자동 확장 정책
- 단계적 조정, 유연한 설정, 다양한 지표 지원, 비용 효율성, 고가용성 등의 기능을 제공
- Amazon CloudWatch, AWS Lambda, Amazon SNS 등과 통합되어 유연한 데이터 처리 및 보안 관리 가능

## 예제 코드
```python
import boto3

# Auto Scaling 클라이언트 생성
autoscaling = boto3.client('autoscaling')

# Step Scaling Policy 생성
response = autoscaling.put_scaling_policy(
    AutoScalingGroupName='my-auto-scaling-group',
    PolicyName='cpu-step-scaling-policy',
    PolicyType='StepScaling',
    AdjustmentType='ChangeInCapacity',
    StepAdjustments=[
        {
            'MetricIntervalLowerBound': 0,
            'MetricIntervalUpperBound': 10,
            'ScalingAdjustment': 1
        },
        {
            'MetricIntervalLowerBound': 10,
            'MetricIntervalUpperBound': 20,
            'ScalingAdjustment': 2
        },
        {
            'MetricIntervalLowerBound': 20,
            'ScalingAdjustment': 3
        }
    ],
    MetricAggregationType='Average'
)

print(response)