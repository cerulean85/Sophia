# Amazon Kinesis Data Streams

- Amazon Web Services(AWS)에서 제공하는 실시간 데이터 스트리밍 서비스
- Kinesis Data Streams를 사용하면 대규모 데이터를 실시간으로 수집하고 처리할 수 있음
- 이 서비스는 데이터 스트리밍 애플리케이션을 구축하고, 실시간 분석, 모니터링, 로깅 등의 다양한 사용 사례에 활용할 수 있음

# 주요 특징
## 1. 실시간 데이터 수집
- 초당 수백 테라바이트의 데이터를 실시간으로 수집할 수 있음
- 다양한 데이터 소스(예 웹사이트 클릭스트림, 애플리케이션 로그, IoT 기기 데이터)에서 데이터를 수집할 수 있음

## 2. 확장성
- 데이터 스트림의 샤드(Shard)를 추가하거나 제거하여 처리량을 동적으로 조정할 수 있음
- 샤드는 데이터 스트림의 기본 단위로, 각 샤드는 초당 1MB의 쓰기와 2MB의 읽기 처리량을 제공

## 3. 내구성 및 가용성
- 데이터를 여러 가용 영역(AZ)에 복제하여 높은 내구성과 가용성을 보장
- 데이터는 기본적으로 24시간 동안 보관되며, 최대 7일 동안 보관 기간을 확장할 수 있음

## 4. 데이터 처리
- Amazon Kinesis Client Library(KCL)를 사용하여 데이터를 실시간으로 처리할 수 있음
- AWS Lambda와 통합하여 서버리스 방식으로 데이터를 처리할 수 있음

## 5. 보안
- 데이터 전송 중 및 저장 중 암호화를 지원
- AWS Identity and Access Management(IAM)를 사용하여 액세스 제어를 관리할 수 있음

# 사용 사례
- 실시간 로그 및 이벤트 데이터 수집
  - 애플리케이션 로그, 시스템 로그, IoT 기기 로그 등을 실시간으로 수집하고 분석할 수 있음

- 실시간 분석
  - 실시간 대시보드, 모니터링 시스템, 실시간 경고 시스템을 구축할 수 있음
  - 예를 들어, 웹사이트 트래픽 분석, 실시간 사용자 행동 분석 등을 수행할 수 있음

- 데이터 파이프라인
  - 실시간 데이터 파이프라인을 구축하여 데이터를 수집, 처리, 저장할 수 있음
  - 데이터를 Amazon S3, Amazon Redshift, Amazon Elasticsearch Service 등으로 전송하여 분석할 수 있음

# 작동 방식
## 1. 데이터 스트림 생성
- AWS Management Console, AWS CLI, AWS SDK를 사용하여 Kinesis 데이터 스트림을 생성
- 스트림의 샤드 수를 설정하여 초기 처리량을 구성

## 2. 데이터 수집
- 다양한 데이터 소스에서 데이터를 수집하여 Kinesis 데이터 스트림으로 전송
- AWS SDK, Kinesis Producer Library(KPL), Kinesis Agent 등을 사용하여 데이터를 스트림으로 전송할 수 있음

## 3. 데이터 처리
- Kinesis Client Library(KCL)를 사용하여 데이터를 실시간으로 처리
- AWS Lambda를 사용하여 서버리스 방식으로 데이터를 처리할 수 있음

## 4. 데이터 저장 및 분석
- 처리된 데이터를 Amazon S3, Amazon Redshift, Amazon Elasticsearch Service 등으로 전송하여 저장하고 분석할 수 있음

# 예제 코드
다음은 AWS SDK for Python (Boto3)을 사용하여 Amazon Kinesis Data Streams의 스트림을 생성하고 데이터를 전송하는 예제 코드
```python
import boto3

# Kinesis 클라이언트 생성
kinesis = boto3.client('kinesis', region_name='us-west-2')

# Kinesis 데이터 스트림 생성
response = kinesis.create_stream(
    StreamName='my_kinesis_stream',
    ShardCount=1
)

# 데이터 전송
response = kinesis.put_record(
    StreamName='my_kinesis_stream',
    Data='Hello, this is a test message!',
    PartitionKey='partition_key'
)

print(response)
```

요약
Amazon Kinesis Data Streams는 대규모 데이터를 실시간으로 수집하고 처리할 수 있는 AWS의 실시간 데이터 스트리밍 서비스 실시간 로그 및 이벤트 데이터 수집, 실시간 분석, 데이터 파이프라인 구축 등의 다양한 사용 사례에 활용할 수 있음 확장성, 내구성, 보안 등의 기능을 제공하여 안정적이고 효율적인 데이터 스트리밍을 지원


---

- 실시간으로 데이터를 수집 및 캡처
- 초당 기가바이트 데이터를 수집, 실시간으로 처리 및 분석에 사용
- 로그 및 이벤트 데이터 수집, 모바일 데이터 수집, IoT 디바이스 데이터 수집

- 다음 다이어그램은 Kinesis Data Streams의 상위 수준 아키텍처를 보여줌
- 생산자가 계속해서 Kinesis Data Streams에 데이터를 푸시하고 소비자가 실시간으로 데이터를 처리

- EC2에서 실행되는 사용자 지정 애플리케이션 또는 Amazon Data Firehose 전송 스트림 등의 소비자는 Amazon DynamoDB, Amazon Redshift 또는 Amazon S3와 같은 AWs 서비스를 사용하여 결과를 저장할 수 있음

<p align="center">
  <img src="../../images/cloud/kinesis_data_stream.png">
</p>

## References
- [Amazon Kinesis Data Streams 용어 및 개념](https//docs.aws.amazon.com/ko_kr/streams/latest/dev/key-concepts.html)
