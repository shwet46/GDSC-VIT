from collections import defaultdict

def count_word_frequencies(sentence):
    word_frequency = defaultdict(int)

    words = sentence.split()

    for word in words:
        word = word.strip('.,!?').lower() 
        word_frequency[word] += 1

    return word_frequency

def main():
    sentence = input("Enter a sentence: ")
    word_frequency = count_word_frequencies(sentence)

    print("Word frequencies:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
