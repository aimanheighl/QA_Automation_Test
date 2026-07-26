# QA Automation Practical Test

Python + Selenium automation for StarProperty.my — registration, bookmarking, comparison, and enquiry flows.

##  Test Cases

| Test | Description                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------|
| **Test Case 1** | User Registration Flow — fill form as Property Agent, upload business card, handle T&C / Privacy Policy tabs, **do not submit** |
| **Test Case 2** | Enquiry & Bookmark Flow — login, search properties, bookmark, compare, send enquiry, **do not submit**                          |

## Included for this test

- Python 3.9+
- Selenium WebDriver
- pytest
- webdriver-manager (auto-manages ChromeDriver)
- Page Object Model (POM)
- Logger (Record logs for success and failed task)

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd QA_Automation_Test
```

### 2. Create & activate virtual environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶ Run Tests

```bash
# Test Case 1 only
pytest tests/test_registration.py -v -s

# Test Case 2 only
pytest tests/test_enquiry_bookmark.py -v -s
```

##  Project Structure

```
QA_Automation_Test/
├── run_tests.py                 # Main runner
├── requirements.txt             # Dependencies
├── README.md
├── .gitignore
├── tests/
│   ├── test_registration.py     # Test Case 1
│   └── test_enquiry_bookmark.py # Test Case 2
├── pages/
│   ├── login_page.py
│   ├── registration_page.py
│   └── property_search_page.py
├── utils/
│   ├── driver.py                # WebDriver setup
│   ├── test_data.py             # Test data + credentials
│   └── logger.py                # Logging utility
└── test_data/
    └── business_card.png        # Dummy business card
```

## ⚠️ Notes

- Test Case 2 requires a pre-registered General user account. Update `LOGIN_USER` in `utils/test_data.py`.
Test Case 2 — Login credentials (REAL ACC NEEDED!)
```bash
LOGIN_USER = {
    "email": "test@gmail.com",
    "password": "test123456789",
}
```
- For Test Case 2, need to remove the added bookmarked as it saves in server side. (For repetition test)
- The register / submit button is **never clicked** — forms are populated only.
- Chrome browser and internet connection required.