# 1.
def sum_to(arg):
  nums = [num for num in range(1, arg + 1)]
  return sum(nums)
print(sum_to(6))

# 2.
def largest(list):
  big = 0
  for num in list:
    if num > big:
      big = num
  return big
print(largest([10, 4, 2, 231, 91, 54]))

# 3.
def occurrences(str1, str2):
  return str1.count(str2)
print(occurrences('fleep floop', 'e'))

# 4.
import math
def product(*args):
  return math.prod(args)
print(product(-1, 4))