input_filename = 'C:\\Users\\amacias5\\Documents\\Python\\coursera\\C_Mod_1\\stores.txt'
output_filename = 'C:\\Users\\amacias5\\Documents\\Python\\coursera\\C_Mod_1\\server_storesAZ.txt'

with open(input_filename, 'r') as fi, open(output_filename, 'w') as f:
    contents = fi.read().splitlines()
    for line in contents:
        number = line.strip().split('\t')[0]
        
        # Asegurarse de que el número tenga exactamente 4/5 dígitos
        number = number.zfill(4)
        
        #output_line = number + "\n"
        output_line = "s" + number + ".autozone.com\n"
        f.write(output_line)