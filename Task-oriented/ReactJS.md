# useEffect 예제

```jsx
import { useCallback, useEffect, useState } from 'react';
import styled from 'styled-components';

const Container = styled.div`
    .context {
        padding: 24px;
    }
`
const App: NextPage = () => {
    const [count, setCount] = useState<number>(0);
    const incrementCount = () => {
        setCount((prev) => prev + 1);
    };

    // 페이지 렌더링 후 최초 한 번 호출
    useEffect(() => {
        console.log(`이건 처음에만 호출됨`)
    }, [])

    // count가 변경될 때마다 호출됨
    useEffect(() => {
        console.log(`이건 count가 변경되면 호출됨`)
    }, [count]);

    return (
        <Container>
            <div className='context'>
                {count}
                <button onClick={incrementCount}>Count UP!!</button>
            </div>
        </Container>
    );
};

export default App;
```


# useCallback 사용하는 이유
- 기본적으로 리액트는 컴포넌트가 리렌더링 될때마다 그 컴포넌트 내에 정의된 모든 함수도 새로 생성함
- 이러면 함수가 계속 새로 생성되므로, 컴포넌트 리렌더링할 때마다 새로운 함수 객체 할당 때문에 불필요한 렌더링이 발생

```jsx
'use client'
import React, { useState, useCallback  } from 'react';

export default function ExampleComponent() {
  const [count, setCount] = useState<number>(0);

  const incrementCount = () => { setCount((prev) => prev + 1); }; // 리렌더링할 때마다 새로운 객체 할당
  const incrementCountCallback = useCallback(() => { setCount((prev) => prev + 1);
  }, []);

  return (
    <div>
        {count}
        <button onClick={incrementCount}>Count UP!!</button>
        <button onClick={incrementCountCallback}>Count UP!!</button>
    </div>
    );
}
```

# useMemo
- `useMemo` 훅은 **값의 계산 결과**를 메모이제이션하여 **불필요한 재계산을 방지**
- 주어진 종속성 배열이 변경되지 않는 한, 이전에 계산된 값을 반환하여 성능 최적화를 도움

## **useMemo**를 사용하는 이유:
- **성능 최적화**
  - `useMemo`를 사용하여 **불필요한 계산을 방지**
  - 예를 들어, `expensiveCalculation`이 많은 리소스를 소비하는 경우, `count`가 바뀔 때만 계산
  - 그 외에는 이전 결과를 재사용하여 성능을 최적화
- **리렌더링 최적화**
  - 컴포넌트가 리렌더링되더라도, 종속성 배열에 있는 값이 변경되지 않으면 메모이제이션된 값이 그대로 반환
  - 리렌더링을 최소화할 수 있음

## **useMemo 사용 시 주의사항**
- **불필요한 사용 지양**
  - `useMemo`는 성능을 최적화하기 위한 훅이지만, 모든 값에 사용해야 하는 것은 아님
  - 계산이 가벼운 값에는 오히려 성능 저하를 일으킬 수 있으므로 복잡한 계산에만 사용하는 것이 좋음

## 버튼 누를 때마다 리렌더링?
- **버튼을 누를 때마다 리렌더링 발생** 
  - 하지만 리렌더링이 일어난다고 해서 모든 것이 다시 계산되지는 않음
  - `useMemo`는 **`count`가 변경되지 않는 한** `memoizedValue`의 값을 다시 계산하지 않기 때문에 성능 최적화가 이루어짐

## 예제: 긴 계산이 필요한 값의 최적화

