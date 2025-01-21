sam init
sam build
sam deploy --guided
aws configure

![alt text](image-1.png)


CREATE_FAILED                                 AWS::IAM::Role                                UntitledFunctionRole                          Resource handler returned message: "User:
                                                                                                                                          arn:aws:iam::307946656924:user/dynamodb is
                                                                                                                                          not authorized to perform: iam:CreateRole
                                                                                                                                          on resource:
                                                                                                                                          arn:aws:iam::307946656924:role/kkennib-
                                                                                                                                          UntitledFunctionRole-ABAwkrra9IKj because
                                                                                                                                          no identity-based policy allows the
                                                                                                                                          iam:CreateRole action (Service: Iam, Status
                                                                                                                                          Code: 403, Request ID:
                                                                                                                                          e635f752-4f57-4d60-b416-1189efca2d5c)"
                                                                                                                                          (RequestToken:
                                                                                                                                          77dfbc46-8444-ad24-0813-e7d33a59eae6,
                                                                                                                                          HandlerErrorCode:
                                                                                                                                          UnauthorizedTaggingOperation)
CREATE_FAILED                                 AWS::CloudFormation::Stack                    kkennib                                       The following resource(s) failed to create:
                                                                                                                                          [UntitledFunctionRole].
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------