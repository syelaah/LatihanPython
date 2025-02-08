#contoh if bersarang
nama=input ("nama karyawan:")
nik=input("NIK karyawan:")
status=input("status (staff/honor):")
gol=input("Golongan (A/B/C):")
if status=='staff':
    gaji=1000000
    if gol=='A':
        bonus=200000
    elif gol=='B':
        bonus=400000
    elif gol=='C':
        bonus=550000
elif status=='honor':
    gaji=750000
    if gol=='A':
        bonus=150000
    elif gol=='B':
        bonus=275000
    elif gol=='C':
        bonus=350000
gatot=gaji+bonus
print("Gaji=",gaji)
print("Bonus=", bonus)
print("Gaji total=",gatot)
