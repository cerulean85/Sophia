# AWS Identity and Access Management

- 계정 관리자가 AWS 리소스로 접근을 통제하는 권한 정책
- 리소스는 고유한 ARN(Amazon Resource Name)을 갖ㅁ
- IAM 권한 정책 중 ```Resource```라는 요소에 ARN을 기술하여 리소스의 접근을 통제
- 리소스는 제공되는 명령어(Operations) 세트로 동작 제어 가능
- ```Action```: 명령어를 사용할 수 있는 사람을 통제하는 IAM 정책
- ```Condition Key```: 어떤 활동의 더 세분화된 통제를 위한 질의키
  - IAM 정책 중 ```Condition``` 요소에 컨디션 키를 참조하여 필요한 추가 환경을 기술할 수 있음
  - ```aws:PrincipalOrgID```
    - 조직의 모든 AWS 계정의 모든 ID를 나열하는 것의 대안을 제공
    - 모든 멤버의 계정을 나열하는 대신 ```Condition``` 요소에 조직 ID를 기술함
    > Principal?
      > 정책에 정의된 권한을 받는 user, service, account
      > ex) The principal is A. A has permission to do B and C.
  - ```aws:PrincipalOrgPaths```
    - 구체적인 조직의 root, OU, children
    - 멤버를 매칭시키기 위한 컨디션 키
    - Principal가 기술된 조직 경로에 있어야 함
  - ```organizations:PolicyType```
    - Organizations 정책 관련 API 명령어를 제한하기 위해 사용
    - 기술된 유형의 Organizations 정책들만 동작시킬 수 있음
    - 컨디션 키값
      - ```AISERVICE_OPT_OUT_POLICY```, ```BACKUP_POLICY```, ```SERVICE_CONTROL_POLICY```, ```TAG_POLICY```