import random
from bcolors import bcolors
import shutil

class question:
    def __init__(self,lines):
        self.completed = False
        if len(lines)>2:
            self.qtype="MCQ"
        else:
            self.qtype="FILL"
        self.q = lines[0][2:-1]
        if self.qtype=="MCQ":
            self.opts = [l[:-1] for l in lines[1:]]
            for i,l in enumerate(self.opts):
                if l[0]=='!':
                    self.correct = i
                    self.opts[i]=self.opts[i][1:]
        else:
            self.correct=lines[1][:-1].split("|")

    def __str__(self):
        if self.qtype == "MCQ":
            return(self.q+"\n"+"".join(["   (" + chr(ord('a')+i) + ") "+opt+"\n" for i, opt in enumerate(self.opts)])[:-1])
        else:
            return self.q

    def getCorrect(self):
        if self.qtype=="MCQ":
            return self.opts[self.correct]
        elif self.qtype=="FILL":
            return " or ".join(self.correct)

    def check(self,ans):
        ans=ans.lower()
        if self.qtype=="MCQ":
            if len(ans)==1:
                match ans:
                    case 't':
                        ans='a'
                    case 'f':
                        ans='b'
                return ord(ans) - ord('a') == self.correct
            elif len(ans) > 1:
                return ans==self.opts[self.correct].lower()
            else:
                return False
        elif self.qtype=="FILL":
            return ans in q.correct


        
s = open("cis475exam1.txt",'r').readlines()
term_width, _ = shutil.get_terminal_size()

questions=[]
lines=None
for i,l in enumerate(s):

    if l[0] == "Q":
        if lines is not None:
            questions.append(question(lines))
        lines=[l]
        continue
    if l!='\n':
        lines.append(l)
questions.append(question(lines))

random.shuffle(questions)

num_correct=0
while num_correct < len(questions):
    for q in questions:
        if q.completed:
            continue
        print("═"+"\u2550"*(term_width-2)+"═")
        print(q)
        ans = input("answer: ")
        if q.check(ans):
            print(f"{bcolors.GREEN}correct{bcolors.ENDC}")
            num_correct+=1
            q.completed = True
        else:
            print(f"{bcolors.RED}incorrect{bcolors.ENDC}")
            print(f"{bcolors.YELLOW}The correct answer was:{bcolors.ENDC}\n"+q.getCorrect())
    print("-"*150)

    percent=num_correct/len(questions)

    print()
    tmp=0
    for i in range(100):
        if tmp < percent:
            print(f'{bcolors.GREEN}\u2588{bcolors.ENDC}',end='')
        else:
            print(f'{bcolors.RED}\u2591{bcolors.ENDC}',end='')
        tmp+=.01
    print()
    print(f"{percent*100:.2f}%")



