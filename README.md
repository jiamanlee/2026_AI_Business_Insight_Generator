# AI Business Insight Generator

AI-powered business diagnostics tool that converts KPI signals and market context into structured strategic insights.

This tool helps product, strategy, and operations teams quickly diagnose business performance using both **structured KPI data and LLM reasoning**.

---

## The Problem

Many teams monitor KPIs but struggle to translate signals into clear strategic insights.

Typical workflow today:

- Export KPI dashboards
- Manually analyze trends
- Compare with market context
- Write strategy notes or reports

This process is **slow, inconsistent, and hard to scale**.

---

## The Solution

AI Business Insight Generator combines:

- **Structured KPI signals**
- **Market context**
- **Evidence data**
- **LLM reasoning**

to automatically generate a **structured business insight report**.

The system also provides:

- KPI trend visualization
- evidence-based summaries
- explainable confidence scoring

---

## Example Output

Input:

- KPI signals  
- industry change  
- market context  
- uploaded KPI data

Output:

- Business insight report
- KPI trend charts
- evidence summary
- analysis confidence score

---

## Demo Features

### 1. Business Context Input

Users provide:

- Business type
- Target market
- Core business problem
- Industry environment change
- KPI changes
- Additional context

---

### 2. Clarification Questions

The system first generates **clarification questions** to reduce ambiguity before producing the final report.

This improves reasoning quality.

---

### 3. Evidence Data Upload

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

### 4. KPI Trend Visualization

Uploaded KPI data is automatically visualized:

- time-series trend charts
- trend summary tables
- KPI change metrics

---

### 5. AI Insight Report

The system generates a structured report including:

- key problem diagnosis
- potential root causes
- strategic recommendations
- risk signals

---

### 6. Explainable Confidence Score

Each report includes a **confidence score (0–7)** based on:

- business context completeness
- KPI specificity
- numeric signals
- clarification answers
- evidence data
- data usability

This improves **AI explainability and trust**.

---

## Screenshots

Example interface:

Business input panel  
KPI trend visualization  
AI insight report  
analysis confidence score

*(Add screenshots here)*

---

## Tech Stack

- Python
- Streamlit
- OpenAI API
- Pandas
- Markdown
- python-docx

---

## Architecture
