# MongoDB

## Filter
- 쿼리 조건을 정의하여 특정 조건을 만족하는 문서만 조회
```python
# 특정 조건을 만족하는 문서 조회
results = collection.find({"age": {"$gt": 25}})
```

### 비교 연산자
- $eq: 값이 같은 문서 조회 (equal)
- $ne: 값이 다른 문서 조회 (not equal)
- $gt: 값이 큰 문서 조회 (greater than)
- $gte: 값이 크거나 같은 문서 조회 (greater than or equal)
- $lt: 값이 작은 문서 조회 (less than)
- $lte: 값이 작거나 같은 문서 조회 (less than or equal)
- $in: 값이 배열에 포함된 문서 조회 (in)
- $nin: 값이 배열에 포함되지 않은 문서 조회 (not in)

## Project
- 조회된 문서에서 특정 필드만 선택하여 반환
```python
# 특정 필드만 선택하여 조회. 1이면 보여주고, 0이면 안 보여줌
results = collection.find({}, {"name": 1, "age": 1, "_id": 0})
```

## Sort
- 조회된 문서를 특정 필드를 기준으로 정렬하는 데 사용

``` python
results = collection.find.sort("age", 1) # 오름차순
results = collection.find.sort("age", -1) # 내림차순)
```

## Collation
- 문자열 비교 규칙을 정의하여 검색 시 언어별로 다른 규칙 적용
```python
# 영어 대소문자를 구분하지 않고 정렬
results = collection.find().sort("name", 1).collation({"locale": "en", "strength": 2})
```


## 예시
```js
var analDataCol = db.getCollection('AnalysisData')
var analData = analDataCol.find().pretty().sort({dateTime: -1}).limit(1).next()
var zeroArr = analData['simulateList'].map((arr) => {
    return arr[45]
})
```