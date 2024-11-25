## Colocation
- 코드와 관련된 데이터를 같은 위치에 배치하여 **구조를 더욱 직관적이고 유지보수하기 쉽게 만드는 패턴**
- 주로 컴포넌트와 해당 컴포넌트와 밀접하게 관련된 파일(스타일, 데이터, 테스트 파일 등)을 같은 디렉토리나 경로에 배치하는 것을 말함
- 컴포넌트 중심 개발 방식과 잘 맞아 Next.js에서 자주 활용되는 유용한 패턴

### **Colocation의 주요 개념**
- **컴포넌트와 관련 리소스의 근접 배치**: 컴포넌트 파일, CSS/SCSS 모듈, 테스트 코드, 그리고 관련 데이터 파일을 하나의 디렉토리 또는 파일 구조 내에 함께 배치함
- **데이터 Fetch와 컴포넌트의 통합**
    - 데이터를 가져오는 코드를 컴포넌트와 가까운 위치에 작성
    - 예를 들어, Next.js의 `getServerSideProps`, `getStaticProps` 또는 `useEffect`로 데이터를 가져오는 코드는 해당 페이지 컴포넌트 파일 내부에 작성
  
### **예시**
```plaintext
/pages
  /products
    index.js            // 제품 목록을 보여주는 페이지 컴포넌트
    products.module.css // 관련 스타일
    fetchProducts.js    // 데이터 Fetch 함수
    products.test.js    // 테스트 코드
```

```javascript
// /products/index.js
import styles from './products.module.css';
import fetchProducts from './fetchProducts';

export async function getStaticProps() {
  const products = await fetchProducts();
  return { props: { products } };
}

export default function ProductsPage({ products }) {
  return (
    <div className={styles.container}>
      {products.map((product) => (
        <div key={product.id}>{product.name}</div>
      ))}
    </div>
  );
}
```

### **Colocation의 장점**
1. **코드 가독성 향상**:
   - 관련된 코드와 파일이 같은 위치에 있어 쉽게 파악할 수 있음
2. **유지보수 용이성**:
   - 특정 컴포넌트의 수정 및 업데이트가 간단함
3. **명확한 구조**:
   - 복잡한 애플리케이션에서도 프로젝트 디렉토리 구조가 직관적으로 유지됨
4. **Next.js의 철학과 일치**:
   - Next.js는 파일 기반 라우팅을 지원하므로, 파일 구조가 중요하며, Colocation을 통해 이점을 극대화할 수 있음

### **Colocation이 필요한 경우**
- **페이지 단위의 데이터 Fetching**: 데이터가 특정 컴포넌트 또는 페이지에만 관련될 때.
- **스타일 분리**: 컴포넌트 단위의 CSS 모듈 사용 시.
- **테스트 코드 관리**: 컴포넌트에 해당하는 테스트 코드를 가까운 위치에 둘 때.

### **Colocation이 적합하지 않은 경우**
- 여러 컴포넌트가 동일한 데이터나 기능을 공유해야 하는 경우, 해당 로직을 **공용 유틸리티 파일**로 분리하는 것이 더 적합
- 예를 들어, 공통 API 호출 함수는 `utils` 디렉토리에 배치합니다. 



# 