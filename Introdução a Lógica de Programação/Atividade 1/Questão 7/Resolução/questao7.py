N, XP = input().split()
XPY, XPL, XPA = input().split()
N = int(N)
XP = int(XP)
XPY = int(XPY)
XPL = int(XPL)
XPA = int(XPA)
xpTotal = N*XP
XPY += xpTotal
XPL += xpTotal
XPA += xpTotal
print(f'Yoda {XPY}')
print(f'Luke {XPL}')
print(f'Ahsoka {XPA}')