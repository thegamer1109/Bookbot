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
    return dict

def print_report(text):
    alphabet = [chr(i) for i in range(97, 123)]
    print(count_words(text), " words found in the document")
    for char, count in count_characters(text).items():
        if char in alphabet:
            print(f"The '{char}' character was fount {count} times")
    print("--- End Report ---")

if __name__ == "__main__":

    try:
        with open("books/frankenstein.txt", 'r') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print("The file was not found.")
        exit(1)
        
    print(print_report(text))
    