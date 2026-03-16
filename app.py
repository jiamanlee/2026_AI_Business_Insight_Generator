import streamlit as st
import pandas as pd
import re
import io
import markdown
from docx import Document
from prompt_engine import build_prompt, build_clarify_prompt
from llm_client import call_llm

# ---------- i18n ----------
I18N = {
    "en": {
        "title": "AI Business Insight Generator",
        "lang_btn": "中文",
        "business_type": "Business Type",
        "target_market": "Target Market",
        "core_problem": "Core Problem",
        "industry_change": "Industry Environment Changes",
        "kpi_changes": "Key KPI Changes (be specific)",
        "kpi_ph": "e.g., Traffic stable, conversion -4%, AOV -7%, repeat unchanged",
        "extra_context": "Extra Context (optional)",
        "extra_ph": "e.g., competitor launched personalization + discounts",
        "btn": "Generate Clarification Questions",
        "clarify_title": "Clarification Questions (answer these, then generate final report)",
        "clarify_btn": "Generate Final Report",
        "answers_label": "Your Answers",
        "report_title": "Business Insight Report",
        "err_kpi": "Please fill in Key KPI Changes.",
        "spinner_q": "Generating clarification questions...",
        "spinner_r": "Generating report...",
        "quota_tip": "If you see API ERROR 429 (insufficient_quota), you need to enable billing/credits in OpenAI Platform.",
        "upload_label": "Upload evidence data (optional): CSV or Excel",
        "upload_note": "Recommended: 2–3 months of weekly/daily KPI data (date + KPI columns).",
        "confidence_title": "Analysis Confidence",
        "confidence_caption": "Confidence Level",
        "evidence_title": "Evidence Summary",
        "chart_title": "KPI Trends",
        "chart_date": "Select date column",
        "chart_metrics": "Select KPI columns to plot",
        "chart_warn_file": "Unable to read the uploaded evidence file.",
        "chart_warn_date": "No valid date values found in the selected column.",
        "chart_warn_kpi": "No numeric KPI columns were detected.",
        "chart_info_kpi": "Please select at least one KPI column.",
        "trend_summary_title": "Trend Summary Table",
        "download_md": "Download Markdown",
        "download_docx": "Download DOCX",
        "download_pdf": "Download PDF",
        "none_text": "None",
        "clarify_label": "Clarification Questions",
        "answers_label_internal": "User Answers",
        "evidence_label": "Evidence Summary",
    },
    "zh": {
        "title": "AI 商业洞察生成器",
        "lang_btn": "English",
        "business_type": "业务类型",
        "target_market": "目标市场",
        "core_problem": "当前核心问题",
        "industry_change": "行业环境变化",
        "kpi_changes": "关键KPI变化（尽量具体）",
        "kpi_ph": "例如：流量稳定，转化率-4%，客单价-7%，复购不变",
        "extra_context": "补充背景（可选）",
        "extra_ph": "例如：竞品上线推荐系统并加大折扣",
        "btn": "生成澄清问题",
        "clarify_title": "关键澄清问题（先回答，再生成最终报告）",
        "clarify_btn": "生成最终报告",
        "answers_label": "你的补充回答",
        "report_title": "商业洞察报告",
        "err_kpi": "请填写关键KPI变化。",
        "spinner_q": "生成澄清问题中...",
        "spinner_r": "生成报告中...",
        "quota_tip": "如果看到 API ERROR 429（insufficient_quota），需要去 OpenAI Platform 开通计费/充值。",
        "upload_label": "上传证据数据（可选）：CSV 或 Excel",
        "upload_note": "建议：2–3个月的周度/日度 KPI 数据（日期 + KPI列）。",
        "confidence_title": "分析置信度",
        "confidence_caption": "置信度",
        "evidence_title": "证据数据摘要",
        "chart_title": "KPI 趋势图",
        "chart_date": "请选择日期列",
        "chart_metrics": "选择要展示的 KPI 列",
        "chart_warn_file": "无法读取上传的证据数据文件。",
        "chart_warn_date": "所选列中未识别到有效日期。",
        "chart_warn_kpi": "未检测到可用的数值型 KPI 列。",
        "chart_info_kpi": "请至少选择一个 KPI 列。",
        "trend_summary_title": "趋势变化汇总",
        "download_md": "下载 Markdown",
        "download_docx": "下载 DOCX",
        "download_pdf": "下载 PDF",
        "none_text": "无",
        "clarify_label": "澄清问题",
        "answers_label_internal": "用户补充回答",
        "evidence_label": "证据数据摘要",
    }
}

OPTIONS = {
    "en": {
        "business_type": ["SaaS Subscription", "E-commerce", "Content Platform", "Local Services/O2O", "Education", "Finance", "Other"],
        "target_market": ["B2B SMB", "B2B Enterprise", "B2C Mass", "B2C Premium", "International", "Other"],
        "core_problem": ["Slowing growth", "Paid conversion drop", "Retention drop", "Margin decline", "CAC increase", "Other"],
        "industry_change": ["No major change", "Competitor price cut", "Competitor new feature", "Platform/channel rule change", "Policy/regulatory change", "Macro demand weakening", "Other"]
    },
    "zh": {
        "business_type": ["SaaS订阅服务", "电商", "内容平台", "本地生活/O2O", "教育", "金融", "其他"],
        "target_market": ["B2B-中小企业", "B2B-大企业", "B2C-大众用户", "B2C-高客单", "海外市场", "其他"],
        "core_problem": ["增长放缓", "付费转化率下降", "留存下降", "利润率下降", "获客成本上升", "其他"],
        "industry_change": ["无明显变化", "竞品降价", "竞品推出新功能", "平台/渠道规则变化", "政策/合规变化", "宏观需求走弱", "其他"]
    }
}

# ---------- session state ----------
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "lang" not in st.session_state:
    st.session_state.lang = "en"
if "clarify_questions" not in st.session_state:
    st.session_state.clarify_questions = ""
if "clarify_answers" not in st.session_state:
    st.session_state.clarify_answers = ""
if "final_report" not in st.session_state:
    st.session_state.final_report = ""

st.set_page_config(page_title="AI Business Insight Generator", layout="wide")

# ---------- header ----------
left, right = st.columns([0.8, 0.2])

with right:
    switch_label = "中文" if st.session_state.lang == "en" else "English"
    if st.button(switch_label):
        st.session_state.lang = "zh" if st.session_state.lang == "en" else "en"
        st.session_state.clarify_questions = ""
        st.session_state.clarify_answers = ""
        st.session_state.final_report = ""
        st.session_state.uploaded_file = None

t = I18N[st.session_state.lang]
opt = OPTIONS[st.session_state.lang]

with left:
    st.title(t["title"])

# ---------- input form ----------
with st.form("survey_form"):
    col1, col2 = st.columns(2)

    with col1:
        business_type = st.selectbox(t["business_type"], opt["business_type"])
        target_market = st.selectbox(t["target_market"], opt["target_market"])
        core_problem = st.selectbox(t["core_problem"], opt["core_problem"])

    with col2:
        industry_change = st.selectbox(t["industry_change"], opt["industry_change"])
        kpi_changes = st.text_area(t["kpi_changes"], placeholder=t["kpi_ph"])
        extra_context = st.text_area(t["extra_context"], placeholder=t["extra_ph"])

    st.caption(t["upload_note"])

    uploaded = st.file_uploader(
        t["upload_label"],
        type=["csv", "xlsx"]
    )

    if uploaded is not None:
        st.session_state.uploaded_file = uploaded

    submitted = st.form_submit_button(t["btn"])

# ---------- helpers ----------
def _normalize_col_name(col: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(col).strip().lower())


def load_uploaded_table(uploaded_file):
    if uploaded_file is None:
        return None, "no_file"

    try:
        uploaded_file.seek(0)
        name = uploaded_file.name.lower()

        if name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        if df is None or df.empty:
            return None, "empty_file"

        df.columns = [_normalize_col_name(c) for c in df.columns]
        return df, None

    except Exception as e:
        return None, str(e)


def auto_detect_date_col(df):
    candidates = [c for c in df.columns if c in ["date", "day", "week", "month", "period"] or "date" in c]
    if candidates:
        return candidates[0]

    best_col = None
    best_rate = 0
    for c in df.columns[:20]:
        parsed = pd.to_datetime(df[c], errors="coerce")
        rate = parsed.notna().mean()
        if rate > best_rate and rate >= 0.6:
            best_rate = rate
            best_col = c

    return best_col


def auto_detect_metric_cols(df):
    numeric_cols = []
    for c in df.columns:
        if df[c].dtype.kind in "biufc":
            if any(k in c for k in ["id", "uuid", "user", "email", "phone"]):
                continue
            numeric_cols.append(c)
    return numeric_cols


