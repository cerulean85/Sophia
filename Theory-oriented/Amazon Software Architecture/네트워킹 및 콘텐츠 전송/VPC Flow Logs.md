# VPC Flow Logs

## 요약
- VPC Flow Logs는 Amazon Virtual Private Cloud(VPC)에서 네트워크 트래픽을 캡처하고 모니터링하는 기능

## 개요
- VPC Flow Logs는 VPC, 서브넷, 또는 네트워크 인터페이스에서 발생하는 네트워크 트래픽을 캡처하여 Amazon CloudWatch Logs 또는 Amazon S3에 저장
- 네트워크 트래픽 분석, 보안 모니터링, 문제 해결에 유용

## 주요 기능 및 특징
- **네트워크 트래픽 캡처**: VPC, 서브넷, 네트워크 인터페이스에서 발생하는 트래픽 캡처
- **로그 저장**: 캡처된 로그를 Amazon CloudWatch Logs 또는 Amazon S3에 저장
- **필터링**: 수집할 트래픽 유형을 필터링하여 필요한 데이터만 캡처
- **보안 모니터링**: 네트워크 트래픽을 모니터링하여 보안 위협 감지
- **문제 해결**: 네트워크 트래픽 로그를 분석하여 문제 해결

## 구성
- **VPC**: 네트워크 트래픽을 캡처할 VPC
- **서브넷**: 네트워크 트래픽을 캡처할 서브넷
- **네트워크 인터페이스**: 네트워크 트래픽을 캡처할 네트워크 인터페이스
- **로그 그룹**: 캡처된 로그를 저장할 CloudWatch Logs 그룹
- **S3 버킷**: 캡처된 로그를 저장할 S3 버킷

## 작동 방식
1. **VPC Flow Logs 생성**
   - VPC, 서브넷, 또는 네트워크 인터페이스에서 VPC Flow Logs 생성
2. **로그 그룹 또는 S3 버킷 지정**
   - 캡처된 로그를 저장할 CloudWatch Logs 그룹 또는 S3 버킷 지정
3. **필터링 설정**
   - 수집할 트래픽 유형을 필터링하여 필요한 데이터만 캡처
4. **로그 캡처 및 저장**
   - 네트워크 트래픽이 캡처되어 지정된 로그 그룹 또는 S3 버킷에 저장
5. **로그 분석**
   - 저장된 로그를 분석하여 네트워크 트래픽 모니터링 및 문제 해결
6. **예제 코드**:
    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents",
            "logs:DescribeLogGroups",
            "logs:DescribeLogStreams"
          ],
          "Resource": "*"
        }
      ]
    }
    ```

## 다른 서비스와의 연관성
- **Amazon CloudWatch Logs**: 캡처된 로그를 저장하고 분석
- **Amazon S3**: 캡처된 로그를 저장하고 장기 보관
- **AWS Lambda**: 로그 이벤트를 기반으로 자동화된 작업 수행
- **AWS CloudTrail**: VPC Flow Logs와 함께 사용하여 네트워크 및 계정 활동 모니터링

## 사용 사례
- **보안 모니터링**: 네트워크 트래픽을 모니터링하여 보안 위협 감지
- **문제 해결**: 네트워크 트래픽 로그를 분석하여 문제 해결
- **규정 준수**: 네트워크 트래픽 로그를 저장하여 규정 준수 요구사항 충족
- **성능 분석**: 네트워크 트래픽 패턴을 분석하여 성능 최적화

## 결론
- VPC Flow Logs는 VPC에서 발생하는 네트워크 트래픽을 캡처하고 모니터링하는 강력한 도구
- 네트워크 트래픽 분석, 보안 모니터링, 문제 해결에 유용
- Amazon CloudWatch Logs 또는 Amazon S3와 통합하여 로그를 저장하고 분석할 수 있음