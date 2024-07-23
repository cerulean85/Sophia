# Amazon Kinesis Data Streams

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
- [Amazon Kinesis Data Streams 용어 및 개념](https://docs.aws.amazon.com/ko_kr/streams/latest/dev/key-concepts.html)
