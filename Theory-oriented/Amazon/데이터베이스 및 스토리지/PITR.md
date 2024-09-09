# Point-in-Time Recovery (PITR)

## 요약
- Point-in-Time Recovery(PITR)는 Amazon DynamoDB 테이블의 데이터를 특정 시점으로 복원할 수 있는 기능

## 개요
- PITR은 데이터 손실이나 손상을 방지하기 위해 DynamoDB 테이블의 변경 사항을 지속적으로 백업
- 사용자는 특정 시점으로 데이터를 복원할 수 있어 데이터 복구가 용이

## 주요 기능 및 특징
- **자동 백업**: DynamoDB 테이블의 모든 변경 사항을 자동으로 백업
- **복원 가능 시점**: 최대 35일 전까지의 데이터 복원 가능
- **간편한 복구**: AWS Management Console, AWS CLI, AWS SDK를 통해 간편하게 복구 가능
- **비용 효율성**: 사용한 스토리지와 복구 요청에 따라 비용 부과

## 구성
- **PITR 활성화**: DynamoDB 테이블에서 PITR 기능 활성화
- **백업 저장**: 변경 사항을 지속적으로 백업하여 저장
- **복원 요청**: 특정 시점으로 데이터 복원 요청

## 작동 방식
1. DynamoDB 테이블에서 PITR 기능 활성화
2. DynamoDB가 테이블의 모든 변경 사항을 자동으로 백업
3. 필요 시 특정 시점으로 데이터 복원 요청
4. AWS Management Console, AWS CLI, AWS SDK를 통해 복구 수행

## 다른 서비스와의 연관성
- **Amazon S3**: 백업 데이터를 S3에 저장하여 추가적인 보안 및 복구 옵션 제공
- **AWS Backup**: AWS Backup을 통해 다른 AWS 서비스와 통합된 백업 및 복구 관리

## 사용 사례
- **데이터 손실 방지**: 실수로 인한 데이터 삭제나 손상 시 특정 시점으로 복구
- **애플리케이션 테스트**: 특정 시점의 데이터를 복원하여 테스트 환경 구성
- **규정 준수**: 데이터 보존 및 복구 요구 사항을 충족

## 결론
- Point-in-Time Recovery(PITR)는 Amazon DynamoDB 테이블의 데이터를 특정 시점으로 복원할 수 있는 강력한 기능
- 자동 백업, 간편한 복구, 비용 효율성을 제공하여 데이터 손실 방지 및 복구에 유용

### 예제 코드
```python
import boto3

# DynamoDB 클라이언트 생성
dynamodb = boto3.client('dynamodb')

# PITR 활성화
response = dynamodb.update_continuous_backups(
    TableName='YourDynamoDBTable',
    PointInTimeRecoverySpecification={
        'PointInTimeRecoveryEnabled': True
    }
)

print(response)

# 특정 시점으로 복원
response = dynamodb.restore_table_to_point_in_time(
    SourceTableName='YourDynamoDBTable',
    TargetTableName='RestoredDynamoDBTable',
    RestoreDateTime='2023-10-01T12:00:00Z'
)

print(response)