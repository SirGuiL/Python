nums = []
pa = []

for c in range(0, 2):
    nums += [int(input('Digite o {}º número: '.format(c + 1)))]

diff = nums[1] - nums[0]

for c in range(nums[0] - diff * 5, diff * 5, diff):
    pa += [c]

print('Progressão aritmética: {}'.format(pa))
