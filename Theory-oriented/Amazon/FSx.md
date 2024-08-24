# Amazon FSx

- 클라우드 내 다기능 고성능 파일 시스템을 쉽고 비용 효과적으로 시작, 실행 및 확장 할 수 있음

- 안정성과 보안성, 확장성 및 폭넓ㄹ은 기능 세트로 광범위한 워크로드를 지원

- 최신 AWS 컴퓨팅, 네트워킹 및 디스크 기술을 기반으로 구축되어 높은 성능과 낮은 TCO 제공

> TCO란?
> 총소유비용(TCO, Total COst of Ownership)은 특정 자산의 구입 가격과 더불어 자산의 존속 기간에 걸친 운영비용을 포함으로, 자산의 매입 가격과 운용 원가를 합한 금액

- NetApp ONTAP, OpenZFS, Windows File Server, Lustre 중에 선택 가능


## FSx File Gateway
- 기존 워크로드가 계속해서 클라우드로 마이그레이션됨에 따라, 일부 고객은 일반적으로 온프레미스 파일 서버에 보관하는 데이터를 호스팅하기 위해 클라우드 네이티브 서비스를 사용할 수 없었습니다. 예를 들어, 팀 및 프로젝트 파일 공유 또는 콘텐츠 관리 시스템에 일반적으로 사용되는 데이터는 고객의 물리적 위치와 클라우드 사이에서 나타나는 긴 지연 시간, 제한된 대역폭 또는 공유 대역폭 문제로 인해 온프레미스에 상주해야 합니다.

오늘 AWS Storage Gateway의 새로운 유형인 Amazon FSx File Gateway를 출시합니다. 이 솔루션은 온프레미스 파일 서버를 계속해서 사용 및 관리하는 대신, Amazon FSx for Windows File Server에서 클라우드에 저장된 데이터에 액세스할 수 있도록 지원합니다. Amazon FSx File Gateway는 네트워크 최적화 및 캐싱을 사용하여, 여전히 온프레미스에 공유 데이터가 있는 것처럼 사용자 및 애플리케이션을 지원합니다. 파일 서버 데이터를 Amazon FSx for Windows File Server로 이전 및 통합하여 클라우드 스토리지의 규모와 경제성을 활용하고, Amazon FSx File Gateway로 지연 시간 및 대역폭에 관한 문제를 해결하는 동시에, 온프레미스 파일 서버 관리와 관련된 획일적인 유지 관리 부담에서 벗어날 수 있습니다.

## 특징
- 모든 기능 포함 및 완전관리형
- 하이브리드 활성화
- 높은 가용성 및 보호
- 비용 효과성

## References
- [Amazon FSx](https://aws.amazon.com/ko/fsx/)
-[Amazon FSx File Gateway – 클라우드에서 파일 서버 데이터에 대한 캐시 기반 빠른 액세스 지원](https://aws.amazon.com/ko/blogs/korea/get-started-using-amazon-fsx-file-gateway-for-fast-cached-access-to-file-server-data-in-the-cloud/)