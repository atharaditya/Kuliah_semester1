# program 3 menghitung biner

print('menghitung biner')
A = int(input('masukan nilai A : '))
B = int(input('masukan nilai B : '))
print(f'nilai biner dari {A} adalah ',format(A,'08b'))
print(f'nilai biner dari {B} adalah ',format(B,'08b'))

print('')
L = A | B

print('nilai a OR b : ', L)
print('nilai biner dari a OR b adalah ',format(L,'08b'))
print('')
D = A & B
print('nilai a AND b : ', D)
print('nilai biner dari a AND b adalah : ',format(D,'08b'))
print('')
print('')
E = A ^ B
print('nilai a XOR b : ', E)
print(f'nilai biner dari a XOR b adalah : ',format(E,'08b'))
print('')
print('')
A = ~A
B = ~B
print(f'nilai ~A : {A} dan nilai ~B adalah {B}')
print('nilai biner dari ~A adalah : ',format(A,'08b'))
print('nilai biner dari ~B adalah : ',format(B,'08b'))