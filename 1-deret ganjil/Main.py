posisi = int(input("posisi : "))
i = 0
b = 1
jml = 0
for i in range(posisi):
    jml = jml + 2*b-1
    b = b+1

print("jumlah deret ",(jml))