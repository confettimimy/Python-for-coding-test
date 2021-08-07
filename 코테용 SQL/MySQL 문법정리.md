# MySQL 문법정리

​    

## IF

select, where절에서 사용가능

```mysql
SELECT IF(10>5, '크다', '작다') AS result;
```

​    

## Order By

Order By 뒤에 우선순위가 있는 열을 순서대로 적는다.

​    

## LIKE

**where절과 함께** 특정 패턴을 검색할 때 사용

```mysql
SELECT * 
FROM STUDENT
WHERE STUDENT_ID LIKE 'a%';

LIKE 'a%' // a로 시작되는 모든것
LIKE '_a%' // 두번째 자리에 a가 들어가는 모든것
```

​      

## IN

**where절 내** 여러 값을 설정하고자 할 때 사용

or 연산과 유사한 효과

```mysql
SELECT *
FROM CUSTOMERS
WHERE country in ('UK', 'Koera')
```

동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.

```mysql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy','Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
```

​    

## Between

where절 내 검색조건으로 범위를 지정하고자 할 때 사용

between과 and 사이에 들어가는 값은 '~이상 ~이하' 이다.

```mysql
SELECT *
FROM PRODUCTS
WHERE PRICE BETWEEN 10 AND 20;

SELECT *
FROM PRODUCTS
WHERE PRICE NOT BETWEEN 10 AND 20;
```

​    

## NULL의 처리

### IFNULL의 사용

