from sqlalchemy import DateTime, String, Integer, Column, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import config


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Serts(Base):
    __tablename__ = 'serts'

    id = Column(Integer, primary_key=True)
    registrated_at = Column(DateTime)
    certificated_at = Column(DateTime)
    end_at = Column(DateTime)
    name_organization = Column(String(500), nullable=False)
    type_management = Column(String(255))
    status = Column(String(255))
    iin = Column(String(255))
    reg_number = Column(String(255))
    name_arrc = Column(String(255))

    def __init__(self, id, iin, reg_number, registrated_at, certificated_at, end_at, status, name_organization,
                 name_arrc, type_management):
        self.id = id
        self.iin = iin
        self.reg_number = reg_number
        self.registrated_at = registrated_at
        self.certificated_at = certificated_at
        self.end_at = end_at
        self.status = status
        self.name_organization = name_organization
        self.name_arrc = name_arrc
        self.type_management = type_management


Base.metadata.create_all(engine)



