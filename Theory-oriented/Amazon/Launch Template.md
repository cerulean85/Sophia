# Launch Template
- Launch Configuration과 비슷하며, 인스턴스 설정 정보를 구체화할 수 있음
- AMI의 ID, 인스턴스 유형, 키 패어, 보안그룹, EC2 인스턴스 런치에 사용하는 여러 파라미터를 포함할 수 있음
- Launch Template을 정의한다는 것은 하나의 Lauhch Template에 대한 여러 가지 버전을 가질 수 있음을 의미
- 전체 파라미터 세트의 하위 세트를 만들 수 있음
- 동일한 Launch Template의 다른 버전을 만들 수 있음


## Referecnes
- [Auto Scaling launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html)