```jsx
import React, { useState, useMemo } from 'react';

const ExpensiveCalculation = () => {
  const [count, setCount] = useState(0);
  const [otherState, setOtherState] = useState(0);

  // 복잡한 계산을 하는 함수
  const expensiveCalculation = (num) => {
    console.log('Calculating...');
    let result = 0;
    for (let i = 0; i < 1000000000; i++) {
      result += num;
    }
    return result;
  };

  // useMemo를 사용하여 값 계산을 메모이제이션
  const memoizedValue = useMemo(() => expensiveCalculation(count), [count]);

  return (
    <div>
      <h1>Expensive Calculation</h1>
      <p>Count: {count}</p>
      <p>Memoized Calculation Result: {memoizedValue}</p>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
      <button onClick={() => setOtherState(otherState + 1)}>Increment Other State</button>
    </div>
  );
};

export default ExpensiveCalculation;
```

# useLayoutEffect
- 컴포넌트가 DOME에 변화를 적용한 후 브라우저가 화면을 그리기 전에 실행
- 주로 레이아웃을 조정하거나 DOM 요소의 크기와 위치를 동기화해야 하는 경우에 사용

## 주요 특징
### 1. 실행 시점
- useEffect는 브라우저가 렌더링을 완료한 후 비동기로 실행
- useLayoutEffect는 브라우저가 레이아웃과 페인팅을 수행하기 직전에 동기적으로 실행

### 2. 용도
- useLayoutEffect는 렌더링과 레이아웃 측정이 밀접하게 연관된 작업에 사용
  - DOM 크기나 위치 측정하는 경우 (getBoundingClientRect)
  - DOM 변경 사항에 따라 스타일을 동적으로 조정해야 하는 경우

### 3. 주의사항
- 차단적 성격
  - useLayoutEffect는 동기적으로 실행되므로 성능에 영향을 줄 수 있음
  - 너무 자주 사용하면 렌더링 속도가 느려질 수 있음
- SSR (Server-Side Rendering)에서의 문제
  - 서버 환경에서는 DOM이 없으므로, useLayoutEffect는 클라이언트 환경에서만 실행
  - 서버 환경에서는 경고를 피하기 위해 useEffect로 대체하는 것이 좋음

## 간단한 예제
```jsx
import React, { useLayoutEffect, useRef, useState } from 'react';

function Example() {
  const divRef = useRef(null);
  const [width, setWidth] = useState(0);

  useLayoutEffect(() => {
    // DOM 요소의 크기를 측정
    if (divRef.current) {
      setWidth(divRef.current.offsetWidth);
    }
  }, []);

  return (
    <div>
      <div ref={divRef} style={{ width: '50%' }}>측정할 요소</div>
      <p>요소의 너비: {width}px</p>
    </div>
  );
}

export default Example;
```

## `useEffect`와 비교
| 특징                  | `useEffect`                     | `useLayoutEffect`               |
|-----------------------|---------------------------------|----------------------------------|
| 실행 시점             | 렌더링 후, 비동기적으로 실행     | 렌더링 후, 동기적으로 실행       |
| DOM 읽기/쓰기 적합성   | DOM 읽기 및 쓰기에 상대적으로 부적합 | DOM 읽기 및 쓰기에 적합          |
| 주요 사용 사례         | 비동기 데이터 로딩, 이벤트 구독 | 레이아웃 측정, DOM 스타일 변경    |

## 사용 시점
- DOM을 조작하거나 레이아웃과 관련된 작업이 필요하다면 `useLayoutEffect`를 사용
- 그렇지 않다면 성능을 위해 `useEffect`를 우선적으로 사용하는 것이 권장


# useSelector (Redux)
- React-Redux 라이브러리에서 제공하는 훅
- 리덕스 스토어의 상태를 리액트 컴포넌트에서 쉽게 가져와 사용할 수 있도록 도와줌
- 이를 통해 특정 상태를 구독하고, 상태가 변경될 때 컴포넌트를 자동으로 업데이트할 수 있음

## 주요특징
### 1. 상태 선택
- ```useSelector```를 사용하면 리덕스 스토어의 전체 상태에서 필요한 부분만 선택해서 사용할 수 있음
- 컴포넌트가 불필요하게 많은 상태를 구독하지 않도록 하여 성능을 최적화하는 데 유용함

