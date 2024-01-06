class WordCounter:

    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = input("Enter a sentence: ")

    def string_spliter(self):
        if self.string == '':
            return 0
        
        split_string = len(self.string.split())
        return split_string
    
wordcounter = WordCounter()
wordcounter.get_string()
print(wordcounter.string_spliter())

        
