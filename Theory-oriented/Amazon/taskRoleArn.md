# taskRoleArn
- AWS Elastic Container Service (ECS)에서 사용되는 IAM 역할을 지정하는 속성
- 이 역할은 ECS 작업(Task)이 AWS 리소스에 접근할 수 있도록 권한을 부여
- taskRoleArn을 사용하면 ECS 작업이 실행되는 동안 필요한 권한을 부여받아, 예를 들어 Amazon S3 버킷에 데이터를 읽고 쓰거나, DynamoDB 테이블에 접근할 수 있dma

# 주요 개념
- IAM 역할
    - AWS 리소스에 대한 접근 권한을 정의하는 역할
    - 역할에는 하나 이상의 정책이 연결되어 있으며, 이 정책은 역할을 사용하는 엔터티가 어떤 작업을 수행할 수 있는지 정의
- ECS 작업(Task)
    - ECS 클러스터에서 실행되는 컨테이너 인스턴스
    - 작업 정의(Task Definition)에 따라 컨테이너를 실행

- taskRoleArn
    - 작업 정의(Task Definition)에서 지정하는 속성
    - ECS 작업이 사용할 IAM 역할의 ARN(Amazon Resource Name)을 나타냄

# 사용 예시
- IAM 역할 생성
    - IAM 콘솔에서 새로운 역할을 생성하고, 필요한 권한을 부여
    - 예를 들어, S3 버킷에 접근할 수 있는 권한을 부여할 수 있음
    - 역할을 생성한 후, 역할의 ARN을 복사함

- 작업 정의(Task Definition)에서 taskRoleArn 설정
    - ECS 작업 정의를 생성하거나 업데이트할 때, taskRoleArn 속성에 IAM 역할의 ARN을 지정
    - 예시 (JSON 형식의 작업 정의):

    ```javascript
    {
    "family": "my-task-family",
    "containerDefinitions": [
        {
        "name": "my-container",
        "image": "my-container-image",
        "memory": 512,
        "cpu": 256,
        "essential": true
        }
    ],
    "taskRoleArn": "arn:aws:iam::123456789012:role/my-ecs-task-role"
    }
    ```