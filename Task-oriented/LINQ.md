
# 목차
- [목차](#목차)
- [LINQ(Language Integrated Query)](#linqlanguage-integrated-query)
  - [List 조회](#list-조회)
    - [조건에 부합하는 요소의 목록 조회](#조건에-부합하는-요소의-목록-조회)
    - [조건에 부합하는 요소의 존재여부 조회](#조건에-부합하는-요소의-존재여부-조회)
    - [입력된 수치에 대해 최대값이나 최소값을 갖는 요소 조회](#입력된-수치에-대해-최대값이나-최소값을-갖는-요소-조회)
    - [주어진 조건에 맞는 요소를](#주어진-조건에-맞는-요소를)
  - [SELECT](#select)
  - [문법 비교](#문법-비교)


# LINQ(Language Integrated Query)
- 특정 데이터들에서 Query로 데이터를 빠르고 편리하게 추출하는 방식
- C# 3.0 부터 추가되기 시작하였으며, 람다표현식을 사용하여 간결하고 가독성 좋게 작성 가능
- SQL과 비슷한 문법으로 Query 할 수 있음

## List 조회

### 조건에 부합하는 요소의 목록 조회
``` cs
List<Something> result = list.FindAll(e => e.val == compVal);
```

### 조건에 부합하는 요소의 존재여부 조회
``` cs
bool result list = list.Any(e => e.val == compVal);
```


### 입력된 수치에 대해 최대값이나 최소값을 갖는 요소 조회
``` cs
Something maxResult = list.MaxBy(e => e.val);
Something minResult = list.MinBy(e => e.val);
```

### 주어진 조건에 맞는 요소를 


## SELECT
- 데이터를 변형하거나 부분 서택하여 새로운 클래스(Anonymous Type)를 만들어 리턴하고 싶을 때 사용

```  cs
var v = list.Where(e => e.val == CompVal).Select(p => new { X = p.x, Y = p.y })
foreach (var o in v)
{
  ...(처리 로직)...
}
```

## 문법 비교
- Where vs. FindAll
  - Where
    - 조건에 부합하는 요소를 포함한 새로운 시퀀스 반환
    - 지연 실행 방식. 쿼리를 바로 실행하지 않고 쿼리식을 만듦
  - FindAll
    - 조건에 부합하는 요소를 포함하는 List 반환
    - 즉시 실행 방식. 쿼리 실행하여 조건에 부합하는 요소를 찾음 
  - FindAll은 결과를 List로 반환하므로, Where에 비해서는 활용이 제한적
  - Where로 조회할 경우 캐스팅이 필요

