
import pandas as pd 

telefones = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/telefones.csv", skip_blank_lines=False)
telefones=telefones.fillna("")
telefones=telefones['Telefones'].tolist()


auxtelefones= []
for contato in telefones:
  numero= contato.replace('(','').replace(')','').replace('-','').replace(' ','')
  if "/" in numero:
    aux = numero.split('/')
    auxtelefones.append(aux)   
  else:
    auxtelefones.append([numero]) 

santelefone = []
for newcontatos in auxtelefones:
  contatos_tratados = []
  for newcontato in newcontatos:
    if len(newcontato) == 0:
      newcontato ="Nao Informado"
    else:
      if len(newcontato) < 11:
        newcontato=newcontato[:2]+"9"+newcontato[2:]
    #print(newcontato)
      newcontato="55"+newcontato
    contatos_tratados.append(newcontato)
  santelefone.append(contatos_tratados)
  
print(santelefone)

df = pd.DataFrame([i for i in santelefone],columns = ["telefones","telefones_2"])

df.to_csv('/content/drive/MyDrive/Colab Notebooks/Telefones_tentativa.csv', index = False)
