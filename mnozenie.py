# -*- coding: utf-8 -*-
"""
@author: ppodl
"""



import random
#import math

def get_max_val():
    print("Wprowadz wartosc maksymalnego wyniku mnozenia w przedziale od 10 do 100. \n(np. wprowadzenie '50' spowoduje, ze w zadaniach nie pojawi\
          sie mnozenie, ktorego wynik jest wiekszy niz 50).")
    max_val = input()
    try:
        max_val = int(max_val)
    except:
        None
    if isinstance(max_val, int) != True or max_val <10 or max_val >100:
        get_max_val()
    else:
        return max_val

def get_next_round():
    print("Czy chcesz rozwiazac kolejnych piec zadan(t/n)?")
    decision = input()
    if decision.upper() not in ['T','N']:
        get_next_round()
    else:
        if decision.upper() == 'T':
            return True
        else:
            return False

def play():
    max_val = get_max_val() 
    nums = list(range(0,10))
    opers = []
    next_round = True
    for op1 in nums:
        for op2 in nums:
            opers.append([op1, op2, '*',op1*op2,' '.join([str(op1),'*',str(op2),'= '])])
    
    opers = [o for o in opers if o[3]<=max_val]
    while next_round:
        opers_todo_nums = random.sample(range(len(opers)), 5)
        tasks = []
        
        for numer in opers_todo_nums:
            tasks.append(opers[numer])
            
        score = 0 
        print("Otrzymasz {} zadan do rozwiaznia. Powodzenia!".format(len(tasks)))
        for i in range(len(tasks)):
            result = input(tasks[i][4]+"")
            tasks[i].extend([result])
            if result == str(tasks[i][3]):
                score = score + 1
                tasks[i].append(1)
            else:
                tasks[i].append(0)
        
        for i in range(len(tasks)):
            print("Dzialanie {}, twoja odpowiedz: {}, prawidlowa odpowiedz: {}, zdobyles {} punktow".format(tasks[i][4],tasks[i][5],\
                                                                                                        tasks[i][3],tasks[i][6]))
        try:         
            total_score = total_score + score
        except:
            total_score = score
        try:    
            total_tasks = total_tasks + len(tasks)
        except: 
            total_tasks = len(tasks)
    
        print("W tej rundzie zdobyles {} na {} mozliwych punktow, czyli {} %.".format(score,len(tasks),round(score/(len(tasks))*100)))
        print("To juz koniec tej rundy.")
        print("Do tej pory we wszystkich rundach zdobyles {} na {} mozliwych punktow ({}%)".format(total_score, total_tasks, round(total_score/total_tasks*100)))
        next_round = get_next_round()
    
    
   
play()

