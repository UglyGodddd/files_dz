files_list = ['text_1.txt', 'text_2.txt']

text_list = []
for file in files_list:
    with open(file, encoding='utf-8') as text_file:
        file_r_list = text_file.readlines()
        text_list.append((file, len(file_r_list), file_r_list))
            

text_list.sort(key=lambda i: i[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for name_file, len_file,texts in text_list:
        result_file.write(f'{name_file}\n')
        result_file.write(f'{len_file}\n')
        for text in texts:
            result_file.write(f'{text}')
        result_file.write(f'\n') 
        

