# Amazon RDS Custom

- Amazon RDS Custom은 Amazon RDS의 관리형 기능과 Amazon EC2의 운영 체제 접근 권한을 결합한 서비스
- 사용자 정의 설정과 스크립트를 실행할 수 있는 유연성을 제공함

## 주요 기능 및 특징
- **운영 체제 접근 가능**: 기본 운영 체제에 대한 접근 권한을 제공하여 사용자 정의 설정과 스크립트를 실행할 수 있음
- **관리형 서비스**: 백업, 패치, 모니터링 등의 관리 작업이 자동화됨
- **유연성**: 사용자 정의 애플리케이션, 타사 소프트웨어 설치 및 구성 가능
- **고가용성 및 DR**: 읽기 복제본을 다른 AWS 리전에 생성하여 재해 복구 설정 가능

## Amazon RDS와의 차이점
- **운영 체제 접근**
  - **Amazon RDS**: 기본 운영 체제에 대한 접근 권한이 없음
  - **Amazon RDS Custom**: 기본 운영 체제에 대한 접근 권한이 있음

- **유연성**
  - **Amazon RDS**: 표준화된 관리형 서비스로 사용자 정의 설정이 제한적
  - **Amazon RDS Custom**: 사용자 정의 설정과 스크립트 실행 가능

- **사용 사례**
  - **Amazon RDS**: 표준화된 관리형 데이터베이스 서비스가 필요한 경우
  - **Amazon RDS Custom**: 사용자 정의 설정이 필요한 복잡한 애플리케이션 및 데이터베이스 환경

## 사용 사례
- **복잡한 애플리케이션**: 사용자 정의 설정이 필요한 복잡한 애플리케이션
- **타사 소프트웨어**: 타사 소프트웨어 설치 및 구성이 필요한 경우
- **운영 체제 접근 필요**: 기본 운영 체제에 접근하여 관리 작업을 수행해야 하는 경우

## 결론
- Amazon RDS Custom은 Amazon RDS의 관리형 기능과 EC2의 운영 체제 접근 권한을 결합하여 유연성과 관리 편의성을 제공함
- 운영 체제 접근이 필요한 복잡한 애플리케이션 및 데이터베이스 환경에 적합

## 예제
### Amazon RDS Custom for Oracle 설정 예제
```json
{
  "DBInstanceIdentifier": "my-custom-db-instance",
  "DBInstanceClass": "db.m5.large",
  "Engine": "custom-oracle-ee",
  "MasterUsername": "admin",
  "MasterUserPassword": "password",
  "AllocatedStorage": 100,
  "DBSubnetGroupName": "my-subnet-group",
  "VpcSecurityGroupIds": ["sg-12345678"],
  "BackupRetentionPeriod": 7,
  "MultiAZ": true,
  "StorageType": "gp2"
}
```