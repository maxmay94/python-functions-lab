# 1. sum_to

def sum_to(arg):
  nums = [num for num in range(1, arg + 1)]
  return sum(nums)
print(sum_to(6))

def largest(list):
  big = 0
  for num in list:
    if num > big:
      big = num
  return big
print(largest([10, 4, 2, 231, 91, 54]))

def occurrences(str1, str2):
  return str1.count(str2)
print(occurrences('fleep floop', 'e'))