import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
#Step 1: use open to read in a text file
def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file. my code does here"""
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file= open_file.read()
        remove_punct = remove_punctuation(read_file)
        lower_case = use_lowercase(remove_punct)
        remove_stop = remove_stop_words(lower_case)
        frequency_count = frequency_counter(remove_stop)
    print(frequency_count)
        #print(len(open_file))
# def split_text(text):
#     return text.split()

#step 2: calculate the frequency of words in the file
def frequency_counter(text):
    freqs = {}
    for word in text:
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
    return freqs

#step 3: Create funciton possibly (reg x) to remove punctuation
    #text.translate(str.maketrans('', '', string.punctuation))
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
#step 4: use lowercase function
def use_lowercase(text):
    return text.lower()
#step 5: remove "stop words"
def remove_stop_words(text):
    text_list = text.split()

    for word in text_list.copy():
        if word in STOP_WORDS:
            text_list.remove(word)
    return text_list

#step 6: posisbly use dictionary to count each word

#step 7: find a way to format print statement...f string






if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
