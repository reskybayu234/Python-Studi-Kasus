array_number = ["324234254874","5678","3456"]
aa = []
for i in range(len(array_number)):
    array_number_str = []
    helper = []
    array_number_str_helper = []
    helper = str(array_number[i])
    for j in helper:
        if j != "4" and j != "5":
            array_number_str.append(j)
        else:
            array_number_str.append("*")
    array_number_str_helper = ''.join(array_number_str)
    aa.append(array_number_str_helper)
print(aa)