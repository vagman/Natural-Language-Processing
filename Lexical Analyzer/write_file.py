from nltk.tokenize import sent_tokenize


class WriteFile():

    # Write the words as list of lists in a txt file
    def write_to_file(self, unsaved_text):
        with open("tokenized_text.txt", "w+", encoding = "utf8") as f:
            for sentance in unsaved_text:
                f.write(str(sentance) + "\n")
        f.close()