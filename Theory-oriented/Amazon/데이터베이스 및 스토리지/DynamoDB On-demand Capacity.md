# 온디맨드 용량 모드에 대해 알려줌

## 요약
- 온디맨드 용량 모드는 Amazon DynamoDB의 용량 관리 옵션 중 하나임

## 개요
- 온디맨드 용량 모드는 DynamoDB 테이블의 읽기 및 쓰기 용량을 자동으로 조정함
- 사용량에 따라 자동으로 확장 및 축소됨

## 주요 기능 및 특징
- **자동 확장 및 축소**: 사용량에 따라 자동으로 읽기 및 쓰기 용량을 조정함
- **무제한 처리량**: 트래픽 급증 시에도 무제한으로 처리량을 제공함
- **비용 효율성**: 사용한 만큼만 비용을 지불함
- **관리 편의성**: 용량 계획 및 조정이 필요 없음
- **빠른 반응 시간**: 트래픽 변화에 빠르게 대응함
- **유연성**: 예측 불가능한 트래픽 패턴에 적합함

## 구성
- AWS Management Console, AWS CLI, AWS SDK를 통해 설정 및 관리 가능
- 테이블 생성 시 또는 기존 테이블의 용량 모드를 변경하여 설정 가능

## 작동 방식
1. AWS Management Console에 로그인
2. DynamoDB 서비스 선택
3. 테이블 생성 또는 기존 테이블 선택
4. 용량 모드에서 "온디맨드" 선택
5. 테이블 생성 또는 변경 사항 저장

## 다른 서비스와의 연관성
- Amazon CloudWatch와 통합되어 모니터링 가능
- AWS Lambda와 함께 사용하여 서버리스 애플리케이션 구축 가능
- Amazon API Gateway와 통합하여 API 요청 처리 가능

## 사용 사례
- 트래픽 패턴이 예측 불가능한 애플리케이션
- 초기 단계의 스타트업
- 이벤트 기반 애플리케이션
- 급격한 트래픽 증가가 예상되는 프로모션 또는 캠페인

## 결론
- 온디맨드 용량 모드는 예측 불가능한 트래픽 패턴을 가진 애플리케이션에 적합한 비용 효율적이고 유연한 용량 관리 옵션임

## 예제 코드
```python
import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
    TableName='ExampleTable',
    KeySchema=[
        {
            'AttributeName': 'PrimaryKey',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'PrimaryKey',
            'AttributeType': 'S'
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

print(response)
```