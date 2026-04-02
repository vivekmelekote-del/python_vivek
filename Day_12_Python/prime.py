def is_prime(num):
    count = 0
    for i in range(2, int(num / 2)):
        if num % i == 0:
            print(f"{num} % {i} = {num % i}")
            count += 1
    if count > 0:
        return False
    else:
        return True
    
print(is_prime(73))