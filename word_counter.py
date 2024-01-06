class WordCounter:
    def __init__(self):
        self._string = ''

    def set_string(self, user_input):
        if isinstance(user_input, str):
            self._string = user_input.strip()  # Remove leading/trailing spaces

    def count_words(self):
        """Count the number of words in the provided string."""
        if not self._string:
            return 0
        
        # Split the string by spaces and count the words
        return len(self._string.split())

# Example Usage:
word_counter = WordCounter()
user_input = input("Enter a sentence: ")

word_counter.set_string(user_input)
word_count = word_counter.count_words()
print(f"Number of words: {word_count}")
