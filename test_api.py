import unittest
from unittest.mock import patch
from src.api.linkedin_scraper import scrape_company_data

class TestAPI(unittest.TestCase):
    @patch('src.api.linkedin_scraper.requests.get')
    def test_scrape_company_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "name": "Test Company",
            "description": "A test company",
            "website": "https://testcompany.com",
            "industry": "Technology",
            "companySize": "51-200 employees",
            "headquarters": "San Francisco, CA",
            "founded": "2020",
            "specialties": ["Testing", "Software"],
            "affiliatedOrganizations": ["Should be filtered out"],
            "locations": ["Should be filtered out"],
            "similarOrganizations": ["Should be filtered out"]
        }

        result = scrape_company_data("https://www.linkedin.com/company/test")
        self.assertEqual(result["name"], "Test Company")
        self.assertNotIn("affiliatedOrganizations", result)
        self.assertNotIn("locations", result)
        self.assertNotIn("similarOrganizations", result)

if __name__ == '__main__':
    unittest.main()