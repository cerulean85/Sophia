# Amazon Lightsail

## 요약
- Amazon Lightsail은 간단하고 저렴한 가상 서버를 제공하는 AWS 서비스임

## 개요
- 소규모 애플리케이션, 웹사이트, 블로그 등을 쉽게 배포하고 관리할 수 있는 서비스
- 복잡한 설정 없이 빠르게 시작할 수 있음

## 주요 기능 및 특징
- 가상 서버(VPS) 제공
- 고정 요금제
- 사전 구성된 애플리케이션 스택
- 관리형 데이터베이스
- 스토리지 및 네트워크 기능
- 간편한 스케일링

## 구성
- 인스턴스: 가상 서버
- 블록 스토리지: 추가 스토리지
- 스냅샷: 백업 및 복원
- 네트워크: 고정 IP, 로드 밸런서, DNS 관리

## 작동 방식
1. AWS 콘솔에서 Lightsail 선택
2. 인스턴스 생성 클릭
3. 운영 체제 및 애플리케이션 선택
4. 인스턴스 플랜 선택
5. 인스턴스 이름 지정 및 생성

## 다른 서비스와의 연관성
- Amazon EC2: 더 복잡한 설정이 필요한 경우 EC2로 마이그레이션 가능
- Amazon RDS: 관리형 데이터베이스 사용 시 RDS와 연동 가능

## 사용 사례
- 소규모 웹사이트 및 블로그 호스팅
- 개발 및 테스트 환경
- 간단한 애플리케이션 배포

## 결론
- Amazon Lightsail은 간단하고 저렴한 가상 서버를 제공하여 소규모 프로젝트에 적합함

## 예제 코드
```bash
# Lightsail 인스턴스 생성 예제 (AWS CLI 사용)
aws lightsail create-instances --instance-names MyFirstInstance --availability-zone us-east-1a --blueprint-id ubuntu_20_04 --bundle-id micro_2_0