### 2. 리렌더링 관리
- 선택한 상태가 변경될 때만 해당 컴포넌트가 리렌더링됨
- ```useMemo```나 ```useCallback```처럼, 불필요한 리렌더링을 방지하여 성능을 개선할 수 있음

### 3. 함수 기반 선택
- 상태를 선택할 때 콜백 함수를 인자로 받음
- 이 함수는 리덕스 스토어의 state를 매개변수로 받아 필요한 값을 반환함

```jsx
import React from 'react';
import { useSelector } from 'react-redux';

const MyComponent = () => {
  // Redux 스토어에서 특정 상태 선택
  const count = useSelector((state) => state.counter.value);

  return <div>Count: {count}</div>;
};
```
## 내부 동작
- ```useSelector```는 리덕스의 ```store.subscribe```를 내부적으로 사용하여 상태 변경을 감지함
- 상태가 변경되면, ```useSelector```가 제공한 선택함수(selector)를 실행해 변경된 값이 이진 값과 다른지 비교(===)
- 값이 변경되었다면 컴포넌트를 리렌더링하고, 값이 동일하면 리렌더링을 건너띔

## 주의사항
### 1. 선택함수는 순수함수여야 함
- 선택함수는 부작용을 일으키지 않는 순수함수로 작성해야 함

### 2. 리렌더링 최적화
- 상태를 선택할 때, 필요한 부분만 선택하도록 선택함수를 최적화하는 것이 중요
- 예를 들어, 큰 상태 객체 전체를 반환하면 성능 문제가 발생할 수 있음

### 3. useSelector와 메모이제이션
- 복잡한 계산이 필요한 경우, reselect 라이브러리로 메모제이션된 selector를 사용하는 것이 좋음


# useDispatch
`useDispatch`는 React-Redux 라이브러리에서 제공하는 Hook으로, Redux 스토어의 `dispatch` 메서드를 React 컴포넌트에서 사용할 수 있게 해줍니다. 이를 통해 Redux 액션(action)을 손쉽게 디스패치하여 상태를 변경할 수 있습니다.

---

### 주요 특징
1. **Redux 액션 디스패치**  
   `useDispatch`를 사용하면 Redux 스토어에 액션을 전달하여 상태를 변경할 수 있습니다.

2. **재사용 가능한 액션 호출**  
   `useDispatch`는 Redux의 `dispatch` 함수를 반환하므로, 이를 사용해 동기 및 비동기 액션을 모두 디스패치할 수 있습니다.

3. **코드 간결화**  
   클래스 기반 컴포넌트에서 사용했던 `connect`와 `mapDispatchToProps`를 대체하여, React Hooks 기반 컴포넌트에서 더 간결하게 액션을 디스패치할 수 있습니다.

---

### 기본 사용법
```jsx
import React from 'react';
import { useDispatch } from 'react-redux';

const MyComponent = () => {
  const dispatch = useDispatch();

  const handleClick = () => {
    dispatch({ type: 'INCREMENT' });
  };

  return <button onClick={handleClick}>Increment</button>;
};
```

---

### 비동기 액션 사용 예
`redux-thunk`와 같은 미들웨어를 사용하는 경우, 비동기 액션 크리에이터도 `dispatch`로 호출할 수 있습니다.

```jsx
import React from 'react';
import { useDispatch } from 'react-redux';
import { fetchUserData } from './userActions';

const MyComponent = () => {
  const dispatch = useDispatch();

  const loadUserData = () => {
    dispatch(fetchUserData()); // 비동기 액션
  };

  return <button onClick={loadUserData}>Load User Data</button>;
};
```

---

### `connect`와의 비교
과거 Redux에서는 `connect`와 `mapDispatchToProps`를 사용하여 액션 디스패치를 설정했습니다. 하지만 `useDispatch`를 사용하면 더 간단하고 선언적인 방식으로 구현할 수 있습니다.

