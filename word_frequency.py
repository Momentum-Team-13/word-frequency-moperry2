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
        # dictionary_count = count_dict(frequency_count)
        new_list = sorted(frequency_count.items(), key=lambda item: item[1], reverse=True)
        for x in new_list:
            print(f"{x[0]:16} | {x[1]} {'*' * x[1]}")
    
#step 2: calculate the frequency of words in the file
def frequency_counter(text):
    freqs = {}
    for word in text:
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
    # print(freqs)
    return freqs

#step 3: Create funciton possibly to remove punctuation
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
