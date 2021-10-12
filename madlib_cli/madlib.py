
import re
from typing import Text  # for regex  




def read_template(path):
    content = open(path )
    
    return content.read()

    

def parse_template(constant):
   
    actual=''
    actual_parts=[]

    Text = constant.split(' ')
    print(Text)
    res=r"^{\w+}|\.$"
    for i in Text:
        if re.match(res,i)==None :
            actual+=f"{i} "
        else :
            if i==Text[-1]:
                actual+='{}.'
                actual_parts+=[i[1:-2]]
            else:
                actual_parts+=[i[1:-1]]
                actual+='{} '

    actual_parts=tuple(actual_parts)
    return (actual,actual_parts)
 
  


def  merge(constant , words):
    list = parse_template(constant)
    return (re.sub(r' {[^}]*}',' {}',constant)).format(*words)

# print(merge("It was a {} and {} {}.", ("dark", "stormy", "night")))

def copyFile(text):
    print(text)
    file = open("assets/dark_and_stormy_night_template_copy.txt",'w')
    file.write(text)

if __name__ == "__main__":
    print("Welcome to Madlib Game")
    print("You will be asked to input some words to play the game !!!")
    content = read_template("assets/dark_and_stormy_night_template.txt")
    lst = parse_template(content)
    words=[]
    for i in range(len(lst)):
        words.append(input("enter a {} ".format(lst[i])))
    toCopy = merge(content, words)
    copyFile(toCopy)

    