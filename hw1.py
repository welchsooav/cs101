"""
Learning Syntax

reference로 wiki doc을 꼭 보기를 바람. (https://wikidocs.net/book/1)

0. Hello World!

1. Data Types 

- boolean 
- numeric 
- list-like objects : list, tuple, set, string  
- dictionary 

2. if-else 

3. for/while loop  

- continue
- break  

4. errors 

- try/except  

5. functions 

- define functions 
- lambda functions  

6. making classes 

- making class 
- class attributes 
- class methods : static, class, instance methods 

실습 

- 오묙 만들기 
- 피보나치 수열 함수 
- 하노이의 탑 
"""

def hello_world():
    pass
    
def datatypes():
    pass
    print(1)
    
def ifelse():
    pass
    
def loops():
    pass
    
def errors():
    pass
    
def functions():
    pass
    
class Desk:
    pass
    

    
def five_in_a_row():
    pass
    
def multiply(a, b):
    return 0 

def fibonacci(i):
    """Function for calculating ith fibonacci number. 
    Fibonacci sequence is a sequence of numbers that is made by following recurrence relation:
    
    f(n) = f(n-1) + f(n-2) 
    f(1) = f(2) = 1
    
    Args:
        i: numeric value 
    Returns:
        A numeric value 
    """
    return 0
    
def tower_of_hanoi(i, from_rod, passing_rod, to_rod,):
    return 0
    
    
if __name__ == '__main__':
    import answer 
    
    fib_cnt = 0
    for i in range(1, 100):
        if fibonacci(i) == answer.fibonacci(i):
            fib_cnt += 1
        # print(answer.fibonacci(i))
    print('%d right out of 100'%fib_cnt)
        
    han_cnt = 0
    from_rod, passing_rod, to_rod = 'A', 'B', 'C'
    for i in range(1, 10):
        if  tower_of_hanoi(i, from_rod, passing_rod, to_rod)\
                == answer.tower_of_hanoi(i, from_rod, passing_rod, to_rod):
            han_cnt += 1
        # print(answer.tower_of_hanoi(i, from_rod, passing_rod, to_rod))
    print('%d right out of 10'%han_cnt)
    
    mul_cnt = 0
    cnt = 0
    for i in range(10, 100):
        for j in range(10, 100):
            if i*j == multiply(str(i) * str(j)):
                mul_cnt += 1
            cnt += 1
    
    print('%d right out of %d'%(mul_cnt, cnt))
    