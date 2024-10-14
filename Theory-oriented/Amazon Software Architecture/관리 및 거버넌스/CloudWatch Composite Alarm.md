# Amazon CloudWatch Composite Alarm

## 요약
- 여러 개의 CloudWatch 경보를 결합하여 단일 경보로 관리

## 개요
- 여러 경보의 상태를 기반으로 경보를 트리거하거나 해제
- 복잡한 모니터링 요구 사항을 충족하고 경보 관리를 단순화

## 주요 기능 및 특징
- **다중 경보 결합**: 여러 CloudWatch 경보를 결합하여 단일 Composite Alarm으로 관리
- **복합 논리**: AND, OR 논리를 사용하여 경보 상태 결정
- **단순화된 모니터링**: 여러 경보를 하나의 Composite Alarm으로 결합
- **자동화된 대응**: Composite Alarm이 트리거될 때 자동으로 대응 작업 수행

## 구성
- **기본 경보**: 개별적으로 설정된 CloudWatch 경보
- **Composite Alarm**: 여러 기본 경보를 결합하여 생성된 경보

## 작동 방식
1. **기본 경보 설정**: 모니터링할 지표에 대해 CloudWatch 경보 설정
2. **Composite Alarm 생성**: 여러 기본 경보를 결합하여 Composite Alarm 생성
3. **복합 논리 적용**: AND, OR 논리를 사용하여 Composite Alarm의 상태 결정
4. **자동화된 대응**: Composite Alarm이 트리거될 때 자동으로 대응 작업 수행

## 다른 서비스와의 연관성
- **AWS Lambda**: Composite Alarm이 트리거될 때 Lambda 함수 실행
- **Amazon SNS**: Composite Alarm이 트리거될 때 SNS 주제로 알림 전송
- **Amazon CloudWatch Dashboards**: Composite Alarm의 상태를 대시보드에서 시각화

## 사용 사례
- **복잡한 모니터링 요구 사항**: 여러 지표를 결합하여 복잡한 모니터링 요구 사항 충족
- **단순화된 경보 관리**: 여러 경보를 하나의 Composite Alarm으로 결합하여 관리 단순화
- **자동화된 대응**: 복합 조건이 충족될 때 자동으로 대응 작업 수행

## 결론
- 여러 개의 CloudWatch 경보를 결합하여 단일 경보로 관리할 수 있는 강력한 기능 제공
- 복잡한 모니터링 요구 사항을 충족하고 경보 관리를 단순화하며 자동화된 대응 작업 수행 가능

## 예제 코드
### Composite Alarm 생성 예제 (AWS CLI)
```bash
aws cloudwatch put-composite-alarm \
    --alarm-name "MyCompositeAlarm" \
    --alarm-rule "ALARM(MyAlarm1) OR ALARM(MyAlarm2)" \
    --actions-enabled \
    --alarm-actions "arn:aws:sns:us-west-2:123456789012:MySNSTopic"
```