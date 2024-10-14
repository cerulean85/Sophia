# Lambda@Edge

## 요약
- Lambda@Edge는 Amazon CloudFront를 통해 전 세계적으로 분산된 위치에서 AWS Lambda 함수를 실행할 수 있는 서비스

## 개요
- Amazon CloudFront의 엣지 로케이션에서 AWS Lambda 함수를 실행하여 사용자 요청을 처리하고 응답을 변환할 수 있음
- 지연 시간을 줄이고 사용자 경험을 향상시키기 위해 콘텐츠를 사용자에게 더 가까운 위치에서 처리

## 주요 기능 및 특징
- 글로벌 분산: 전 세계적으로 분산된 CloudFront 엣지 로케이션에서 Lambda 함수를 실행하여 지연 시간 최소화
- 서버리스 아키텍처: 인프라 관리 없이 코드를 실행할 수 있는 서버리스 환경 제공
- 다양한 트리거: CloudFront 이벤트(뷰어 요청, 뷰어 응답, 오리진 요청, 오리진 응답)에 따라 Lambda 함수를 트리거할 수 있음
- 실시간 데이터 처리: 사용자 요청을 실시간으로 처리하고 변환 가능
- 보안: IAM 역할을 통해 Lambda 함수와 CloudFront 리소스에 대한 접근 제어 강화
- 비용 효율성: 사용한 만큼만 비용을 지불하는 종량제 요금제

## 구성
- Lambda 함수: CloudFront 엣지 로케이션에서 실행할 AWS Lambda 함수
- CloudFront 배포: Lambda@Edge 함수를 연결할 CloudFront 배포
- 트리거 이벤트: Lambda 함수를 트리거할 CloudFront 이벤트 (뷰어 요청, 뷰어 응답, 오리진 요청, 오리진 응답)
- IAM 역할: Lambda 함수와 CloudFront 리소스에 대한 접근을 제어하는 IAM 역할

## 작동 방식
1. AWS Lambda 콘솔에서 Lambda 함수를 작성함
2. CloudFront 배포를 생성하거나 기존 배포를 선택함
3. Lambda 함수를 CloudFront 이벤트(뷰어 요청, 뷰어 응답, 오리진 요청, 오리진 응답)에 연결함
4. 사용자 요청이 CloudFront 엣지 로케이션에 도달하면 Lambda 함수가 트리거되어 요청을 처리하고 응답을 변환함

## 다른 서비스와의 연관성
- Amazon CloudFront와 통합되어 글로벌 분산 콘텐츠 전송 및 Lambda 함수 실행 가능
- AWS Identity and Access Management(IAM)와 연동하여 Lambda 함수와 CloudFront 리소스에 대한 접근 제어 강화
- Amazon S3와 통합하여 정적 콘텐츠를 CloudFront를 통해 제공하고 Lambda 함수를 사용하여 실시간으로 변환 가능

## 사용 사례
- 사용자 요청을 실시간으로 처리하고 변환하여 지연 시간을 최소화할 때
- 콘텐츠를 사용자에게 더 가까운 위치에서 처리하여 사용자 경험을 향상시킬 때
- CloudFront를 통해 제공되는 콘텐츠에 대한 사용자 정의 로직을 적용할 때

## 결론
- Lambda@Edge는 Amazon CloudFront를 통해 전 세계적으로 분산된 위치에서 AWS Lambda 함수를 실행할 수 있는 서비스
- 글로벌 분산, 서버리스 아키텍처, 다양한 트리거, 실시간 데이터 처리 등의 기능을 제공하여 사용자 요청을 효율적으로 처리하고 응답을 변환할 수 있음
- Amazon CloudFront, AWS IAM, Amazon S3 등과 통합되어 유연한 데이터 처리 및 보안 관리 가능

## 예제 코드
```python
import json

def lambda_handler(event, context):
    # CloudFront 이벤트에서 요청 객체 가져오기
    request = event['Records'][0]['cf']['request']
    
    # 요청 URI를 변경하는 예제
    if request['uri'] == '/old-path':
        request['uri'] = '/new-path'
    
    # 변경된 요청 반환
    return request