# Amazon S3 Requester Pays

## 요약
- Amazon S3 Requester Pays는 데이터 요청자가 데이터 전송 및 요청 비용을 부담하는 기능

## 개요
- S3 버킷 소유자가 데이터 전송 비용을 절감할 수 있도록 지원
- 데이터 요청자가 데이터 요청 및 전송 비용을 지불

## 주요 기능 및 특징
- **비용 절감**: 버킷 소유자가 데이터 전송 비용을 절감
- **유연한 비용 분담**: 데이터 요청자가 비용을 부담
- **간편한 설정**: S3 콘솔, AWS CLI, AWS SDK를 통해 설정 가능
- **보안**: IAM 정책을 통해 접근 제어 가능

## 구성
- **버킷 설정**: S3 버킷에서 Requester Pays 기능 활성화
- **IAM 정책**: 요청자에게 필요한 권한 부여
- **비용 청구**: 요청자에게 데이터 요청 및 전송 비용 청구

## 작동 방식
1. S3 버킷에서 Requester Pays 기능 활성화
2. 데이터 요청자가 S3 버킷에 접근하여 데이터 요청
3. 요청자가 데이터 요청 및 전송 비용을 지불
4. 버킷 소유자는 비용 절감

## 다른 서비스와의 연관성
- **Amazon S3**: S3 버킷에서 Requester Pays 기능 활성화
- **AWS IAM**: IAM 정책을 통해 접근 제어 및 권한 부여

## 사용 사례
- **데이터 공유**: 여러 사용자와 데이터를 공유하면서 비용 절감
- **공공 데이터 세트**: 공공 데이터 세트를 제공하면서 비용 부담을 요청자에게 전가
- **협력 프로젝트**: 협력 업체와 데이터를 공유하면서 비용 절감

## 결론
- Amazon S3 Requester Pays는 데이터 요청자가 데이터 전송 및 요청 비용을 부담하는 기능
- 버킷 소유자가 비용을 절감할 수 있으며, 유연한 비용 분담이 가능

### 예제 코드
```python
import boto3

# S3 클라이언트 생성
s3 = boto3.client('s3')

# Requester Pays 활성화
response = s3.put_bucket_request_payment(
    Bucket='your-bucket-name',
    RequestPaymentConfiguration={
        'Payer': 'Requester'
    }
)

print(response)