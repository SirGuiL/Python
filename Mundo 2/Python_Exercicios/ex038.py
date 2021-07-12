nums = []
count = 1

while count <= 2:
    nums += [int(input('Digite um número inteiro: '))]
    count += 1

if(nums[0] > nums[1]):
    print('O primeiro valor é maior.')
elif(nums[0] < nums[1]):
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais.')
