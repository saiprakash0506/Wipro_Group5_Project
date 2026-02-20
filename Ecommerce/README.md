# 🛒 Ecommerce – Automation Testing Framework

> A comprehensive **end-to-end automation testing suite** for an E-Commerce web application, built as part of the **Wipro Group 5 Training Project**.  
> Demonstrates UI test automation using both **Pytest (Page Object Model)** and **Robot Framework (Keyword-Driven)** methodologies.

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python"/></a>
  <a href="https://pytest.org"><img src="https://img.shields.io/badge/Pytest-7.0+-orange.svg" alt="Pytest"/></a>
  <a href="https://robotframework.org"><img src="https://img.shields.io/badge/Robot%20Framework-6.0+-red.svg" alt="Robot Framework"/></a>
  <a href="https://selenium.dev"><img src="https://img.shields.io/badge/Selenium-4.0+-green.svg" alt="Selenium"/></a>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen.svg" alt="Status"/>
  <img src="https://img.shields.io/badge/License-Educational-lightgrey.svg" alt="License"/>
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Features Implemented](#-features-implemented)
- [Framework Design](#-framework-design)
- [Installation](#-installation)
- [Running the Tests](#-running-the-tests)
- [Test Reports](#-test-reports)
- [Learning Outcomes](#-learning-outcomes)
- [Project Status](#-project-status)
- [Team](#-team)
- [Acknowledgments](#-acknowledgments)

---

## 🔍 Overview

This project is a dual-framework automation testing suite designed to validate an E-Commerce web application across multiple user journeys — from login and product browsing to cart management and checkout. It was built collaboratively by a team of 6 during the **Wipro Training Program** to demonstrate real-world QA automation skills.

**Two frameworks, one goal:** ensure quality across the entire e-commerce user journey.

| Framework | Approach | Best For |
|---|---|---|
| **Pytest + POM** | Page Object Model | Modular, developer-centric test design |
| **Robot Framework** | Keyword-Driven | Business-readable, BDD-style test suites |

---

## 🚀 Technology Stack

| Component | Technology | Version |
|---|---|---|
| **Language** | Python | 3.8+ |
| **UI Automation** | Selenium WebDriver | 4.0+ |
| **Framework 1** | Pytest | 7.0+ |
| **Framework 2** | Robot Framework | 6.0+ |
| **Browser Driver** | ChromeDriver / GeckoDriver | Matching browser |
| **Libraries** | selenium, pytest, robotframework-seleniumlibrary | Latest stable |
| **Design Pattern** | Page Object Model (POM) | — |
| **Test Data** | Data-driven (JSON / CSV / Excel) | — |
| **Reporting** | pytest-html, Robot built-in HTML | — |

---

## 📁 Project Structure

```
Ecommerce/
│
├── Pytest-framework/                  # Pytest automation suite
│   ├── data/                          # Test data files (JSON/CSV/Excel)
│   ├── pages/                         # Page Object Model classes
│   │   ├── home_page.py               #   → HomePage interactions
│   │   ├── login_page.py              #   → LoginPage interactions
│   │   ├── cart_page.py               #   → CartPage interactions
│   │   └── checkout_page.py           #   → CheckoutPage interactions
│   ├── reports/                       # Generated HTML test reports
│   ├── tests/                         # Pytest test cases
│   │   ├── test_login.py              #   → Login & registration tests
│   │   ├── test_cart.py               #   → Cart tests
│   │   ├── test_search.py             #   → Search & product tests
│   │   └── test_checkout.py           #   → Checkout flow tests
│   ├── conftest.py                    # Pytest fixtures (browser setup/teardown)
│   ├── requirements.txt               # Python dependencies
│   └── runcommand.txt                 # Quick-reference run commands
│
├── robot-framework/                   # Robot Framework automation suite
│   ├── keywords/                      # Custom reusable keyword definitions
│   │   └── common_keywords.robot      #   → Shared actions & helpers
│   ├── tests/                         # Robot Framework test suites
│   │   ├── login_tests.robot          #   → Login scenarios
│   │   ├── cart_tests.robot           #   → Cart scenarios
│   │   └── checkout_tests.robot       #   → Checkout scenarios
│   ├── variables/                     # Centralized variable files
│   │   └── variables.py               #   → URLs, credentials, selectors
│   └── reports/                       # Generated Robot HTML reports
│
└── README.md                          # Project documentation
```

---

## 📌 Features Implemented

### 1️⃣ Pytest Framework (Page Object Model)

- ✅ **Page Object Model** – Clean separation of locators, actions, and test logic
- ✅ **Modular page classes** – Reusable across multiple test files
- ✅ **Data-driven testing** – Tests driven by external JSON/CSV/Excel files
- ✅ **Pytest fixtures** – Automatic browser setup and teardown via `conftest.py`
- ✅ **Parameterized tests** – Single test covers multiple input scenarios
- ✅ **HTML report generation** – Visual test results via `pytest-html`

### 2️⃣ Robot Framework (Keyword-Driven)

- ✅ **Custom keyword library** – Business-readable, reusable test steps
- ✅ **Keyword-driven test design** – Tests written in plain English-like syntax
- ✅ **Centralized variable management** – URLs, credentials, and data in one place
- ✅ **Setup & teardown hooks** – Suite-level and test-level lifecycle management
- ✅ **Integration & E2E flow testing** – Full user journey across multiple pages
- ✅ **Rich HTML reports** – Summary, log, and XML output for CI/CD integration

### 3️⃣ E-Commerce Scenarios Covered

| Test Scenario | Pytest | Robot Framework |
|---|:---:|:---:|
| User Login (valid credentials) | ✅ | ✅ |
| User Login (invalid credentials) | ✅ | ✅ |
| User Registration | ✅ | ✅ |
| Product Search & Browsing | ✅ | ✅ |
| Add to Cart | ✅ | ✅ |
| Remove from Cart | ✅ | ✅ |
| Checkout Flow (End-to-End) | ✅ | ✅ |
| Form Validation (positive cases) | ✅ | ✅ |
| Form Validation (negative cases) | ✅ | ✅ |
| Navigation & UI Verification | ✅ | ✅ |

---

## 🏗️ Framework Design

### Pytest – Page Object Model (POM)

```
┌──────────────────────────────────────────┐
│            Tests Layer                   │
│   test_login.py / test_cart.py / ...     │  ← Assertions & Test Scenarios
└────────────────────┬─────────────────────┘
                     │ uses
┌────────────────────▼─────────────────────┐
│            Pages Layer                   │
│   LoginPage / CartPage / HomePage / ...  │  ← Locators, Actions, Interactions
└────────────────────┬─────────────────────┘
                     │ reads
┌────────────────────▼─────────────────────┐
│             Data Layer                   │
│        JSON / CSV / Excel files          │  ← External Test Data
└──────────────────────────────────────────┘
```

**Key principle:** Test files contain **no locators**. All page interactions are encapsulated in page classes. Changing a locator requires an update in one place only.

---

### Robot Framework – Keyword-Driven Architecture

```
┌──────────────────────────────────────────┐
│            Tests Layer                   │
│   login_tests.robot / cart_tests.robot   │  ← Test Cases using Keywords
└────────────────────┬─────────────────────┘
                     │ calls
┌────────────────────▼─────────────────────┐
│           Keywords Layer                 │
│       common_keywords.robot              │  ← Reusable Steps & Actions
└────────────────────┬─────────────────────┘
                     │ uses
┌────────────────────▼─────────────────────┐
│           Variables Layer                │
│          variables.py                    │  ← URLs, Credentials, Selectors
└──────────────────────────────────────────┘
```

**Key principle:** Non-technical stakeholders can read and understand test cases. Keywords abstract away all Selenium complexity.

---

## 💻 Installation

### Prerequisites

Before setting up, ensure you have the following installed:

- Python **3.8 or higher** → [Download](https://www.python.org/downloads/)
- pip (comes bundled with Python)
- Google Chrome **or** Firefox browser
- ChromeDriver **or** GeckoDriver — must match your installed browser version
  - ChromeDriver: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
  - GeckoDriver: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

> 💡 **Tip:** Add the driver to your system `PATH` so Selenium can find it automatically.

---

### Step 1 – Clone the Repository

```bash
git clone https://github.com/saiprakash0506/Wipro_Group5_Project.git
cd Wipro_Group5_Project/Ecommerce
```

### Step 2 – Setup Pytest Framework

```bash
cd Pytest-framework

# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### Step 3 – Setup Robot Framework

```bash
cd ../robot-framework

# Install Robot Framework core
pip install robotframework

# Install Selenium integration library
pip install robotframework-seleniumlibrary
```

---

## 🧪 Running the Tests

### ▶️ Pytest Tests

```bash
cd Pytest-framework

# Run all tests
pytest -v

# Run a specific test file
pytest tests/test_login.py -v

# Run tests matching a keyword
pytest -k "login" -v

# Run with HTML report output
pytest --html=reports/report.html --self-contained-html -v

# Run with coverage report
pytest --cov=pages --cov-report=html

# Run and stop on first failure
pytest -x -v
```

> See `runcommand.txt` for additional run configurations.

---

### ▶️ Robot Framework Tests

```bash
cd robot-framework

# Run all test suites
robot tests/

# Run a specific test suite
robot tests/login_tests.robot

# Run with a custom output directory
robot --outputdir reports/ tests/

# Run with a specific browser variable
robot --variable BROWSER:chrome tests/

# Run only tests with a specific tag
robot --include smoke tests/

# Run with verbose logging
robot --loglevel DEBUG tests/
```

---

## 📊 Test Reports

Both frameworks generate rich, human-readable reports after each test run.

### Pytest Reports — `Pytest-framework/reports/`

| File | Description |
|---|---|
| `report.html` | Visual HTML summary of all test results |
| `.coverage` | Code coverage data (if `--cov` flag used) |
| `htmlcov/` | HTML coverage report directory |

### Robot Framework Reports — `robot-framework/reports/`

| File | Description |
|---|---|
| `report.html` | High-level summary of all test suites and results |
| `log.html` | Step-by-step execution log with screenshots |
| `output.xml` | Machine-readable results (CI/CD integration ready) |

---

### Sample Console Output

**Pytest:**
```
collected 8 items

tests/test_login.py::test_valid_login          PASSED  [  12%]
tests/test_login.py::test_invalid_login        PASSED  [  25%]
tests/test_cart.py::test_add_to_cart           PASSED  [  37%]
tests/test_cart.py::test_remove_from_cart      PASSED  [  50%]
tests/test_checkout.py::test_checkout_flow     PASSED  [  62%]
tests/test_checkout.py::test_invalid_card      FAILED  [  75%]
...

====== 7 passed, 1 failed in 43.21s ======
```

**Robot Framework:**
```
==============================================================================
Login Tests
==============================================================================
Valid Login With Correct Credentials                              | PASS |
Invalid Login With Wrong Password                                 | PASS |
Login With Empty Fields Triggers Validation                       | PASS |
==============================================================================
Login Tests                                                       | PASS |
3 tests, 3 passed, 0 failed
==============================================================================
```

---

## 🎯 Learning Outcomes

By building and exploring this project, you will gain practical skills in:

- UI test automation using **Selenium WebDriver** with Python
- Implementing **Page Object Model (POM)** pattern with Pytest
- Building **keyword-driven test frameworks** using Robot Framework
- Applying **data-driven testing** techniques with external data sources
- Writing effective **fixtures, setup, and teardown** for test lifecycle management
- Generating and interpreting **HTML test reports** for stakeholders
- Structuring **scalable and maintainable** automation projects
- Comparing and selecting the right framework for different testing contexts
- Collaborating on a shared QA project using **Git and GitHub**

---

## 📈 Project Status

| Component | Status |
|---|---|
| Pytest Framework Setup | ✅ Complete |
| Page Object Model (POM) | ✅ Complete |
| Pytest Test Cases | ✅ Complete |
| Test Data Files | ✅ Complete |
| Robot Framework Setup | ✅ Complete |
| Robot Keywords & Variables | ✅ Complete |
| Robot Test Cases | ✅ Complete |
| Test Reports (both frameworks) | ✅ Complete |
| Documentation / README | ✅ Complete |
| Code Review | 🟡 Ready for Review |

---

## 👥 Team

Developed with 💙 by **Wipro Training – Group 5**

| # | Name |
|---|---|
| 1 | **Sai Prakash** |
| 2 | **Prashant Kumar Jha** |
| 3 | **Bhagyashree N** |
| 4 | **Chowdam Mahendra** |
| 5 | **Praseed Sreepadmakumar** |
| 6 | **Ravinesh Tiwari** |

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes
   ```bash
   git commit -m "Add: description of your change"
   ```
4. Push to your branch
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a **Pull Request** and describe your changes

Please ensure any new test files follow existing naming conventions (`test_*.py` for Pytest, `*_tests.robot` for Robot Framework).

---

## 📄 License

This project was developed for **educational purposes** as part of the Wipro Training Program.  
It is intended for learning and portfolio demonstration only.

---

## 🙏 Acknowledgments

- [Selenium WebDriver Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Robot Framework SeleniumLibrary](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
- Wipro Training mentors and instructors

---

<p align="center">
  <b>Happy Testing! 🚀</b><br/>
  <i>Built with ❤️ by Wipro Group 5</i>
</p>
