# AWS Global Accelerator

- 전 세계적으로 애플리케이션의 고가용성과 성능을 향상시키기 위해 설계된 네트워크 서비스
- 사용자가 애플리케이션에 접근할 때 가장 가까운 AWS 글로벌 네트워크 엣지 로케이션을 통해 트래픽을 라우팅하여 지연 시간을 줄이고, 애플리케이션의 가용성을 높임

## 주요 기능
1. 정적 IP 주소
  - 두 개의 정적 IP 주소를 제공하여 애플리케이션 엔드포인트에 대한 일관된 접근 보장
  - 정적 IP 주소는 변경되지 않으므로, DNS 설정을 자주 업데이트할 필요가 없음
1. 트래픽 라우팅
  - 트래픽을 가장 가까운 AWS 글로벌 네트워크 엣지 로케이션으로 라우팅하여 지연 시간을 최소화함
  - 헬스 체크를 통해 비정상적인 엔드포인트를 감지하고, 트래픽을 자동으로 정상적인 엔드포인트로 라우팅함
1. 고가용성
  - 여러 AWS 리전에 걸쳐 트래픽을 분산시켜 애플리케이션의 가용성을 높임
  - 장애 발생 시 자동으로 트래픽을 다른 리전으로 라우팅하여 서비스 중단을 최소화함
1. 성능 향상
  - AWS 글로벌 네트워크를 통해 트래픽을 전송하여 인터넷 경로보다 더 빠르고 안정적인 연결을 제공함
  - TCP 및 UDP 트래픽을 모두 지원함
1. 자동 확장
  - 트래픽 양에 따라 자동으로 확장하여 애플리케이션의 성능을 유지함

## 사용 사례
- 글로벌 애플리케이션: 전 세계 사용자에게 낮은 지연 시간과 높은 가용성을 제공해야 하는 애플리케이션에 적합
- 게임: 빠른 응답 시간과 안정적인 연결이 중요한 게임 애플리케이션에 적합
- IoT: 전 세계적으로 분산된 IoT 디바이스와의 안정적인 통신이 필요한 경우에 적합


- 다양한 AWS 리전에 있는 엔드포인트를 지원하는 글로벌 서비스
- 표준 Accelerator는 최적의 지역 엔드포인트로 트래픽을 라우팅
  - health, Client location, policy 고려
- 기본적으로 사용자의 Accelerator와 연결된 고정 IP 주소를 제공하며, 고정 IP 주소는 AWS 엣지 네트워크의 애니캐스트임
  > 애니캐스트?
  > 요청을 가장 효율적으로 철할 수 있는 포인트(데이터 센터, 엔드포인트 등)로 트래픽을 라우팅
  > 즉, 1:1로 결합 가능한 케이스가 여러 개
- 표준 Accelerator의 엔드포인트는 NLB, ALB, EC2 인스턴스, EIP 주소 등이 될 수 있음
- 이 서비스는 즉각적으로 health 변화, 클라이언트의 인터넷 트래픽이 항상 healthy 엔드포인트에 연결됨을 보장하는 설정 변화에 대응

- Global Accelerator는 지원된 엔드포인트에 대해 Route 53 ARC 트래픽 리다이렉션을 존중(respect)하여, 잠재적으로 손상된 zonal shift, zonal autoshift를 가진 AZ로부터 트래픽을 라우팅

- Custom 라우팅 Accelerator는 Amazon VPC 서브넷 유형만 지원하고, 이 서브넷 내에서 프라이빗 IP주소의 트래픽을 라우팅

  > zonal shift?
  > Amazon Route 53 애플리케이션 리커버리 컨트롤러(Route 53 ARC)의 기능
  > 손상된 AZ로부터 로드밸런싱을 이동시켜 AWS리전에서 다른 건강한 AZ에서 운영을 계속 할 수 있음
  


AWS Global Accelerator standard accelerator에 대해 설명해줘.
ChatGPT
AWS Global Accelerator는 애플리케이션의 성능과 가용성을 향상시키기 위해 설계된 네트워크 서비스입니다. 표준 가속기(Standard Accelerator)는 AWS Global Accelerator의 기본적인 유형으로, 애플리케이션 트래픽을 전 세계적으로 분산시키고 최적의 경로로 전달함으로써 지연 시간을 줄이고 애플리케이션의 성능을 최적화합니다.

주요 기능 및 특징
글로벌 성능 향상:

AWS Global Accelerator는 AWS 글로벌 네트워크를 활용하여 사용자 트래픽을 애플리케이션 엔드포인트로 전달합니다. 이를 통해 지연 시간을 줄이고 성능을 향상시킵니다.
고가용성:

AWS Global Accelerator는 여러 AWS 리전에 걸쳐 엔드포인트를 지원하며, 하나의 리전이나 엔드포인트가 실패할 경우 자동으로 다른 건강한 엔드포인트로 트래픽을 라우팅합니다.
지능형 라우팅:

글로벌 가속기는 사용자 위치에 따라 가장 가까운 AWS 엣지 로케이션으로 트래픽을 유도합니다. 엣지 로케이션에서 트래픽은 AWS 백본 네트워크를 통해 최적의 엔드포인트로 전달됩니다.
고정된 애니캐스트 IP:

Global Accelerator는 고정된 두 개의 애니캐스트 IP 주소를 제공합니다. 이를 통해 사용자는 전 세계 어디서나 동일한 IP 주소를 사용하여 애플리케이션에 접근할 수 있습니다.
트래픽 관리 및 모니터링:

트래픽 분포 및 성능을 모니터링할 수 있는 기능을 제공하여, 사용자에게 최적의 경험을 제공할 수 있도록 도와줍니다.
작동 방식
애니캐스트 IP:

AWS Global Accelerator는 두 개의 고정된 애니캐스트 IP 주소를 제공합니다. 사용자는 이 IP 주소로 애플리케이션에 접속합니다.
AWS 엣지 로케이션:

사용자의 요청은 가장 가까운 AWS 엣지 로케이션으로 라우팅됩니다. 엣지 로케이션에서 트래픽은 AWS 백본 네트워크를 통해 최적의 엔드포인트로 전달됩니다.
엔드포인트 그룹:

Global Accelerator는 엔드포인트 그룹으로 구성되며, 각 그룹은 하나 이상의 엔드포인트(AWS 리전의 EC2 인스턴스, Elastic IP, ALB 등)를 포함할 수 있습니다.
헬스 체크:

Global Accelerator는 정기적으로 엔드포인트의 상태를 모니터링하여 비정상적인 엔드포인트로의 트래픽 전달을 방지하고, 자동으로 건강한 엔드포인트로 라우팅합니다.
사용 사례
웹 애플리케이션: 글로벌 사용자에게 더 나은 응답 시간을 제공하고, 고가용성을 보장하기 위해.
게임: 전 세계 플레이어에게 지연 시간을 최소화한 게임 경험을 제공하기 위해.
미디어: 동영상 스트리밍과 같은 고속 데이터 전송이 필요한 서비스에 활용.
AWS Global Accelerator의 표준 가속기는 전 세계 사용자에게 일관된 고성능 및 고가용성을 제공하며, 애플리케이션의 성능을 최적화하는 데 매우 유용합니다.