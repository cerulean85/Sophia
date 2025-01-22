aws configure


sam init
sam build
sam deploy --guided

도커 데스크톱 켜야됨

![alt text](image-1.png)



sam deploy




람다서버	https://mtsa5h0nak.execute-api.ap-northeast-2.amazonaws.com/Prod/post/about/about-1			
	https://was.kkennib.net/post/about/about-1			
	https://serv.kkennib.net/post/about/about-1			
				
				
[Spring / AWS] Spring Boot 3 + AWS Lambda 사용하기	https://davidy87.tistory.com/37			
AWS API Gateway Custom domain 설정	https://seokbin.tistory.com/entry/AWS-API-Gateway-Custom-domain-%EC%84%A4%EC%A0%95?category=678488			
				
AWS Lambda + API Gateway로 Serverless API 환경 구성하기	https://velog.io/@seeh_h/AWS-Lambda-API-Gateway%EB%A1%9C-API-%EB%A7%8C%EB%93%A4%EA%B8%B0			


StreamLambdaHandler.java
RequestStreamHandler.java
template.yml


implementation 'org.springframework.boot:spring-boot-starter-web'
implementation 'org.projectlombok:lombok:latest.release'
implementation 'com.amazonaws:aws-java-sdk-dynamodb:1.12.429'
implementation 'org.springframework.boot:spring-boot-starter-webflux'

implementation 'com.amazonaws.serverless:aws-serverless-java-container-springboot3:2.0.1'
implementation 'org.springframework.cloud:spring-cloud-function-adapter-aws:3.2.5'
implementation 'org.springframework.cloud:spring-cloud-starter-function-web:3.2.5'
implementation 'com.amazonaws:aws-lambda-java-core:1.2.3'
implementation 'com.amazonaws:aws-lambda-java-events:3.11.4'


task buildZip(type: Zip) {
	from compileJava
	from processResources
//	dependencies {
//		exclude(group: 'org.springframework.boot', module: 'spring-boot-starter-tomcat')
//	}
	into('lib') {
		from(configurations.compileClasspath) {
			exclude 'tomcat-embed-*'
		}
	}
}

build.dependsOn buildZip