# ⛽ Global Fuel Analytics: Global Fuel Prices and Taxation Trends

> **Data Analytics Capstone Project**  
> *A Comprehensive Empirical Analysis of International Fuel Pricing, Brent Crude Benchmarks, and Government Taxation Policies.*

---

## 📌 Project Overview

**Global Fuel Analytics** is a modern, responsive web application built with **Python Flask** and **Bootstrap 5**, integrating an interactive **Tableau Public** dashboard and Tableau Story.

The application allows researchers, policymakers, energy economists, and students to visually explore how retail prices for **Petrol (Gasoline)**, **Diesel**, and **Liquefied Petroleum Gas (LPG)** fluctuate across international markets relative to the **Brent Crude USD** benchmark, and how sovereign fiscal policies (**Tax Percentage** & **Subsidy Levels**) influence the final pump price paid by consumers.

### 🔗 Tableau Public Dashboard
- **Active Dashboard:** [Tableau Public Live Visualization](https://public.tableau.com/views/GlobalFuelPricesandTaxationTrend/GlobalFuelPriceDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 🌟 Key Features

1. **Modern Dark Navy Analytics UI**: Clean, accessible design featuring deep navy backgrounds (`#0a0f1d`), vibrant teal accents (`#14b8a6`), crisp typography, and high-contrast cards.
2. **Interactive Tableau Embedding API v3**: Utilizes Tableau's modern Web Component (`<tableau-viz>`) with seamless cross-origin communication, fullscreen mode, reload controls, and an automatic iframe fallback.
3. **Structured Dataset Dictionary**: Comprehensive documentation of all 10 core dimensions and measures (Country, Date, Income Level, Region, Subsidy Level, Brent Crude USD, Diesel USD Liter, LPG USD Liter, Petrol USD Liter, Tax Percentage).
4. **Tableau Story Walkthrough**: Guided narrative sequence illustrating price pass-through elasticity, fiscal policy divergence, and socio-economic vulnerability tiers.
5. **Jinja2 Template Inheritance**: Modular, clean web architecture with reusable `base.html` layout, responsive navbar, and sticky footer.
6. **Robust Error Handling**: Customized 404 and 500 error pages with user-friendly recovery paths.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.10+ / Flask 3.0.3
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5.3.3 & Bootstrap Icons
- **Data Visualization**: Tableau Desktop & Tableau Public (Embedding API v3)
- **Production Server**: Gunicorn 22.0.0
- **Version Control**: Git & GitHub

---

## 📁 Project Directory Structure

```text
global-fuel-analytics/
├── app.py                  # Main Flask application and routing logic
├── requirements.txt        # Python package dependencies
├── README.md               # Complete project documentation
├── .gitignore              # Files to ignore in Git version control
├── templates/              # Jinja2 HTML templates
│   ├── base.html           # Reusable master layout with navbar and footer
│   ├── index.html          # Homepage with hero, highlights, and summary cards
│   ├── dashboard.html      # Interactive Tableau Public embedded dashboard
│   ├── story.html          # Tableau Story narrative walkthrough
│   ├── about.html          # Dataset dictionary, methodology, and limitations
│   ├── contact.html        # Feedback and researcher contact page
│   └── 404.html            # Custom error 404 page
└── static/                 # Static assets
    ├── css/
    │   └── style.css       # Custom modern dark navy & teal styling
    ├── js/
    │   └── main.js         # Client-side interactions and Tableau helpers
    └── images/             # Visual previews and screenshots
```

---

## 🚀 Quickstart Guide (Local Setup)

Follow these steps to run the web application locally on your computer.

### Step 1: Clone or Open the Repository
```bash
git clone https://github.com/<your-username>/global-fuel-analytics.git
cd global-fuel-analytics
```

### Step 2: Create and Activate a Virtual Environment (Recommended)
On **Windows (PowerShell)**:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
On **macOS / Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Application
```bash
python app.py
```

### Step 5: Open in Your Web Browser
Open your browser and navigate to:
```text
http://127.0.0.1:5000/
```

---

## ⚙️ How to Configure Your Own Tableau URLs

If you make modifications or publish a new workbook on Tableau Public, you can easily change the URLs in `app.py`:

```python
# app.py line 18-35
USER_TABLEAU_LINK = (
    'https://public.tableau.com/views/GlobalFuelPricesandTaxationTrend/'
    'GlobalFuelPriceDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
)

app.config['TABLEAU_DASHBOARD_URL'] = os.environ.get(
    'TABLEAU_DASHBOARD_URL',
    USER_TABLEAU_LINK
)

app.config['TABLEAU_STORY_URL'] = os.environ.get(
    'TABLEAU_STORY_URL',
    USER_TABLEAU_LINK
)
```

Alternatively, you can set them using environment variables without modifying the code:
```bash
export TABLEAU_DASHBOARD_URL="<your-new-tableau-url>"
export TABLEAU_STORY_URL="<your-new-story-url>"
```

---

## 📊 Dataset Schema Reference

| Field Name | Type | Description |
| :--- | :--- | :--- |
| **Country** | Dimension (String) | Sovereign nation reporting fuel price records |
| **Date** | Dimension (Date) | Observation date for chronological trend indexing |
| **Income Level** | Dimension (Categorical) | World Bank classification (High, Upper-Middle, Lower-Middle, Low) |
| **Region** | Dimension (Geographic) | Continental or economic regional cluster |
| **Subsidy Level** | Dimension (Categorical) | Tier of price regulation or fiscal subsidy intervention |
| **Brent Crude USD** | Measure (Numeric) | Global crude benchmark price per barrel in USD |
| **Diesel USD Liter**| Measure (Currency) | Retail automotive diesel price per liter in USD |
| **LPG USD Liter**   | Measure (Currency) | Retail liquefied petroleum gas price per liter in USD |
| **Petrol USD Liter**| Measure (Currency) | Retail motor gasoline pump price per liter in USD |
| **Tax Percentage**  | Measure (Percent)  | Net effective taxation (excise + VAT) as % of retail price |

---

## 🚢 Deployment Guide

You can easily deploy this Flask web application to free cloud platforms like **Render**, **Railway**, or **PythonAnywhere**.

### Deploying to Render.com (Recommended & Free)

1. Create a free account at [render.com](https://render.com).
2. Push your code to a new repository on your **GitHub** account.
3. In Render Dashboard, click **New +** $\rightarrow$ **Web Service**.
4. Connect your GitHub repository.
5. Configure the build and start settings:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click **Create Web Service**. Your app will be live within 2-3 minutes at `https://<your-app-name>.onrender.com`.

---

## 💼 Adding to SkillWallet & Portfolio

To submit this project to **SkillWallet** or showcase it on your resume/LinkedIn:

1. **Live Website URL**: Copy your deployed website link (e.g., `https://global-fuel-analytics.onrender.com`).
2. **GitHub Repository URL**: Copy your repository link (e.g., `https://github.com/<your-username>/global-fuel-analytics`).
3. **Tableau Public URL**: Add your official visualization link:
   `https://public.tableau.com/views/GlobalFuelPricesandTaxationTrend/GlobalFuelPriceDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link`
4. Paste the links in the respective submission fields on your SkillWallet assignment portal.

---

## 👤 Author

- **Name:** Suhan
- **Project:** Global Fuel Prices and Taxation Trends: A Comprehensive Analysis
- **Program:** Data Analytics with Tableau

