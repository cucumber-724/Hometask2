def merge_files(input_files, output_files):
    files = []
    for file_1 in input_files:
        with open(file_1, 'r', encoding='utf-8') as inp_f:
            lines_1 = inp_f.readlines()
            files.append(
                {'name': file_1, 'line_count': len(lines_1), 'text': lines_1})

    files.sort(key=lambda x: x['line_count'])

    with open(output_files, 'w', encoding='utf-8') as out_f:
        z = 0
        for file_2 in files:
            if z == 0:
                out_f.write(f"{file_2['name']}\n")
                out_f.write(f"{file_2['line_count']}\n")
                out_f.writelines(file_2['text'])
                z += 1
            else:
                out_f.write(f"\n{file_2['name']}\n")
                out_f.write(f"{file_2['line_count']}\n")
                out_f.writelines(file_2['text'])

    with open('4.txt', 'r', encoding='utf-8') as q:
        text = q.read()
        print(text)


input_files = ['1.txt', '2.txt', '3.txt']
output_file = '4.txt'

merge_files(input_files, output_file)
