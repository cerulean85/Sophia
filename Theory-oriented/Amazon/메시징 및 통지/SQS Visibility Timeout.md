# Amazon SQS Visibility Timeout

## 개요
- Amazon SQS Visibility Timeout은 메시지가 대기열에서 읽힌 후 다른 소비자에게 보이지 않도록 하는 시간
- 메시지가 처리 중일 때 다른 소비자가 동일한 메시지를 처리하지 않도록 방지

## 주요 기능 및 특징
- **기본 설정**: 기본 visibility timeout은 30초
- **최대 설정**: 최대 12시간까지 설정 가능
- **유연성**: 메시지별로 visibility timeout을 개별적으로 설정 가능
- **재처리 방지**: 메시지가 처리 중일 때 다른 소비자가 동일한 메시지를 처리하지 않도록 방지
- **타임아웃 연장**: 필요에 따라 visibility timeout을 연장하여 메시지 처리가 완료될 때까지 보이지 않도록 설정 가능

## 다른 서비스와의 연관성
### AWS Lambda
- **이벤트 처리**: Lambda 함수를 트리거로 SQS 메시지를 처리할 때 visibility timeout을 설정하여 중복 처리를 방지
- **자동화**: 메시지 처리 중 visibility timeout을 연장하여 안정적인 처리 보장

### Amazon CloudWatch
- **모니터링**: CloudWatch를 통해 visibility timeout 관련 지표를 모니터링
- **알람 설정**: CloudWatch 알람을 설정하여 visibility timeout 관련 문제 감지

### Amazon S3
- **데이터 저장**: SQS 메시지를 S3에 저장하여 처리 완료 후 데이터 보관
- **백업**: 메시지 데이터를 S3에 백업하여 안전하게 보관

## 사용 사례
- **비동기 작업 처리**: 비동기 작업을 처리할 때 visibility timeout을 설정하여 중복 처리를 방지
- **장시간 작업**: 장시간 작업이 필요한 경우 visibility timeout을 연장하여 안정적인 처리 보장
- **재처리 방지**: 메시지가 처리 중일 때 다른 소비자가 동일한 메시지를 처리하지 않도록 방지

## 요약
- Amazon SQS Visibility Timeout은 메시지가 대기열에서 읽힌 후 다른 소비자에게 보이지 않도록 하는 시간
- 기본 설정은 30초이며, 최대 12시간까지 설정 가능
- Lambda, CloudWatch, S3 등 다양한 AWS 서비스와 통합하여 중복 처리 방지, 안정적인 처리 보장, 모니터링 등 다양한 사용 사례에 활용 가능
- 비동기 작업 처리, 장시간 작업, 재처리 방지 등의 주요 기능을 제공하여 메시지 처리를 효율적으로 관리할 수 있음