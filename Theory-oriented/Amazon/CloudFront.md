# AWS CloudFront

- AWS의 CDN(Content Delivery Network) 서비스
- Client의 콘텐츠 요청으로 서버에서 받아온 콘텐츠를 캐싱한 후 같은 요청에 대해 캐싱한 것으로 제공하는 서비스
  - 물리적으로 거리가 먼 곳에도 빠르게 요청을 처리 가능
  - 서버의 부하를 낮출 수 있음

## Edge Location
- CloudFront 서비스가 콘텐츠를 캐싱하고 Client에게 제공하는 지점 혹은 캐시 서버를 의미

- 장소나 환경에 구애를 최대한 받지 않도록 빠른 서비스를 제공하기 위해 전 세계 주요 도시에 300개 이상의 Edge Location이 분포

- 사용자가 요청한 콘텐츠의 캐시가 Edge Location에 있다면 멀리 있는 서버에 직접 요청이 아닌 가까운 Edge Location에 저장된 캐시를 불러올 수 있음

![alt text](../images/cloud/cloudfront_1.png)

## Region Edge Cache(REC)
- 사용자가 접근할 수 있는 글로벌 하게 배포되어 있는 CloudFront 위치
- Origin과 Edge Location 사이에 위치해 있는데, 콘텐츠가 캐시가 유지될 정도로 인기 있지 않아도 캐시는 더 오랫동안 남으며 Edge Location 보다 캐시 스토리지 용량이 더 큼
- REC로 인해 CloudFront가 Origin에 요청하는 것을 줄여줌

## CloudFront 동작 순서
![alt text](../images/cloud/cloudfront_2.png)

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

CloudFront는 다른 CDN과 다르게 '정적' 콘텐츠와 '동적' 콘텐츠를 모두 처리한다. 

정적 콘텐츠에는 서버(EC2)가 필요하지 않은 이미지 같은 것이 포함된다. 미리 캐싱해둔 뒤, 모든 사용자에게 동일하게 전달해줘도 무방한 데이터에 사용할 수 있다.

동적 콘텐츠는 서버가 필요한 콘텐츠를 의미한다. 즉, 서버가 무언가 해줘야 하는 데이터다. 예를 들면 뒷단의 데이터베이스에서 끌어오는 로그인 자료라던지 혹은 실시간으로 새롭게 추가되는 게시판이 될 수 있다. 이런 자료를 정적 캐싱한다면 TTL 시간 동안 사용자는 새롭게 추가/수정된 데이터를 볼 수 없게 된다.

이것을 간략하게 AWS 구성해보자면 다음과 같다. 서버(EC2)의 연산이 필요한 동적 콘텐츠의 요청을 EC2로 향하게 Distribution 처리하고 서버가 필요하지 않은 정적 콘텐츠는 S3 버킷 등으로 Distribution 처리하는 구성을 고려해볼 수 있다.


## 참고사이트
- [[AWS] CloudFront 에 대하여](https://bosungtea9416.tistory.com/entry/AWS-CloudFront)




다음 문장에서 the ALB as origins 가 무슨 의미일까?

Create an Amazon CloudFront distribution that has the S3 bucket and the ALB as origins. Configure Route 53 to route traffic to the CloudFront distribution.

ChatGPT
문장에서 "the ALB as origins"는 Amazon CloudFront 배포(Distribution)의 원본(origin)으로 ALB(Application Load Balancer)를 사용한다는 의미입니다. 즉, CloudFront 배포가 콘텐츠를 제공하기 위해 ALB를 원본 서버로 사용한다는 뜻입니다.

자세한 설명:
Amazon CloudFront: 글로벌 콘텐츠 전송 네트워크(CDN) 서비스로, 전 세계 사용자에게 더 빠르고 안전하게 콘텐츠를 제공하기 위해 사용됩니다.
S3 버킷: Amazon S3(Simple Storage Service) 버킷으로, 정적 콘텐츠(이미지, 동영상, HTML 파일 등)를 저장하는 데 사용됩니다.
ALB (Application Load Balancer): AWS의 로드 밸런서 서비스로, 여러 EC2 인스턴스에 걸쳐 애플리케이션 트래픽을 분산시키는 데 사용됩니다.
문장의 의미:
CloudFront 배포 생성: CloudFront 배포를 만들 때, 콘텐츠를 제공할 원본 서버로 S3 버킷과 ALB를 지정합니다.
S3 버킷과 ALB를 원본으로 사용: CloudFront가 콘텐츠를 제공할 때, 일부 콘텐츠는 S3 버킷에서 가져오고, 다른 일부 콘텐츠는 ALB를 통해 제공되는 애플리케이션 서버에서 가져옵니다.
Route 53 설정: Route 53(도메인 네임 시스템 서비스)을 설정하여, 사용자 트래픽을 CloudFront 배포로 라우팅합니다. 이를 통해 사용자 요청이 CloudFront를 거쳐 원본 서버(S3 버킷 및 ALB)로 전달됩니다.
예시 시나리오:
S3 버킷: 정적 콘텐츠(이미지, CSS 파일 등)를 저장.
ALB: 동적 콘텐츠(웹 애플리케이션, API 등)를 처리.
CloudFront: 전 세계 사용자에게 콘텐츠를 캐시하고 제공하여 성능을 향상.
Route 53: 사용자가 도메인(예: www.example.com)으로 접근하면, Route 53이 트래픽을 CloudFront로 라우팅.
전체 흐름:
사용자가 도메인(www.example.com)에 접근.
Route 53이 트래픽을 CloudFront 배포로 라우팅.
CloudFront가 요청을 받고 캐시된 콘텐츠를 제공하거나, 캐시에 없는 경우 원본 서버(S3 버킷 또는 ALB)로부터 콘텐츠를 가져옴.
S3 버킷에서 정적 파일을, ALB에서 동적 콘텐츠를 가져와 사용자에게 전달.
이렇게 설정하면 전 세계 사용자에게 더 빠르고 효율적으로 콘텐츠를 제공할 수 있으며, 정적 및 동적 콘텐츠를 모두 지원할 수 있습니다.