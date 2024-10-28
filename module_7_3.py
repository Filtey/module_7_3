class WordsFinder:
    file_name = []
    def __init__(self, *file_name):
        for value in file_name:
            self.file_name.append(value)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for value in self.file_name:
            with open(value, 'r') as file:
                str = file.read().lower()
                str = str.replace('\n', '')

                for symbol in str:
                    if (symbol in punctuation):
                        str = str.replace(symbol, ' ')

                all_words[value] = str.split(' ')
        return all_words


    def find(self, word):
        word_pos = {}
        all_words = self.get_all_words()

        for key, value in all_words.items():
            pos = value.index(word.lower())
            word_pos[key] = pos + 1
        return word_pos

    def count(self, word):
        word_count = {}
        all_words = self.get_all_words()
        rez = 0

        for key, value in all_words.items():
            for i in value:
                if(i == word.lower()):
                    rez += 1
            word_count[key] = rez
        return word_count



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



