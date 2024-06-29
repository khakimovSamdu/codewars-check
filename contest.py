# n = int(input())
# print(f'The next number for the number {n} is {n+1}.\nThe previous number for the number {n} is {n-1}.')

# f = open('INPUT.TXT')
# data = f.read()
# f.close()
# d = open('OUTPUT.TXT', 'w')
# d.write(str(data[-2]))
# d.close()


# a, b = map(int, input().split())
# s = a*b 
# if s>109 and s>0:
#     print(abs(s-109+1))
# elif 
# else:
#     print(abs(s))

# a, b = map(int, input().split())
# if (a>0 and b>0) or (a<0 and b>0):
#     print(a%(b))
# elif (a>0 and b<0):
#     print(a%abs(b))
# elif (a<0 and b<0) :
#     df = (abs(a)//abs(b))
#     k = (df+1)*abs(b)
#     print(a+k)

# qalam = 3
# ruch = qalam-2  = 1
# # ruch = flam - 7
# flam = 8

# h1, m1, s1 = map(int, input().split())
# h2, m2, s2 = map(int, input().split())
# td = (h2-h1)*3600 + (m2 - m1)*60 + s2-s1
# print(td)

# n = int(input())
# k = n%2
# t1 = (n//2)*15 + (n//2)*5
# if k==0:
#     t1 -= 15

# t1 = (t1 + 45*n)*60
# print(f'{t1//3600+9} {t1%3600//60}')

a, b, c = map(int, input().split())
h = a-b
day = b - c
print(h//day + 1)