# Playwright Python Test Automation Framework

![CI](https://github.com/kallurayaankit/playwright-framework/actions/workflows/ci.yml/badge.svg)

A maintainable test automation framework using **Playwright (Python)**, **pytest**, and **Page Object Model** for [SauceDemo](https://www.saucedemo.com).

## Features
- Page Object Model (POM) for clean, reusable page classes
- Parameterized tests for login & cart, driven by JSON test data
- Automatic screenshot on test failure
- Parallel execution with pytest-xdist
- HTML reports (pytest-html)
- CI/CD pipeline with GitHub Actions (runs on push + daily schedule)

## Tech Stack
- Python 3.11+
- Playwright (Chromium)
- Pytest, pytest-html, pytest-xdist

## Setup (local)

```bash
# Clone the repo
git clone https://github.com/kallurayaankit/playwright-framework.git
cd playwright-framework

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate.bat   # (or source venv/bin/activate on Mac/Linux)

# Install dependencies
pip install -r requirements.txt
playwright install chromium