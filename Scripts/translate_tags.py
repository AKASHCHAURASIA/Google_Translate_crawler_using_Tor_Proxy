import requests
import json
from fake_useragent import UserAgent
from googletrans.gtoken import TokenAcquirer
from time import sleep
import sys
def func(l):
    
    dic = {}
    
    proxies = {'http': 'socks5://127.0.0.1:9150','https': 'socks5://127.0.0.1:9150'}
    name=sys.argv[2].split('.')
    name=name[0]
    
    for i in l:
        csv=''
        
        f=open("Data/"+name+"_"+sys.argv[1]+"_tags.csv","a")


        try:

            acq = TokenAcquirer()
            text = i
            tk = acq.do(text)

            r = requests.get('https://translate.google.co.in/translate_a/single?client=webapp&sl=auto&tl='+sys.argv[1]+'&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=2&ssel=0&tsel=0&xid=1791807&kc=1&tk='+tk+'&q='+i,proxies = proxies)
            a=r.json()
            
            dic[text]= a[0][0][0]
            
            csv = i.strip()+','
            temp = dic[i]
            csv = csv + temp
            csv = i.strip()+','
            temp = dic[i]
            csv = csv + temp
            f.write(csv +'\n')
            f.close()
            
        except:
            dic[text]=''
            
    
            


    return dic



with open(sys.argv[2], 'r') as f:
    data = f.readlines()
    dict = {}
    l = []
    ex_dict = {}
    count = 0
    for i in data:
            a = i.replace('"', '')
            l.append(a)

            name=sys.argv[2].split(".")
name=name[0]
d={}

d=func(l)
