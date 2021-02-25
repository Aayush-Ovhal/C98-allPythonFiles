def countWords():
    inputFile = input("Enter the file name: ")
    openFile = open(inputFile, 'r')
    
    countWords = 0

    for i in openFile:
        wordCount = i.split()
        countWords += len(wordCount)
        print(wordCount)
        print("The no. of words are: " + str(countWords))

countWords()
    
