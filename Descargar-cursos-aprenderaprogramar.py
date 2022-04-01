#! /usr/bin/python3.6

import requests, os, bs4

# url = 'https://www.aprenderaprogramar.com/index.php?option=com_content&view=article&id=90:indice-del-curso-qbases-de-la-programacion-nivel-iq-cu00102a&catid=28&Itemid=59'

print("URL de inicio: ", end="")
url = input()
print("Carpeta de destino: ", end="")
carpetaDestino = input()
path = os.path.join(os.getcwd(), carpetaDestino)
os.makedirs(path, exist_ok=True)

siguiente = True

while siguiente:
    # Acceder url
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Título
    title = soup.select('h1.contentheading > a')
    titleText = title[0].getText()
    
    # Formato texto
    titleText = titleText.strip()
    titleText = titleText.replace('/', '-')
    number = titleText[-9:-2]
    titleText = titleText[0:-10]
    titleText = number + ' - ' + titleText
    print(titleText)

    # PDF
    pdf = soup.select('div.attachmentsContainer a.at_url')
    linkPdf = pdf[0].get('href')

    # Acceder pdf
    res = requests.get(linkPdf)
    res.raise_for_status()

    # Abrir fichero
    pdfFile = open(os.path.join(path, titleText), 'wb')

    # Descargar PDF
    for chunk in res.iter_content(100000):
        pdfFile.write(chunk)
        
    # Cerrar fichero  
    pdfFile.close()
    print('OK')

    # Click next
    nextButton = soup.select('li.next > a.hasTooltip')
    if len(nextButton) == 0:
        siguiente = False
        print('\nFIN')
    else:
        linkNextButton = nextButton[0].get('href')
        url = 'https://www.aprenderaprogramar.com' + linkNextButton
    
