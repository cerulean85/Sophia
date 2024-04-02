# What is gRPC?

gRPC는 구글이 개발한 원격 프로토콜 호출(RPC, Remote Protocol Call) 방식이다. gRPC는 데이터 전송을 위해 HTTP/2를 이용하고 프로토콜 버퍼(Protocol Buffer)라는 인터페이스 정의 언어(IDL, Interface Definition Language)를 사용하여 다른 프로세스의 메소드를 호출한다.

HTTP/2는 HTTP/1의 성능을 개선한 버전이다. HTTP/1은 기본적으로 클라이언트 요청에 서버가 응답하기 때문에 매 요청마다 커넥션(connection)을 생성해야 하며 쿠키를 포함한 헤더로 인해 용량이 크다. 반면 HTTP/2는 헤더 테이블과 호프만 인코딩 기법을 사용하여 헤더 정보를 압축하고, 서버가 클라이언트 요청 없이도 리소스를 전달할 수 있으며 하나의 커넥션만으로 데이터 교환이 가능하기 때문에 HTTP/1에 비하여 성능이 뛰어나다.

RPC를 이용하는 환경에서 클라이언트는 서버의 메소드를 직접 호출하여 데이터를 요청한다. 만약 서버와 클라이언트 구현에 사용된 프로그래밍 언어나 프레임워크가 서로 다르다면 동일한 데이터 구조임에도 불구하고 표현 방식이 달라 데이터 전송을 하지 못할 수 있다. 직렬화는 이처럼 상이한 시스템 환경에서 데이터 구조를 동일한 표현으로 변환하는 과정으로, 프로토콜 버퍼는 gRPC에서 사용하는 직렬화 데이터 표현 방식이다.

gPRC는 다양한 언어와 플랫폼에서 사용이 가능하고, RPC의 다른 방식 보다 구현이 쉽고 지원하는 기능 많고 성능이 우수하다. 또한 HTTP/2 기반이기 때문에 실시간 및 비동기식 데이터 전송, 푸시 서비스를 간단하게 구현할 수도 있다. 이러한 장점 덕분에 로컬환경 내의 애플리케이션 간 데이터 교환이나 마이크로서비스(Microservice)를 구축하기 위한 해법으로 많은 개발자들에 의해 채택되고 있다. 

## Example: Python 
### 설치
```bash
pip3 install grpcio
python -m pip install grpcio

pip3 install grpcio-tools
```

### proto 예시 및 빌드
- proto 폴더 생성 후 아래 예시 파일 생성
- 파일명: ./proto/WorkProtocolService.proto
```proto
syntax = "proto3";
package net.kkennib.grpc;

message Work {
  int32 no = 1;
  int32 groupNo = 2;
  repeated string keywords = 3;
  repeated string channels = 4;
  repeated string collectionDates = 5;
  string state = 6;
  string message = 7;
    string requestType = 8;
}

message Works {
  repeated Work workList = 1;
}

message WorkResponse {
  string state = 1;
  string message = 2;
}

service WorkProtocolService {
  rpc echo(Works) returns (Works);
  rpc collectUrls(Works) returns (WorkResponse);
  rpc collectDocs(Works) returns (WorkResponse);
  rpc extractTexts(Works) returns (WorkResponse);
  rpc extractContents(Works) returns (WorkResponse);
  rpc request(Works) returns (Works);
}


```

- proto 빌드
```bash
# proto 폴더 이동 후 아래 명령어 입력
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --proto_path=. ./WorkProtocolService.proto
```

- 파일명: server.py
```python
import os
import network as net
import config as cfg

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    conf = cfg.get_config(path=current_path)
    net.start_rpc_server(conf["server"]["worker"]["addr"], conf["server"]["worker"]["port"])
```

- 파일명: client.py
```python
import sys
sys.path.append(r'C:\Users\zhkim\Desktop\git\test\proto')

import os
import grpc
import config as cfg
from proto import WorkProtocolService_pb2
from proto import WorkProtocolService_pb2_grpc


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    conf = cfg.get_config(path=current_path)
    addr = conf["server"]["worker"]["addr"]
    port = conf["server"]["worker"]["port"]
    channel = grpc.insecure_channel(f"{addr}:{port}")
    stub = WorkProtocolService_pb2_grpc.WorkProtocolServiceStub(channel)

    reponseList = [ { "message": "111" }, { "message": "222" } ]
    result = stub.echo(WorkProtocolService_pb2.Works(workList=reponseList))
    result = stub.collectUrls(WorkProtocolService_pb2.Works(workList=reponseList))
    print(result)

```

- 파일명: network.py
```python
import sys
sys.path.append(r'C:\Users\zhkim\Desktop\git\test\proto')
from proto.WorkProtocol import WorkProtocol
from proto import WorkProtocolService_pb2_grpc
from concurrent import futures
import grpc

import sys
sys.path.append("C:/Users/zhkim/Desktop/git/test/proto")

def start_rpc_server(addr, port):
    print("Started gRPC Server... {}:{}".format(addr, port))
    proc = WorkProtocol()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    WorkProtocolService_pb2_grpc.add_WorkProtocolServiceServicer_to_server(proc, server)
    server.add_insecure_port("{}:{}".format(addr, port))
    server.start()
    server.wait_for_termination()

```

- 파일명: config.py
```python
import json
def get_config(path=''):
    with open(path + "/config.json", "r") as st_json:
        conf = json.load(st_json)
    return conf
```

- 파일명: config.json
```json
{
  "server": {
    "director": {
      "addr": "localhost",
      "port": 8084
    },
    "worker": {
      "addr": "localhost",
      "port": 8085
    }
  },

  "storage": {
    "save_dir": "../data/",
    "kafka": {
      "addr": "localhost",
      "port": 9092
    }
  },
}
```

