num = count = 1

while True:
    count = 0
    num = int(input('Digite um número inteiro: '))
    if num < 0: break
    
    while count <= 10:
        print(f'{num} X {count} = {num * count}')
        count += 1
