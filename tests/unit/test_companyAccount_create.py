from src.account import CompanyAccount

class TestCompanyAccount:
    def test_create_company_account(self):
        testificate = CompanyAccount("Test Company","1234567890")
        assert testificate.company_name == "Test Company"
        assert testificate.nip_number == "1234567890"
    def test_invalid_company_account(self):
        testificate = CompanyAccount("Test Company","1234590")
        assert testificate.company_name == "Test Company"
        assert testificate.nip_number == "Invalid"
        