## I. TCP 혼잡제어 정의

- 특정 TCP가 보낸 세그먼트들이 손실됨에 따른 재전송 증가, 혼잡 악화, 통신 충돌을 제어하는 작업


## II. TCP 혼잡제어 과정

![Alt text](image.png)



과정 | 설명
-- | --
느린 시작(Slow Start) | - 2의 지수배로 윈도우 사이즈 증가<br>- sshthresh2(Slow Start threshhold). 혼잡을 감지하게 되는 상황 도달
혼잡회피(Congestion Avoidance) | - 윈도우 사이즈가 선형으로 증가<br>- TCP 수신측 중복된 ACK 수신 > 세그먼트 지연(??)
빠른 재전송(Fast Retransmit) | - 사이즈 접란에서 다시 시작<br>- sshthresh2까지 윈도우 사이즈를 현재의 절반으로 감소
빠른 회복(Fast Recovery) | - 선형적으로 윈도우 사이즈 증가