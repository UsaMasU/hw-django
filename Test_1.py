import sys


def dig_in(fst, lst):
    dig_set = set()
    dig_list = list()
    for i in range(fst, lst):
        dig_set.add(sys.stdin.readline().strip())
        dig_list.append(int(i))
        dig_list.sort()
    return dig_list


n = int(sys.stdin.readline().strip())
dig_set = set()
dig_list = list()

fst, lst = 0, n
cnt = -1
m = n // 2
ex = True

for i in range(fst, lst):
    cnt += 1
    dig_set.add(sys.stdin.readline().strip())
    dig_list.append(int(i))
    dig_list.sort()


print(dig_set)
dig_list.sort()

for i in dig_list:
    print(i)
