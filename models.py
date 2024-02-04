from sqlalchemy import DateTime, String, Integer, Column, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('localhost:5432')

Base = declarative_base()

class Serts(Base):
    __tablename__ = 'serts'
    id = Column(Integer, primary_key=True)
    registrated_at = Column(DateTime)
    certificated_at = Column(DateTime)
    end_at = Column(DateTime)
    name_organization = Column(String(255), nullable=False)
    type_management = Column(String(255))
    status = Column(String(255))
    iin = Column(String(255))
    reg_number = Column(String(255))
    name_arrc = Column(String(255))


Base.metadata.create_all(engine)



