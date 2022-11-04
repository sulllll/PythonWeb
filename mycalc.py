## 함수 선언

def add_func(n1,n2) :
    return n1+n2

def sub_func(n1,n2) :
    return n1-n2

## 전역 변수
num1=100
num2=200
res=0

## 메인 코드
res=add_func(num1, num2)
print(num1, "+", num2, "=" , res)
res=sub_func(num1, num2)
print(num1, "-", num2, "=" , res)
