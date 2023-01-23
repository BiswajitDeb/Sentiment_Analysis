import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#print(string.punctuation)
text=open('user_input.txt',encoding='utf-8').read()
print(text)
lower_case=text.lower()
punc_removed=lower_case.translate(str.maketrans('','',string.punctuation))
#Tokenizing sentences
tokenized_words=word_tokenize(punc_removed,"english")
#print(tokenized_words)

final_words=[]
for i in tokenized_words:
    if i not in stopwords.words('english'):
        final_words.append(i)
#print(final_words)

#emotion anal
emotion_present=[]

with open('emotions.txt','r') as file: 
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        #print("Word : "+ word + "" + "Emotion : " + emotion)
        #print(clear_line)
        if word in final_words:
            emotion_present.append(emotion)

print("The emotions present in the reviews are : ")
print(emotion_present)
w=Counter(emotion_present)
print(w)

#graph without auto adjustment
# plt.bar(w.keys(),w.values())
# plt.savefig('graph.png')
# plt.show()

#graph with auto adjustment
fig,ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()