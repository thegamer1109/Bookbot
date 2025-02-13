def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else: 
            dict[char] = 1

if __name__ == "__main__":

    try:
        with open("books/frankenstein.txt", 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("The file was not found.")
        exit(1)
        
    print(count_characters(text))
    