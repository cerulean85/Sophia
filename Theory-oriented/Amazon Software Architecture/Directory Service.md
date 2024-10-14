# AWS Directory Service에 대해 알려줘

## 요약
- AWS Directory Service는 AWS 클라우드에서 디렉터리 기반 워크로드를 쉽게 설정하고 관리할 수 있도록 지원하는 서비스

## 개요
- AWS Directory Service는 Microsoft Active Directory(AD)와 호환되는 디렉터리 서비스를 제공
- 온프레미스 AD와의 통합을 통해 하이브리드 클라우드 환경을 지원

## 주요 기능 및 특징
- Managed Microsoft AD: AWS에서 완전 관리형 Microsoft Active Directory 제공
- AD Connector: 온프레미스 AD와 AWS 리소스를 연결하는 프록시 서비스
- Simple AD: 기본적인 AD 기능을 제공하는 저비용 디렉터리 서비스
- 보안 및 규정 준수: AWS의 보안 및 규정 준수 기능과 통합

## 구성
- Managed Microsoft AD: AWS에서 관리되는 AD 도메인 컨트롤러
- AD Connector: 온프레미스 AD와 AWS 리소스를 연결하는 프록시
- Simple AD: 기본적인 AD 기능을 제공하는 저비용 디렉터리

## 작동 방식
1. AWS Management Console에서 AWS Directory Service 생성
2. 디렉터리 유형 선택 (Managed Microsoft AD, AD Connector, Simple AD)
3. 디렉터리 설정 구성 (도메인 이름, VPC, 서브넷 등)
4. 디렉터리 생성 완료 후, AWS 리소스와 통합

## 다른 서비스와의 연관성
- Amazon EC2: EC2 인스턴스를 도메인에 가입시켜 중앙 관리 가능
- Amazon RDS: RDS 인스턴스에 대한 Windows 인증 제공
- Amazon WorkSpaces: WorkSpaces 환경에서 AD 사용자 인증 제공

## 사용 사례
- 온프레미스 AD와 AWS 리소스 간의 통합
- 클라우드 기반 애플리케이션의 사용자 인증 및 권한 관리
- 하이브리드 클라우드 환경에서의 중앙 집중식 디렉터리 관리

## 결론
- AWS Directory Service는 클라우드 및 하이브리드 환경에서 디렉터리 기반 워크로드를 쉽게 설정하고 관리할 수 있는 강력한 도구

## 예제 코드
```bash
# AWS Directory Service 생성 예제 (AWS CLI 사용)
aws ds create-directory \
    --name example.com \
    --short-name EXAMPLE \
    --password Password1234 \
    --description "Example Directory" \
    --size Small \
    --vpc-settings SubnetIds=subnet-12345678,subnet-87654321


---

# AWS Directory Service
- 마이크로소프트 Active Directory나 LDAP(Lightweight Directory Access Protocol), 혹은 클라우드에서 사용한다고 알려진 애플리케이션을 이미 가진 고객에게 다양한 디렉토리 선택을 제공

- 사용자, 그룹, 접근 관리 위해 디렉토리를 필요로 하는 개발자들에게 동일한 선택 제공

## Active Directory
- 회사 직원들의 계정 정보, 컴퓨터 정보, 사내 강제 정책에 대한 정보를 저장하는 DB의 일종
- 암호화되어 있어 메모장이나 텍스트 에디터로는 열 수 없음

## References
- [What is AWS Directory Service?](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)