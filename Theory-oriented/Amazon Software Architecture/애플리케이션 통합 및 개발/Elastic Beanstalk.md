# AWS Elastic Beanstalk

- 웹 애플리케이션과 서비스를 배포하고 관리하기 위한 완전 관리형 서비스
- 애플리케이션 코드를 업로드하기만 하면 자동으로 인프라를 프로비저닝하고, 로드 밸런싱, 확장, 모니터링 등을 설정할 수 있음
- 이를 통해 인프라 관리에 신경 쓰지 않고 애플리케이션 개발에 집중할 수 있음

# 주요 기능
- 자동 인프라 프로비저닝
    - 애플리케이션 코드를 업로드하면 Elascit Beanstalk가 자동으로 필요한 인프라(EC2 인스턴스, 로드 밸런서, Auto Scaling 그룹 등)를 프로비저닝
- 자동 확장
    - 애플리케이션의 트래픽에 따라 자동으로 인스턴스를 추가하거나 제거하여 확장성을 제공
    - Auto Scaling을 통해 애플리케이션의 부하에 따라 동적으로 리소스를 조절할 수 있음
- 다양한 플랫폼 지원
    - Java, .NET, Node.js, Python, Ruby, Go, Docker 등 다양한 언어와 플랫폼을 지원
    - 각 플랫폼에 맞는 환경을 자동으로 설정하고 관리
- 모니터링 및 로깅
    - Amazon CloudWatch와 통합되어 애플리케이션의 상태와 성능을 모니터링할 수 있음
    - 로그 파일을 쉽게 액세스하고 분석할 수 있음
- 환경 구성 및 관리
    - Elastic Beanstalk 콘솔, CLI, API를 통해 환경을 구성하고 관리할 수 있음
    - 환경 설정을 쉽게 변경하고, 새로운 버전의 애플리케이션을 배포할 수 있음
- 보안
    - IAM 역할과 정책을 사용하여 애플리케이션의 보안을 강화할 수 있음
    - VPC와 통합하여 네트워크 보안을 설정할 수 있음

# 사용 사례
- 웹 애플리케이션 배포
    - 웹 애플리케이션을 빠르고 쉽게 배포하고 관리할 수 있음
    - 예: 전자상거래 사이트, 블로그, 포털 사이트 등
- API 서비스
    - RESTful API 서비스를 배포하고 관리할 수 있음
    - 예: 모바일 애플리케이션 백엔드, IoT 서비스 등
- 마이크로서비스
    - 마이크로서비스 아키텍처를 사용하여 애플리케이션을 배포하고 관리할 수 있음
    - 각 마이크로서비스를 독립적으로 배포하고 확장할 수 있음

---


- Elastic Beanstalk를 이용하면 애플리케이션 운영에 필요한 인프라에 대한 학습 없이 AWS 클라우드에서 애플리케이션을 관리하고 빠르게 배포할 수 있음
- Elastic Beanstalk는 선택이나 통제 제한 없이 관리 복잡성을 줄임
- 애플리케이션을 간단히 업로드하여고 Elastic Beanstalk를 이용하여 자등으로 Capacity 프로비저닝의 상세한 부분과 로드밸런싱, 스케일링, 애플리케이션 Health 모니터링을 다룰 수 있음

- Elastic Beanstalk는 Go, Java, .NET, Node.js, PHP, Python, 그리고 Ruby로 개발된 애플리케이션을 지원함
- 애플리케이션을 배포하면 Elastic Beanstalk는 선택된 지원 플랫폼 버전을 빌드하고, 애플리케이션을 동작시키기 위해 Amazon EC2 인스턴스 같은 한 개 이상의 AWS 리소스를 비저닝할 수 있음

- Elastic Beanstalk 콘솔, AWS CLI, 혹은 eb, Elastic Beanstalk를 위해 전문적으로 설계된 고수준 CLI 등을 이용하여 Elastic Beanstalk과 상호작용할 수 있음

To learn more about how to deploy a sample web application using Elastic Beanstalk, see Getting Started with AWS: Deploying a Web App.

You can also perform most deployment tasks, such as changing the size of your fleet of Amazon EC2 instances or monitoring your application, directly from the Elastic Beanstalk web interface (console).

To use Elastic Beanstalk, you create an application, upload an application version in the form of an application source bundle (for example, a Java .war file) to Elastic Beanstalk, and then provide some information about the application. Elastic Beanstalk automatically launches an environment and creates and configures the AWS resources needed to run your code. After your environment is launched, you can then manage your environment and deploy new application versions. The following diagram illustrates the workflow of Elastic Beanstalk.

![alt text](../../images/cloud/beanstalk.png)

After you create and deploy your application, information about the application—including metrics, events, and environment status—is available through the Elastic Beanstalk console, APIs, or Command Line Interfaces, including the unified AWS CLI.


## References
- [What is AWS Elastic Beanstalk?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)