from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud
import models
import schemas

app = FastAPI()

# Configuração do banco de dados
models.Base.metadata.create_all(bind=engine)


# Função para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas CRUD


@app.post("/trades/", response_model=schemas.Trade)
def create_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db)):
    return crud.create_trade(db, trade)


@app.get("/trades/{trade_id}", response_model=schemas.Trade)
def read_trade(trade_id: int, db: Session = Depends(get_db)):
    trade = crud.get_trade(db, trade_id)
    if trade is None:
        raise HTTPException(status_code=404, detail="Trade not found")
    return trade


@app.put("/trades/{trade_id}", response_model=schemas.Trade)
def update_trade(trade_id: int, trade: schemas.TradeUpdate, db: Session = 
                 Depends(get_db)):
    existing_trade = crud.get_trade(db, trade_id)
    if existing_trade is None:
        raise HTTPException(status_code=404, detail="Trade not found")
    return crud.update_trade(db, trade_id, trade)


@app.delete("/trades/{trade_id}", response_model=schemas.Trade)
def delete_trade(trade_id: int, db: Session = Depends(get_db)):
    existing_trade = crud.get_trade(db, trade_id)
    if existing_trade is None:
        raise HTTPException(status_code=404, detail="Trade not found")
    return crud.delete_trade(db, trade_id)
