# S3 Object Lambda

## 요약
- S3 Object Lambda는 Amazon S3 객체를 요청 시 실시간으로 처리할 수 있는 기능을 제공하는 서비스

## 개요
- Amazon S3의 객체를 요청할 때 AWS Lambda 함수를 사용하여 실시간으로 데이터를 처리하고 변환할 수 있음
- 기존 애플리케이션을 수정하지 않고도 데이터를 동적으로 변환하여 제공 가능

## 주요 기능 및 특징
- 실시간 데이터 처리: S3 객체를 요청할 때 AWS Lambda 함수를 사용하여 실시간으로 데이터를 처리하고 변환할 수 있음
- 기존 애플리케이션 호환: 애플리케이션 코드를 수정하지 않고도 데이터를 동적으로 변환하여 제공 가능
- 다양한 사용 사례 지원: 이미지 변환, 데이터 필터링, 포맷 변환 등 다양한 사용 사례에 적용 가능
- 보안 및 접근 제어: IAM 정책을 통해 Lambda 함수와 S3 버킷에 대한 접근을 제어할 수 있음
- 비용 효율성: 사용한 만큼만 비용을 지불하는 종량제 요금제

## 구성
- S3 버킷: 데이터를 저장하는 기본 스토리지
- Lambda 함수: S3 객체를 요청할 때 데이터를 처리하고 변환하는 함수
- S3 Object Lambda 액세스 포인트: S3 객체에 대한 요청을 Lambda 함수로 라우팅하는 액세스 포인트
- IAM 역할: Lambda 함수와 S3 버킷에 대한 접근을 제어하는 IAM 역할

## 작동 방식
1. S3 버킷에 데이터를 저장함
2. Lambda 함수를 작성하여 데이터를 처리하고 변환하는 로직을 구현함
3. S3 Object Lambda 액세스 포인트를 생성하고 Lambda 함수를 연결함
4. 애플리케이션에서 S3 Object Lambda 액세스 포인트를 통해 데이터를 요청함
5. Lambda 함수가 데이터를 실시간으로 처리하고 변환하여 응답함

## 다른 서비스와의 연관성
- AWS Lambda와 통합되어 실시간 데이터 처리 및 변환 기능 제공
- Amazon S3와 통합되어 객체 스토리지와의 원활한 데이터 처리 가능
- AWS Identity and Access Management(IAM)와 연동하여 보안 및 접근 제어 강화

## 사용 사례
- 이미지 변환: S3에 저장된 이미지를 요청 시 실시간으로 크기 조정, 포맷 변환 등 처리
- 데이터 필터링: S3에 저장된 로그 파일을 요청 시 특정 조건에 맞게 필터링하여 제공
- 포맷 변환: S3에 저장된 데이터를 요청 시 CSV에서 JSON으로 변환하여 제공

## 결론
- S3 Object Lambda는 Amazon S3 객체를 요청 시 실시간으로 처리할 수 있는 기능을 제공하는 서비스
- 실시간 데이터 처리, 기존 애플리케이션 호환, 다양한 사용 사례 지원 등의 기능을 제공
- AWS Lambda, Amazon S3, IAM 등과 통합되어 원활한 데이터 처리 및 보안 관리 가능

## 예제 코드
```python
import json

def lambda_handler(event, context):
    # S3 객체 내용 가져오기
    s3_object_content = event['getObjectContext']['inputS3Url']
    
    # 데이터 처리 로직 (예: JSON 포맷 변환)
    processed_data = json.loads(s3_object_content)
    processed_data['new_key'] = 'new_value'
    
    # 처리된 데이터 반환
    return {
        'statusCode': 200,
        'body': json.dumps(processed_data)
    }