def summarize_uploaded_data(uploaded_file, lang):
    df, err = load_uploaded_table(uploaded_file)

    if df is None:
        return "", False

    date_col = auto_detect_date_col(df)
    if not date_col:
        if lang == "en":
            return "Evidence file uploaded, but no recognizable date column was found.", False
        else:
            return "已上传证据文件，但未识别到可用的日期列。", False

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col]).sort_values(date_col)

    if len(df) < 2:
        if lang == "en":
            return "Evidence file uploaded, but there are not enough valid rows for trend analysis.", False
        else:
            return "已上传证据文件，但有效数据行不足，无法进行趋势分析。", False

    summary_lines = []

    def add_pct_change(col, label_en, label_zh):
        if col in df.columns:
            first = df[col].iloc[0]
            last = df[col].iloc[-1]
            if pd.notna(first) and first != 0 and pd.notna(last):
                pct = ((last - first) / first) * 100
                if lang == "en":
                    summary_lines.append(f"- {label_en}: changed {pct:.1f}% over the uploaded period")
                else:
                    summary_lines.append(f"- {label_zh}：在上传周期内变化了 {pct:.1f}%")

    def add_pp_change(col, label_en, label_zh):
        if col in df.columns:
            first = df[col].iloc[0]
            last = df[col].iloc[-1]
            if pd.notna(first) and pd.notna(last):
                pp = (last - first) * 100
                if lang == "en":
                    summary_lines.append(f"- {label_en}: changed {pp:.1f} percentage points over the uploaded period")
                else:
                    summary_lines.append(f"- {label_zh}：在上传周期内变化了 {pp:.1f} 个百分点")

    add_pct_change("new_signups", "New signups", "新客注册量")
    add_pp_change("trial_to_paid_rate", "Trial-to-paid rate", "试用转付费率")
    add_pct_change("active_users", "Active users", "活跃用户数")
    add_pp_change("enterprise_upgrade_rate", "Enterprise upgrade rate", "企业版升级率")

    if not summary_lines:
        if lang == "en":
            return "Evidence file uploaded, but no supported KPI columns were detected.", False
        else:
            return "已上传证据文件，但未识别到支持的KPI列。", False

    return "\n".join(summary_lines), True


def calculate_confidence(
    business_type,
    target_market,
    core_problem,
    industry_change,
    kpi_changes,
    clarify_answers,
    uploaded_file,
    lang
):
    score = 0

    # structured context
    if business_type and target_market and core_problem and industry_change:
        score += 1

    # KPI specificity
    if kpi_changes and len(kpi_changes.strip()) > 30:
        score += 1

    # KPI numeric density
    if kpi_changes and ("%" in kpi_changes or any(ch.isdigit() for ch in kpi_changes)):
        score += 1

    # clarify answer completeness
    if clarify_answers and len(clarify_answers.strip()) > 50:
        score += 1

    # clarify answer structure
    if clarify_answers and ("\n" in clarify_answers or "-" in clarify_answers or "1." in clarify_answers):
        score += 1

    # file uploaded
    if uploaded_file is not None:
        score += 1

    # file parseability / usability
    _, file_valid = summarize_uploaded_data(uploaded_file, lang)
    if file_valid:
        score += 1

    return min(score, 7)


def render_kpi_charts(uploaded_file, lang):
    if uploaded_file is None:
        return

    df, err = load_uploaded_table(uploaded_file)

    if df is None:
        st.warning(t["chart_warn_file"])
        return

    st.markdown(f"### {t['chart_title']}")

    guessed_date_col = auto_detect_date_col(df)

    date_col = st.selectbox(
        t["chart_date"],
        options=list(df.columns),
        index=(list(df.columns).index(guessed_date_col) if guessed_date_col in df.columns else 0),
        key="chart_date_col"
    )

    df["_parsed_date"] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=["_parsed_date"]).sort_values("_parsed_date")

    if df.empty:
        st.warning(t["chart_warn_date"])
        return

    metric_candidates = auto_detect_metric_cols(df)

    if not metric_candidates:
        st.warning(t["chart_warn_kpi"])
        return

    selected_metrics = st.multiselect(
        t["chart_metrics"],
        options=metric_candidates,
        default=metric_candidates[:3],
        key="chart_metric_cols"
    )

    if not selected_metrics:
        st.info(t["chart_info_kpi"])
        return

    chart_df = df.set_index("_parsed_date")[selected_metrics]
    st.line_chart(chart_df)

    summary_rows = []
    for c in selected_metrics:
        first = chart_df[c].iloc[0]
        last = chart_df[c].iloc[-1]
        abs_change = last - first

        pct_change = ""
        if pd.notna(first) and first != 0:
            pct_change = f"{((last - first) / first) * 100:.1f}%"

        summary_rows.append({
            "metric": c,
            "first": first,
            "last": last,
            "absolute_change": abs_change,
            "percent_change": pct_change
        })

    st.markdown(f"#### {t['trend_summary_title']}")
    st.dataframe(pd.DataFrame(summary_rows))


