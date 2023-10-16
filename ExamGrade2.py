level = (int(input("What level of exam are you taking?: ")))
grade = (int(input("What was your grade?: ")))


if level == 1:
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
        
if level == 2:
    if 66 <= grade <= 100:
        print ("Distinction")
    elif 51 <= grade <= 65:
        print ("Merit")
    elif 50 <= grade <= 50:
        print ("Pass")
    elif 40 < grade:
        print ("You failed the exam :(")
    else:
        print ("Error: marks must be between 1 and 100")
    
