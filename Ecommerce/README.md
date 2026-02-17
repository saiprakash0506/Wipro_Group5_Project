# 🛒 Ecommerce – Automation Testing Framework

A comprehensive **automation testing suite** for an E-Commerce web application, built as part of the **Wipro Group 5 Training Project**. The project demonstrates end-to-end UI test automation using both **Pytest (Page Object Model)** and **Robot Framework (Keyword-Driven)** methodologies.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Pytest](https://img.shields.io/badge/Pytest-7.0+-orange.svg)](https://pytest.org)
[![Robot Framework](https://img.shields.io/badge/Robot%20Framework-6.0+-red.svg)](https://robotframework.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)](https://selenium.dev)

---

## 📋 Table of Contents

- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Features](#-features-implemented)
- [Installation](#-installation)
- [Running the Tests](#-running-the-tests)
- [Framework Design](#-framework-design)
- [Reports](#-test-reports)
- [Team](#-team)
- [Learning Outcomes](#-learning-outcomes)
- [Project Status](#-project-status)

---

## 🚀 Technology Stack

| Component          | Technology                                       |
| ------------------ | ------------------------------------------------ |
| **Language**       | Python 3.8+                                      |
| **UI Automation**  | Selenium WebDriver                               |
| **Framework 1**    | Pytest (Page Object Model)                       |
| **Framework 2**    | Robot Framework (Keyword-Driven)                 |
| **Libraries**      | selenium, pytest, robotframework-seleniumlibrary |
| **Design Pattern** | Page Object Model (POM)                          |
| **Test Data**      | Data-driven (external data files)                |
| **Reporting**      | HTML Reports (pytest-html, Robot built-in)       |

---

## 📁 Project Structure

```
Ecommerce/
│
├── Pytest-framework/               # Pytest automation suite
│   ├── .pytest_cache/              # Pytest cache directory
│   ├── data/                       # Test data files (JSON/CSV/Excel)
│   ├── pages/                      # Page Object Model classes
│   │   └── ...                     # (HomePage, LoginPage, CartPage, etc.)
│   ├── reports/                    # Generated HTML test reports
│   ├── tests/                      # Pytest test cases
│   │   └── ...                     # (test_login.py, test_cart.py, etc.)
│   ├── venv/                       # Python virtual environment
│   ├── requirements.txt            # Python dependencies
│   └── runcommand.txt              # Commands reference for running tests
│
├── robot-framework/                # Robot Framework automation suite
│   ├── keywords/                   # Custom reusable keyword definitions
│   ├── reports/                    # Generated Robot test reports
│   ├── tests/                      # Robot Framework test suites
│   │   └── ...                     # (.robot test files)
│   └── variables/                  # Variable files (URLs, credentials, data)
│
└── README.md                       # Project documentation
```

---

## 📌 Features Implemented

### 1️⃣ Pytest Framework (POM)

- ✅ Page Object Model design pattern
- ✅ Modular and reusable page classes
- ✅ Data-driven testing with external data files
- ✅ Fixtures for browser setup and teardown
- ✅ Parameterized tests for multiple scenarios
- ✅ HTML report generation

### 2️⃣ Robot Framework (Keyword-Driven)

- ✅ Custom keyword library
- ✅ Keyword-driven test design
- ✅ Centralized variable management
- ✅ Separate setup and teardown
- ✅ Integration and end-to-end flow testing
- ✅ HTML reports with execution logs

### 3️⃣ E-Commerce Test Scenarios Covered

- ✅ User Login & Registration
- ✅ Product Search & Browsing
- ✅ Add to Cart / Remove from Cart
- ✅ Checkout Flow
- ✅ Form Validation (positive & negative cases)
- ✅ Navigation & UI Verification

---

## 💻 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google Chrome / Firefox browser
- ChromeDriver / GeckoDriver (matching your browser version)

### Setup Steps

**1. Clone the repository**

```bash
git clone https://github.com/saiprakash0506/Wipro_Group5_Project.git
cd Wipro_Group5_Project/Ecommerce
```

**2. Setup Pytest Framework**

```bash
cd Pytest-framework

# Create and activate virtual environment
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**3. Setup Robot Framework**

```bash
cd ../robot-framework

# Install Robot Framework and SeleniumLibrary
pip install robotframework
pip install robotframework-seleniumlibrary
```

---

## 🧪 Running the Tests

### Pytest Tests

```bash
cd Pytest-framework

# Run all tests
pytest -v

# Run a specific test file
pytest tests/test_login.py -v

# Run with HTML report
pytest --html=reports/report.html --self-contained-html

# Run with coverage
pytest --cov=pages --cov-report=html

# See runcommand.txt for more run options
```

### Robot Framework Tests

```bash
cd robot-framework

# Run all test suites
robot tests/

# Run a specific test suite
robot tests/login_tests.robot

# Run with a custom output directory
robot --outputdir reports tests/

# Run with specific variables
robot --variable BROWSER:chrome tests/
```

---

## 🏗️ Framework Design

### Pytest – Page Object Model

```
┌─────────────────────────────────────┐
│            Tests Layer              │  ← Test cases (test_*.py)
│   (Assertions & Test Scenarios)     │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│            Pages Layer              │  ← Page Object classes
│  (Locators, Actions, Interactions)  │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│             Data Layer              │  ← External test data
│     (JSON / CSV / Excel files)      │
└─────────────────────────────────────┘
```

### Robot Framework – Keyword-Driven

```
┌─────────────────────────────────────┐
│            Tests Layer              │  ← .robot test suites
│    (Test Cases using Keywords)      │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│          Keywords Layer             │  ← Custom keyword definitions
│    (Reusable Steps & Actions)       │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│          Variables Layer            │  ← Centralized config/data
│  (URLs, Credentials, Selectors)     │
└─────────────────────────────────────┘
```

---

## 📊 Test Reports

Both frameworks generate detailed reports after test execution.

### Pytest Reports

Located in `Pytest-framework/reports/`:

- `report.html` – Visual HTML test summary

### Robot Framework Reports

Located in `robot-framework/reports/`:

- `report.html` – High-level test summary
- `log.html` – Step-by-step execution log
- `output.xml` – Machine-readable results

---

## 📝 API Response / Test Result Format

### Pytest Console Output (Sample)

```
PASSED tests/test_login.py::test_valid_login
PASSED tests/test_cart.py::test_add_to_cart
FAILED tests/test_checkout.py::test_invalid_card - AssertionError
```

### Robot Framework Output (Sample)

```
==============================================================================
Login Tests
==============================================================================
Valid Login With Correct Credentials              | PASS |
Invalid Login With Wrong Password                 | PASS |
==============================================================================
Login Tests                                       | PASS |
2 tests, 2 passed, 0 failed
==============================================================================
```

---

## 🎯 Learning Outcomes

Through this project, you will learn:

- ✅ UI test automation using Selenium WebDriver
- ✅ Page Object Model (POM) design pattern with Pytest
- ✅ Keyword-driven test design with Robot Framework
- ✅ Data-driven testing techniques
- ✅ Test fixtures, setup, and teardown strategies
- ✅ Generating and interpreting HTML test reports
- ✅ Structuring scalable and maintainable automation frameworks
- ✅ Cross-framework comparison (Pytest vs Robot Framework)

---

## 🏆 Project Status

| Component                  | Status              |
| -------------------------- | ------------------- |
| Pytest Framework Setup     | ✅ Complete         |
| Page Object Model (POM)    | ✅ Complete         |
| Pytest Test Cases          | ✅ Complete         |
| Robot Framework Setup      | ✅ Complete         |
| Robot Keywords & Variables | ✅ Complete         |
| Robot Test Cases           | ✅ Complete         |
| Test Reports               | ✅ Complete         |
| Documentation              | ✅ Complete         |
| Code Review                | 🟡 Ready for Review |

---

## 👥 Team

Developed by **Wipro Training – Group 5**

| #   | Name                   |
| --- | ---------------------- |
| 1   | Sai Prakash            |
| 2   | Prashant Kumar Jha     |
| 3   | Bhagyashree N          |
| 4   | Chowdam Mahendra       |
| 5   | Praseed Sreepadmakumar |
| 6   | Ravinesh Tiwari        |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is developed for educational purposes as part of the Wipro Training Program.

---

## 🙏 Acknowledgments

- Selenium WebDriver documentation
- Pytest documentation
- Robot Framework community
- Wipro Training mentors and instructors

---

**Happy Testing! 🚀**
