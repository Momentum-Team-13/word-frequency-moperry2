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
        read_file= open_file.readlines()
    print(read_file)
        #print(len(open_file))
        
#step 2: calculate the frequency of words in the file
freqs = {}
for word in text:
    if word not in freqs:
        freqs[word] = 1
    else:
        freqs[word] += 1
file.close()

#step 3: Create funciton possibly (reg x) to remove punctiation
    #text.translate(str.maketrans('', '', string.punctuation))
#step 4: use lowercase function
#step 5: remove "stop words"
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
