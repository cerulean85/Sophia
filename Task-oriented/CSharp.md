
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




## List 조회
- 코딩 전에 <font color="red"><b>[이 사이트](https://learn.microsoft.com/ko-kr/dotnet/api/system.linq.enumerable.thenby?view=net-8.0)</b></font>에서 필요한 커맨드를 확인해서 이용할 것!!
- <font color="yellow">**커맨드 잘 사용하면 코드량을 엄청 줄일 수 있음!!**</font>
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

### 입력된 조건에 부합하는 하나의 요소 반환
- 만족하는 요소가 없다면 Default 반환
``` cs
Something result = list.SingleOrDefault(e => e.val == compVal)
```

### OrderBy 후 중첩 정렬
```cs
List<Something> reuslt = list.OrderBy(e => e.val1).ThenBy(e => e.val2)
```

### List 합치기
```cs
List<Something> target = new List<Something>();
List<Something> target1 = ...;
List<Something> target2 = ...;
target.AddRange(target1);  // target에 target1 합침
target.AddRange(target2);  // target에 target2 합침
```

### 원하는 개수 만큼 요소 반환
- 앞에서부터 순회하며 원하는 개수 만큼 요소를 반환
```cs
List<Something> target = ...
// 정렬 후, 앞에 3개 건너 뛰고, 5개 반환
List<Something> result = target.OrderBy(e => e.val).Skip(3).Take(5).ToList();
```

### 두 시퀀스소를 합쳐 지정한 메서드의 반환값이 요소인 새로운 시퀀스를 생성
```cs

int[] numbers = { 1, 2, 3, 4, 5};
string[] words = { "one", "two", "three", "four", "five" };
var result = numbers.Zip(words, (numIndex, wordIndex) => $"{numIndex} = {wordIndex}");
foreach (var item in result)
{
  Console.WriteLine(item)
  // 1 = one
  // 2 = tow
  // 3 = three
  // 4 = four
  // 5 = five
}

```


- Average
- Distinct
- Contains
- UnionBy
- Sum

# LINQ(Language Integrated Query)
- 특정 데이터들에서 Query로 데이터를 빠르고 편리하게 추출하는 방식
- C# 3.0 부터 추가되기 시작하였으며, 람다표현식을 사용하여 간결하고 가독성 좋게 작성 가능
- SQL과 비슷한 문법으로 Query 할 수 있음

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


## 문법
### from 
- 쿼리식의 대상이 될 데이터 원본과 안에 들어있는 각 요소 데이터를 나타내는 범위 변수를 지정
- from의 데이터 원본은 IEnumerable<T> 인터페이스를 상속하는 형식이어야 합니다. 

### where
- 해당 조건에 부합하는 데이터만을 걸러낼때 사용하는 연산자 입니다.  

### orderby
- 데이터의 정렬을 수행하는 연산자입니다.

### select
- 최종 결과를 추출합니다.
- 데이터를 변형하거나 부분 서택하여 새로운 클래스(Anonymous Type)를 만들어 리턴하고 싶을 때 사용

```  cs
var v = list.Where(e => e.val == CompVal).Select(p => new { X = p.x, Y = p.y })
foreach (var o in v)
{
  ...(처리 로직)...
}
```

### LINQ 쿼리식 예시
``` cs
var profileList = from profile in Profiles
                  where profile.Height < 175
                  orderby profile.Height
                  select
                  new
                  {
                    Name = profile.Name,
                    Height = profile.Height
                  };
```

### 메소드 호출 방식 예시
``` cs
var profileList = Profiles.
                  Where(profile => profile.Height < 175).
                  Orderby(profile => profile.Height).
                  Select(profile => 
                  new
                  {
                    Name = profile.Name,
                    Height = profile.Height
                  })

```
### Join 예시
``` cs
var joinList = from profile in Profiles
               join product in Products on profile.Name equals product.Star
               select
               new
               {
                Name = profile.Name,
                Work = product.Title,
                Height = profile.Height
               }
```