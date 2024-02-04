from sqlalchemy.orm import Session
from models import Serts


def insert_value(session: Session, serts: Serts):
    try:
        session.add(serts)
        session.commit()
    except Exception as e:
        print(e)


def select_value(session: Session, target_id):
    try:
        result = session.query(Serts).filter(Serts.id == target_id).first()
        return result
    except Exception as e:
        print(e)


def update_value(session: Session, target_id, **kwargs):
    sert_to_update = session.query(Serts).filter_by(id=target_id).first()

    if sert_to_update:
        for key, value in kwargs.items():
            setattr(sert_to_update, key, value)

        session.commit()

    return sert_to_update
