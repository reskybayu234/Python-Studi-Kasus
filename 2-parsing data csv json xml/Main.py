import csv
siswa = [
    ('yuniar supardi','A',90),
    ('nia yusnia','B',85),
    ('tanio noor','A',80),
    ('ganesha noor','B',90),
    ('zumastina','C',70)
]

f = open("/Pemrograman/python_mini/2-parsing data csv json xml/siswa.csv","w")
w = csv.writer(f)
w.writerow(('nama','kelas','nilai'))

# menulis file csv
for i in siswa:
    w.writerow(i)

# menutup file csv
f.close()