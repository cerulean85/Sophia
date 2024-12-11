# use client 지시어
- 이 지시어와 관련하여 다음과 같은 오류가 나타날 수 있음

```
Error:  You're importing a component that needs useState. This React hook only works in a client component. To fix, mark the file (or its parent) with the "use client" directive.
```

- React 서버 컴포넌트에서는 상태 관리가 불가능하므로, 상태를 필요로 하는 부분을 클라이언트 컴포넌트로 따로 분리해야 함

```js
// proj\app\page.tsx
import ExampleComponent from "@/component/Example";

export default function Home() {

  return (
    <div>
      <ExampleComponent></ExampleComponent>
    </div>
  );
}

```

```js
// proj\component\Example.tsx
'use client'
import { useState } from 'react';

export default function ExampleComponent() {
  const [count, setCount] = useState<number>(0);
  const incrementCount = () => {
      setCount((prev) => prev + 1);
  };

  return (
    <div>
        {count}
        <button onClick={incrementCount}>Count UP!!</button>
    </div>
    );
}

```