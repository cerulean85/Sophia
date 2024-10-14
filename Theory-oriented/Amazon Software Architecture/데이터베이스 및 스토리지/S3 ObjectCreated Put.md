# s3:ObjectCreated:Put

- `s3:ObjectCreated:Put`는 Amazon S3 이벤트 유형 중 하나로, S3 버킷에 객체가 업로드될 때 발생하는 이벤트
- 이 이벤트는 객체가 S3 버킷에 성공적으로 업로드된 후 트리거됨

## 주요 기능 및 특징
- **이벤트 트리거**: S3 버킷에 객체가 업로드될 때 자동으로 트리거됨
- **자동화**: Lambda 함수, S3 이벤트 알림, Amazon EventBridge 등과 통합하여 자동화된 작업 수행 가능
- **유연성**: 다양한 작업을 자동으로 수행할 수 있도록 설정 가능 (예: 데이터 처리, 알림 전송, 데이터 복제 등)

## 구성
- **S3 버킷 설정**: S3 버킷에 이벤트 알림을 설정하여 `s3:ObjectCreated:Put` 이벤트를 트리거
- **Lambda 함수 설정**: Lambda 함수를 이벤트 알림의 대상으로 설정하여 자동으로 실행되도록 구성
- **EventBridge 설정**: Amazon EventBridge 규칙을 설정하여 이벤트를 처리할 대상 지정

## 작동 방식
1. **객체 업로드**: S3 버킷에 객체가 업로드됨
2. **이벤트 트리거**: `s3:ObjectCreated:Put` 이벤트가 트리거됨
3. **이벤트 알림**: 설정된 대상(Lambda 함수, EventBridge 등)으로 이벤트 알림이 전송됨
4. **자동 작업 수행**: 대상에서 정의된 작업이 자동으로 수행됨 (예: 데이터 처리, 알림 전송 등)

## 다른 서비스와의 연관성
- **AWS Lambda**: S3 이벤트 알림을 통해 Lambda 함수를 자동으로 실행하여 데이터 처리 작업 수행
- **Amazon EventBridge**: S3 이벤트를 EventBridge 규칙으로 전송하여 다양한 AWS 서비스와 통합
- **Amazon SNS**: S3 이벤트 알림을 통해 SNS 주제로 알림 전송

## 사용 사례
- **데이터 처리 자동화**: S3 버킷에 업로드된 데이터를 자동으로 처리
- **알림 전송**: 객체 업로드 시 알림을 전송하여 사용자에게 통지
- **데이터 복제**: 객체 업로드 시 다른 S3 버킷으로 자동 복제

## 결론
- `s3:ObjectCreated:Put` 이벤트는 S3 버킷에 객체가 업로드될 때 자동으로 트리거되어 다양한 자동화 작업을 수행할 수 있도록 지원
- Lambda 함수, EventBridge 등과 통합하여 유연하고 강력한 자동화 솔루션을 구현할 수 있음

## 예제 코드
### S3 이벤트 알림 설정 예제
```json
{
  "LambdaFunctionConfigurations": [
    {
      "LambdaFunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:ProcessS3Event",
      "Events": ["s3:ObjectCreated:Put"]
    }
  ]
}