function groupByWeek(data, n) {
  const result = {};

  // 날짜를 기준으로 주의 시작일을 계산하는 함수
  function getStartOfWeek(date) {
    const d = new Date(date.split(`T`)[0]); // 날짜만 추출
    const day = d.getDay() || 7; // Sunday is 0, Monday is 1, ...
    d.setDate(d.getDate() - day + 1); // Set to Monday of the current week
    return d.toISOString().split('T')[0]; // Return in YYYY-MM-DD format
  }

  // n주 전 날짜 계산
  function getNWeeksAgo(n) {
    const date = new Date();
    date.setDate(date.getDate() - (n * 7)); // 현재 날짜에서 n주를 빼기
    return date;
  }

  const nWeeksAgo = getNWeeksAgo(n);

  // 주별로 데이터를 그룹화하고 합계를 계산
  data.forEach(item => {
    const itemDate = new Date(item.date);
    if (itemDate >= nWeeksAgo) { // n주 전 이후의 데이터만 처리
      const weekStart = getStartOfWeek(item.date);
      if (!result[weekStart]) {
        result[weekStart] = 0; // 주가 처음 등장하면 합계를 0으로 초기화
      }
      result[weekStart] += item.value; // 해당 주에 value 추가
    }
  });

  return result;
}

// // 예시 데이터
// const data = [
//   { date: '2025-02-01', value: 10 },
//   { date: '2025-02-02', value: 20 },
//   { date: '2025-02-05', value: 30 },
//   { date: '2025-02-08', value: 40 },
//   { date: '2025-02-12', value: 50 },
//   { date: '2025-02-14', value: 60 },
//   { date: '2025-01-10', value: 70 }, // 4주 전 데이터
// ];

// 예시 데이터 (datetime 형식)
const data = [
  { date: '2025-02-01T08:00:00Z', value: 10 },
  { date: '2025-02-02T14:00:00Z', value: 20 },
  { date: '2025-02-05T09:00:00Z', value: 30 },
  { date: '2025-02-08T10:00:00Z', value: 40 },
  { date: '2025-02-12T11:00:00Z', value: 50 },
  { date: '2025-02-14T15:00:00Z', value: 60 },
  { date: '2025-01-10T17:00:00Z', value: 70 }, // 4주 전 데이터
];

// n = 4 주 전까지의 데이터를 구할 때
console.log(groupByWeek(data, 4));
