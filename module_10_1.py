from threading import Thread
from time import sleep
from datetime import datetime

time_start1 = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}' + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    return

ans1 = write_words(10, 'example1.txt')
ans2 = write_words(30, 'example2.txt')
ans3 = write_words(200, 'example3.txt')
ans4 = write_words(100, 'example4.txt')

time_end1 = datetime.now()
elapsed_time1 = time_end1 - time_start1
print(elapsed_time1)

time_start2 = datetime.now()
thr1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

time_end2 = datetime.now()
elapsed_time2 = time_end2 - time_start2
print(elapsed_time2)