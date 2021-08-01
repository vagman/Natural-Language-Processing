from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

class Tokenizer():

    # Creare list of the sentances of the given text
    def tokenize_sentences(self, raw_text: str):
        sentences = sent_tokenize(raw_text)

        return sentences

    # Create list of words from a given list of sentences
    def tokenize_words(self, sentence_list: list):
        words = []
 
        for sentence in sentence_list:
            words_of_sentece = word_tokenize(sentence)
            words.append(words_of_sentece)

        return words