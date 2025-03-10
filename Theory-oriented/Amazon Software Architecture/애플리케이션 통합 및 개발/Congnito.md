# Amazon Cognito

## 개요
- Amazon Cognito는 AWS의 사용자 인증, 권한 부여 및 사용자 관리 서비스
- 웹 및 모바일 애플리케이션에 사용자 인증 및 접근 제어 기능을 쉽게 통합할 수 있도록 지원

## 주요 기능 및 특징
- **사용자 풀(User Pool)**: 사용자 등록, 로그인, 계정 복구 등 사용자 관리 기능 제공
- **연동 ID 제공자**: Facebook, Google, Amazon 등 외부 ID 제공자와 연동 가능
- **호스팅 UI**: 사용자 인증을 위한 호스팅된 웹 UI 제공
- **다중 인증(MFA)**: 다중 인증을 통해 보안 강화
- **사용자 속성**: 사용자 프로필 정보를 저장하고 관리
- **보안**: 데이터 암호화, 액세스 제어, AWS IAM과의 통합을 통해 보안 강화

## Cognito 2가지 컴포넌트
### User Pool
- 로그인 관리
- User Pool은 애플리케이션의 사용자 인증과 관리(회원가입, 로그인)를 위한 컴포넌트
- 사용자 가입, 로그인, 비밀번호 재설정 등의 기본 기능을 제공
- User Pool에서 자체적으로 관리하는 사용자 뿐만 아니라, 외부 ID Provider(예: 구글)와 연동된 사용자 인증도 지원

- 사용자 인증 방식
  - User Pool이 제공하는 방식: 로그인을 위한 커스터마이징 가능한 Web UI를 제공
  - 외부 ID Provider와 연동하는 인증 방식: 소셜 로그인(Facebook, Google, Apple, Amazon)
- 인증이 완료되면 토큰(*)이 발급되며, 애플리케이션 측에서 사용자의 식별이나 Amazon API Gateway에 대한 접근 제어 등에 사용될 수 있음
- 또한, ID Pool과 결합하여 AWS의 다양한 서비스에 접근할 수 있는 일시적인 인증 정보를 얻을 수도 있음
- 발급되는 토큰은 JWT로, 인증 정보를 JSON 형식으로 저장함
- 다단계 인증(MFA): 보안 강화를 위해 MFA를 활성화하면, 로그인 시 추가적인 인증 단계를 요구할 수 있음
- 사용자 속성 관리: 사용자 이름, 이메일, 전화번호 등 사용자 속성을 관리할 수 있음

### Identity Pool
- 로그인 후 AWS 서비스 접근 관리
- ID Pool은 로그인 인증된 사용자에 대한 허가를 수행
- ID Pool은 사용자가 로그인하면 AWS 서비스에 액세스할 수 있는 임시 자격 증명을 발급
- 이를 통해 사용자는 S3와 DynamoDB 같은 AWS 서비스에 접근 가능
- 인증 시 속성 정보에 따라 사전에 정의된 IAM Role이 할당되며, 이 IAM Role에 부여된 권한에 따라 AWS의 다양한 서비스에 접근할 수 있는 일시적인 임시 자격 증명이 발급
- ID Pool 자체에도 외부 ID Provider와 연동된 인증 기능이 구현되어 있어 User Pool을 사용하지 않고 ID Pool 만으로 인증을 구현할 수 있음


## 다른 서비스와의 연관성
### Amazon API Gateway
- **API 보호**: Cognito를 사용하여 API Gateway에서 API 요청을 인증 및 권한 부여
- **사용자 인증**: 사용자 인증을 통해 API 접근 제어

### AWS Lambda
- **트리거**: Cognito 이벤트(예: 사용자 등록, 로그인 등)를 트리거로 Lambda 함수를 실행하여 후속 작업 수행
- **백엔드 로직**: 사용자 인증 후 백엔드 로직을 처리

### Amazon S3
- **파일 접근 제어**: Cognito를 사용하여 S3 버킷에 대한 사용자 접근 제어
- **보안**: 인증된 사용자만 S3 버킷에 접근 가능

### Amazon CloudWatch
- **모니터링**: Cognito 사용자 활동 및 인증 이벤트를 CloudWatch로 모니터링
- **로그 분석**: 사용자 인증 로그를 분석하여 보안 강화

## 사용 사례
- **사용자 인증 및 관리**: 웹 및 모바일 애플리케이션에서 사용자 인증 및 관리 기능 구현
- **소셜 로그인**: Facebook, Google, Amazon 등 소셜 ID 제공자를 통한 로그인 기능 제공
- **다중 인증(MFA)**: 보안이 중요한 애플리케이션에서 다중 인증을 통해 보안 강화
- **API 접근 제어**: API Gateway와 통합하여 API 접근 제어 및 보호

## 요약
- Amazon Cognito는 AWS의 사용자 인증, 권한 부여 및 사용자 관리 서비스로, 웹 및 모바일 애플리케이션에 쉽게 통합 가능
- API Gateway, Lambda, S3, CloudWatch 등 다양한 AWS 서비스와 연동하여 사용자 인증, 접근 제어, 모니터링 등 다양한 사용 사례에 활용 가능
- 사용자 풀, 연동 ID 제공자, 호스팅 UI, 다중 인증, 사용자 속성, 보안 등의 주요 기능을 제공하여 사용자 인증 및 관리를 효율적으로 수행할 수 있음



## References
- https://jibinary.tistory.com/194#2.%20ID%20%ED%92%80%20(Identity%20Pool)%3A%20%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%ED%9B%84%EC%97%90%20AWS%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%A0%91%EA%B7%BC%20%EA%B4%80%EB%A6%AC-1