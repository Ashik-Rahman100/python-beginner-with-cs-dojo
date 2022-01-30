# Input two words, show the letters which are common in both words. If no match, then print "No Match"

first_word = input("Enter your first input: ");  #"dhaka"
second_word = input("Enter your second input: ")  #"khulna";

for i in first_word:
    for j in second_word:
        if(i == j):
            common_word = set(first_word)&set(second_word);
            print(common_word);
        else:
            print("No Match");

     



        

