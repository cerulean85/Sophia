# Amazon SQS Extended Client Library

## 요약
- Amazon SQS Extended Client Library는 Amazon SQS와 Amazon S3를 통합하여 대용량 메시지를 처리할 수 있도록 지원하는 라이브러리

## 개요
- Amazon SQS는 메시지 크기가 최대 256KB로 제한
- 대용량 메시지를 처리하기 위해 Amazon SQS Extended Client Library를 사용하여 메시지를 Amazon S3에 저장하고 SQS 메시지에는 S3 객체의 참조를 포함시킴

## 주요 기능 및 특징
- **대용량 메시지 지원**: 256KB 이상의 메시지를 처리할 수 있도록 지원
- **자동 저장**: 메시지 크기가 설정된 임계값을 초과하면 자동으로 Amazon S3에 저장
- **투명한 통합**: 기존 SQS 클라이언트와 호환되며, 추가적인 코드 변경 없이 대용량 메시지를 처리할 수 있음

## 작동 방식
1. 메시지 크기가 설정된 임계값을 초과하면 메시지를 Amazon S3에 저장
2. SQS 메시지에는 S3 객체의 참조를 포함
3. 메시지를 수신할 때 S3에서 실제 메시지를 가져옴

## 사용 사례
- **대용량 데이터 처리**: 로그 파일, 이미지, 비디오 등 대용량 데이터를 메시지로 처리할 때
- **비동기 데이터 전송**: 대용량 데이터를 비동기적으로 전송하고 처리할 때

## 예제 코드
### Java 예제
```java
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.AmazonSQSClientBuilder;
import com.amazonaws.services.sqs.ExtendedClientConfiguration;
import com.amazonaws.services.sqs.AmazonSQSExtendedClient;

public class SQSExtendedClientExample {
    public static void main(String[] args) {
        AmazonS3 s3 = AmazonS3ClientBuilder.defaultClient();
        AmazonSQS sqs = AmazonSQSClientBuilder.defaultClient();

        ExtendedClientConfiguration extendedClientConfig = new ExtendedClientConfiguration()
                .withLargePayloadSupportEnabled(s3, "your-s3-bucket-name");

        AmazonSQSExtendedClient sqsExtended = new AmazonSQSExtendedClient(sqs, extendedClientConfig);

        String queueUrl = sqs.getQueueUrl("your-queue-name").getQueueUrl();
        String messageBody = "This is a large message that will be stored in S3";

        // Send a message
        sqsExtended.sendMessage(queueUrl, messageBody);

        // Receive a message
        String receivedMessage = sqsExtended.receiveMessage(queueUrl).getMessages().get(0).getBody();
        System.out.println("Received message: " + receivedMessage);
    }
}
```