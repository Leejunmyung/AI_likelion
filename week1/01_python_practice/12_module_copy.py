file1 = 'smalldog.jpeg'
backup = "smalldog_back04.jpeg"

infile = open(file1, 'rb')
outfile = open(backup, 'wb')

for i in range(5):
    copy_buffer = infile.read(1024)
    outfile.write(copy_buffer)

infile.close()
outfile.close()
print("복사완료")