
## useEffect 예제
```js
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