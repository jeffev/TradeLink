from sqlalchemy import Column, Integer, String, DateTime, Float
from database import Base


class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    Data = Column(DateTime)
    Duracao = Column(Float)
    Ativo = Column(String, index=True)
    Tipo = Column(String)
    Qtde = Column(Float)
    Direction = Column(String)
    Tendencia = Column(String)
    Sentimento = Column(String)
    Execucao = Column(String)
    Erro = Column(String)
    TimeFrame = Column(String)
    Setup = Column(String)
    Pontos = Column(Float)
    Valor = Column(Float)
    Percentual = Column(Float)
    Imagem = Column(String)
    Observacao = Column(String)
