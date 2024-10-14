# Amazon API Gateway

## 요약
- Amazon API Gateway는 개발자가 API를 생성, 배포, 유지 관리할 수 있도록 지원하는 완전 관리형 서비스

## 개요
- RESTful API 및 WebSocket API를 생성하고 관리할 수 있는 서비스
- 백엔드 서비스와의 통신을 위한 API를 쉽게 생성하고 배포할 수 있음

## 주요 기능 및 특징
- API 생성 및 배포: RESTful API 및 WebSocket API를 생성하고 배포할 수 있음
- 트래픽 관리: API 트래픽을 모니터링하고 제어할 수 있음
- 보안: IAM, Amazon Cognito, API 키 등을 사용하여 API 접근을 제어할 수 있음
- 모니터링 및 로깅: Amazon CloudWatch와 통합되어 API 호출을 모니터링하고 로그를 기록할 수 있음
- 확장성: 자동으로 트래픽에 맞게 확장 가능
- 비용 효율성: 사용한 만큼만 비용을 지불하는 종량제 요금제

## 구성
- API: API Gateway에서 생성된 API
- 리소스: API의 각 엔드포인트를 나타내는 리소스
- 메서드: 각 리소스에 대해 수행할 수 있는 작업 (GET, POST, PUT, DELETE 등)
- 통합: API Gateway와 백엔드 서비스 간의 통신 설정
- 배포: API를 배포하여 엔드포인트를 공개

## 작동 방식
1. API를 생성함
2. 리소스를 정의하고 각 리소스에 메서드를 추가함
3. 백엔드 서비스와의 통합을 설정함
4. API를 배포하여 엔드포인트를 공개함
5. 트래픽을 모니터링하고 보안을 설정함

## 다른 서비스와의 연관성
- AWS Lambda와 통합하여 서버리스 아키텍처를 구현할 수 있음
- Amazon CloudWatch와 통합하여 API 호출을 모니터링하고 로그를 기록할 수 있음
- AWS Identity and Access Management(IAM)와 연동하여 API 접근 제어를 강화할 수 있음
- Amazon Cognito와 통합하여 사용자 인증 및 권한 부여를 관리할 수 있음

## 사용 사례
- 모바일 및 웹 애플리케이션을 위한 백엔드 API 생성
- 서버리스 애플리케이션을 위한 API 생성
- 마이크로서비스 아키텍처에서 서비스 간 통신을 위한 API 생성

## 결론
- Amazon API Gateway는 개발자가 API를 생성, 배포, 유지 관리할 수 있도록 지원하는 완전 관리형 서비스
- RESTful API 및 WebSocket API를 쉽게 생성하고 배포할 수 있으며, 트래픽 관리, 보안, 모니터링 및 로깅 등의 기능을 제공함
- AWS Lambda, Amazon CloudWatch, IAM 등 다양한 AWS 서비스와 통합 가능

## 예제 코드
```python
import boto3

# API Gateway 클라이언트 생성
apigateway = boto3.client('apigateway')

# REST API 생성
response = apigateway.create_rest_api(
    name='MyAPI',
    description='This is my API'
)

api_id = response['id']
print(f'API ID: {api_id}')

# 리소스 생성
resources = apigateway.get_resources(
    restApiId=api_id
)
root_id = resources['items'][0]['id']

resource = apigateway.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='myresource'
)
resource_id = resource['id']
print(f'Resource ID: {resource_id}')

# 메서드 생성
apigateway.put_method(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

# 통합 설정
apigateway.put_integration(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)

# 배포 생성
apigateway.create_deployment(
    restApiId=api_id,
    stageName='dev'
)

print('API 배포 완료')
```