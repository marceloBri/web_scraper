from bs4 import BeautifulSoup
import requests 
from googlesearch import search  



output = ''
blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script', 
        'style', 
        'div'
        # se pueden agregar mas elementos como 'a', etc.
    ]


# busca los links en google 
google_query= str(input("ingrese el término o palabras a buscar en google :")) 
google_query_new=google_query.replace(' ', '_') 
print(google_query_new)
valores=[]

#ingresa el numero de páginas a buscar texto
webpages_to_search= int(input("ingrese el número de paginas a buscar: "))
file_list=[]

for i in search(google_query, start=0, pause=2, stop=webpages_to_search): 
    str(valores.append(i)) 
      
# guarda la información de las páginas en un archivo de texto y limpia las etiquetas del html
with open (f'{google_query_new}.txt', 'w' , encoding="utf-8") as file:
    for pg in range(len(valores)):
        page = requests.get(valores[pg]) 
        html_page= page.content
        soup = BeautifulSoup(html_page, "html.parser")
        ticker = soup.find_all(text=True)
        
        for t in ticker:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)  
    print(output, file=file )           
            
    