- AWS WAF(웹 애플리케이션 방화벽)를 사용하면 인터넷 접근을 제어할 수 없음
    - 그 이유는 AWS WAF는 주로 웹 애플리케이션을 보호하는 데 사용되며,
    - 웹 트래픽(HTTP/HTTPS)을 필터링하고 악의적인 요청을 차단하는 역할을 하므로, 
    - 인터넷 연결 자체를 차단하는 기능을 제공하지는 않음
        - 물론 모든 트래픽을 필터링 해버리면 인터넷에 연결되지 않은 것처럼 보일 수는 있음


- AWS WAF는 웹 애플리케이션 계층(Layer 7)의 보안을 담당
    - DDoS 공격, SQL 인젝션, 크로스사이트 스크립팅(XSS) 등 웹 애플리케이션에 대한 악의적인 요청을 필터링하는 데 사용
    - CloudFront, API Gateway, Application Load Balancer (ALB) 등과 함께 사용하여 웹 애플리케이션 트래픽을 보호

- 인터넷 접근 자체를 제어하려면 AWS WAF 대신 네트워크 계층에서 접근을 제어할 수 있는 도구들이 필요
    - 이를 위해서는 다음과 같은 AWS 네트워크 보안 기능을 사용할 수 있음
        - 인터넷 게이트웨이(Internet Gateway), NAT 게이트웨이(NAT Gateway)
        - 보안 그룹(Security Groups), 네트워크 ACL(Access Control Lists)VPC 내부의 

