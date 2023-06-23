def player() :
    score = 0
    with open('quizfile.txt') as quizfile:
        questionsstring = quizfile.read()
        questionslist = eval(questionsstring)
        for i in range(len(questionslist)):
            for j in range(len(questionslist[0]) - 1):
                print(questionslist[i][j])
            ans = input('Enter you choice (a/b/c): ')
            if ans == (questionslist[i][4]):
                score += 1
                print('Correct answer :)')
            else:
                print('Incorrect answer :(')
        print('You scored', score, 'out of', len(questionslist))


def admin():
    choice = input('What do you want to do?\n(a)Display quiz.\n(b)Add a question to the quiz.\n(c)Go back.\n\nEnter choice: ')
    if choice == 'a':
        print('\n\n--------Displaying quiz--------\n\n')
        with open('quizfile.txt') as quizfile:
            questionsstr = quizfile.read()
            questionslist = eval(questionsstr)
            for i in range(len(questionslist)):
                for j in range(len(questionslist[0]) - 1):
                    print(questionslist[i][j])
                print('Correct answer:', questionslist[i][4])
    elif choice == 'b':
        print('\n\n--------Preparing quiz for editing--------\n\n')
        Ques = []
        Ques.append(input('Enter the question: '))
        Ques.append(input('Enter the first option [eg: (a)option a]: '))
        Ques.append(input('Enter the second option: '))
        Ques.append(input('Enter the third option: '))
        Ques.append(input('Enter the correct option (a/b/c): '))

        with open('quizfile.txt') as quizfile:
            questionsstr = quizfile.read()
            questionslist = eval(questionsstr)
            questionslist.append(Ques)
        with open('quizfile.txt', 'w') as quizfile:
            quizfile.write(str(questionslist))
    elif choice == 'c':
        menu()


def menu():
    print('--------Welcome to the quiz!--------')
    username = input('Enter username to start: ')
    username = username.upper()
    if username == 'PLAYER':
        password = input('Enter the password to begin:')
        if password == 'abc123':
            print('Entering the quiz...')
            player()
        else:
            print('The password is incorrect.')
    elif username == 'ADMINISTRATOR':
        password = input('Enter the password to begin:')
        if password == 'def456':
            print('Allowing edit access...')
            admin()
        else:
            print('The password is incorrect.')
    else:
        print('Kindly enter a valid username!')

menu()