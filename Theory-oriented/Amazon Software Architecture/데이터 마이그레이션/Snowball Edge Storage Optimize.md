# AWS Snowball Edge Storage Optimized

## 요약
- AWS Snowball Edge Storage Optimized는 대용량 데이터 전송과 엣지 스토리지를 지원하는 디바이스입니다.

## 개요
- AWS Snowball Edge 시리즈의 일부로, 대규모 데이터 세트를 AWS로 전송하거나 엣지에서 데이터를 저장하고 처리할 수 있는 솔루션
- 데이터 전송과 엣지 스토리지 기능을 결합하여 원격지나 제한된 네트워크 환경에서 유용하게 사용 가능

## 주요 기능 및 특징
- **스토리지 용량**: 80TB의 사용 가능한 스토리지
- **컴퓨팅 성능**: 40 vCPUs, 80 GiB 메모리
- **엣지 컴퓨팅**: 로컬에서 데이터 처리 및 분석 가능
- **데이터 전송**: 안전하고 효율적인 대용량 데이터 전송
- **S3 호환 인터페이스**: 로컬에서 Amazon S3 API를 사용하여 데이터에 접근 가능

## 사용 사례
- **데이터 수집 및 저장**: 원격지나 제한된 네트워크 환경에서 대규모 데이터 수집 및 저장
- **데이터 마이그레이션**: 대규모 데이터 세트를 AWS로 안전하게 전송
- **백업 및 복구**: 대용량 데이터의 백업 및 복구 솔루션
- **엣지 분석**: 엣지에서 데이터 분석 및 처리

## 작동 방식
1. AWS Management Console에서 Snowball Edge Storage Optimized 디바이스를 주문
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