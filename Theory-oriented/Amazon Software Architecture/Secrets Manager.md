
# AWS Secrets Manager
- 하드코딩된 자격증명을 런타임 콜로 대체 가능
- 필요할 때 Secrets Manager에서 자격증명 검색 가능
- 비밀 정보를 자동화된 로테이션 스케쥴을 설정 가능
- 자격증명이 더이상 애플리케이션에 저장되지 않고, 자격증명 로테이팅이 애플리케이션의 업데이트와 애플리케이션 클라이언트에게 변화를 배포하지 않게 함

- AWS에서 제공하는 비밀 관리 서비스로, 자체 인프라 운영에 대한 선행 투자 및 지속적인 유지 관리 비용 없이 애플리케이션, 서비스 및 IT 리소스에 대한 액세스를 보호할 수 있음

- 애플리케이션 소스코드에 자격증명 하드 코딩할 필요가 없으므로 보안 노출 개선

- Secrets Manager에 자격증명을 저장하는 것은 애플리케이션이나 컴포넌트를 검사할 수 있는 사람에 의한 손상 가능성을 피하도록 도움

  - AWS Credentials
  - Encryption keys
  - SSH keys
  - Private keys and certificates

- 런타임 호출로 대체하여 필요할 때 자격 증명을 동적으로 검색할 수 있음



- 데이터베이스 자격 증명, 온프레미스 리소스 자격 증명, SaaS 애플리케이션 암호 및 SSH(Secure Shell) 키와 같은 중요한 정보를 관리하고 보호하는 데 도움이 됨

- Auto Rotation 지원

## 주요 기능
- 비밀 보안 및 관리
- 세분화된 액세스 제어
- 자동화된 암호 교체
- 감시 및 모니터링
- 다른 AWS 서비스와의 통합
- 교차 계정 액세스
- 프로그래밍 방식으로 암호에 액세스

## 유형
- 다양한 유형의 암호 값 저장 가능
  - 데이터베이스 자격 증명
  - API 키
  - OAuth 토큰
  - SSH 키
  - TLS/SSL 인증서 및 개인키
  - 일반 텍스트 또는 JSON 형식의 기타 민감한 정보

## 참고사이트
- [AWS Secrets Manager란?(OAuth, SSO)](https://somaz.tistory.com/183)
- [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)