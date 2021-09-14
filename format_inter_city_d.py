
file = open('att48_d.txt', 'r')
file_csv = open('att48_d_formated.txt', 'w')

for line in file:
    exploded_line = line.split(' ')
    exploded_line = [x.replace('\n','') for x in exploded_line if x != '']

    write_string = ''

    for index,elem in enumerate(exploded_line):
        if index != len(exploded_line)-1:
            write_string += elem+' '
        else:
            write_string += elem+'\n'

        file_csv.write(write_string)

file_csv.close()
file.close()