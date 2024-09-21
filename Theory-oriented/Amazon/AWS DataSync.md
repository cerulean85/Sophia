# AWS DataSync

- AWS DataSync는 온프레미스 스토리지와 AWS 스토리지 서비스 간의 데이터 전송을 자동화하고 가속화하는 서비스
- 대규모 데이터 이동을 간편하고 효율적으로 수행할 수 있음

## 주요 기능 및 특징
- 데이터 전송 자동화
  - 데이터 전송 작업을 자동화하여 수동 작업을 줄일 수 있음
  - 정기적인 데이터 동기화 작업을 예약할 수 있음

- 전송 속도 가속화
  - 네트워크 최적화 기술을 사용하여 데이터 전송 속도를 가속화함
  - 대규모 데이터 세트를 빠르게 전송할 수 있음

- 다양한 소스 및 대상 지원
  - 온프레미스 스토리지, Amazon S3, Amazon EFS, Amazon FSx for Windows File Server 등 다양한 소스와 대상을 지원함
  - NFS, SMB 프로토콜을 통한 데이터 전송을 지원함

- 데이터 무결성 및 보안
  - 전송 중 데이터 무결성을 검증하여 데이터 손상을 방지함
  - 전송 중 및 전송 후 데이터 암호화를 지원함

## 구성
- DataSync 에이전트 설치
- 데이터 전송 작업 생성
- 소스 및 대상 스토리지 설정
- 전송 작업 실행 및 모니터링

## 작동 방식
1. DataSync 에이전트를 온프레미스 환경에 설치함
2. AWS Management Console, AWS CLI, 또는 AWS SDK를 사용하여 데이터 전송 작업을 생성함
3. 소스 및 대상 스토리지를 설정하고 전송 작업을 구성함
4. 전송 작업을 실행하여 데이터를 전송함
5. 전송 작업의 상태를 모니터링하고 필요한 경우 조정함

## 다른 서비스와의 연관성
- Amazon S3: 데이터 전송 대상 또는 소스로 사용
- Amazon EFS: 데이터 전송 대상 또는 소스로 사용
- Amazon FSx: 데이터 전송 대상 또는 소스로 사용
- AWS CloudWatch: 전송 작업의 모니터링 및 로깅

## 사용 사례
- 온프레미스 데이터 센터에서 AWS로 데이터 마이그레이션
  - 예: 기존 데이터 센터의 데이터를 Amazon S3로 이전
- 정기적인 데이터 백업 및 동기화
  - 예: 온프레미스 파일 서버의 데이터를 Amazon EFS로 정기적으로 동기화
- 대규모 데이터 세트 전송
  - 예: 연구 데이터, 로그 파일 등의 대규모 데이터 세트를 AWS로 전송

## 결론
- AWS DataSync는 온프레미스 스토리지와 AWS 스토리지 서비스 간의 데이터 전송을 자동화하고 가속화하는 데 유용한 서비스
- 다양한 소스와 대상을 지원하며, 데이터 무결성과 보안을 보장함

## 예제 코드
```json
{
  "SourceLocationArn": "arn:aws:datasync:us-west-2:123456789012:location/loc-1234567890abcdef0",
  "DestinationLocationArn": "arn:aws:datasync:us-west-2:123456789012:location/loc-0987654321fedcba0",
  "CloudWatchLogGroupArn": "arn:aws:logs:us-west-2:123456789012:log-group:/aws/datasync/log-group",
  "Name": "MyDataSyncTask",
  "Options": {
    "VerifyMode": "ONLY_FILES_TRANSFERRED",
    "OverwriteMode": "ALWAYS",
    "Atime": "BEST_EFFORT",
    "Mtime": "PRESERVE",
    "Uid": "INT_VALUE",
    "Gid": "INT_VALUE",
    "PreserveDeletedFiles": "PRESERVE",
    "PreserveDevices": "NONE",
    "PosixPermissions": "PRESERVE",
    "BytesPerSecond": -1,
    "TaskQueueing": "ENABLED",
    "LogLevel": "TRANSFER"
  }
}