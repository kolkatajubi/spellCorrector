#!/usr/bin/env python
# coding: utf-8

# In[1]:


from similarity.jarowinkler import JaroWinkler
import time
import re
from flask import Flask
from flask import request
from flask import jsonify


# In[2]:


with open('linuxwords.txt', 'r',newline='') as f:
    dictionary = f.read().lower().splitlines()


# In[3]:


def is_correct(word, dictionary):
    return (word.lower() in dictionary)


# In[4]:


def correct(word,dictionary):
    if is_correct(word,dictionary):
        return (word, 1.0)
    else:
        jarowinkler = JaroWinkler()
        score = []
        for dict_word in dictionary:
            score.append(jarowinkler.similarity(word,dict_word))
        return (dictionary[score.index(max(score))],max(score))


# In[5]:


cache = {}


# In[6]:


app = Flask(__name__)
@app.route('/' , methods = ['POST'])
def testDict():
    output={}
    content = request.get_json()
    word = content["word"]
    word = re.sub(r'[0987654321~`’!#@$%^&*(){}\[\];:"\'<,.>?\/\\|_+=-]',"",word.strip()).strip()
    if word in cache:
        start = time.clock()
        print("from cache")
        print("i/p word :"+word)
        print("o/p word : "+cache[word]['answer'])
        print("score : "+str(cache[word]['score']))
        print("time taken : "+str(time.clock()-start))
    else:
        cache[word]={}
        start = time.clock()
        ans, score = correct(word,dictionary)
        print("i/p word :"+word)
        print("o/p word : "+ans)
        print("score : "+str(score))
        print("time taken : "+str(time.clock()-start))
        cache[word]['answer'] = ans
        cache[word]['score'] = score
    output['i/p word'] = word
    output['o/p word'] = cache[word]['answer']
    output['score'] =cache[word]['score']
    output['status'] = 'success'
    output['totalTime'] = time.clock() - start
    print("OUTPUT : ", output)
    return jsonify(output)


# In[7]:


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 2900)


# In[ ]:




