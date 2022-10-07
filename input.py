a = input()
print(a) #1 2 3

a = input("입력: ")
print(a) #1 2 3

a = input().split()
print(a) #['1', '2', '3']

a = list(input().split())
print(a) #['1', '2', '3']

a = tuple(input().split())
print(a) #('1', '2', '3')

a = map(int, input().split())
print(a) #<map object at 0x0000017FBDBBFFA0>

a = list(map(int, input().split()))
print(a) #[1, 2, 3]

a = tuple(map(int, input().split()))
print(a) #(1, 2, 3)

a, b, c = input().split()
print(a) #1
print(b) #2
print(c) #3