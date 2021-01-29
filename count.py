import sys
str1 = " "
alphabets = digits = special = 0

for line in sys.stdin:
    str1 = line
    for i in range(len(str1)):
        if((str1[i] >= 'A' and str1[i] <= 'Z') or (str1[i] >= 'a' and str1[i] <= 'z')): 
            alphabets = alphabets + 1 
        elif(str1[i] >= '0' and str1[i] <= '9'):
            digits = digits + 1
        else:
            special = special + 1

sys.stdout.write("Total Angka: " + str(digits) + "\n\n")
sys.stdout.write("Total Huruf: " + str(alphabets) + "\n\n")
sys.stdout.write("Total Symbol: " + str(special) + "\n\n")

