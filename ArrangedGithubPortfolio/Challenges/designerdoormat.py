nmIn = input().split(" ")
nmMap = list(map(int,nmIn))
n = nmMap[0]
m = nmMap[1]
welcomePos = (n // 2) + 1
changNum = 3
dotpipedot = 1
md2 = m // 2
for _ in range(welcomePos - 1):
    print(f'{"-"* (md2 - (changNum - 2)) }{".|." * dotpipedot}{"-"* (md2 - (changNum - 2))}')
    changNum += 3
    dotpipedot += 2
print(f"{'-' * ((m // 2) - 3)}WELCOME{'-' * ((m // 2) - 3)}")
changNum -= 3
dotpipedot -= 2
for _ in range(welcomePos - 1):
    print(f'{"-"* (md2 - (changNum - 2))}{".|." * dotpipedot}{"-"* (md2 - (changNum - 2))}')
    changNum -= 3
    dotpipedot -= 2