# ---------- compute reusable evidence / score ----------
data_summary, file_valid = summarize_uploaded_data(
    st.session_state.uploaded_file,
    st.session_state.lang
)

score = calculate_confidence(
    business_type,
    target_market,
    core_problem,
    industry_change,
    kpi_changes,
    st.session_state.clarify_answers,
    st.session_state.uploaded_file,
    st.session_state.lang
)

# ---------- stage 1: generate clarification questions ----------
if submitted:
    st.session_state.final_report = ""
    if not kpi_changes.strip():
        st.error(t["err_kpi"])
    else:
        with st.spinner(t["spinner_q"]):
            clarify_prompt = build_clarify_prompt(
                st.session_state.lang,
                business_type,
                target_market,
                kpi_changes,
                core_problem,
                industry_change,
                extra_context
            )
            questions = call_llm(clarify_prompt)

        st.session_state.clarify_questions = questions

# ---------- clarification UI ----------
if st.session_state.clarify_questions:
    st.subheader(t["clarify_title"])
    st.markdown(st.session_state.clarify_questions)
    st.caption(t["quota_tip"])

    st.session_state.clarify_answers = st.text_area(
        t["answers_label"],
        value=st.session_state.clarify_answers,
        placeholder="Answer the 3 questions here (bullet points are fine)."
        if st.session_state.lang == "en"
        else "在这里回答上述3个问题（用要点写即可）"
    )

    if st.button(t["clarify_btn"]):
        with st.spinner(t["spinner_r"]):
            extra_plus = (extra_context + "\n\n") if extra_context else ""

            if data_summary:
                extra_plus += t["evidence_label"] + ":\n" + data_summary + "\n\n"

            extra_plus += t["clarify_label"] + ":\n" + st.session_state.clarify_questions + "\n\n"
            extra_plus += t["answers_label_internal"] + ":\n" + (
                st.session_state.clarify_answers.strip()
                if st.session_state.clarify_answers.strip()
                else t["none_text"]
            )

            prompt = build_prompt(
                st.session_state.lang,
                business_type,
                target_market,
                kpi_changes,
                core_problem,
                industry_change,
                extra_plus
            )
            report = call_llm(prompt)

        st.session_state.final_report = report

# ---------- final report + evidence + charts + confidence + downloads ----------
if st.session_state.final_report:
    st.subheader(t["report_title"])
    st.markdown(st.session_state.final_report)

    report_md = st.session_state.final_report

    # Evidence summary after final report
    if data_summary:
        st.markdown(f"### {t['evidence_title']}")
        st.markdown(data_summary)

    # KPI charts after final report
    render_kpi_charts(st.session_state.uploaded_file, st.session_state.lang)

    # Confidence after final report

    st.markdown(f"### {t['confidence_title']}")

    if st.session_state.lang == "en":
        st.caption(
            "ⓘ Confidence score is based on the completeness and reliability of the inputs "
            "(business context, KPI signals, clarification answers, uploaded evidence data, and data usability)."
        )
    else:
        st.caption(
            "ⓘ 该分数根据输入信息的完整度和可靠性计算（业务背景、KPI信号、澄清问题回答、证据数据及数据可用性）。"
        )

    bars = ""
    for i in range(7):
        if i < score:
            if score >= 5:
                bars += "🟩"
            elif score >= 3:
                bars += "🟨"
            else:
                bars += "🟥"
        else:
            bars += "⬜"

    st.markdown(bars)

    if score >= 6:
        level_label = "High" if st.session_state.lang == "en" else "高"
    elif score >= 4:
        level_label = "Medium" if st.session_state.lang == "en" else "中"
    else:
        level_label = "Low" if st.session_state.lang == "en" else "低"

    st.caption(f"{t['confidence_caption']}: {score}/7 ({level_label})")

    # Downloads
    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label=t["download_md"],
            data=report_md,
            file_name="business_insight_report.md",
            mime="text/markdown"
        )

    with col2:
        doc = Document()
        for line in report_md.split("\n"):
            doc.add_paragraph(line)

        doc_buffer = io.BytesIO()
        doc.save(doc_buffer)

        st.download_button(
            label=t["download_docx"],
            data=doc_buffer.getvalue(),
            file_name="business_insight_report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

