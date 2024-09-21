# S3 Cross-Region Replication

## 요약
- S3 Cross-Region Replication(CRR)은 Amazon S3 버킷의 객체를 다른 AWS 리전의 버킷으로 자동으로 복제하는 기능

## 개요
- 데이터의 가용성, 내구성, 지연 시간을 개선하기 위해 사용
- 규정 준수 및 재해 복구를 위한 데이터 복제

## 주요 기능 및 특징
- **자동 복제**: S3 버킷의 객체를 다른 리전의 버킷으로 자동 복제
- **다중 리전 지원**: 여러 AWS 리전 간 데이터 복제 가능
- **보안**: 전송 중 데이터 암호화 및 IAM 역할 기반 접근 제어
- **유연한 설정**: 전체 버킷 또는 특정 객체에 대해 복제 설정 가능

## 구성
- **원본 버킷**: 복제를 시작할 S3 버킷
- **대상 버킷**: 복제된 객체를 저장할 S3 버킷
- **복제 규칙**: 복제할 객체 및 조건 설정
- **IAM 역할**: 복제 작업을 수행할 권한 부여

## 작동 방식
1. 원본 버킷과 대상 버킷 설정
2. 복제 규칙 생성 및 적용
3. IAM 역할 설정 및 권한 부여
4. S3가 원본 버킷의 객체를 대상 버킷으로 자동 복제

## 다른 서비스와의 연관성
- **Amazon S3**: S3 버킷 간 데이터 복제
- **AWS IAM**: 복제 작업을 위한 권한 관리
- **AWS CloudTrail**: 복제 작업의 로깅 및 모니터링

## 사용 사례
- **재해 복구**: 다른 리전에 데이터 복제하여 재해 복구 계획 수립
- **규정 준수**: 데이터 보존 및 규정 준수를 위해 다중 리전에 데이터 저장
- **지리적 분산**: 데이터를 여러 리전에 분산하여 지리적 장애에 대비
- **지연 시간 감소**: 사용자와 가까운 리전에 데이터 복제하여 지연 시간 감소

## 결론
- S3 Cross-Region Replication은 데이터의 가용성, 내구성, 지연 시간을 개선하고 규정 준수 및 재해 복구를 지원하는 강력한 기능
- 자동 복제, 다중 리전 지원, 보안 및 유연한 설정을 제공

### 예제 코드
```python
import boto3

# S3 클라이언트 생성
s3 = boto3.client('s3')

# 복제 규칙 생성
replication_configuration = {
    'Role': 'arn:aws:iam::account-id:role/replication-role',
    'Rules': [
        {
            'ID': 'ReplicationRule1',
            'Status': 'Enabled',
            'Prefix': '',
            'Destination': {
                'Bucket': 'arn:aws:s3:::destination-bucket-name'
            }
        }
    ]
}

# 복제 설정 적용
response = s3.put_bucket_replication(
    Bucket='source-bucket-name',
    ReplicationConfiguration=replication_configuration
)

print(response)
```