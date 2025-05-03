# operasi aritma

a = 10
b = 3

# operasi penjumlahan
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan
hasil = a - b
print(a,'-',b, '=',hasil)

# operasi perkalian
hasil = a * b
print(a,'*',b, '=',hasil)

# operasi pembagian
hasil = a / b
print(a,'/',b, '=',hasil)

# operasi eksponen
hasil = a ** b
print(a,'**',b, '=',hasil)

#operasi modulus
hasil = a % b
print(a, '%',b, '=',hasil)

# operasi floor division
hasil = a // b
print(a, '//',b, '=',hasil)

#prioritas operasi, operatioana precedence
# urutan operasi
# 1. ()
# 2. **
# 3. *, /, //, %, +, -
# 4. +, -

x = 3
y = 2
z = 4

hasil = (x + y) * z
print('(', x, '+', y, ')', '*', z, '=', hasil)

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)
# hasil = 3 ** 2 * 4 + 3 / 2 - 2 % 4 // 3
# hasil = 9 * 4 + 3 / 2 -2 % 2 // 3
# hasil = 36 + 1.5 - 0 = 37.5
