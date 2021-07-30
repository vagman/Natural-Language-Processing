class ReadFile():
    
    def read_from_file(self):
        txt_file_given = str(input("Enter the file for Lexical Analysis: "))
        
        try:
            with open(txt_file_given , encoding="utf8") as f:
                text = f.readline()
            f.close()
            return text
            
        except FileNotFoundError as e:
            print("File was not fond.\nError message: {}".format(str(e)))
    
    