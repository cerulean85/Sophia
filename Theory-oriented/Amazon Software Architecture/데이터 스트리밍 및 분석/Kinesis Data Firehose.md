# Amazon Kinesis Data Firehose
- Amazon Web Services(AWS)에서 제공하는 완전 관리형 데이터 스트리밍 서비스
- Kinesis Data Firehose를 사용하면 데이터를 실시간으로 스트리밍하여 AWS 서비스나 타사 서비스로 전송하고, 데이터를 변환 및 로드할 수 있음
- 데이터 스트리밍을 간소화하고, 실시간 데이터 분석 및 처리를 가능하게 함

# 주요 특징
## 1. 실시간 데이터 스트리밍
- 데이터를 실시간으로 스트리밍하여 Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, Splunk 등 다양한 대상에 전송할 수 있음

## 2. 데이터 변환
- AWS Lambda 함수를 사용하여 스트리밍 데이터의 변환, 필터링, 포맷 변경 등을 수행할 수 있음
- 데이터 형식을 JSON, CSV, Parquet, ORC 등으로 변환할 수 있음

## 3. 자동 스케일링
- 데이터 스트림의 처리량에 따라 자동으로 확장 및 축소하여, 데이터 처리 성능을 최적화


## 4. 내구성 및 보안
- 데이터를 안전하게 전송하기 위해 전송 중 및 저장 중 암호화를 지원
- AWS Identity and Access Management(IAM)를 사용하여 액세스 제어를 관리할 수 있음

## 5. 모니터링 및 로깅
- Amazon CloudWatch를 사용하여 스트리밍 데이터의 모니터링 및 로깅을 수행할 수 있음
- 데이터 전송 상태, 처리량, 오류 등을 실시간으로 모니터링할 수 있음

# 사용 사례
- 실시간 로그 분석
    - 애플리케이션 로그, 서버 로그, IoT 기기 로그 등을 실시간으로 수집하고 분석할 수 있음
    - 로그 데이터를 Amazon S3, Amazon Redshift, Elasticsearch Service 등에 저장하여 분석할 수 있음

- 실시간 데이터 파이프라인
    - 실시간 데이터 파이프라인을 구축하여, 데이터 수집, 변환, 로드 작업을 자동화할 수 있음
    - 데이터 파이프라인을 통해 실시간 데이터 분석 및 처리를 수행할 수 있음

- IoT 데이터 스트리밍
    - IoT 기기에서 생성된 데이터를 실시간으로 수집하고, 분석하여 인사이트를 도출할 수 있음
    - IoT 데이터를 Amazon S3, Amazon Redshift 등에 저장하여 장기 보관 및 분석할 수 있음

# 작동 방식
## 1. 데이터 소스 설정
- 데이터 소스를 설정하여 Kinesis Data Firehose로 데이터를 스트리밍함
- 데이터 소스는 애플리케이션 로그, IoT 기기, 서버 로그 등 다양한 소스가 될 수 있음

## 2. 데이터 변환 설정
- AWS Lambda 함수를 사용하여 스트리밍 데이터를 변환할 수 있음
- 데이터 필터링, 포맷 변경, 집계 등의 작업을 수행할 수 있음

## 3. 데이터 대상 설정
- 데이터를 전송할 대상을 설정함
- Amazon S3, Amazon Redshift, Elasticsearch Service, Splunk 등 다양한 대상에 데이터를 전송할 수 있음

## 4. 데이터 스트리밍 및 모니터링
- 설정된 데이터 소스에서 데이터를 스트리밍하고, Kinesis Data Firehose가 데이터를 변환하여 설정된 대상으로 전송함
- Amazon CloudWatch를 사용하여 데이터 스트리밍 상태를 모니터링하고, 처리량, 오류 등을 확인할 수 있음


# 예제 코드
- 다음은 AWS SDK for Python (Boto3)을 사용하여 Amazon Kinesis Data Firehose의 스트림을 생성하고 데이터를 전송하는 예제 코드
```python
import boto3

# Kinesis Firehose 클라이언트 생성
firehose = boto3.client('firehose', region_name='us-west-2')

# Firehose 전송 스트림 생성
response = firehose.create_delivery_stream(
    DeliveryStreamName='my_firehose_stream',
    S3DestinationConfiguration={
        'RoleARN': 'arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_ROLE_NAME',
        'BucketARN': 'arn:aws:s3:::YOUR_BUCKET_NAME',
        'Prefix': 'my_prefix/',
        'BufferingHints': {
            'SizeInMBs': 5,
            'IntervalInSeconds': 300,
        },
        'CompressionFormat': 'UNCOMPRESSED'
    }
)

# 데이터 전송
response = firehose.put_record(
    DeliveryStreamName='my_firehose_stream',
    Record={
        'Data': 'Hello, this is a test message!'
    }
)

print(response)
```

---

- 수집 및 캡쳐된 데이터를 분석 서비스로 로드 및 전송
- 데이터를 분석 및 모니터링
- 실시간 데이터 스트림 준비 및 로드
- 최종 저장소는 Amazon S3, Redshift, Elasticsearch Service, Splunk, HTTP 엔드포인트

## References
- [Kinesis Data Streams 와 Kinesis Data Firehose 비교](https://may9noy.tistory.com/441)