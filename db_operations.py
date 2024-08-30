from sqlalchemy.orm import Session
from . import models

def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()

def create_enriched_company(db: Session, company_data: dict):
    db_company = models.EnrichedCompany(**company_data)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)