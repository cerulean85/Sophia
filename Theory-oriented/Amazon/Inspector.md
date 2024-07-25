# Amazon Inspector

- ```취약점 관리 서비스```로 자동으로 워크로드를 발견하고, 소프트웨어 취약점과 의도되지 않은 네트워크 노출을 발견하기 위해 워크로드를 지속적으로 스캔

- Inspector는 EC2 인스턴스, Amazon ECR에서 컨테이너 이미지, Lambda 함수를 발견하고 스캔

- Inspector가 소프트웨어 취약점이나 의도하지 않은 네트워크 노출을 발견하면 이슈에 대한 상세 레포트(finding)를 만듦
- Inspector 콘솔이나 API에서 이 레포트를 관리할 수 있음


## Inspector 특징
- 여러 Amazon Inspector 계정을 중앙에서 관리
- 취약점과 네트워크 노출에 대해 환경을 지속적으로 스캔
- Amazon Inspector 리스크 스코오로 정확하게 취약점을 평가
- Amazon Inspector 대시보드로 큰 영향을 주는 findings를 식별
- 커스터마이징 가능한 뷰를 이용하여 findings를 관리
- 다른 서비스와 시스템으로 findings를 모니터링하고 처리


## References
- [What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)