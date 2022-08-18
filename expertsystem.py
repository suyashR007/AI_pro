# -*- coding: utf-8 -*-
"""

@author: afaan

PROGRAM :- EXPERT SYSTEM
"""


knowledge_base={
    'commonflu':['muscle pain','cough','fever','runny nose','sneezing','sore throat'],
    'coronavirus':['loss of taste','loss of smell','sore throat','cough','fever','shortness of breath']
}
def inference(symptoms):
    probabilty={}
    for disease in knowledge_base.keys():
        count=0
        for symptom in knowledge_base[disease]:
            if symptom in symptoms:
                count+=1
        probabilty[disease]=count/len(knowledge_base[disease])

    maxprobability=0
    for disease in probabilty.keys():
        if probabilty[disease]>maxprobability:
            maxprobability=probabilty[disease]
    
    diseases=''
    for disease in probabilty.keys():
        if probabilty[disease]==maxprobability:
            diseases+=disease+', '

    diseases=list(diseases)
    diseases[-2]='.'
    diseases=''.join(diseases)
    
    if maxprobability==1:
        print('You are having '+diseases)
    elif maxprobability>0:
        print('You may have '+diseases)
    else:
        print('You are not having any disease')

def askquestions():
    symptoms=[]
    questions=[]
    for disease in knowledge_base.keys():
        questions+=knowledge_base[disease]

    questions=list(set(questions))
    print('Please answer the following questions: ')
    for question in questions:
        answer=input(f'Do you have {question} ? [yes/no] : ' )
        if answer=='yes':
            symptoms.append(question)
    print('')
    return symptoms

symptoms=askquestions()
inference(symptoms)









