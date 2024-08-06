Amazon 심플 큐 서비스란?
PDF
RSS
Amazon Simple Queue Service(Amazon SQS)는 내구력 있고 가용성이 뛰어난 보안 호스팅 대기열을 제공하며 이를 통해 분산 소프트웨어 시스템과 구성 요소를 통합 및 분리할 수 있습니다. Amazon SQS는 배달 못한 편지 대기열 및 비용 할당 태그와 같은 공용 구성을 제공합니다. AWS SDK가 지원하는 모든 프로그래밍 언어를 사용하여 액세스할 수 있는 일반 웹 서비스 API를 제공합니다.


Amazon SQS 제한 시간 초과
PDF
RSS
소비자가 대기열에서 메시지를 수신하고 처리하면 메시지는 계속 대기열에 있습니다. Amazon SQS는 메시지를 자동으로 삭제하지 않습니다. Amazon SQS는 분산 시스템이므로 소비자가 메시지를 실제로 받는지 보장할 수 없습니다(예를 들어, 연결 문제 또는 소비자 애플리케이션 문제로 인해). 또한, 소비자는 메시지를 수신하고 처리한 후 대기열에서 이 메시지를 삭제해야 합니다.

## Amazon SQS visibility timeout
- 컨슈머가 큐에서 메시지 받아 처리하면 메시지는 여전히 큐에 남음
- Amazon SQS는 컨슈머가 실제로 메시지 받았는지 보장하지 않으므로, 컨슈머가 큐에서 메시지를 없애야 함
- 모든 컨슈머가 메시지를 받거나 처리하지 못하게 하려면 visibility timeout 설정 (기본30분, 최대12시간)


https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html

https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html