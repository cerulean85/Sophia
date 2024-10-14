# Amazon CloudFront

## 개요
Amazon CloudFront는 AWS의 Content Delivery Network(CDN) 서비스로, 전 세계적으로 콘텐츠를 빠르게 배포할 수 있도록 도와줌
- CloudFront는 웹 사이트, 동영상 스트리밍, API, 데이터 파일 등을 사용자에게 더 가까운 위치에서 제공하여 지연 시간을 줄이고 성능을 향상시킴

## 주요 기능 및 특징
- **글로벌 네트워크**: 전 세계에 분포된 Edge Location을 통해 콘텐츠를 빠르게 배포
- **캐싱**: 자주 요청되는 콘텐츠를 캐싱하여 서버 부하를 줄이고 응답 시간을 단축
- **보안**: DDoS 공격 방어, SSL/TLS 암호화, AWS WAF와의 통합을 통해 보안을 강화
- **자동 확장**: 트래픽 증가에 따라 자동으로 확장
- **유연한 가격 정책**: 사용량에 따라 비용을 지불하는 유연한 가격 정책을 제공
- **여러 버전의 콘텐츠**: 장치나 지역에 따라 적절한 버전의 콘텐츠 제공

## 다른 서비스와의 연관성
### Amazon S3 (Simple Storage Service)
- **정적 콘텐츠 배포**: S3 버킷에 저장된 정적 콘텐츠를 CloudFront를 통해 전 세계에 배포할 수 있음
- **보안**: S3와 CloudFront를 연동하여 콘텐츠에 대한 액세스를 제어할 수 있음

### AWS Lambda
- **Lambda@Edge**: CloudFront의 엣지 로케이션에서 Lambda 함수를 실행하여 사용자 요청을 처리할 수 있음
- **실시간 데이터 처리**: 사용자 요청에 대한 실시간 데이터 처리를 수행할 수 있음

### Amazon EC2
- **동적 콘텐츠 배포**: EC2 인스턴스에서 생성된 동적 콘텐츠를 CloudFront를 통해 배포할 수 있음
- **로드 밸런싱**: CloudFront와 EC2를 연동하여 로드 밸런싱을 구현할 수 있음

### AWS WAF (Web Application Firewall)
- **보안 강화**: CloudFront와 WAF를 연동하여 웹 애플리케이션에 대한 보안을 강화할 수 있음
- **DDoS 방어**: WAF를 통해 DDoS 공격을 방어할 수 있음

## 사용 사례
- **웹사이트 가속화**: 전 세계 사용자에게 빠르게 웹 콘텐츠를 제공할 수 있음
- **비디오 스트리밍**: 실시간 및 온디맨드 비디오 스트리밍을 지원
- **API 가속화**: API 응답 시간을 단축하고 성능을 향상시킬 수 있음
- **보안 강화**: DDoS 공격 방어, SSL/TLS 암호화, AWS WAF와의 통합을 통해 보안을 강화할 수 있음

## 요약
Amazon CloudFront는 AWS의 CDN 서비스로, 전 세계적으로 콘텐츠를 빠르게 배포하고 서버 부하를 줄일 수 있음
다양한 AWS 서비스와 연동하여 보안, 성능, 확장성을 강화할 수 있으며, 웹사이트 가속화, 비디오 스트리밍, API 가속화 등 다양한 사용 사례에 활용될 수 있음


--- 

- AWS의 CDN(Content Delivery Network) 서비스
- Client의 콘텐츠 요청으로 서버에서 받아온 콘텐츠를 캐싱한 후 같은 요청에 대해 캐싱한 것으로 제공하는 서비스
  - 물리적으로 거리가 먼 곳에도 빠르게 요청을 처리 가능
  - 서버의 부하를 낮출 수 있음

## Edge Location
- CloudFront 서비스가 콘텐츠를 캐싱하고 Client에게 제공하는 지점 혹은 캐시 서버를 의미

- 장소나 환경에 구애를 최대한 받지 않도록 빠른 서비스를 제공하기 위해 전 세계 주요 도시에 300개 이상의 Edge Location이 분포

- 사용자가 요청한 콘텐츠의 캐시가 Edge Location에 있다면 멀리 있는 서버에 직접 요청이 아닌 가까운 Edge Location에 저장된 캐시를 불러올 수 있음

![alt text](../../images/cloud/cloudfront_1.png)

## Region Edge Cache(REC)
- 사용자가 접근할 수 있는 글로벌 하게 배포되어 있는 CloudFront 위치
- Origin과 Edge Location 사이에 위치해 있는데, 콘텐츠가 캐시가 유지될 정도로 인기 있지 않아도 캐시는 더 오랫동안 남으며 Edge Location 보다 캐시 스토리지 용량이 더 큼
- REC로 인해 CloudFront가 Origin에 요청하는 것을 줄여줌

## CloudFront 동작 순서
![alt text](../../images/cloud/cloudfront_2.png)

1. 사용자가 애플리케이션에 요청을 함
2. DNS는 사용자에게 적합한 Edge Location으로 라우팅 함
3. Edge Location에 캐시를 확인하고 있으면 이것을 사용자에게 반환함
4. 없으면 가장 가까운 REC로 캐시가 있는지 요청함
5. 없으면 CloudFront는 오리진으로 요청을 전달함
6. 오리진은 오리진 > REC > Edge Location > CloudFront가 사용자에게 전달수순을 밟음
7. REC에 캐시가 있다면 REC는 콘텐츠를 요청한 Edge Location으로 반환
8. REC로부터 콘텐츠의 첫 번째 바이트가 도착하는 즉시 Edge Location은 이를 사용자에게 반환함
9. Edge Location은 나중을 위해 이 콘텐츠 캐시를 저장함

## CloudFonrt의 Static / Dynamic 콘텐츠 처리
- CLoudFront는 다른 CDN과 다르게 정적, 동적 콘텐츠 모두 처리

- 정적 콘텐츠에는 서버(EC2)가 필요하지 않은 이미지나 HTML, CSS 등의 리소스가 포함
  - 캐싱하여 모든 사용자에게 동일하게 전달해도 무방한 데이터

- 동적 콘텐츠는 데이터베이스와 같이 수시로 변경되는 콘텐츠를 의미
  - 이런 데이터를 정적 캐싱한다면 TTL 시간 동안 사용자는 새롭게 추가/수정된 데이터를 볼 수 없음

- 동적 콘텐츠의 경우 서버(EC2)의 연산이 필요하므로 요청을 EC2로 향하게 Distribution 처리
- 정적 콘텐츠의 경우 S3 버킷 등으로 Distribution 처리


### as origin
- ```the ALB as origins```
-  Amazon CloudFront 배포(Distribution)의 원본(origin)으로 ALB를 사용한다는 의미로, CloudFront 배포가 콘텐츠를 제공하기 위해 ALB를 원본 서버로 사용한다는 뜻
- ```S3 버킷과 ALB를 원본으로 사용```
-  CloudFront가 콘텐츠를 제공할 때, 일부 콘텐츠는 S3 버킷에서 가져오고, 다른 일부 콘텐츠는 ALB를 통해 제공되는 애플리케이션 서버에서 가져옴

## 참고사이트
- [[AWS] CloudFront 에 대하여](https
- //bosungtea9416.tistory.com/entry/AWS-CloudFront)

