from datetime import datetime

def generate_phone_number():
    timestamp = datetime.now().strftime("%H%M%S")

    # +60131 + 6 digits
    return f"+60131{timestamp}"

# Test Case 1 — Register

TEST_USER = {
    "first_name": "Aiman Azmi",
    "last_name": "Anuar",
    "email": "azmi.itcorporation@gmail.com",
    "phone": generate_phone_number(),
    "password": "TestPassword123!",
    "date_of_birth": "01-01-1990",
    "agency_ecode": "E1234",
    "ren_code": "REN12345",
}

# Test Case 2 — Login credentials (REAL ACC NEEDED!)
LOGIN_USER = {
    "email": "test@gmail.com",
    "password": "test123456789",
}