#### `connect` 방식
```jsx
import { connect } from 'react-redux';

const mapDispatchToProps = (dispatch) => ({
  increment: () => dispatch({ type: 'INCREMENT' }),
});

const MyComponent = ({ increment }) => {
  return <button onClick={increment}>Increment</button>;
};

export default connect(null, mapDispatchToProps)(MyComponent);
```

#### `useDispatch` 방식
```jsx
const MyComponent = () => {
  const dispatch = useDispatch();

  const increment = () => {
    dispatch({ type: 'INCREMENT' });
  };

  return <button onClick={increment}>Increment</button>;
};
```

---

### 사용 시 주의사항
1. **dispatch 함수는 불변**  
   `useDispatch`로 얻은 `dispatch` 함수는 항상 동일한 참조를 유지하므로, React 컴포넌트의 렌더링 사이에 변경되지 않습니다.

2. **로직 간소화**  
   디스패치할 액션은 컴포넌트에서 정의하거나, 별도의 액션 크리에이터 함수로 관리하는 것이 좋습니다. 액션 객체를 컴포넌트 내부에 직접 작성하면 코드가 복잡해질 수 있습니다.

3. **타입스크립트와 함께 사용**  
   타입스크립트를 사용하는 경우, Redux 스토어의 `dispatch` 타입을 명시적으로 지정하면 더 안전하게 코드를 작성할 수 있습니다.

---

### 고급 사용: 바운드 액션 크리에이터
`useDispatch`와 액션 크리에이터를 함께 사용하여 보다 읽기 쉬운 코드를 작성할 수 있습니다.

```jsx
import { increment } from './counterSlice';

const MyComponent = () => {
  const dispatch = useDispatch();

  const handleIncrement = () => {
    dispatch(increment()); // increment는 액션 크리에이터
  };

  return <button onClick={handleIncrement}>Increment</button>;
};
```

---

`useDispatch`는 Redux의 상태 관리 기능을 React Hooks 기반 컴포넌트에서 자연스럽게 활용할 수 있도록 해주는 핵심 도구입니다. `useSelector`와 함께 사용하면 더욱 직관적이고 간결한 Redux 관리가 가능합니다.


# useRef
`useRef`는 React에서 제공하는 Hook 중 하나로, **React 컴포넌트에서 DOM 요소나 값을 참조하고 관리**하기 위해 사용됩니다. 이 Hook은 렌더링과 상관없이 값을 유지할 수 있어 다양한 상황에서 유용하게 쓰입니다.

---

### 주요 특징

1. **DOM 요소 접근**  
   `useRef`는 컴포넌트 내 특정 DOM 요소를 직접 참조할 수 있습니다. 이를 통해 DOM을 제어하거나 값을 읽을 수 있습니다.

2. **값의 유지**  
   `useRef`로 관리되는 값은 컴포넌트가 다시 렌더링되더라도 초기화되지 않고 유지됩니다.

3. **리렌더링 방지**  
   `useRef`로 저장된 값이 변경되어도 컴포넌트는 리렌더링되지 않습니다. 이는 `useState`와의 주요 차이점입니다.

---

### 기본 사용법: DOM 참조
`useRef`는 DOM 요소를 직접 다룰 때 많이 사용됩니다.

```jsx
import React, { useRef } from 'react';

const InputFocus = () => {
  const inputRef = useRef(null);

  const handleFocus = () => {
    inputRef.current.focus(); // input 요소에 포커스
  };

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={handleFocus}>Focus Input</button>
    </div>
  );
};

export default InputFocus;
```

---

### 상태 유지 사용법
`useRef`는 렌더링 간 값을 유지하는 데도 사용됩니다. 예를 들어, 이전 상태 값을 저장하거나, 타이머 ID와 같은 값을 관리할 수 있습니다.

