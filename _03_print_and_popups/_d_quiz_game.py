from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question_1 = simpledialog.askstring('Question', "Do you play video games?")
    #      // 3.  Use an if statement to check if their answer is correct
    if question_1 == "yes":
        score = (score +1)
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    question_2 = simpledialog.askstring('Question', "Do you follow any shows?")
    if question_2 == "yes":
        score = (score +1)
    else:
        score = (score -1)
    question_3 = simpledialog.askstring('Question', "Do you follow sports?")
    if question_3 == "yes":
        score = (score +1)
    else:
        score = (score -1)
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    print(str(score))
    # Run the window's .mainloop() method
    window.mainloop()
