from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    company_linkedin_url = Column(String, unique=True, index=True)

class EnrichedCompany(Base):
    __tablename__ = "enriched_companies"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, index=True)
    name = Column(String)
    description = Column(String)
    website = Column(String)
    industry = Column(String)
    company_size = Column(String)
    headquarters = Column(String)
    founded = Column(String)
    specialties = Column(String)
