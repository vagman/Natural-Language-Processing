from read_file import ReadFile
from tokenizer import Tokenizer
from write_file import WriteFile

# Create objects of the classes we created
read = ReadFile()
tok = Tokenizer()
write = WriteFile()

# Initialize sentence list: ex. ['sentence A', 'sentence B', ...]
sentences_list = tok.tokenize_sentences(read.read_from_file())

# Initialize words list: ex. [['word A1', 'word A2'], [word B1], [word B2], ...]
write.write_to_file(tok.tokenize_words(sentences_list))