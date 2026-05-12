from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time

print('SOFTWARE VALIDADOR DE QUANTIDADE DE DIGITOS DE CPF EM IMP.NOME')
time.sleep(3)
def abre_arquivo(): #Retorna o arquivo aberto para analise e edição
    Tk().withdraw()

    caminho_arquivo = askopenfilename(
        title="Selecione um arquivo!",
        filetypes=[
        ("Texto", "*.txt")
        ]
    )
    with open(caminho_arquivo,"r",encoding="latin-1") as f: #Abre o arquivo e captura o conteúdo
        abertura_arquivo= f.read()
    
    
    return abertura_arquivo

informacao_arquivo = abre_arquivo() #Abre o arquivo


quebra_linha = informacao_arquivo.splitlines() #Divide o arquivo em linhas cada linha dentro de uma lista de str

erros = [
    i for i in quebra_linha
    if not (i[0:10].isdigit() and i[11:13] == "  ")
] #Valida se o campo que deveria ter cpf está com 11 digitos e se existe o dblspace entre o campo cpf e nome;
#Logo após as linhas que não cumprirem a condição serão armazenadas dentro da lista 'erros'


#Caso a lista 'erros' seja verdadeira, ou seja, contenha algum elemento, um for percorre e printa suas listas
if erros: 
    for e in erros:
        print(e)
else:
    print('Documento não contém erros de CPF e formatação') #Caso não tenha erros será exibida essa mensagem.
   
print('\n')
print('PROGRAMA EXECUTADO!')
input('Finalize o programa clicando Enter...')













