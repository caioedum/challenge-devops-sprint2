from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Dentista(Base):
    __tablename__ = "T_DENTISTA"

    id = Column("ID", Integer, primary_key=True, autoincrement=False)
    nome = Column("NOME", String(100), nullable=False)
    especialidade = Column("ESPECIALIDADE", String(100), nullable=False)

    agendamentos = relationship("Agendamento", back_populates="dentista")


class Agendamento(Base):
    __tablename__ = "T_AGENDAMENTO"

    id = Column("ID", Integer, primary_key=True, autoincrement=False)
    dentista_id = Column("DENTISTA_ID", Integer, ForeignKey("T_DENTISTA.ID"), nullable=False)
    data_consulta = Column("DATA_CONSULTA", Date, nullable=False)

    dentista = relationship("Dentista", back_populates="agendamentos")
