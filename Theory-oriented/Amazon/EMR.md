# Amazon EMR

## 요약
- 대규모 데이터 처리 및 분석을 위한 클라우드 기반 서비스

## 개요
- Apache Hadoop, Apache Spark 등 오픈 소스 빅 데이터 프레임워크 사용
- 데이터 과학, 데이터 엔지니어링, 데이터 분석 작업 수행

## 주요 기능 및 특징
- 확장성: 클러스터 크기 동적 조정
- 유연성: 다양한 오픈 소스 도구와 통합
- 비용 효율성: 사용한 만큼만 비용 지불
- 보안: 데이터 암호화, 네트워크 격리 등 보안 기능 제공

## 구성
- 클러스터: 여러 개의 EC2 인스턴스로 구성
- 마스터 노드: 클러스터 관리 및 작업 조정
- 코어 노드: 데이터 저장 및 처리 작업 수행
- 태스크 노드: 추가적인 데이터 처리 작업 수행

## 작동 방식
1. 클러스터 생성
2. 데이터 로드
3. 작업 제출
4. 데이터 처리
5. 결과 저장
6. 클러스터 종료

## 다른 서비스와의 연관성
- Amazon S3: 데이터 저장 및 로드
- AWS Lambda: 데이터 처리 파이프라인의 일부
- Amazon RDS: 처리된 데이터 저장
- AWS Glue: 데이터 카탈로그 및 ETL 작업

## 사용 사례
- 로그 분석: 대규모 로그 데이터 분석
- 데이터 웨어하우징: 대규모 데이터 웨어하우스 구축 및 관리
- 기계 학습: 대규모 데이터 세트를 사용한 기계 학습 모델 훈련

## 결론
- 대규모 데이터 처리 및 분석을 위한 강력하고 유연한 클라우드 서비스
- 다양한 오픈 소스 도구와 통합하여 데이터 과학, 데이터 엔지니어링, 데이터 분석 작업 효율적으로 수행

## 예제 코드
```python
import boto3

# EMR 클라이언트 생성
emr_client = boto3.client('emr', region_name='us-west-2')

# 클러스터 생성
response = emr_client.run_job_flow(
    Name='MyEMRCluster',
    Instances={
        'InstanceGroups': [
            {
                'Name': 'Master nodes',
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 1,
            },
            {
                'Name': 'Core nodes',
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 2,
            }
        ],
        'Ec2KeyName': 'my-key-pair',
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
    },
    Applications=[
        {'Name': 'Hadoop'},
        {'Name': 'Spark'}
    ],
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
    VisibleToAllUsers=True,
    LogUri='s3://my-emr-logs/'
)

print(f'Created cluster with ID: {response["JobFlowId"]}')