import re
textStr = "From john.doe@ab.etc Thu Jun 15 02:04:09 2010"
#Q1: extract email extension
output=re.findall(r'\@(\w+\S\w+)',textStr)

#list_of_string=textStr.split('@')
#output=re.findall(r'\w+\S\w+',list_of_string[1])
print(output)

#Q2: Extract email from the above string using re.findall
output=re.findall(r'[^"From"]\w+\.?\w+\@\w+\.\w+',textStr)
print(output)

#Q3: Extract 'From: Using the :' from the above string x. [Use re.findall]
x ='From: Using the : character'
output=re.findall(r'^F.+:',x)
print(output)

MathScores = """
Ann got 99 and Maria got 95,
David got 84 and Jose got 21
"""
MathScores_List=MathScores.split(',')
line1=MathScores_List[0].split()
line2=MathScores_List[1].split()
Mathscores_Dict={}
i=0
j=0
count=0
while count<4:
    if count<2:
        search_string=' '.join(line1[i:i+3])
        Mathscores_Dict[(re.search(r'.\w+',search_string)).group()]=re.search(r'.\d+',search_string).group()
        count+=1
        i += 4
    else:
        search_string = ' '.join(line2[j:j + 3])
        Mathscores_Dict[(re.search(r'.\w+', search_string)).group()] = re.search(r'.\d+', search_string).group()
        j += 4
        count += 1
print(Mathscores_Dict)


