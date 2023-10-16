grade = (int(input("What was your grade?: ")))

if 71 <= grade <= 100:
    print ("Distinction")
elif 61 <= grade <= 70:
    print ("Merit")
elif 50 <= grade <= 60:
    print ("Pass")
elif 50 < grade:
    print ("You failed the exam :(")
else:
    print ("Error: marks must be between 1 and 100")
    
