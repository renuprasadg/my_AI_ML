import pickle
from fastapi import FastAPI
from pydantic import BaseModel
with open("iris_model.pkl",'rb') as f:
  model = pickle.load(f)
with open("iris_model.pkl",'rb') as f2:
  model2 = pickle.load(f2)  
app = FastAPI()
class IrisInput(BaseModel):
  sl:float
  sw:float
  pl:float
  pw:float
class DiaInput(BaseModel):
  age:float
  sex:float
  bmi:float
  bp:float
@app.get("/")
def read_root():
  return{"message":"welcome to fastapi"}
@app.post("/predict/")
def predict(data:IrisInput):
  input_data = [[data.sl,data.sw,data.pl,data.pw]]
  prediction = model.predict(input_data)[0]
  return {'prediction is:',int(prediction)}
@app.post("/predict/diabetes/")
def predict_dia(data:DiaInput):
  input_data = [[data.age, data.sex, data.bmi, data.bp]]
  prediction = model2.predict(input_data)[0]
  return {"Prediction is:",int(prediction)}
