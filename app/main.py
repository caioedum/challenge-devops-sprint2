from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from . import crud, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/dentistas/")
def create_dentista(nome: str, especialidade: str, db: Session = Depends(get_db)):
    return crud.create_dentista(db=db, nome=nome, especialidade=especialidade)

@app.get("/dentistas/")
def read_dentistas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_dentistas(db, skip=skip, limit=limit)

@app.delete("/dentistas/{dentista_id}")
def delete_dentista(dentista_id: int, db: Session = Depends(get_db)):
    dentista = crud.delete_dentista(db=db, dentista_id=dentista_id)
    if dentista is None:
        raise HTTPException(status_code=404, detail="Dentista não encontrado")
    return dentista

@app.post("/agendamentos/")
def create_agendamento(dentista_id: int, data_consulta: date, db: Session = Depends(get_db)):
    return crud.create_agendamento(db=db, dentista_id=dentista_id, data_consulta=data_consulta)

@app.get("/agendamentos/")
def read_agendamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_agendamentos(db, skip=skip, limit=limit)

@app.delete("/agendamentos/{agendamento_id}")
def delete_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    agendamento = crud.delete_agendamento(db=db, agendamento_id=agendamento_id)
    if agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return agendamento
