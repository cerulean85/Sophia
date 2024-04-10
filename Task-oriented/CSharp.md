
# 목차
- [목차](#목차)
  - [List 조회](#list-조회)
    - [조건에 부합하는 요소의 목록 조회](#조건에-부합하는-요소의-목록-조회)
    - [조건에 부합하는 요소의 존재여부 조회](#조건에-부합하는-요소의-존재여부-조회)
    - [입력된 수치에 대해 최대값이나 최소값을 갖는 요소 조회](#입력된-수치에-대해-최대값이나-최소값을-갖는-요소-조회)
    - [입력된 조건에 부합하는 하나의 요소 반환](#입력된-조건에-부합하는-하나의-요소-반환)
    - [OrderBy 후 중첩 정렬](#orderby-후-중첩-정렬)
    - [List 합치기](#list-합치기)
    - [원하는 개수 만큼 요소 반환](#원하는-개수-만큼-요소-반환)
    - [두 시퀀스를 합쳐 지정한 메서드의 반환값이 요소인 새로운 시퀀스를 생성](#두-시퀀스를-합쳐-지정한-메서드의-반환값이-요소인-새로운-시퀀스를-생성)
    - [평균 계산](#평균-계산)
    - [중복없이 시퀀스의 요소 반환(Distinct)](#중복없이-시퀀스의-요소-반환distinct)
    - [특정값이 존재하는지 확인](#특정값이-존재하는지-확인)
    - [두 시퀀스를 중복없이 병합하기](#두-시퀀스를-중복없이-병합하기)
    - [시퀀스의 숫자형 요소 합계(Sum)](#시퀀스의-숫자형-요소-합계sum)
- [LINQ(Language Integrated Query)](#linqlanguage-integrated-query)
  - [문법](#문법)
    - [from ](#from)
    - [where](#where)
    - [orderby](#orderby)
    - [select](#select)
    - [LINQ 쿼리식 예시](#linq-쿼리식-예시)
    - [메소드 호출 방식 예시](#메소드-호출-방식-예시)
    - [Join 예시](#join-예시)
  - [비교](#비교)
  - [GUID 생성](#guid-생성)
  - [Enum](#enum)
    - [Enum To String](#enum-to-string)
    - [String To Enum](#string-to-enum)
- [Null 처리](#null-처리)
  - [코드정리 및 설명 필요](#코드정리-및-설명-필요)
- [String 처리](#string-처리)
  - [bool.TryParse](#booltryparse)




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
- Single vs. SingleOrDefault
  - Single은 요소를 찾지 못하면 Exception을 발생시킴

### OrderBy 후 중첩 정렬
```cs
List<Something> reuslt = list.OrderBy(e => e.val1).ThenBy(e => e.val2)
```
- ThenBy는 OrderBy 이후에 부차적인 정렬을 다시 진행할 수 있음

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

### 두 시퀀스를 합쳐 지정한 메서드의 반환값이 요소인 새로운 시퀀스를 생성
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


### 평균 계산
```cs
List<int> exam = new List<int>() { 1, 2, 3, 4 };
var val1 = (from num in exam
           where num > 0
           select num).Average();
var val2 = exam.Average();
var val3 = exam.FindAll(v => v > 2).Average();

# val1 = 2.5
# val2 = 2.5
# val3 = 3.5

# 클래스 사용하는 경우
List<A> exam = new List<A>()
{
    new A(){ Num = 1 },
    new A(){ Num = 2 },
    new A(){ Num = 3 },
    new A(){ Num = 4 },
};
var val1 = (from t in exam
            where t.Num > 0
            select t.Num).Average();
var val2 = exam.Average(e => e.Num);
var val3 = exam.FindAll(x => x.Num > 2).Average(e => e.Num);
Debug.WriteLine(val3);

# val1 = 2.5
# val2 = 2.5
# val3 = 3.5

```

### 중복없이 시퀀스의 요소 반환(Distinct)
```cs
List<int> numArray = new List<int>()
{
    1, 2, 2, 3, 3, 3, 4, 5, 5,
};

numArray.Distinct().ToList().ForEach(x => Debug.WriteLine(x));
# Result: 1, 2, 3, 4, 5

# 클래스 예시
List<A> exam = new List<A>()
{
    new A(){ Num = 1 },
    new A(){ Num = 2 },
    new A(){ Num = 2 },
    new A(){ Num = 3 },
    new A(){ Num = 3 },
    new A(){ Num = 3 },
    new A(){ Num = 4 },
    new A(){ Num = 5 },
    new A(){ Num = 5 }
};

# Select로 Distinct 할 프로퍼티 선택
exam.Select(e => e.Num).Distinct().ToList().ForEach(x => Debug.WriteLine(x));
# Result: 1, 2, 3, 4, 5
```

### 특정값이 존재하는지 확인
```cs
List<string> fruits = new List<string>()
{
    "사과", "사과", "바나나", "토마토", "귤", "바나나", "오렌지"
};
Debug.WriteLine(fruits.Contains("사과")); // true
Debug.WriteLine(fruits.Contains("수박")); // false

# 클래스 예시
List<Exam> examList = new List<Exam>()
{
    new Exam() { Fruit = "사과" },
    new Exam() { Fruit = "사과" },
    new Exam() { Fruit = "바나나" },
    new Exam() { Fruit = "토마토" },
    new Exam() { Fruit = "귤" },
    new Exam() { Fruit = "바나나" },
    new Exam() { Fruit = "오렌지" },
};
Debug.WriteLine(examList.Select(e => e.Fruit).Contains("사과"));  // true
Debug.WriteLine(examList.Select(e => e.Fruit).Contains("수박"));  // false
```
### 두 시퀀스를 중복없이 병합하기
- Union과 UnionBy 사용
- UnionBy는 특정 프로퍼티를 지정하여 중복제거

```cs
List<string> fruits1 = new List<string>() { "사과", "바나나", "토마토", "귤", "오렌지" };
List<string> fruits2 = new List<string>() { "옥수수", "망고", "자몽", "바나나", "사과", "감" };

fruits1.Union(fruits2).ToList().ForEach(f => Debug.WriteLine(f));
// 중복된 "바나나", "사과" 제거
// Result: 사과, 바나나, 토마토, 귤, 오렌지, 옥수수, 망고, 자몽, 감
```

- Union 클래스 예시

```cs
List<Exam1> examList1 = new List<Exam1>()
{
    new Exam1() { Fruit = "사과" },
    new Exam1() { Fruit = "바나나" },
    new Exam1() { Fruit = "토마토" },
    new Exam1() { Fruit = "귤" },
    new Exam1() { Fruit = "오렌지" },
};

List<Exam1> examList2 = new List<Exam1>()
{
    new Exam1() { Fruit = "옥수수" },
    new Exam1() { Fruit = "망고" },
    new Exam1() { Fruit = "자몽" },
};
examList1.Union(examList2).ToList().ForEach(f => Debug.WriteLine(f.Fruit));
// Result: 사과, 바나나, 토마토, 귤, 오렌지, 옥수수, 망고, 자몽
```
- UnionBy 예시1
```cs
List<Exam1> examList1 = new List<Exam1>()
{
    new Exam1() { Fruit = "사과", Num = 1 },
    new Exam1() { Fruit = "사과", Num = 1 },
    new Exam1() { Fruit = "바나나", Num = 2 },
    new Exam1() { Fruit = "토마토", Num = 3 },
    new Exam1() { Fruit = "귤", Num = 4 },
    new Exam1() { Fruit = "바나나", Num = 5 },
    new Exam1() { Fruit = "오렌지", Num = 6 },
};

List<Exam1> examList2 = new List<Exam1>()
{
    new Exam1() { Fruit = "옥수수", Num = 1 },
    new Exam1() { Fruit = "망고", Num = 1 },
    new Exam1() { Fruit = "자몽", Num = 3 },
    new Exam1() { Fruit = "바나나", Num = 1 },
    new Exam1() { Fruit = "사과", Num = 7 },
    new Exam1() { Fruit = "감", Num = 18 },
};

// 단일 프로퍼티 
examList1.Select(s => s.Fruit)
          .UnionBy(examList2.Select(t => t.Fruit), s => s)
          .ToList()
          .ForEach(f => Debug.WriteLine(f));
// Result: 사과, 바나나, 토마토, 귤, 오렌지, 옥수수, 망고, 자몽

// 여러 프로퍼티. 튜플로 등록
examList1.Select(s => (s.Fruit, s.Num))
          .UnionBy(examList2.Select(t => (t.Fruit, t.Num)), s => s)
          .ToList()
          .ForEach(f => Debug.WriteLine(f.Fruit));
// Result: 사과, 바나나, 토마토, 귤, 오렌지, 옥수수, 망고, 자몽                    
```

- UnionBy 예시2
  - 서로 다른 클래스 Union
```cs
// examList1의 Fruit와 examList2의 FruitName는 동일한 프로퍼티로 이름만 다름
List<Exam1> examList1 = new List<Exam1>()
{
    new Exam1() { Fruit = "사과", Num = 1 },
    new Exam1() { Fruit = "사과", Num = 1 },
    new Exam1() { Fruit = "바나나", Num = 2 },
    new Exam1() { Fruit = "토마토", Num = 3 },
    new Exam1() { Fruit = "귤", Num = 4 },
    new Exam1() { Fruit = "바나나", Num = 5 },
    new Exam1() { Fruit = "오렌지", Num = 6 },
};
List<Exam2> examList2 = new List<Exam2>()
{
    new Exam2() { FruitName = "옥수수", Num = 1 },
    new Exam2() { FruitName = "망고", Num = 1 },
    new Exam2() { FruitName = "자몽", Num = 3 },
    new Exam2() { FruitName = "바나나", Num = 1 },
    new Exam2() { FruitName = "사과", Num = 7 },
    new Exam2() { FruitName = "감", Num = 18 },
};

// 여러 프로퍼티. 튜플로 등록.
// 클래스의 프로퍼티명이 다르다면, Fruit: t.FruitName 앞쪽 클래에 맞게 얼라이싱
examList1.Select(s => (s.Fruit, s.Num))
          .UnionBy(examList3.Select(t => (Fruit: t.FruitName, t.Num)), s => s)
          .ToList()
          .ForEach(f => Debug.WriteLine(f.Fruit));
// Result: 사과, 바나나, 토마토, 귤, 오렌지, 옥수수, 망고, 자몽          
```
- 
### 시퀀스의 숫자형 요소 합계(Sum)
```cs
# 클래스 예시
List<A> exam = new List<A>()
{
    new A(){ Num = 1 },
    new A(){ Num = 2 },
    new A(){ Num = 2 },
    new A(){ Num = 3 },
    new A(){ Num = 3 },
    new A(){ Num = 3 },
    new A(){ Num = 4 },
    new A(){ Num = 5 },
    new A(){ Num = 5 }
};
var val = exam.Sum(e => e.Num);
Debug.WriteLine(val);
```

# LINQ(Language Integrated Query)
- 특정 데이터들에서 Query로 데이터를 빠르고 편리하게 추출하는 방식
- C# 3.0 부터 추가되기 시작하였으며, 람다표현식을 사용하여 간결하고 가독성 좋게 작성 가능
- SQL과 비슷한 문법으로 Query 할 수 있음

## 문법
### from 
- 쿼리식의 대상이 될 데이터 원본과 안에 들어있는 각 요소 데이터를 나타내는 범위 변수를 지정
- from의 데이터 원본은 IEnumerable<T> 인터페이스를 상속하는 형식이어야 함

### where
- 해당 조건에 부합하는 데이터만을 걸러낼 때 사용하는 연산자

### orderby
- 데이터의 정렬을 수행하는 연산자

### select
- 최종 결과를 추출
- 데이터를 변형하거나 부분 선택하여 새로운 Anonymous Type의 클래스를 만들어 반활할 때 사용

```  cs
# 메소드 호출 방식 예시
var v = list.Where(e => e.val == CompVal).Select(p => new { X = p.x, Y = p.y })
foreach (var o in v)
{
  ...(처리 로직)...
}
```

### LINQ 쿼리식 예시
``` cs
# Anonymous Type으로 반환하므로 반환 결과 사용 시 캐스팅 필요
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
# Anonymous Type으로 반환하므로 반환 결과 사용 시 캐스팅 필요
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

## 비교
- Where vs. FindAll
  - Where
    - 조건에 부합하는 요소를 포함한 새로운 시퀀스 반환
    - 지연 실행 방식. 쿼리를 바로 실행하지 않고 쿼리식을 만듦
  - FindAll
    - 조건에 부합하는 요소를 포함하는 List 반환
    - 즉시 실행 방식. 쿼리 실행하여 조건에 부합하는 요소를 찾음 
  - FindAll은 결과를 List로 반환하므로, Where에 비해서는 활용이 제한적
  - Where로 조회할 경우 캐스팅이 필요


## GUID 생성
- 전역 고유 식별자(Globally Unique Identifier, CUGID)
- 응용 S/W에서 사용되는 유사 난수
- 중복된 값을 생성할 가능성이 매우 낮음
  - 사용할 수 있는 모든 값의 수가 2^128 = 3.4028 x 10^38개로 매우 크
```cs
Guid guid = Guid.NewGuid();
string guidStr = guid.ToString();
```


## Enum

### Enum To String
```cs

enum FruitType { 사과, 배, 복숭아, 수박, 멜론 }
string EnumToString(FruitType fruit) { return fruit.ToString(); }
```

### String To Enum
```cs
enum FruitType { 사과, 배, 복숭아, 수박, 멜론 }
FruitType StringToEnum(string fruitName)
{
  return (FruitType) Enum.Parse(typeof(FruitType), fruitName);
}

```
```cs
enum FruitType { 사과, 배, 복숭아, 수박, 멜론 }

var nameList = Enum.GetNames(typeof(FruitType));
foreach (var name in nameList)
  Console.WriteLine($"{name}");
// Result: 사과, 배, 복숭아, 수박, 멜론

var valueList = Enum.GetValues(typeof(Colors));
foreach (var value in valueList)
  Console.WriteLine($"{(int)value} > {(FruitType)value}");
// 0 > 사과
// 1 > 배
// 2 > 복숭아
// 3 > 수박
// 4 > 멜론

```



# Null 처리
## 코드정리 및 설명 필요
```cs
        Test test = null;
        int? a = null;
        
        a = test?.testCol; // test가 null이면  null 반환. 반대는 멤버(testCol)를 반환
        Console.WriteLine($"{a} / {a == null}"); // Result: / true

        a = test?.testCol ?? 100;
        Console.WriteLine($"{a}"); // Result: 100


        test = new Test();
        test.testCol = 66;
        a = test?.testCol;
        Console.WriteLine($"{a} / {a == null}"); // Result: 66 / false

        a = test?.testCol ?? 100;
        Console.WriteLine($"{a}"); // Result: 66. 그냥 a 출력

        // 물음표(엘비스)를 쓰면 null과 string 두 가지로 형태가 될 수 있음을 암시
        string? x = null; 

        // 느낌표(!, null-forgiving)를 사용하면 x의 반환형 중 null을 무시함을 암시
        // 즉, x를 string으로만 인식하도록 함
        int length = x.Length;

        // 반면, 물음표를 쓰면 x의 반환형이 null이나 string을 암시하므로 오류
        int length = x?.Length;
```


# String 처리
## bool.TryParse
- string이 대소문자를 구분하지 않는 true/false 일 때 bool로 변환을 해줌
- 좀 헷갈리는 문법이라 잘 확인하고 사용해야 함

```CS
string fruit = "True";
bool result = false;
bool.TryParse(fruit, out result);
Console.WriteLine($"{fruit} / 변환 결과: {result}");
```