from time import sleep

def counter(start, end, step):
    if start < end:
        count = start
        while count <= end:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count += step
        print('')
    else:
        count = start
        while count >= end:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count -= step
        print('')


# programa principal
print('Contando de 1 a 10')
counter(1, 10, 1)
print('Contando de 10 a 1, com passo 2')
counter(10, 1, 2)

start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))

counter(start, end, step)
