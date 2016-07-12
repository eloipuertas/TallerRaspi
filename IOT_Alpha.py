
# coding: utf-8

# # Projecte IoT -> Fer una applicació que li puguis introduir una pregunta i que la respongui, consultant la web de wolframalpha
# 
# ## Requeriments:
# 
# Wolframalpha API
# 
# > pip3 install wolframalpha
# 
# Crear un compte de [desenvolupador a wolframalpha (gratuït)](https://developer.wolframalpha.com/portal/apisignup.html?_ga=1.121653707.1501519151.1464623520)
# 

# In[1]:

import wolframalpha

from IPython.core.display import display, HTML
from IPython.display import Image

print ("Què vols saber avui?")
query  = input()
#'temperature in Barcelona on July 9, 2016'

f = open('account', 'r')
account = f.readline();

client = wolframalpha.Client(account.strip()) # agafar-ho d'un fitxer
res = client.query(query)

for pod in res.pods:
    
    display(HTML("<H1>" + pod.title + ': </H1>'))
    for sb in pod:
        if sb.title:
            display(HTML("<H2>" + sb.title + '</H2>'))
        if sb.img:
            display(Image(url= sb.img))
   


