import csv

vocab = {}

with open('german.csv', newline='') as csvfile:
    vocab_file = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in vocab_file:
        vocab[row[0]] = row[1]

for word in vocab:
    
    if len(word) < 5: tab = "\t\t\t"
    elif len(word) > 15: tab = "\t"
    else : tab = "\t\t"
    
    print(word,tab,end="")
    given_word = input()
    while vocab[word] != given_word:
        print("Try again or type 'help'")
        print(word,tab,end="")
        given_word = input()
        if given_word.lower() == "help":
            print("'"+word+"' is '"+vocab[word]+"'")
            break

print("You've drilled",len(vocab),"words! Good job!")