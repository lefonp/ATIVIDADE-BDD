#Importação de biblioteca
import pymongo

#Conectando com o mongo
client = pymongo.MongoClient("mongodb://localhost:27017/")

#Criar banco de dados
db = client["Agenda"]

#Criando a agenda
Colecao = db["Contatos"]
documento = {"nome": "Leticia","sobrenome": "Fontes", "Número": "+5581985612720", "Email": "leticia.patriota@edu.pe.senac.br"}
resultado = Colecao.insert_one(documento)
print(resultado)

#Lendo dados
filtro = {"nome": "Leticia"}
resultado = Colecao.find_one(filtro)
print(resultado)

#Atualizando um documento
filtro = {"nome": "Leticia"}
atualizacoes = {"$set": {"Número": "+5581987623831"}}
resultado = Colecao.update_one(filtro, atualizacoes)
print(resultado.modified_count)

#Excluindo um documento
filtro = {"nome": "João"}
resultado = Colecao.delete_one(filtro)
print(resultado)