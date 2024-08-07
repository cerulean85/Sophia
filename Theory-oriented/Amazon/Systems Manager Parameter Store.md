# AWS System Manager
- AWS 애플리케이션 및 리소스를 위한 운영 허브이자, 안전한 운영이 대규모로 활성화되는 하이브리드 및 멀티클라우드 환경을 위한 안전한 엔드 투 엔드 관리 솔루션

## 작동 방식




# AWS Systems Manager Parameter Store

- 애플리케이션의 구성 데이터 및 비밀을 안전하게 저장하고 관리하는 데 도움이 됨

- 이 정보를 중앙에서 관리하고 액세스할 수 있으므로 애플리케이션 구성을 보다 쉽게 유지 관리하고 업데이트할 수 있음

- Parameter Store를 사용하면 키-값 쌍을 매개변수로 저장할 수 있음
- 여기서 값은 단순한 문자열이거나 암호화된 암호와 같은 보다 복잡한 데이터 유형일 수 있음

- 이러한 매개벼수는 경로와 같은 구조로 계층적으로 구성할 수 있으므로 대규모 매개변수 세트를 구성하고 관리하는 것이 편리

- Parameter Store 사용의 주요 이점 중 하나는 다른 AWS 서비스와의 통합
  - EC2 인스턴스, Lambda 함수 또는 Elastic Beanstalk 환경과 같은 AWS 리소스에 저장된 파라미터를 참조할 수 있음
  - 이렇게 하면 애플리케이션 코드에서 직접 값을 하드코딩할 필요 없이 리소스를 동적으로 구성하고 업데이트 할 수 있음

- 안전한 저장 및 액세스 제어를 위한 기능도 제공
  - AWS Key Management Service를 사용하여 민감한 파라미터를 암호화하고 세분화된 액세스 정책을 정의하여 파라미터를 검색하거나 수정할 수 있는 사람을 제어할 수 있음

- 전반적으로 애플리케이션의 구성 데이터 및 암호 관리를 간소화하여 매개변수를 중앙 집중화하고 보호하는 동시에 다른 AWS 서비스와의 간편한 통합을 제공함




## 참고사이트
- [파라미터 스토어 (AWS Systems Manager Parameter Store)](https://velog.io/@el0902/%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-%EC%8A%A4%ED%86%A0%EC%96%B4-AWS-Systems-Manager-Parameter-Store)

- [AWS Systems Manager (SSM)란?](https://seongduck.tistory.com/236)