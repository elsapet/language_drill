import csv

vocab = {}

file_name = input("Please enter file name e.g. 'vocab.csv'\n")

with open(file_name, newline='') as csvfile:
    vocab_file = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in vocab_file:
        vocab[row[0]] = row[1]

print("Ready? Here we go!\n")

for word in vocab:
    
    given_word = input(word+"\t\t")
    while vocab[word] != given_word:
        print("Try again or type 'help'")
        given_word = input(word+"\t\t")
        if given_word.lower() == "help":
            print("'"+word+"' is '"+vocab[word]+"'")
            break

print("\nYou've drilled",len(vocab),"words! Good job!")