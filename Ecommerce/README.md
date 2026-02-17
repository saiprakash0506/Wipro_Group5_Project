# 🛒 Ecommerce Web Application

A front-end e-commerce web application developed as part of the **Wipro Group 5 Training Project**. The application is built using core web technologies (HTML & CSS) and includes automated UI testing powered by **Robot Framework**.

---

## 📁 Project Structure

```
Ecommerce/
├── index.html              # Landing / Home page
├── products.html           # Product listing page
├── product_detail.html     # Individual product detail page
├── cart.html               # Shopping cart page
├── checkout.html           # Checkout / order summary page
├── login.html              # User login page
├── register.html           # User registration page
├── css/
│   └── style.css           # Main stylesheet
├── images/                 # Product and UI images
└── tests/                  # Robot Framework test scripts
    └── ecommerce_tests.robot
```

> ⚠️ *Actual file names may vary. See the repository for the exact structure.*

---

## ✨ Features

- **Home Page** – Hero banner, featured products, and navigation
- **Product Listing** – Browse and filter available products
- **Product Detail** – View product descriptions, pricing, and images
- **Shopping Cart** – Add/remove items and view cart totals
- **Checkout Flow** – Order form and summary
- **User Authentication** – Login and registration pages
- **Responsive Design** – Mobile-friendly layout using HTML & CSS

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| HTML5 | Page structure and content |
| CSS3 | Styling and layout |
| Python | Test automation support |
| Robot Framework | Automated UI testing |

---

## 🚀 Getting Started

### Prerequisites

No build tools or server setup required for the front end. Simply open any `.html` file in a modern browser.

For running automated tests:

```bash
pip install robotframework
pip install robotframework-seleniumlibrary
```

### Running the Application

1. **Clone the repository:**

   ```bash
   git clone https://github.com/saiprakash0506/Wipro_Group5_Project.git
   cd Wipro_Group5_Project/Ecommerce
   ```

2. **Open the app in your browser:**

   ```bash
   # Simply open index.html in your browser
   open index.html        # macOS
   start index.html       # Windows
   xdg-open index.html    # Linux
   ```

---

## 🧪 Running Tests

Automated tests are written using **Robot Framework** to validate core e-commerce flows such as navigation, cart interactions, and form submissions.

```bash
# From the Ecommerce directory
robot tests/ecommerce_tests.robot
```

Test reports will be generated as:
- `report.html` – Summary report
- `log.html` – Detailed execution log
- `output.xml` – Machine-readable results

---

## 👥 Team

Developed by **Wipro Training – Group 5**

| Member | GitHub |
|---|---|
| Sai Prakash | [@saiprakash0506](https://github.com/saiprakash0506) |

---

## 📄 License

This project was built for educational purposes as part of a Wipro training program. No commercial license applies.

---

## 🔗 Related

- [Foodie App](../Foodie_App/) – The companion food ordering app in this project
- [Full Repository](https://github.com/saiprakash0506/Wipro_Group5_Project)