```jsx
import React, { useRef, useState } from 'react';

const Counter = () => {
  const countRef = useRef(0); // 초기값 0
  const [renderCount, setRenderCount] = useState(0);

  const increment = () => {
    countRef.current += 1; // countRef 값은 렌더링되지 않음
    console.log(`Count: ${countRef.current}`);
  };

  return (
    <div>
      <p>Render Count: {renderCount}</p>
      <button onClick={() => setRenderCount(renderCount + 1)}>Re-render</button>
      <button onClick={increment}>Increment</button>
    </div>
  );
};

export default Counter;
```

---

### 주요 차이점: `useState`와 비교
| **특징**              | **`useState`**                       | **`useRef`**                   |
|-----------------------|-------------------------------------|--------------------------------|
| **값 변경 시 렌더링** | 컴포넌트를 다시 렌더링함             | 렌더링되지 않음                |
| **값 초기화**         | 컴포넌트가 재렌더링되면 초기화 가능  | 재렌더링과 상관없이 값 유지    |
| **사용 목적**         | 상태 관리                            | 값 참조 및 렌더링 영향 없는 값 관리 |

---

### 고급 사용법: 이전 상태 값 저장
`useRef`는 이전 상태 값을 기억하는 데 유용합니다.

```jsx
import React, { useEffect, useRef, useState } from 'react';

const PreviousValue = () => {
  const [count, setCount] = useState(0);
  const prevCountRef = useRef();

  useEffect(() => {
    prevCountRef.current = count; // 이전 값을 저장
  });

  const prevCount = prevCountRef.current;

  return (
    <div>
      <p>Current Count: {count}</p>
      <p>Previous Count: {prevCount}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};

export default PreviousValue;
```

---

### 사용 시 주의사항
1. **초기값 설정**  
   `useRef`는 초기값을 지정할 수 있습니다. 초기값이 `null`이 기본이며, DOM 요소를 참조할 때 많이 사용됩니다.

2. **`current` 프로퍼티 사용**  
   `useRef`가 반환하는 객체는 `{ current: 초기값 }` 형태입니다. 이 값을 직접 변경할 수 있지만, 컴포넌트 렌더링에는 영향을 미치지 않습니다.

3. **리렌더링이 필요할 경우 `useState` 사용**  
   `useRef`로 값이 변경되더라도 화면에 반영되지 않습니다. 화면에 변화를 보여주어야 한다면 `useState`를 사용하세요.

---

### `useRef`가 필요한 상황
- 특정 DOM 요소에 직접 접근해야 할 때 (예: 포커스 설정, 스크롤 제어).
- 값이 렌더링 간 유지되어야 하지만 렌더링 트리거가 불필요할 때.
- 이전 값이나 외부 타이머/이벤트 핸들러의 참조를 저장해야 할 때.

`useRef`는 DOM 접근 외에도 다양한 상황에서 React 컴포넌트를 더 효율적으로 관리하는 데 유용합니다!



# rem
CSS에서 **`rem`**은 글자 크기를 지정할 때 사용하는 상대 단위 중 하나입니다. **`rem`**은 **Root EM**의 약자로, 문서의 루트 요소(`html`)에 정의된 폰트 크기를 기준으로 상대적인 크기를 계산합니다.

---

### **특징**
1. **기준 요소**:  
   `rem`은 **루트 요소의 폰트 크기(`html`의 `font-size`)**를 기준으로 계산됩니다.
   
2. **일관된 크기**:  
   `rem`은 `em`과 달리 계층적이지 않으므로, 중첩 구조에서도 기준값이 항상 동일합니다.

3. **반응형 디자인에 적합**:  
   `rem`은 사용자가 브라우저에서 기본 글자 크기를 변경하면 전체적으로 반응하여 유연하게 작동합니다.

---

### **기본 사용법**

#### **1. 루트 요소 정의**
HTML 문서에서 기본 `font-size`는 브라우저마다 기본값이 다르지만, 일반적으로 **16px**입니다.

예를 들어, `html`의 `font-size`를 설정한 경우:
```css
html {
  font-size: 16px; /* 기본값: 16px */
}
```

