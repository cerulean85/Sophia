# AWS DataSync

- DataSync 에이전트를 통해 온프레미스 혹은 AWS 클라우드의 스토리지 서버(혹은 스토리지 서비스)에서 AWS의 또 다른 스토리지 서비스로 데이터를 동기화하는 서비스

- 온프레미스의 데이터를 AWS 스토리지 서비스로 복사

![alt text](../images/cloud/datasync_1.png)

- AWS EFS에서 또다른 AWS EFS로 데이터 복사

![alt text](../images/cloud/datasync_2.png)

- DataSync만을 위한 별도의 에이전트를 온프레미스 환경이나 AWS 환경에 배포해야 함

- 소스 데이터는 DataSync 에이전트를 통해 AWS 스토리지로 동기화

- 온프레미스에 DataSync 에이전트를 배포하기 위해 DataSync에서는 ESXi, KVM, Hyper-V 방식의 하이퍼바이저에서 구동될 DataSync 에이전트 이미지를 제공하고 있음

- AWS 환경에 DataSync 에이전트를 배포하기 위해 DataSync 에이전트 전용 AMI 이미지로 EC2 인스턴스를 생성하도록 안내하고 있음

- AWS 문서에 따르면 온프레미스의 데이터를 DataSync를 통해 동기화하기 위해서는 온프레미스-AWS 인프라로의 진입 거기를 최소화해야 AWS에서 개발한 가속 프로토콜을 이용하여 최대한의 속도를 낼 수 있기에 DataSync 에이전트를 온프레미스 소스 스토리지와 근접한 곳에 배포할 것을 권장하고 있음

## 참고사이트
- [AWS DataSync 개념 및 간단한 사용 예시](https://engmisankim.tistory.com/42)

