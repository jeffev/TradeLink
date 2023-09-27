from sqlalchemy.orm import Session
import models


def create_trade(db: Session, trade: models.Trade):
    db_trade = models.Trade(**trade.dict())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade


def get_trade(db: Session, trade_id: int):
    return db.query(models.Trade).filter(models.Trade.id == trade_id).first()


def update_trade(db: Session, trade_id: int, trade: models.Trade):
    db_trade = (
        db.query(models.Trade)
        .filter(models.Trade.id == trade_id)
        .first()
    )

    if db_trade:
        for key, value in trade.dict().items():
            setattr(db_trade, key, value)
        db.commit()
        db.refresh(db_trade)
    return db_trade


def delete_trade(db: Session, trade_id: int):
    db_trade = (
        db.query(models.Trade)
        .filter(models.Trade.id == trade_id)
        .first()
    )

    if db_trade:
        db.delete(db_trade)
        db.commit()
    return db_trade