#### **2. `rem`으로 글자 크기 지정**
`rem`을 사용하면, 지정된 크기가 **html의 `font-size`**를 기준으로 계산됩니다.

```css
p {
  font-size: 1rem; /* 16px (1 x 16px) */
}

h1 {
  font-size: 2rem; /* 32px (2 x 16px) */
}

h2 {
  font-size: 1.5rem; /* 24px (1.5 x 16px) */
}
```

---

### **장점**

1. **중첩 영향을 받지 않음**  
   `rem`은 부모 요소의 폰트 크기(`font-size`)와 관계없이 **항상 `html`의 `font-size`**를 기준으로 계산되므로, 크기 계산이 단순하고 예측 가능합니다.

   **예시 (rem vs em)**:
   ```css
   html {
     font-size: 16px;
   }

   .parent {
     font-size: 2em; /* 부모 폰트 크기: 32px */
   }

   .child-em {
     font-size: 1.5em; /* 32px x 1.5 = 48px */
   }

   .child-rem {
     font-size: 1.5rem; /* 16px x 1.5 = 24px */
   }
   ```

2. **반응형 디자인에 유리**  
   `rem`은 `html`의 `font-size`를 변경함으로써 전체적인 크기를 손쉽게 조정할 수 있습니다.

   **예시 (글자 크기 조정)**:
   ```css
   /* 기본 */
   html {
     font-size: 16px;
   }

   /* 반응형 (화면이 작아질수록 폰트 크기 축소) */
   @media (max-width: 768px) {
     html {
       font-size: 14px;
     }
   }

   @media (max-width: 480px) {
     html {
       font-size: 12px;
     }
   }

   p {
     font-size: 1rem; /* 화면 크기에 따라 16px, 14px, 12px로 조정 */
   }
   ```

3. **접근성 개선**  
   브라우저 설정에서 기본 폰트 크기를 조정할 경우, `rem`을 사용하면 전체적인 비율이 자동으로 반영됩니다. 사용자가 설정한 기본 크기를 따르므로 접근성이 높아집니다.

---

### **rem과 다른 단위 비교**

| **단위** | **설명**                                              | **기준**                                     |
|----------|------------------------------------------------------|---------------------------------------------|
| **px**   | 고정 크기(픽셀 단위). 화면 크기에 상관없이 동일함.       | 절대 단위                                   |
| **em**   | 부모 요소의 `font-size`에 상대적임.                     | 부모 요소의 `font-size`                     |
| **rem**  | 루트 요소(`html`)의 `font-size`에 상대적임.              | `html`의 `font-size`                        |
| **%**    | 부모 요소의 `font-size`에 상대적임.                     | 부모 요소의 `font-size`                     |
| **vw/vh**| 뷰포트 너비/높이에 상대적임.                           | 브라우저의 뷰포트 크기                       |

---

### **실제 사용 사례**

#### **1. 기본 스타일 설정**
```css
html {
  font-size: 16px;
}

body {
  font-size: 1rem; /* 16px */
}

h1 {
  font-size: 2rem; /* 32px */
}

p {
  font-size: 1rem; /* 16px */
}
```

#### **2. 반응형 타이포그래피**
```css
html {
  font-size: 16px;
}

@media (max-width: 768px) {
  html {
    font-size: 14px;
  }
}

@media (max-width: 480px) {
  html {
    font-size: 12px;
  }
}

h1 {
  font-size: 2rem; /* 32px → 28px → 24px */
}

p {
  font-size: 1rem; /* 16px → 14px → 12px */
}
```

---

### **결론**
- **`rem`**은 `html`의 `font-size`를 기준으로 하는 상대 단위로, 중첩 구조에서도 일관성을 유지하며 크기를 계산할 수 있습니다.
- 반응형 디자인과 접근성을 고려한 웹 개발에 적합한 단위입니다.
- CSS에서 `rem`을 적극적으로 활용하면 유지보수와 확장성이 높은 스타일링을 구현할 수 있습니다.