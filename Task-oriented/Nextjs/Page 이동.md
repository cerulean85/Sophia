# Next.js에서 버튼을 눌러 페이지 이동하기 (챗봇 질의 문장)

1. [Link] Link 컴포넌트 사용
- Next.js에서 기본적으로 제공하는 `Link` 컴포넌트는 정적인 페이지 이동에 적합합니다. 

2. [파라미터 전달] 동적 라우팅 및 URL 파라미터 전달
- 페이지 이동 시 URL 파라미터를 포함하여 동적 라우팅을 처리할 수 있습니다.

3. [사전 처리] useRouter 사용
- 버튼 클릭 시 로직을 실행한 후 페이지를 이동하려면 `useRouter`를 사용하는 것이 좋습니다. 이 방법은 동적 라우팅이나 이동 전에 상태 설정이 필요할 때 유용합니다.

4. [사전 처리] 페이지 이동 전에 데이터 처리
- 비동기 로직이나 상태 업데이트가 필요하면 `async/await`를 사용합니다.

5. [기록 안 남기기] router.replace 사용
- `router.replace`를 사용하면 이동 기록을 히스토리에 남기지 않고 페이지를 이동합니다. 사용 사례는 로그인 후 리디렉션 등입니다.

6. [Pre-load] 정적 경로 미리 로드
Next.js는 `Link`를 사용하면 자동으로 페이지를 미리 로드하지만, `router.prefetch`를 사용하여 수동으로 페이지를 미리 로드할 수도 있습니다.

---

### 1. **`Link` 컴포넌트 사용**
Next.js에서 기본적으로 제공하는 `Link` 컴포넌트는 정적인 페이지 이동에 적합합니다. 

#### 코드 예제:
```javascript
import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>Home Page</h1>
      <Link href="/about">
        <button>Go to About</button>
      </Link>
    </div>
  );
}
```

- **장점**: 클라이언트 사이드 네비게이션이 가능하며, 성능이 뛰어남.
- **제한**: 이동 전에 추가 로직을 실행하기 어렵습니다.

---

### 2. **`useRouter` 사용**
버튼 클릭 시 로직을 실행한 후 페이지를 이동하려면 `useRouter`를 사용하는 것이 좋습니다. 이 방법은 동적 라우팅이나 이동 전에 상태 설정이 필요할 때 유용합니다.

#### 코드 예제:
```javascript
'use client'; // 클라이언트 컴포넌트 선언

import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter();

  const handleNavigation = () => {
    // 추가 로직 실행
    console.log('Navigating to About Page...');
    router.push('/about');
  };

  return (
    <div>
      <h1>Home Page</h1>
      <button onClick={handleNavigation}>Go to About</button>
    </div>
  );
}
```

- **장점**: 이동 전 데이터 처리, 이벤트 트래킹 등 추가 로직을 실행할 수 있음.
- **제한**: 반드시 클라이언트 컴포넌트에서만 사용 가능.

---

### 3. **`router.replace` 사용**
`router.replace`를 사용하면 이동 기록을 히스토리에 남기지 않고 페이지를 이동합니다. 사용 사례는 로그인 후 리디렉션 등입니다.

#### 코드 예제:
```javascript
const handleRedirect = () => {
  router.replace('/dashboard'); // 히스토리 기록 없음
};
```

---

### 4. **동적 라우팅 및 URL 파라미터 전달**
페이지 이동 시 URL 파라미터를 포함하여 동적 라우팅을 처리할 수 있습니다.

#### 코드 예제:
```javascript
const handleDynamicNavigation = () => {
  router.push('/profile/123'); // '/profile/[id]' 경로로 이동
};
```

`profile/[id].js`에서 매개변수를 사용:
```javascript
export default function Profile({ params }) {
  return <h1>Profile ID: {params.id}</h1>;
}
```

---

### 5. **페이지 이동 전에 데이터 처리**
비동기 로직이나 상태 업데이트가 필요하면 `async/await`를 사용합니다.

#### 코드 예제:
```javascript
const handleAsyncNavigation = async () => {
  // 데이터 처리
  await fetch('/api/log', { method: 'POST', body: JSON.stringify({ event: 'navigate' }) });
  router.push('/dashboard');
};
```

---

### 6. **정적 경로 미리 로드 (`router.prefetch`)**
Next.js는 `Link`를 사용하면 자동으로 페이지를 미리 로드하지만, `router.prefetch`를 사용하여 수동으로 페이지를 미리 로드할 수도 있습니다.

#### 코드 예제:
```javascript
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    router.prefetch('/about'); // 'about' 페이지 미리 로드
  }, [router]);

  return (
    <div>
      <h1>Home Page</h1>
    </div>
  );
}
```

---

### 요약
1. **`Link` 컴포넌트**: 단순 페이지 이동.
2. **`useRouter`의 `push`/`replace`**: 추가 로직 실행 후 이동.
3. **동적 라우팅**: URL 파라미터 전달 및 처리.
4. **`prefetch`**: 사용자 경험 최적화를 위한 사전 로드.

상황에 따라 적합한 방법을 선택하여 구현하면 됩니다! 😊