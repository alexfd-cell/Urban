import io

def custom_write(file_name, strings):
    strings_positions, i = {}, 1
    file = open(file_name, 'w', encoding='utf-8')
    for item in strings:
        tpl = ()
        tpl = (i, file.tell())
        strings_positions[tpl] = item
        file.write(item + '\n')
        i += 1
    file.close()
    return strings_positions


info = ['Text for tell.','Используйте кодировку utf-8.',
        'Because there are 2 languages!','Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)