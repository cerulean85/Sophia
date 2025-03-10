# EC2 Instance Profile
- AWS IAM 역할을 EC2 인스턴스에 할당하기 위해 사용하는 컨테이너
- EC2 인스턴스에 권한을 부여하기 위해 **IAM 역할**을 EC2 인스턴스 프로파일로 감싸 인스턴스에 할당
- 이렇게 하면 애플리케이션이 인스턴스 내부에서 AWS 서비스에 접근할 수 있게 됨

### 주요 개념
1. **IAM 역할(Role)**: AWS 서비스들이 API 호출 등을 통해 다른 서비스에 접근할 수 있도록 권한을 부여하는 IAM 객체입니다. 예를 들어, S3에 접근해야 하는 EC2 인스턴스는 S3 접근 권한을 가진 IAM 역할을 필요로 합니다.

2. **Instance Profile**: IAM 역할을 EC2 인스턴스에 연결하는 매개체 역할을 합니다. Instance Profile을 EC2에 할당하면 해당 IAM 역할에 부여된 권한을 사용하여 인스턴스에서 다른 AWS 리소스에 접근할 수 있습니다.

3. **사용 예시**:
   - 예를 들어, EC2 인스턴스에서 S3 버킷에 데이터를 저장하거나 읽어야 하는 경우, 인스턴스 프로파일에 S3 접근 권한이 있는 IAM 역할을 포함시켜 EC2 인스턴스에 할당합니다. 그러면 인스턴스 내의 애플리케이션이 S3에 안전하게 접근할 수 있습니다.

### 작동 방식
1. **Instance Profile 생성**: IAM 콘솔에서 역할을 생성하고 이를 Instance Profile로 감싸서 사용
2. **EC2 인스턴스에 할당**: EC2 인스턴스를 생성할 때 또는 이후에 Instance Profile을 할당할 수 있음
3. **권한 사용**: 인스턴스 내부 애플리케이션에서 AWS SDK, CLI 등을 사용해 IAM 역할 권한으로 AWS 리소스에 접근할 수 있음


## EC2 Instance Profile 사용 이유
IAM 사용자에게 역할을 직접 부여하지 않고 **EC2 Instance Profile**을 사용하는 이유는 보안 및 운영 효율성 때문입니다. 아래와 같은 이유들이 있습니다.

### 1. **보안 강화**
   - **임시 자격 증명**: Instance Profile에 할당된 IAM 역할은 EC2 인스턴스가 자동으로 임시 자격 증명을 받아 AWS 서비스에 접근하게 합니다. 이렇게 하면 인스턴스에서 장기적인 접근 키(access key)와 비밀 키(secret key)를 사용할 필요가 없어, 키 유출 위험을 줄이고 보안이 강화됩니다.
   - **IAM 사용자 키 관리 부담 감소**: IAM 사용자에게 접근 권한을 주기 위해서는 접근 키를 관리하고 주기적으로 교체해야 합니다. Instance Profile을 사용하면 이러한 키 관리를 대신하고, 역할에 따라 EC2가 임시 자격 증명을 자동으로 갱신합니다.

### 2. **작동의 자동화와 유연성**
   - **역할 변경의 유연성**: Instance Profile에 연결된 IAM 역할을 변경하면, EC2 인스턴스에 별도의 조작 없이도 새 역할의 권한을 사용할 수 있게 됩니다. IAM 사용자 키를 사용했다면, 키 교체와 관련된 작업이 수동으로 필요할 것입니다.
   - **다수 인스턴스 관리의 효율성**: 동일한 역할을 여러 EC2 인스턴스에 쉽게 적용할 수 있습니다. 새로운 인스턴스가 추가되더라도 해당 인스턴스에 Instance Profile을 할당하면 IAM 사용자 관리 없이 AWS 리소스에 접근할 수 있습니다.

### 3. **최소 권한 접근 원칙**
   - Instance Profile은 특정 작업에 필요한 최소 권한만을 부여하도록 설정할 수 있어, 인스턴스의 권한 관리를 IAM 사용자 관리보다 세밀하게 수행할 수 있습니다. 이는 보안 강화를 위해 권장되는 접근 방식입니다.

결론적으로, **Instance Profile은 EC2 인스턴스에 IAM 역할을 안전하고 효율적으로 부여하는 방식**으로, 보안 위험을 줄이고 권한 관리를 단순화하여 운영 효율성을 높여줍니다.