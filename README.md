# AI Business Insight Generator

![Business Input Panel (default)](./screenshots/Business%20Input%20Panel%20(default).png)

AI-powered business diagnostics tool that translates **KPI signals, market context, and evidence data** into structured strategic insights.

Designed for **product, strategy, and operations teams**, the system combines structured analytics with **LLM reasoning** to diagnose business performance faster and more consistently.

---

## Live Demo

Run the application locally with Streamlit.

### Step 1 - Clone the repository

```bash
git clone https://github.com/yourusername/2026_AI_Business_Insight_Generator.git
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

```text
http://localhost:8501
```

---

## The Problem

Many teams monitor KPIs but struggle to translate signals into **clear strategic insights**.

Typical workflow today:

- Export KPI dashboards
- Manually analyze trends
- Compare with market context
- Write strategy notes or reports

This process is **slow, inconsistent, and difficult to scale**.

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
- evidence-based KPI summaries
- explainable confidence scoring

---

## How It Works

### Input

- KPI signals
- industry environment change
- market context
- uploaded KPI data

### Output

- structured business insight report
- KPI trend charts
- evidence summaries
- analysis confidence score

---

## Product Features

### 1. Business Context Input

![Business Input Panel (with input)](./screenshots/Business%20Input%20Panel%20(with%20input).png)

Users provide key business signals:

- Business type
- Target market
- Core business problem
- Industry environment change
- KPI changes
- Additional context

---

### 2. Clarification Questions

![Clarification Questions](./screenshots/Clarification%20Questions.png)

The system first generates **clarification questions** to reduce ambiguity before producing the final report.

This improves reasoning quality and helps the AI produce more accurate insights.

---

### 3. Evidence Data Upload

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

### 4. KPI Trend Visualization

![KPI Trend Visualization](./screenshots/KPI%20Trends%20Visualization.png)

Uploaded KPI data is automatically visualized through:

- time-series trend charts
- trend summary tables
- KPI change metrics

This helps validate insights with **actual performance signals**.

---

### 5. AI Insight Report

![AI Insight Report 1](./screenshots/AI%20Insights%20Report%20-%201.png)
![AI Insight Report 2](./screenshots/AI%20Insights%20Report%20-%202.png)

The system generates a structured report including:

- key problem diagnosis
- potential root causes
- strategic recommendations
- risk signals

The output is designed to resemble a **consulting-style strategy memo**.

---

### 6. Explainable Confidence Score

![Analysis Confidence & Export Report](./screenshots/Analysis%20Confidence%20&%20Export%20Report.png)

Each report includes a **confidence score (0–7)** based on:

- business context completeness
- KPI specificity
- numeric KPI signals
- clarification answers
- evidence data
- data usability

This improves **AI explainability and trust** by showing how reliable the analysis is.

---

## Tech Stack

- **Python**
- **Streamlit** - interactive analytics interface
- **OpenAI API** - LLM reasoning engine
- **Pandas** - evidence data parsing and KPI analysis
- **Markdown / python-docx** - report generation and export

---

## Architecture

The system follows a structured reasoning pipeline combining **user input, evidence data, and LLM-based analysis**.

Workflow:

```text
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
Structured Report Output
```

## Example Use Cases

This tool can be used for:

- Product teams diagnosing KPI changes  
- Growth teams analyzing conversion trends  
- Strategy teams evaluating market shifts  
- Startup founders understanding early product signals  
- Operations teams summarizing business performance
