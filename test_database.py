import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Base, Company, EnrichedCompany
from src.database.db_operations import get_companies, create_enriched_company

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_get_companies(self):
        company = Company(company_id=1, company_linkedin_url="https://www.linkedin.com/company/test")
        self.session.add(company)
        self.session.commit()

        companies = get_companies(self.session)
        self.assertEqual(len(companies), 1)
        self.assertEqual(companies[0].company_linkedin_url, "https://www.linkedin.com/company/test")

    def test_create_enriched_company(self):
        company_data = {
            "company_id": 1,
            "name": "Test Company",
            "description": "A test company",
            "website": "https://testcompany.com",
            "industry": "Technology",
            "company_size": "51-200 employees",
            "headquarters": "San Francisco, CA",
            "founded": "2020",
            "specialties": "Testing, Software"
        }

        enriched_company = create_enriched_company(self.session, company_data)
        self.assertEqual(enriched_company.name, "Test Company")
        self.assertEqual(enriched_company.industry, "Technology")