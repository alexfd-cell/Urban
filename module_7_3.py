import string
class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words, words = {}, ''
        punc = [',', '.', '=', '!', '?', ';', ':', '-', '—']
        file_name = str(*self.file_names)
        with open(*self.file_names, encoding='utf-8') as file:
            for line in file:
                char_lines = ''
                for char in line:
                    if char not in punc:
                        char_lines += char
                words += char_lines.lower()
        words = words.split()
        all_words[file_name] = words
        return all_words

    def find(self, word):
        self.word = word.lower()
        required_word = {}
        file_name = str(*self.file_names)
        words = self.get_all_words().get(file_name)
        for i in range(len(words)):
            if self.word == words[i]:
                required_word[file_name] = i + 1
                break
        return required_word


    def count(self, word):
        self.word = word.lower()
        count_word, c = {}, 0
        file_name = str(*self.file_names)
        words = self.get_all_words().get(file_name)
        for item in words:
            if self.word == item:
                c += 1
        count_word[file_name] = c
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('CAPTAIN')) # 2-е слово по счёту
print(finder2.count('captaiN')) # 10 слов captain в тексте всего

# O Captain! My Captain!
#
# O Captain! my Captain! our fearful trip is done,
# The ship has weather’d every rack, the prize we sought is won,
# The port is near, the bells I hear, the people all exulting,
# While follow eyes the steady keel, the vessel grim and daring;
# But O heart! heart! heart!
# O the bleeding drops of red,
# Where on the deck my Captain lies,
# Fallen cold and dead.
#
# O Captain! my Captain! rise up and hear the bells;
# Rise up — for you the flag is flung — for you the bugle trills,
# For you bouquets and ribbon’d wreaths — for you the shores a - crowding,
# For you they call, the swaying mass, their eager faces turning;
# Here Captain! dear father!
# This arm beneath your head!
# It is some dream that on the deck,
# You’ve fallen cold and dead.
#
# My Captain does not answer, his lips are pale and still,
# My father does not feel my arm, he has no pulse nor will,
# The ship is anchor’d safe and sound, its voyage closed and done,
# From fearful trip the victor ship comes in with object won;
# Exult O shores, and ring O bells!
# But I with mournful tread,
# Walk the deck my Captain lies,
# Fallen cold and dead.
#
# Walt Whitman