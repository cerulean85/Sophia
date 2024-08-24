# AWS Certificate Manager
- 웹 사이트와 애플리케이션을 보호하는 퍼블릭, 프라이빗 SSL/TLS X.509 인증서와 키 갱신, 발급, 저장 등의 복잡성을 다룸

- both ACM and third-party certificates are provided.
- Be able to secure singular domain anmes, multiple specific domain names, wildcard domains, or combinations of these.

- ACM wildcard certificates protect an unlimited number of subdomains.
- export ACM certificates singed by AWS PRivate CA for use anywhere in your internal PKI.

- ACM is not responsible for monitoring and renewal. Amazon Cloudwatch Events sends notices before the certification expires. To renew the imported certificate, you renew with the certificate issuer or create a new certificate with ACM.


## References
- [What Is AWS Certificate Manager?](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)

- [Amazon Certificate Manager](https://abiabi0707.medium.com/amazon-certificate-manager-8c8ed24c0691)
