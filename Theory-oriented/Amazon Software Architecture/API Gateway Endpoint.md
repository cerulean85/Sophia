# API Gateway Endpoint

## 요약
- API Gateway Endpoint는 Amazon API Gateway에서 API를 배포하고 접근할 수 있는 URL을 제공하는 구성 요소

## 개요
- API Gateway에서 생성된 API를 외부에서 접근할 수 있도록 하는 URL
- 다양한 유형의 엔드포인트를 제공하여 다양한 사용 사례에 대응

## 주요 기능 및 특징
- Regional Endpoint: 특정 AWS 리전에서 API를 배포하고 접근할 수 있는 엔드포인트
- Edge-Optimized Endpoint: 전 세계적으로 분산된 Amazon CloudFront 엣지 로케이션을 통해 API를 배포하여 성능을 최적화
- Private Endpoint: VPC 내부에서만 접근 가능한 엔드포인트로, 보안이 중요한 내부 API에 적합

## 구성
- 엔드포인트 유형: Regional, Edge-Optimized, Private
- API Gateway 스테이지: 엔드포인트와 연결된 API의 특정 배포 버전
- 도메인 이름: 사용자 정의 도메인 이름을 API Gateway 엔드포인트에 연결 가능
- 인증서: HTTPS를 통한 보안 통신을 위해 AWS Certificate Manager(ACM)에서 인증서를 가져와 사용

## 작동 방식
1. API를 생성하고 엔드포인트 유형을 선택함
2. API Gateway 스테이지를 생성하여 엔드포인트와 연결함
3. 필요에 따라 사용자 정의 도메인 이름을 설정하고 인증서를 연결함
4. 엔드포인트 URL을 통해 API에 접근함

## 다른 서비스와의 연관성
- Amazon CloudFront와 통합하여 Edge-Optimized Endpoint를 제공
- AWS Certificate Manager(ACM)와 연동하여 HTTPS 인증서 관리
- Amazon Route 53과 통합하여 사용자 정의 도메인 이름을 설정하고 트래픽을 라우팅

## 사용 사례
- 특정 리전에서 API를 배포하고 접근할 때: Regional Endpoint 사용
- 전 세계적으로 분산된 사용자에게 최적의 성능을 제공할 때: Edge-Optimized Endpoint 사용
- VPC 내부에서만 접근 가능한 보안이 중요한 API를 배포할 때: Private Endpoint 사용

## 결론
- API Gateway Endpoint는 API를 배포하고 접근할 수 있는 URL을 제공하는 구성 요소
- 다양한 엔드포인트 유형을 제공하여 다양한 사용 사례에 대응 가능
- Amazon CloudFront, AWS Certificate Manager, Amazon Route 53 등과 통합하여 성능, 보안, 트래픽 관리를 최적화할 수 있음

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

# 사용자 정의 도메인 이름 설정
response = apigateway.create_domain_name(
    domainName='api.example.com',
    certificateArn='arn:aws:acm:us-east-1:123456789012:certificate/abcd1234-5678-90ab-cdef-EXAMPLE11111'
)

# 사용자 정의 도메인 이름에 API 매핑
apigateway.create_base_path_mapping(
    domainName='api.example.com',
    restApiId=api_id,
    stage='dev'
)

print('API 배포 및 사용자 정의 도메인 이름 설정 완료')
```

# API Gateway Endpoint
- AWS API Gateway를 통해 제공되는 API의 URL
- 클라이언트가 서버와 상호작용할 수 있는 접점을 의미
- API Gateway는 RESTful API나 WebSocket API를 생성하여 요청을 처리하고, Lambda, EC2, S3와 같은 AWS 리소스 또는 다른 외부 서비스를 호출하는 역할을 함

## API Gateway Endpoint의 구체적인 예시
- 예시: 사용자 정보를 조회하는 API Gateway 엔드포인트
```bash
https://abc123xyz.execute-api.us-east-1.amazonaws.com/prod/users
```
- 엔드포인트 구성 요소 분석:
https://

이 엔드포인트는 HTTPS를 사용해 안전하게 통신합니다.
abc123xyz.execute-api.us-east-1.amazonaws.com

abc123xyz는 API Gateway 인스턴스의 고유 식별자입니다.
execute-api는 AWS API Gateway 도메인입니다.
us-east-1은 API가 위치한 AWS 리전을 나타냅니다. 이 경우 미국 동부 1 리전입니다.
amazonaws.com은 AWS 도메인 이름입니다.
/prod

**API 단계(Stage)**를 나타냅니다. prod는 프로덕션(운영) 환경을 의미하며, 개발이나 테스트 단계에서는 dev, test 등의 다른 스테이지 이름이 사용될 수 있습니다.
/users

이 부분은 리소스 경로입니다. 이 경우, 사용자 정보를 조회하는 엔드포인트로 해석됩니다. 예를 들어 GET /users 요청을 보내면 사용자 목록을 반환하는 API일 수 있습니다.
예시 API 요청과 응답:
요청 방법 (HTTP Method):

GET /users: 전체 사용자 목록을 조회
GET /users/{id}: 특정 사용자 ID에 대한 정보 조회
POST /users: 새로운 사용자 생성
PUT /users/{id}: 기존 사용자 정보 수정
DELETE /users/{id}: 특정 사용자 삭제
응답 예시 (JSON):

json
코드 복사
{
    "userId": "12345",
    "name": "John Doe",
    "email": "john.doe@example.com"
}
API Gateway Endpoint의 역할:
클라이언트는 위와 같은 엔드포인트를 통해 API 요청을 보내고, 서버에서 처리된 결과를 받아옵니다.
이 과정에서 API Gateway는 트래픽 관리, 인증 및 권한 부여, 로깅, 모니터링 등을 처리해줍니다.
정리:
API Gateway Endpoint는 AWS API Gateway가 제공하는 API의 URL로, 클라이언트와 서버가 데이터를 주고받는 주요 통신 접점입니다.