# # ACCEESING STUDENT CLASS FROM ANOTHERE FILE
#
# # from Student import Student
# # student1=Student("NAGARJ",3,"COLLEGE","BiTM")
# # student2=Student("NS",3,"COLLEGE","BiTM")
# # print(student1.sem)
#
# # QUIZ
# from Quiz_Question import Quiz_Question
# quiz_q=[
#     "color of apple? \n (a). Red\n (b). Orange\n (c). Black\n (d). Purple\n\n ",
#     "color of orange? \n (a). Red\n (b). Orange\n (c). Black\n (d). Purple\n\n ",
#     "color of bannannanna? \n (a). Red\n (b). Orange\n (c). Black\n (d). Purple\n\n ",
# ]
# questions=[
#     Quiz_Question(question_prompt[0],"a"),
#     Quiz_Question(question_prompt[1],"b"),
#     Quiz_Question(question_prompt[2],"c"),
# ]
# def run_test(questions):
#     score=0
#     for question in questions:
#         answer= input(question.prompt)
#         if answer == question.answer:
#             score+=1
#     print("u got"+str(score)+ "/"+str(len(question)))

# CLASS_-----FUNCTION

