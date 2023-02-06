n = int(input('Digíte um número: '))
c = 0

for i in range(1, n + 1):
    if n % i == 0:
        c += 1
        print("\033[32m", end='')
    else:
        print("\033[31m", end='')

    print(f'{i} ', end='')

if c == 2:
    print('\n\n\033[mEsse número foi divisível 2 vezes então ele é primo')
else:
    print(f'\n\n\033[mEsse número foi dividido {c} ves(zes) então ele não é primo')
