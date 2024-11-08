from sqlalchemy.orm import Session
from .models import Dentista, Agendamento

def create_dentista(db: Session, nome: str, especialidade: str):
    dentista = Dentista(nome=nome, especialidade=especialidade)
    db.add(dentista)
    db.commit()
    db.refresh(dentista)
    return dentista

def get_dentistas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Dentista).offset(skip).limit(limit).all()

def get_dentista(db: Session, dentista_id: int):
    return db.query(Dentista).filter(Dentista.id == dentista_id).first()

def delete_dentista(db: Session, dentista_id: int):
    dentista = db.query(Dentista).filter(Dentista.id == dentista_id).first()
    if dentista:
        db.delete(dentista)
        db.commit()
    return dentista

def create_agendamento(db: Session, dentista_id: int, data_consulta):
    agendamento = Agendamento(dentista_id=dentista_id, data_consulta=data_consulta)
    db.add(agendamento)
    db.commit()
    db.refresh(agendamento)
    return agendamento

def get_agendamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Agendamento).offset(skip).limit(limit).all()

def delete_agendamento(db: Session, agendamento_id: int):
    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()
    if agendamento:
        db.delete(agendamento)
        db.commit()
    return agendamento
