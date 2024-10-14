# AWS Launch Permission

## 요약
- AWS Launch Permission은 AMI(Amazon Machine Image)를 특정 사용자 또는 계정이 사용할 수 있도록 권한을 부여하는 기능

## 개요
- AWS Launch Permission은 AMI를 공유하거나 제한된 사용자에게만 사용할 수 있도록 설정하는 데 사용됨
- 이를 통해 AMI의 보안을 강화하고, 특정 사용자에게만 접근 권한을 부여할 수 있음

## 주요 기능 및 특징
- AMI 공유: 특정 AWS 계정과 AMI를 공유할 수 있음
- 퍼블릭 AMI 설정: 모든 AWS 사용자에게 AMI를 공개할 수 있음
- 권한 관리: AMI에 대한 접근 권한을 부여하거나 철회할 수 있음
- 보안 강화: AMI 접근을 제한하여 보안을 강화할 수 있음

## 구성
- AMI ID: 공유할 AMI의 고유 식별자
- AWS 계정 ID: AMI를 사용할 수 있도록 권한을 부여할 AWS 계정의 ID
- 퍼블릭 설정: AMI를 모든 사용자에게 공개할지 여부

## 작동 방식
1. AWS Management Console 또는 AWS CLI를 사용하여 AMI를 선택
2. AMI의 Launch Permission 설정을 열기
3. 특정 AWS 계정 ID를 추가하여 권한 부여
4. 필요 시 퍼블릭