# AWS Database Migration Service (AWS DMS)

## 요약
- AWS Database Migration Service(AWS DMS)는 데이터베이스를 AWS로 마이그레이션하거나 AWS 내에서 데이터베이스를 이동할 수 있도록 지원하는 관리형 서비스

## 개요
- AWS DMS는 데이터베이스를 최소한의 다운타임으로 AWS로 마이그레이션하거나 AWS 내에서 데이터베이스를 이동할 수 있도록 지원
- 다양한 데이터베이스 엔진을 지원하며, 데이터 변환 및 복제 기능을 제공

## 주요 기능 및 특징
- 다양한 데이터베이스 지원: Oracle, SQL Server, MySQL, PostgreSQL, MariaDB, Amazon Aurora 등 다양한 데이터베이스 엔진 지원
- 최소한의 다운타임: 데이터베이스를 마이그레이션하는 동안 애플리케이션의 가동 중단을 최소화
- 지속적인 복제: 데이터베이스를 지속적으로 복제하여 소스와 대상 데이터베이스 간의 동기화 유지
- 데이터 변환: AWS Schema Conversion Tool(AWS SCT)을 사용하여 데이터베이스 스키마 및 코드 변환 지원
- 관리형 서비스: 인프라 관리 없이 데이터베이스 마이그레이션 작업을 수행할 수 있는 완전 관리형 서비스
- 보안: 데이터 암호화, 네트워크 격리, IAM 역할을 통한 접근 제어 등 보안 기능 제공

## 구성
- 소스 엔드포인트: 마이그레이션할 원본 데이터베이스
- 대상 엔드포인트: 마이그레이션할 대상 데이터베이스
- 복제 인스턴스: 데이터베이스 마이그레이션 작업을 수행하는 컴퓨팅 리소스
- 마이그레이션 작업: 데이터베이스 마이그레이션을 정의하는 작업

## 작동 방식
1. AWS Management Console에서 DMS 복제 인스턴스를 생성함
2. 소스 및 대상 엔드포인트를 설정함
3. 마이그레이션 작업을 생성하고 소스와 대상 데이터베이스를 연결함
4. 마이그레이션 작업을 실행하여 데이터를 복제하고 변환함
5. 마이그레이션 작업이 완료되면 데이터베이스를 검증하고 애플리케이션을 전환함

## 다른 서비스와의 연관성
- Amazon RDS와 통합되어 데이터베이스 마이그레이션 및 복제 지원
- AWS Schema Conversion Tool(AWS SCT)과 연동하여 데이터베이스 스키마 및 코드 변환 지원
- AWS Identity and Access Management(IAM)와 연동하여 데이터베이스 마이그레이션 작업에 대한 접근 제어 강화

## 사용 사례
- 온프레미스 데이터베이스를 AWS로 마이그레이션할 때
- AWS 내에서 데이터베이스를 이동하거나 업그레이드할 때
- 데이터베이스를 지속적으로 복제하여 고가용성을 유지할 때

## 결론
- AWS Database Migration Service(AWS DMS)는 데이터베이스를 AWS로 마이그레이션하거나 AWS 내에서 데이터베이스를 이동할 수 있도록 지원하는 관리형 서비스
- 다양한 데이터베이스 지원, 최소한의 다운타임, 지속적인 복제, 데이터 변환, 관리형 서비스, 보안 등의 기능을 제공
- Amazon RDS, AWS SCT, IAM 등과 통합되어 유연한 데이터베이스 마이그레이션 및 관리 가능

## 예제 코드
```python
import boto3

# DMS 클라이언트 생성
dms = boto3.client('dms')

# 복제 인스턴스 생성
response = dms.create_replication_instance(
    ReplicationInstanceIdentifier='my-replication-instance',
    AllocatedStorage=100,
    ReplicationInstanceClass='dms.t2.micro',
    VpcSecurityGroupIds=['sg-12345678'],
    AvailabilityZone='us-west-2a',
    MultiAZ=False,
    EngineVersion='3.4.4'
)

print(response['ReplicationInstance']['ReplicationInstanceArn'])