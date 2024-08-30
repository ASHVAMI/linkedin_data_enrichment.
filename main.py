from database.db_config import SessionLocal
from database.db_operations import get_companies, create_enriched_company
from api.linkedin_scraper import scrape_company_data

def main():
    db = SessionLocal()
    try:
        companies = get_companies(db)
        for company in companies:
            enriched_data = scrape_company_data(company.company_linkedin_url)
            if enriched_data:
                enriched_company = {
                    "company_id": company.company_id,
                    "name": enriched_data.get("name"),
                    "description": enriched_data.get("description"),
                    "website": enriched_data.get("website"),
                    "industry": enriched_data.get("industry"),
                    "company_size": enriched_data.get("companySize"),
                    "headquarters": enriched_data.get("headquarters"),
                    "founded": enriched_data.get("founded"),
                    "specialties": ", ".join(enriched_data.get("specialties", []))
                }
                create_enriched_company(db, enriched_company)
                print(f"Enriched data for company {company.company_id} stored successfully.")
            else:
                print(f"Failed to enrich data for company {company.company_id}")
    finally:
        db.close()

if __name__ == "__main__":
    main()