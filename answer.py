def multiply(a, b):
    mul = {}
    
    for i in range(1,10):
        for j in range(1,10):
            mul[(str(i), str(j))] = i*j
    res = 0
    # print(mul)
    for idx_a, digit_a in enumerate(a[::-1]):
        for idx_b, digit_b in enumerate(b[::-1]):
            print(digit_a, digit_b)
            res += mul[(digit_a, digit_b)]*10**(idx_a + idx_b)
            
    return res
    
def fibonacci(i):   
    tmp = [1, 1]
    
    for i in range(i-2):
        tmp.append(tmp[-1]+tmp[-2])
        
    return tmp[-1]
    
def tower_of_hanoi(i, from_rod, passing_rod, to_rod):
    res = ''
    
    if i == 1:
        res += 'move %d from %s to %s\n'%(i, from_rod, to_rod)
    else:
        res += tower_of_hanoi(i-1, from_rod, to_rod, passing_rod)
        res += 'move %d from %s to %s\n'%(i, from_rod, to_rod)
        res += tower_of_hanoi(i-1, passing_rod, from_rod, to_rod)
    
    return res
        
        
if __name__ == '__main__':
    print(multiply('1', '2'))
    print(multiply('1232', '212'), 1232*212)
    # print(tower_of_hanoi(3, 'A', 'B', 'C'))