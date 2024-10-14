# AWS Snowball Edge Compute Optimize

## 요약
- AWS Snowball Edge Compute Optimized는 대용량 데이터 전송과 엣지 컴퓨팅을 지원하는 디바이스

## 개요
- AWS Snowball Edge 시리즈의 일부로, 데이터 전송과 엣지 컴퓨팅을 결합한 솔루션
- 대규모 데이터 세트를 AWS로 전송하거나 엣지에서 데이터 처리 및 분석을 수행할 수 있음

## 주요 기능 및 특징
- **고성능 컴퓨팅**: 52 vCPUs, 208 GiB 메모리
- **스토리지**: 42TB의 사용 가능한 스토리지
- **GPU 옵션**: 선택적으로 NVIDIA Tesla V100 GPU 포함
- **엣지 컴퓨팅**: 로컬에서 데이터 처리 및 분석 가능
- **데이터 전송**: 안전하고 효율적인 대용량 데이터 전송

## 사용 사례
- **데이터 수집 및 분석**: 원격지나 제한된 네트워크 환경에서 데이터 수집 및 실시간 분석
- **비디오 처리**: 고해상도 비디오 처리 및 분석
- **기계 학습**: 엣지에서 기계 학습 모델 훈련 및 추론
- **데이터 마이그레이션**: 대규모 데이터 세트를 AWS로 안전하게 전송

## 작동 방식
1. AWS Management Console에서 Snowball Edge Compute Optimized 디바이스를 주문
2. 디바이스를 수령한 후, 로컬 네트워크에 연결
3. 데이터를 디바이스에 복사하거나 엣지 컴퓨팅 작업 수행
4. 작업 완료 후, 디바이스를 AWS로 반환
5. AWS에서 데이터를 자동으로 업로드

## 예제 코드
### AWS CLI를 사용한 데이터 전송 예제
```bash
# Snowball Edge 디바이스에 데이터 복사
aws s3 cp /local/path s3://bucket-name --recursive --endpoint http://snowball-edge-ip

# Snowball Edge 디바이스에서 데이터 복사
aws s3 cp s3://bucket-name /local/path --recursive --endpoint http://snowball-edge-ip