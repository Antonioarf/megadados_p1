from pickle import DICT
from typing import List, Union
import json
from fastapi import FastAPI, Query,HTTPException
from fastapi.encoders import jsonable_encoder

app = FastAPI()


app = FastAPI()
guarda_obj={}

class Prod:
    quant: int
    nome: str
    info: Union[str, None]
    def __init__(self, name:str, quant=None, inf= None):
        self.nome = name
        self.quant = quant
        self.inf = inf

#@app.on_event("startup")
#def startup_event():
#    with open('bdd.json', 'r') as f:
#        guarda_obj = dict(json.load(f))
#    print("oioi!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#    print(guarda_obj)
#    for i in guarda_obj:
#        print(i)

#@app.on_event("shutdown") #@app.on_event("startup")
#def shutdown_event():
#    print("oioi!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#    print(guarda_obj)
#    json_compatible_item_data = jsonable_encoder(guarda_obj)
#    with open('bdd.json', 'w') as json_file:
#        json.dump(json_compatible_item_data, json_file)

@app.post("/")
async def cria(nome: str , quant:int= 0, inf:Union[str, None]= None):
    if nome in guarda_obj:
        raise HTTPException(status_code=404, detail="Item ja existe")
    guarda_obj[nome]= Prod(nome,quant, inf)
    return {'criado id': nome}

@app.get("/")
async def mostra(nome:Union[str, None]= None):
    if nome:
        if nome not in guarda_obj:
            raise HTTPException(status_code=404, detail="Item inexistente")
        return guarda_obj[nome]
    return guarda_obj

@app.put("/")
async def muda(nome: str , quant:Union[int, None]= 0, inf:Union[str, None]= None, soma: bool = True):
    if nome not in guarda_obj:
            raise HTTPException(status_code=404, detail="Item inexistente")
    if quant:
        if soma: #input eh um delta
            guarda_obj[nome].quant += quant
        else: #input eh absoluto
            guarda_obj[nome].quant = quant
    if inf:
        guarda_obj[nome].inf = inf
    return guarda_obj[nome]

@app.get("/")
async def apaga(nome: str):
    if nome not in guarda_obj:
            raise HTTPException(status_code=404, detail="Item inexistente")
    apagado = guarda_obj[nome]
    return {'deletando': apagado}
