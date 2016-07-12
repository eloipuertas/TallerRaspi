
# coding: utf-8

# # Introducció a Python
# ---
# 
# <img src="python.jpg">
# 
#                                 Eloi Puertas Prats
# 
# 
# 

# <H1> Què és Python
# 
# <H3>
# *   Llenguatge multi-propòsit. 
# *  Orientat a objectes
# *  Interpretat
# *  <U>Fortament</U> tipat i <U>Dinàmicament</U> tipat
# * Es centra en la llegibilitat i productivitat del codi 

# <H1> Versions
# 
# <H3>
# [Python 2.7 VS Python 3](https://wiki.python.org/moin/Python2orPython3)
# 
# * Python 2.7 s'està quedant obsolet, Python 3 és la versió que està adoptant la gent que comença amb python
# * Codi 2.7 no te compatibilitat amb 3.0, hi ha canvis subtils

# In[1]:

# Codi compatible Python 3.0 i Python 2.7
print ("Hello World")


# In[3]:

# Codi no compatible amb Python 3.0
print "Hello World"


# In[7]:

2/3
# En Python 3.0 fa divisió real


# In[8]:

# En Python 2.0 fa divisió sencera
#  >>> 2/3
#  0


# Per executar Python des de línia de comandes, obriu un terminal i poseu:
# 
# > ` python ` per executar python 2.7 o
# 
# > `python3` per executar python 3
# 
# Entrereu en una consola on podreu escriure codi Python directament com si fos una calculadora.
# 
# Podeu executar un script Python simplement passant-li el nom del fitxer .py on està el codi escrit en Python:
# 
# > `python3 holaMon.py`
# 
# Si esteu en linux podeu fer que l'script s'executi directament, fent que el fitxer .py sigui executable:
# 
# > `chmod +x holaMon.py`
# 
# i posant la següent capçalera a dalt de tot de l'script:
# 
# > `#!/usr/bin/python`
# 
# Per executar només cal obrir el terminal, anar al subdirectori que toca i fer:
# 
# > `./holaMon.py`
# 
# 

# In[21]:

get_ipython().system(u'cat holaMon.py')

get_ipython().system(u'./holaMon.py')


# #  Entorns de desenvolupament

# * IDLE està instal·lat de sèrie a la Raspberry.
#     * Disposa d'un intérpret on pots entrar comandes Python directament. Els resultats es mostren a la pantalla sense necessitat de fer cap print.
#     * Pots editar fitxers .py desar-se i executar-los
#     * Disposa de debugger
#     * Molt bàsic

# * Jupyter Notebook
#     * Entorn de desenvolupament que s'executa en el navegador
#     * Permet intercalar codi i texte.
#     * Molt adient per fer xerrades, presentacions, memòries...
#     * Adient també per fer prototipatges i proves ràpides
# 

# * Per instal·lar jupyter cal fer des d'un terminal:
# 
# ```
# pip3 install jupyter
# ```
# 
# * Per executar jupyter notebook cal obrir un terminal i executar:
# 
# ``` 
# jupyter notebook
# ```
# 
# 

# Amb l'opció  `EDIT` del menú de dalt es poden insertar noves cel·les i amb l'opció `CELL` executar-les d'una en una o totes de cop.
# 
# Des del menú `File` es pot descarregar el notebook `Download as` com a script Python i així poser-lo executar des de la línia de comandes.
# 
# Es poden fer servir "short-cuts" amb el teclat per:
# 
# * Executar una cel·la: `Ctrl + Enter` 
# * Afegir una cel·la Abaix: `Ctrl M B`
# * Afegir una cel·la Amunt: `Ctrl M A`
# * Canviar el tipus de cel·la a Markdown (texte): `Ctrl M M`
# 

# # Convencions
# 
# * Fer servir espais al voltant dels operadors a = 1 + 2 en comptes de a=1+2 
# * Màxim longidtud de lína de 79 caràcters. I
# * Fer servir 4 espais en comptes de TAB per identar 
# 
# La Filosofia de Python s'explica en el mateix Python:

# In[9]:

import this


# # Instal·lar paquets
# 
# Una de les parts fonamentals de Python és la gran quantitat de paquets que existeixen creats per la comunitat. Per instal·lar un paquet de Python es pot fer de diferents maneres:
# 
# 

# ## APT
# 
# Alguns paquets es poden trobar en els arxius de Rasbpian i es poden instal·lar via el gestor de paquets apt:
# 
# Per actualitzar els paquets disponibles,
# > `sudo apt-get update`
# 
# Per instal·lar un de concret
# > `sudo apt-get install ipython-notebook`
# 
# Per actualitzar tots els paquets del sistema
# 
# > `sudo apt-get upgrade`

# ## PIP
# 
# No tots els paquets es troben disponibles a l'arxiu de Raspbian, o si s'hi troben poden estar desactualitzats. Podeu instal·lar-vos el Python Package Index (pip) per a buscar més paquets.
# 
# > `sudo apt-get install python-pip` 
# 
# > `sudo pip install wolframalpha`
# 

# ## Des dels fonts
# 
# A vegades ens caldrà instal·lar el codi directament del codi font que es trobi en algun repositori. Normalment els codis es troben a GitHub, per accedir al codi:
# 
# > `git clone https://github.com/Eelviny/nxt-python.git` 
# 
# > `cd nxt-python`
# 
# > `python setup.py install`
# 

# # Coneceptes bàsics del Python

# # INDENTACIÓ (Sagnat)
# 
# En Python no es fan servir les claus per a delimitar blocs de codi.
# S'utilitza la indentació, és obligatòria. Si no es fa, la instrucció queda fora del bloc.
# Tampoc fa falta posar finals d'instrucció, com punts i coma, cada instrucció va en una línia
# 
# Per exemple, en el cas d'un bucle for: (Fixeu-vos que s'acaba amb dos punts)
# 

