'''
with open("macbook.txt","a") as dosya:
    dosya.write("merhaba ugurcan?n bilgisayar?na ho?geldiniz.Iyi g?nler ve iyi ?al??malar dileriz..")


with open("macbook.txt","r") as dosya:
    dosya.seek(2)
    str1=dosya.read(10)

    print(str1)



with open("macbook.txt","r+") as dosya:
    data=dosya.read()
    dosya.seek(0)
    data="yaaaaa yine mi ptyhon\n"+data
    dosya.write(data)
'''

with open("macbook.txt","r+") as dosya:
    data=dosya.readlines()
    data.insert(1,"yaaaaaa ne salak bir ?ey oldu bu\n")
    dosya.seek(0)
    dosya.writelines(data)
