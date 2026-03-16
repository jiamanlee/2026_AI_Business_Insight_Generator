# AI Business Insight Generator

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-green)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

Turn KPI signals and market context into **structured strategic insights** using AI.

AI-powered analytics tool combining **LLM reasoning + structured KPI signals + evidence data** to generate explainable business diagnostics.

![AI Insight Generator Demo](./screenshots/Business%20Input%20Panel%20(default).png)

---

## Key Features

- AI-powered business diagnostics  
- KPI trend visualization from uploaded datasets  
- clarification question workflow to reduce ambiguity  
- evidence-based reasoning using structured KPI signals  
- explainable confidence scoring  
- exportable consulting-style reports (Markdown / DOCX)

---

# Quick Start

Run the application locally using Streamlit.

### Step 1 - Clone the repository

```bash
git clone https://github.com/jiamanlee/2026_AI_Business_Insight_Generator.git
cd 2026_AI_Business_Insight_Generator
```

### Step 2 - Install required dependencies

```bash
pip install -r requirements.txt
```

### Step 3 - Set your OpenAI API key

Before running the application, set your OpenAI API key:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

You can obtain an API key from:

https://platform.openai.com

### Step 4 - Run the Streamlit app

```bash
streamlit run app.py
```

The application will open automatically in your browser:

```
http://localhost:8501
```

---

# The Problem

Many teams monitor KPIs but struggle to translate signals into **clear strategic insights**.

Typical workflow today:

- Export KPI dashboards
- Manually analyze trends
- Compare with market context
- Write strategy notes or reports

This process is **slow, inconsistent, and difficult to scale**.

---

# The Solution

AI Business Insight Generator combines:

- **Structured KPI signals**
- **Market context**
- **Evidence data**
- **LLM reasoning**

to automatically generate a **structured business insight report**.

The system also provides:

- KPI trend visualization
- evidence-based KPI summaries
- explainable confidence scoring

---

# How It Works

### Input

Users provide:

- KPI signals
- industry environment change
- market context
- uploaded KPI datasets

### Output

The system generates:

- structured business insight report
- KPI trend charts
- evidence summaries
- analysis confidence score

---

# Product Walkthrough

## 1. Business Context Input

![Business Input Panel](./screenshots/Business%20Input%20Panel%20(with%20input).png)

Users provide key business signals including:

- business type
- target market
- core business problem
- industry environment change
- KPI changes
- additional context

---

## 2. Clarification Questions

![Clarification Questions](./screenshots/Clarification%20Questions.png)

The system first generates **clarification questions** to reduce ambiguity before producing the final report.

This improves reasoning quality and helps the AI produce more accurate insights.

---

## 3. Evidence Data Upload

![Evidence Data Upload](./screenshots/Evidence%20Data%20Upload.png)

Users can upload KPI datasets (CSV / Excel), such as:

- new_signups
- conversion_rate
- active_users
- revenue
- upgrade_rate

The system automatically:

- detects date columns
- detects KPI metrics
- summarizes KPI trends

---

## 4. KPI Trend Visualization

![KPI Trend Visualization](./screenshots/KPI%20Trends%20Visualization.png)

Uploaded KPI data is automatically visualized through:

- time-series trend charts
- trend summary tables
- KPI change metrics

This helps validate insights using **actual performance signals**.

---

## 5. AI Insight Report

![AI Insight Report](./screenshots/AI%20Insights%20Report%20-%201.png)
![AI Insight Report](./screenshots/AI%20Insights%20Report%20-%202.png)

The system generates a structured report including:

- key problem diagnosis
- potential root causes
- strategic recommendations
- risk signals

The output is designed to resemble a **consulting-style strategy memo**.

---

## 6. Explainable Confidence Score + Export

![Analysis Confidence](./screenshots/Analysis%20Confidence%20&%20Export%20Report.png)

Each report includes a **confidence score (0–7)** based on:

- business context completeness
- KPI specificity
- numeric KPI signals
- clarification answers
- evidence data
- data usability

Reports can be exported as:

- Markdown  
- DOCX  

---

# Tech Stack

- **Python**
- **Streamlit** – interactive analytics interface
- **OpenAI API** – LLM reasoning engine
- **Pandas** – evidence data parsing and KPI analysis
- **Markdown / python-docx** – report generation and export

---

# Architecture

The system follows a structured reasoning pipeline combining **user input, evidence data, and LLM-based analysis**.

```
User Input
      ↓
Clarification Question Generation (LLM)
      ↓
User Answers
      ↓
Evidence Data Parsing (Pandas)
      ↓
KPI Trend Visualization
      ↓
Business Insight Generation (LLM)
      ↓
Confidence Scoring
      ↓
Report Rendering & Export
```

---

# Example Use Cases

This tool can be used for:

- Product teams diagnosing KPI changes  
- Growth teams analyzing conversion trends  
- Strategy teams evaluating market shifts  
- Startup founders understanding early product signals  
- Operations teams summarizing business performance  

---

# Related Projects

More analytics projects:

- Hotel Revenue Intelligence Dashboard  
- WTD Analytics & Trend Tracker  
- Top-of-Funnel Spend Optimization (MMM)

GitHub Portfolio:

https://github.com/jiamanlee
