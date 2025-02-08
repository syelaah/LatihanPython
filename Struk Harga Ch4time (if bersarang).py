print("PROGRAM STRUK HARGA CH4TIME")
nama=input("Nama pembeli:")
print("Menu varian:\n1.Ch4time Milk Tea \n2.Matcha Milk Tea \n3.Brown Sugar Milk Tea \n4.Apple Milk tea \n5.Caramel Milk Tea")
menu=input("Pilih menu:")
temp=input("Temperatur (hot/cold):")
size=input("Size (regular/large):")
print("Topping:\n1.Pearl \n2.Coffe Jelly")
topping=input("Pilih Topping:")
if menu=='Ch4time Milk Tea':
    harga=23000
    if size=='regular':
        harga_tambahan=0
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000
    elif size=='large':
        harga_tambahan=3000
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000 
elif menu=='Matcha Milk Tea':
    harga=23000
    if size=='regular':
        harga_tambahan=0
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000
    elif size=='large':
        harga_tambahan=4000
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000       
elif menu=='Brown Sugar Milk':
    harga=21000
    if size=='regular':
        harga_tambahan=0
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000
    elif size=='large':
        harga_tambahan=2000
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000            
elif menu=='Apple Milk Tea':
    harga=21000
    if size=='regular':
        harga_tambahan=0
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000
    elif size=='large':
        harga_tambahan=5000
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000         
elif menu=='Caramel Milk Tea':
    harga=23000
    if size=='regular':
        harga_tambahan=0
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000
    elif size=='large':
        harga_tambahan=3000
        if topping=='Pearl':
            harga_topping=3000
        elif topping=='Coffe Jelly':
            harga_topping=4000
hartot=harga+harga_tambahan+harga_topping
print("                                                             STRUK HARGA PEMBELIAN                                                     ")
print("=======================================================================================================================================")
print(" | Nama Pembeli    | Menu              | Size    | Temp    | Harga   | Tambahan Harga (L) | Topping | Harga Topping  | Total Harga   | ")
print(" | %s          "%(nama),"| %s  "%(menu),"| %s  "%(size),"| %s    "%(temp),"| %i  "%(harga),"| %i              "%(harga_tambahan),"| %s   "%(topping),"| %i         "%(harga_topping),"| %i        "%(hartot),"|")



      
