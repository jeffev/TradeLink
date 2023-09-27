from pydantic import BaseModel
from datetime import datetime


class TradeBase(BaseModel):
    Data: datetime
    Duracao: float
    Ativo: str
    Tipo: str
    Qtde: float
    Direction: str
    Tendencia: str
    Sentimento: str
    Execucao: str
    Erro: str
    TimeFrame: str
    Setup: str
    Pontos: float
    Valor: float
    Percentual: float
    Imagem: str
    Observacao: str


class TradeCreate(TradeBase):
    pass


class TradeUpdate(TradeBase):
    pass


class Trade(TradeBase):
    id: int

    class Config:
        orm_mode = True
