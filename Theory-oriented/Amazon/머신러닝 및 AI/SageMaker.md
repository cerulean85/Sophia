# Amazon SageMaker
- Amazon Web Services(AWS)에서 제공하는 완전 관리형 머신 러닝(ML) 서비스
- SageMaker는 데이터 과학자와 개발자가 머신 러닝 모델을 쉽게 구축, 훈련, 배포할 수 있도록 도와줌
- SageMaker는 머신 러닝 워크플로우의 모든 단계를 간소화하고 자동화하여, 모델 개발과 배포를 빠르고 효율적으로 수행할 수 있게 함


# 주요 특징
## 1. 데이터 준비
- SageMaker Data Wrangler를 사용하여 데이터를 준비하고 변환할 수 있음
- 다양한 데이터 소스에서 데이터를 가져오고, 데이터 정제, 변환, 시각화를 수행할 수 있음

## 2. 모델 구축
- SageMaker Studio는 통합 개발 환경(IDE)으로, 코드 작성, 데이터 탐색, 모델 훈련 및 배포를 한 곳에서 수행할 수 있음
다양한 내장 알고리즘과 프레임워크(TensorFlow, PyTorch, MXNet 등)를 지원

## 3. 모델 훈련
- SageMaker는 분산 훈련을 지원하여 대규모 데이터셋과 모델을 효율적으로 훈련할 수 있음
- 자동 모델 튜닝 기능을 제공하여 최적의 하이퍼파라미터를 자동으로 찾을 수 있음

## 4. 모델 배포
- 실시간 추론 및 배치 추론을 지원
- 모델을 쉽게 배포하고, 확장 가능한 엔드포인트를 생성할 수 있음
- A/B 테스트와 다중 모델 배포를 지원하여 모델 성능을 비교하고 최적의 모델을 선택할 수 있음

## 5. 모니터링 및 관리
- SageMaker Model Monitor를 사용하여 배포된 모델의 성능을 모니터링하고, 데이터 드리프트를 감지할 수 있음
- SageMaker Pipelines를 사용하여 머신 러닝 워크플로우를 자동화하고 관리할 수 있음

## 6. 보안 및 규정 준수
- SageMaker는 데이터 암호화, 네트워크 격리, 액세스 제어 등 다양한 보안 기능을 제공
- 규정 준수를 지원하여, GDPR, HIPAA, PCI-DSS 등의 요구 사항을 충족할 수 있음

# 사용 사례
- 예측 분석
    - SageMaker를 사용하여 판매 예측, 수요 예측, 재고 관리 등 다양한 예측 분석 모델을 구축할 수 있음

- 자연어 처리(NLP)
    - 텍스트 분류, 감정 분석, 번역, 챗봇 등 다양한 NLP 모델을 개발할 수 있음

- 컴퓨터 비전
    - 이미지 분류, 객체 탐지, 이미지 생성 등 컴퓨터 비전 모델을 구축할 수 있음

- 이상 탐지
    - 금융 사기 탐지, 네트워크 보안, 품질 관리 등 다양한 이상 탐지 모델을 개발할 수 있음

# 작동 방식
## 1. 데이터 준비
- SageMaker Data Wrangler를 사용하여 데이터를 가져오고, 정제하고, 변환
- 데이터 준비가 완료되면, SageMaker Studio에서 데이터를 탐색하고 시각화할 수 있음

## 2. 모델 구축
- SageMaker Studio에서 Jupyter Notebook을 사용하여 모델을 구축
- 내장 알고리즘 또는 사용자 정의 알고리즘을 사용하여 모델을 개발할 수 있음

## 3. 모델 훈련
- SageMaker 훈련 작업을 생성하여 모델을 훈련
- 분산 훈련과 자동 모델 튜닝을 사용하여 훈련 시간을 단축하고 성능을 최적화할 수 있습니다.

## 4.모델 배포
- 훈련된 모델을 SageMaker 엔드포인트에 배포하여 실시간 추론을 수행
- 배치 추론 작업을 생성하여 대규모 데이터셋에 대한 예측을 수행할 수 있음

## 5. 모니터링 및 관리
- SageMaker Model Monitor를 사용하여 배포된 모델의 성능을 모니터링
- SageMaker Pipelines를 사용하여 머신 러닝 워크플로우를 자동화하고 관리

요약
- 데이터 과학자와 개발자가 머신 러닝 모델을 쉽게 구축, 훈련, 배포할 수 있도록 도와주는 완전 관리형 머신 러닝 서비스
- 데이터 준비, 모델 구축, 훈련, 배포, 모니터링 및 관리의 모든 단계를 지원하여 머신 러닝 워크플로우를 간소화하고 자동화
- 다양한 사용 사례에 적용할 수 있으며, 보안 및 규정 준수를 지원


- 완전관리형 인프라, 도구 및 워크플로를 활용하여 모든 사용 사례에 적합한 기계 학습 모델을 구축, 훈련 및 배포

- Amazon SageMaker JumpStart를 사용하여 기계 학습을 빠르고 쉽게 시작할 수 있음
- 완벽하게 맞추화 가능하고 클릭 한 번으로 배포되며 자연어 처리, 객체 탐지 및 이미지 분류 모델과 같은 150개가 넘는 널리 사용되는 오픈 소스 모델에 대한 세분화된 튜닝도 지원
- 


## References
- [기계 학습 서비스 - Amazon SageMaker](https://aws.amazon.com/ko/pm/sagemaker/?gclid=EAIaIQobChMI5YD09eHNhwMVrOgWBR33_jfNEAAYASAAEgJUI_D_BwE&trk=83e980bd-feef-4dc8-827c-21089d3b5592&sc_channel=ps&ef_id=EAIaIQobChMI5YD09eHNhwMVrOgWBR33_jfNEAAYASAAEgJUI_D_BwE:G:s&s_kwcid=AL!4422!3!532438441650!e!!g!!amazon%20sagemaker!11549845637!116491972070)