# In[134]:

#Identació correcte
for i in range(3):
    print(i, end= " ")
    print("Hello World")


# In[135]:

#Identació Incorrecte
for i in range(3):
    print(i, end= " ")
print("Hello World")


# # VARIABLES
# 
# Per assignar un valor a una variable, feu-ho així:

# In[59]:

name = "Raül"
age = 15

print (name)
print (age)


# Fixeu-vos-hi que no s'assignen cap mena de tipus, aquest són inferits, i es poden canviar de forma dinamica

# In[60]:

age = "15"
print ("En " + name  + " te " + age + " anys")


# In[61]:

age = 15
age += 1 # incrementar edat en 1
print ("En " + name  + " te " + age + " anys") #Error: DINAMIC però Fortament Tipat 


# In[47]:

print ("En " + name  + " te " + str(age) + " anys") # Funció print necessita un STRING i no pot convertir int a str implicitament


# # Comentaris
# 
# Els comentaris són ignorats pel intèrpret, però molt necessaris per a fer el codi més interpretable pels humans. S'utilitza el `#` davant de la línia que es vulgui comentar. 
# Els comentaris Multi-Linia utilitzen triple dobles cometes:

# In[49]:

"""
This is a very simple Python program that prints "Hello".
That's all it does.
"""

print("Hello")


# # Col·leccions
# 
# Les col·leccions en Python són molt importants. En tenim de tres tipus:
# 
# * Llistes []
# * Tuples ( )
# * Diccionaris { }

# ## Llistes
# 
# Les llistes són col·leccions de qualsevol tipus:
# 

# In[95]:

numbers = [1, "2", 3] # No tenen perquè ser homogènies

numbers.append(4) # Afegir un nou valor a la llista pel final.

numbers[3] # Accés directe amb índex de 0 a n-1


# Per iterar sobre els valors de les col·leccions fem servir la instrucció `for`.
# 

# In[96]:

for number in numbers:
    print (number, end=' ')
    


# Un `String` és una llista de caràcters. Per tant també podem fer servir com a llista: 

# In[86]:

dog_name = "BINGO"

print (dog_name[3])

for char in dog_name:
    print (char, end=' ')


# Es pot usar sempre la funció `len` per saber la longitud d'una col·lecció:

# In[129]:

name = "Jamie"
print(len(name))  # 5

names = ["Bob", "Jane", "James", "Alice"]
print(len(names))  # 4


# ## Tuples i Diccionaris
# 
# Les tuples funcionen bastant igual que les llistes, però són immutables.
# La seva filosofia és la d'una etiqueta formada per diferents elements.

# In[99]:

a = [1,2] # llista
b= (1,2)  # tupla
a[0] = 3
b[0] = 1


# Els diccionaris, son parelles clau valor:

# In[120]:

fitxa = {'nom': 'Bob', 'edat':15} # Diccionari per emular un registre
print (fitxa['nom'])  # per accedir a un element via la clau
fitxa['edat'] = 16  # per canviar un valor via la clau

for key,value in fitxa.items(): # Iterar per totes les claus i valors del diccionari.
    print (key + " : " + str(values))


# In[127]:

telefons ={'Pau':55563, 'Guillem': 55534, "Sara": 55532} # Diccionari per emular una col·lecció amb índexos que siguin noms

print (telefons['Pau']) # accés a un element per clau

telefons['Julia'] = 55589  #afegir nova clau al diccionari

for nom,telefon in telefons.items(): # Iterar per totes les claus i valors del diccionari.
    print (nom + " : " + str(telefon))


# ## Range
# 
# Per iterar des d'un sencer fins a un altre, en python no funciona, ja que un nombre no pot ser iterable.

# In[83]:

for i in 3:
    print (i, end=' ')


# La funció `range` ens permet definir un conjunt de nombres que sigui iterable:

# In[82]:

for i in range(3): # de 0 a 2
    print (i, end=' ', )

print()    

for i in range(1,5): # d'1 a 4
     print (i, end=' ')

print()  

for i in range(1,7,2): # d'1 a 5, només senars, saltant de dos en dos.
     print (i, end=' ')


# ## CONDICIONALS
# 
# Els condicionals es fan amb la instrucció `if`:

# In[130]:

name = "Raül"

if len(name) > 3:
    print("Nice name,")
    print(name)
else:
    print("That's a short name,")
    print(name)


# # Recursos docents
# 
# https://www.raspberrypi.org/resources/

# # IoT
# 
# La "Internet de les coses" és el proper gran boom d'internet. Bàsicament, si qualsevol tipus de dispositiu pot connectar-se a internet, llavors internet serà no només una xarxa d'ordinadors sino que una xarxa de sensors i actuadors. Fent servir aquesta xarxa dels dispositius, serà possible que petits dispositius connectats entre ells facin aplicacions molt més complexes, que si estiguessin aïllades. Ericsson va predir que hi haurien 50 mil millons de dispositius connectats a Internet al 2020.
# 
# Resumint, qualsevol dispositiu petit pot produir dades i pujar-les a internet. Aquestes dades poden ser llavors utilitzades per servidors més potents, o aplicacions mòbils o poden ser utilitzades per enviar missatges a altres dispositius connectats a internet, que puguin per exemple actuar en el món real.
# Basically, any tiny connected device can produce data that is uploaded to the internet. This 
# 

# 1. [Raspberry Pi Camera + Twitter](IoT_Camera.ipynb)
# 2. [Raspberry Pi + Lego NXT](IoT_NXT.ipynb)
# 3. [Raspberry Pi + Wolfram Alfa](IOT_Alpha.ipynb)
