"""
Global Fuel Analytics - Flask Web Application
Project: Global Fuel Prices and Taxation Trends: A Comprehensive Analysis
Author: Suhan
"""

import os
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fuel-analytics-secret-key-2026')

# ==============================================================================
# TABLEAU PUBLIC CONFIGURATION
# ==============================================================================
# User provided Tableau Public link used everywhere across the application:
USER_TABLEAU_LINK = (
    'https://public.tableau.com/views/GlobalFuelPricesandTaxationTrend/'
    'GlobalFuelPriceDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
)

# 1. Dashboard URL:
app.config['TABLEAU_DASHBOARD_URL'] = os.environ.get(
    'TABLEAU_DASHBOARD_URL',
    USER_TABLEAU_LINK
)

# 2. Story URL:
app.config['TABLEAU_STORY_URL'] = os.environ.get(
    'TABLEAU_STORY_URL',
    USER_TABLEAU_LINK
)


@app.context_processor
def inject_global_vars():
    """Global template variables accessible across all Jinja2 templates."""
    d_url = app.config['TABLEAU_DASHBOARD_URL']
    s_url = app.config['TABLEAU_STORY_URL']

    # Clean base URLs for embedding and iframe fallback
    d_clean = d_url.split('?')[0] + '?:embed=yes&:showVizHome=no&:toolbar=yes'
    s_clean = s_url.split('?')[0] + '?:embed=yes&:showVizHome=no&:toolbar=yes'

    return {
        'app_name': 'Global Fuel Analytics',
        'dashboard_url': d_url,
        'story_url': s_url,
        'dashboard_embed_url': d_clean,
        'story_embed_url': s_clean,
        'current_year': 2026
    }


# ==============================================================================
# APPLICATION ROUTES
# ==============================================================================

@app.route('/')
def home():
    """Home Page: Hero section, fuel metrics overview, project overview, and CTAs."""
    fuel_categories = [
        {
            'name': 'Petrol (Gasoline)',
            'icon': 'bi-fuel-pump-fill',
            'badge': 'Consumer Transport',
            'desc': 'Analyzes retail petrol prices across global markets, tracking daily & monthly consumer expenditure patterns and regional disparities.',
            'metric_label': 'Key Metric',
            'metric_value': 'USD / Liter'
        },
        {
            'name': 'Diesel Fuel',
            'icon': 'bi-truck-front-fill',
            'badge': 'Commercial Logistics',
            'desc': 'Crucial driver for global supply chains, freight transportation, agriculture, and heavy industrial machinery economics.',
            'metric_label': 'Key Metric',
            'metric_value': 'USD / Liter'
        },
        {
            'name': 'Liquefied Petroleum Gas (LPG)',
            'icon': 'bi-fire',
            'badge': 'Domestic & Auto Gas',
            'desc': 'Monitors household heating, cooking, and clean automotive fuel adoption trends with sensitivity to government intervention.',
            'metric_label': 'Key Metric',
            'metric_value': 'USD / Liter'
        },
        {
            'name': 'Taxation & Subsidies',
            'icon': 'bi-percent',
            'badge': 'Fiscal Policy',
            'desc': 'Uncovers net tax percentage, excise duties, VAT, and fiscal subsidy levels that determine the divergence between crude and pump prices.',
            'metric_label': 'Key Indicator',
            'metric_value': 'Tax % & Subsidy Tier'
        }
    ]

    dataset_highlights = [
        {'title': 'Crude Benchmark', 'val': 'Brent Crude USD', 'icon': 'bi-droplet-half'},
        {'title': 'Socio-Economic Filter', 'val': 'Income Level & Region', 'icon': 'bi-globe-americas'},
        {'title': 'Policy Classification', 'val': 'Subsidy Level & Tax %', 'icon': 'bi-shield-check'},
        {'title': 'Temporal Span', 'val': 'Multi-Year Historical', 'icon': 'bi-calendar-range'}
    ]

    return render_template('index.html', active_page='home', fuel_categories=fuel_categories, dataset_highlights=dataset_highlights)


@app.route('/dashboard')
def dashboard():
    """Interactive Dashboard Page: Official Tableau Embedding API v3 with interactive controls and fallback."""
    return render_template(
        'dashboard.html',
        active_page='dashboard',
        viz_url=app.config['TABLEAU_DASHBOARD_URL']
    )


@app.route('/story')
def story():
    """Tableau Story Page: Narrative walkthrough of trends, key analytical observations, and policy conclusions."""
    return render_template(
        'story.html',
        active_page='story',
        story_url=app.config['TABLEAU_STORY_URL']
    )


@app.route('/about')
def about():
    """About Project Page: Dataset schema, methodology, visualizations created, tools, and limitations."""
    schema_fields = [
        {'field': 'Country', 'type': 'Dimension (Categorical)', 'desc': 'Sovereign nation or territory reporting fuel pricing data.'},
        {'field': 'Date', 'type': 'Dimension (Date/Time)', 'desc': 'Observation timestamp for price indexing and longitudinal trend study.'},
        {'field': 'Income Level', 'type': 'Dimension (Categorical)', 'desc': 'World Bank economic classification (Low, Lower-Middle, Upper-Middle, High income).'},
        {'field': 'Region', 'type': 'Dimension (Geographic)', 'desc': 'Geographic regional clustering (e.g., Sub-Saharan Africa, Europe, Americas, APAC).'},
        {'field': 'Subsidy Level', 'type': 'Dimension (Categorical)', 'desc': 'Degree of government price intervention, artificial price caps, or direct subsidies.'},
        {'field': 'Brent Crude USD', 'type': 'Measure (Numeric)', 'desc': 'Global benchmark price of sweet light crude oil per barrel in US Dollars.'},
        {'field': 'Diesel USD Liter', 'type': 'Measure (Currency)', 'desc': 'Retail price of automotive diesel per liter converted to USD.'},
        {'field': 'LPG USD Liter', 'type': 'Measure (Currency)', 'desc': 'Retail price of liquefied petroleum gas per liter in USD.'},
        {'field': 'Petrol USD Liter', 'type': 'Measure (Currency)', 'desc': 'Retail pump price of gasoline/petrol per liter in USD.'},
        {'field': 'Tax Percentage', 'type': 'Measure (Percentage)', 'desc': 'Composite taxation rate (Excise, VAT, environmental levies) as % of retail price.'}
    ]

    return render_template('about.html', active_page='about', schema_fields=schema_fields)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact & Feedback Page."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash('Kripya sabhi zaroori fields (Name, Email, Message) bharein.', 'warning')
        else:
            flash(f'Dhanyawad {name}! Aapka message successfully receive ho gaya hai. Hum jaldi sampark karenge.', 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html', active_page='contact')


# ==============================================================================
# ERROR HANDLERS
# ==============================================================================

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 Page Not Found error handler."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    """Custom 500 Internal Server Error handler."""
    return render_template('404.html', error_title="500 - Server Error", error_msg="Server par ek takneeki samasya aayi hai. Kripya thodi der baad punah prayas karein."), 500


if __name__ == '__main__':
    # Local development server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

