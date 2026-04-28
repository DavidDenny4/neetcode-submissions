class TextProcessor:
    # Implement method overloading for format_text method
    # pass
    def format_text(self, first:str, second:str = ""):
        if second == "":
            return str.upper(first)
        else:
            return first + second



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
