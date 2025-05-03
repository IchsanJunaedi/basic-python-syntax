# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

#celcius
celcius = float(input("Masukan suhu dalam celcius:"))
print("suhu dalam celcius adalah: ",celcius, "celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah: ",reamur, "reamur")

# fahrenheit
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah: ",fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah: ",kelvin, "kelvin")

# fahrenheit ke kelvin
kelvin2 = ((fahrenheit - 32) * 5 / 9) + 273 
print("suhu dalam kelvin (dari fahrenheit): ",kelvin2, "kelvin")

# kelvin ke fahrenheit
fahrenheit2 = ((kelvin - 273)) *9/5 + 32
print("suhu dalam fahrenheit (dari kelvin): ",fahrenheit2, "fahrenheit")
