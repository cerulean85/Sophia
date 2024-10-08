# Read Replica
- 데이터베이스의 읽기 작업을 분산하여 성능을 향상시키기 위한 기능
- 주로 읽기 작업이 많은 애플리케이션에서 사용되며, 데이터베이스의 부하를 줄이고 응답 시간을 개선하는 데 도움이 됨

# 주요 특징:
- 읽기 전용 복제본
    - Read Replica는 원본 데이터베이스(Primary DB)의 읽기 전용 복제본
    - 쓰기 작업은 원본 데이터베이스에서만 수행되며, Read Replica는 읽기 작업만 처리

- 비동기 복제
    - Read Replica는 원본 데이터베이스와 비동기적으로 데이터를 복제합
    - 이는 데이터 일관성을 약간 희생하더라도 읽기 성능을 향상시키는 데 중점을 둠

- 확장성
    - 여러 개의 Read Replica를 생성하여 읽기 작업을 분산할 수 있음
    - 이를 통해 애플리케이션의 읽기 성능을 수평적으로 확장할 수 있음

- 고가용성
    - Read Replica는 원본 데이터베이스의 장애 시 대체 읽기 소스로 사용할 수 있음
    - 또한, 필요에 따라 Read Replica를 승격하여 새로운 원본 데이터베이스로 사용할 수 있음

- 다중 리전 지원
    - 일부 데이터베이스 엔진은 다중 리전에서 Read Replica를 생성할 수 있음
    - 이를 통해 지리적으로 분산된 사용자에게 더 빠른 읽기 응답 시간을 제공할 수 있음

# 사용 사례
- 읽기 성능 향상:
    - 읽기 작업이 많은 애플리케이션에서 Read Replica를 사용하여 원본 데이터베이스의 부하를 줄이고 응답 시간을 개선할 수 있음

- 보고 및 분석
    - 보고서 생성이나 데이터 분석 작업을 Read Replica에서 수행하여 원본 데이터베이스의 성능에 영향을 주지 않도록 할 수 있음

- 백업 및 복구
    - Read Replica를 사용하여 백업 작업을 수행하면, 원본 데이터베이스의 성능에 영향을 주지 않으면서 백업을 생성할 수 있음

- 지리적 분산
    - 다중 리전 Read Replica를 사용하여 지리적으로 분산된 사용자에게 더 빠른 읽기 응답 시간을 제공할 수 있음

- 지원되는 데이터베이스 엔진
    - Amazon RDS
        - MySQL
        - PostgreSQL
        - MariaDB
        - Oracle
        - SQL Server
    - Amazon Aurora:
        - MySQL 호환
        - PostgreSQL 호환