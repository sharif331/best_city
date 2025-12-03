# Best City – UI Automation Testing Project (Selenium + Pytest)

This project contains UI automation test cases written using **Python**, **Selenium**, and **Pytest** following a **Page Object Model (POM)** structure.

The purpose of this project is to demonstrate practical UI automation skills for interview evaluations.  
The tests interact with a sample real-estate investment web application.

---

## 📦 Project Setup

### 1. Clone the Repository

```bash
git clone git@github.com:sharif331/best_city.git
cd best_city
```

### 🐍 2. Create & Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 📥 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### ▶️ Running Tests
Run a specific test:
```bash
pytest tests/test_property.py
```
Run in headless mode with HTML report:
```bash
HEADLESS=true pytest tests/test_property.py --html=report.html --self-contained-html
```
Run with custom URL:
```bash
HEADLESS=true URL=http://localhost:3000/ pytest tests/test_property.py --html=report.html --self-contained-html
```

### 🌍 Environment Variables
HEADLESS=true	 Run Chrome in headless mode,
URL=<value>	 Override the application's base URL

