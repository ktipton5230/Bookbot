def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text) #prints out the text of the frankenstein.txt file, used as a testcase for first part of project.

    amount_of_words = word_count(text)
    #print(f"{amount_of_words} words are found in this book.") # this printed the total words in the text, used for the second part of the project.

    #amount_of_letters = letter_count(text)
    #print(f"{amount_of_letters} letters are found in this book.") #last step prior to the actual report, printing out the letters withing the text.

    letters = letter_count(text)
    book_report = report(letters)
    sorted_report = sorted(book_report, key=lambda x: x['name']) #I wanted to take the project 1 step farther, this sorts the dictionaries alphabetically.

    #print(book_report) # used as the original test print to see if the program was working as intended. It was! :)
    print("****This is the beginning of the letter report for frankenstein!****")
    print()#newline for clarity in output
    print(f"{amount_of_words} words are found in this book.")
    print()#newline for clarity in output
    for item in sorted_report:
        print(f"The letter '{item['name']}' was found {item['count']} times")

    print()#newline for clarity in output
    print("****Thank you for looking at this project! This completes the report!****")

def get_book_text(path): # opens up the frankenstein.txt file and returns the text to the program to be printed out
    with open(path) as f:
        return f.read()

def word_count(text): # counts the words in the book and returns the number to the console
    words = text.split()
    return len(words)

def letter_count(text):# counts the letters after adding them to a dictionary
    lower_case = text.lower() # takes the texts and makes all of the letters lowercase for easier counting
    letters = {}
    for l in lower_case:
        if l.isalpha():#used to sort out the non-alphabet characters in the text.
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
    return letters

def sort_on(letters): #
    return letters["count"]

def report(letters): # this function seperates each letter into a different dictionary and then appends that dictionary to an empty list for the report.
    list_of_dicts = []
    for letter, count in letters.items():
        letter_dict = {"name": letter, "count":count}
        list_of_dicts.append(letter_dict)
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts


main()