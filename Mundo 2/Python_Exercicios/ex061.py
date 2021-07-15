nums = []
pa = []
count = 0

while count < 2:
    nums += [int(input('Digite o {}º número: '.format(count + 1)))]
    count += 1

diff = nums[1] - nums[0]

count = nums[0]

while count <= diff * 10:
    pa += [count]
    count += diff

print('Progressão aritmética: {}'.format(pa))
