def convert (value, unit) :
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9 
    else:
        print("tidak ada unit yang sesuai")
        
value = int(input("Masukkan nilai suhu: "))
unit = input("Masukkan unit suhu (C/F): ")
result = convert(value, unit)
print(f"Hasil konversi: {result}")