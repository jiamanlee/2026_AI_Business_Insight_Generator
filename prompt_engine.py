def build_prompt(
    lang: str,
    business_type: str,
    target_market: str,
    kpi_changes: str,
    core_problem: str,
    industry_change: str,
    extra_context: str
):
    extra = extra_context.strip() if extra_context and extra_context.strip() else ("None" if lang == "en" else "无")

    if lang == "en":
        return f"""
You are a senior business analyst and AI product strategy advisor.

Generate a structured business insight report based on the following information:

[Business Type] {business_type}
[Target Market] {target_market}
[Key KPI Changes] {kpi_changes}
[Core Problem] {core_problem}
[Industry Changes] {industry_change}
[Extra Context] {extra}

Output Rules:
- Do NOT repeat the report title. Start directly from the first section.
- Use a highly conclusion-driven style; avoid generic explanations.
- Use bold section headers (**Header**) for consistent readability.
- Keep each section concise (max 3–4 bullets).

Strict Output Structure (Executive / Consulting Memo Style):

**Executive Conclusion**
- 1–2 sentences: the most likely core driver of the KPI changes
- Include the immediate strategic implication

**Key Evidence Signals**
- 3–4 most critical facts or data signals supporting the conclusion
- Prefer: time pattern, segment pattern, funnel drop point, alignment with competitor actions

**Primary Diagnosis**
- State the single most likely root cause
- Provide a short reasoning chain:
  Observation → Key evidence → Why this cause best explains the KPI pattern

**Secondary Considerations (Optional)**
- Only include if truly relevant (max 1–2)
- For each: what additional data would confirm or refute it

**Prioritized Strategic Actions**

P0 (Immediate, high confidence)
- Specific action + target segment/use case + expected KPI impact

P1 (Next phase)
- Specific action + rationale + appropriate timing

P2 (Long-term structural move)
- Structural shift in product / pricing / channel / GTM strategy
- Why it matters for long-term competitiveness

**Critical Data to Validate**
- 3–5 precise analyses or experiments
- Must directly validate or challenge the primary diagnosis

Style: concrete, actionable, professional. Avoid vague advice.
"""
    else:
        return f"""
你是一名资深商业分析师 + AI产品策略顾问。

请基于以下信息生成一份结构化商业分析报告：

【业务类型】{business_type}
【目标市场】{target_market}
【关键KPI变化】{kpi_changes}
【核心问题】{core_problem}
【行业环境变化】{industry_change}
【补充信息】{extra}

输出规则：
- 不要重复报告标题，直接从第一个部分开始。
- 使用高度结论导向的表达，避免铺垫和空泛描述。
- 小标题统一使用加粗格式（**标题**），提升可读性。
- 每个部分尽量控制在3-4条以内，保持管理层阅读效率。

严格输出结构（咨询公司/高管备忘录风格）：

**核心结论**
- 用1–2句话明确指出：最可能导致KPI变化的核心驱动因素
- 同时给出对当前业务策略的直接含义（Implication）

**关键证据信号**
- 列出3–4个最关键的事实或数据现象，用于支撑核心结论
- 优先包含：时间变化、客户细分变化、漏斗掉点位置、与竞品动作的时间对齐关系

**主因判断**
- 明确指出“最可能的单一根因”
- 用简短逻辑链说明：
  现象 → 关键证据 → 为什么该根因最能解释当前KPI变化（而非其他因素）

**次要可能因素（可选）**
- 仅在确有必要时，列出1–2个次要解释路径
- 对每个说明：需要看到什么额外数据，才能验证或否定该解释

**优先级战略动作**

P0（立即执行，高确定性）
- 具体动作 + 目标客户/使用场景 + 预期改善的核心KPI

P1（下一阶段推进）
- 具体动作 + 执行理由 + 适合启动的时间窗口

P2（中长期结构性调整）
- 产品 / 定价 / 渠道 / GT策略层面的结构性调整
- 说明其对长期竞争力的意义

**关键验证数据**
- 列出3–5项最关键的数据分析或实验
- 这些数据应能最快验证或推翻“主因判断”

要求：专业、具体、可执行，避免空泛建议。
"""

def build_clarify_prompt(
    lang: str,
    business_type: str,
    target_market: str,
    kpi_changes: str,
    core_problem: str,
    industry_change: str,
    extra_context: str
):
    extra = extra_context.strip() if extra_context and extra_context.strip() else ("None" if lang == "en" else "无")

    if lang == "en":
        return f"""
You are a senior business strategy analyst.

Goal: Ask clarification questions that will significantly improve the accuracy of the final business insight report.

Context:
Business Type: {business_type}
Target Market: {target_market}
Key KPI Changes: {kpi_changes}
Core Problem: {core_problem}
Industry Changes: {industry_change}
Extra Context: {extra}

Instructions:
Step 1: Generate 5 candidate clarification questions.
Step 2: Evaluate each question based on:
- Whether the answer would materially change strategic recommendations
- Whether the question is concrete and data-verifiable (not vague)
- Whether it targets root causes rather than surface symptoms
Step 3: Select the top 3 most impactful questions.

Output Rules:
- Do NOT repeat the report title.
- Only output the final selected 3 questions.
- Each question must be highly actionable and specific to the context.

Output Format (strictly follow):
**1. Key Question**
- Why ask

**2.Key Question**
- Why ask

**3.Key Question**
- Why ask

Rules:
- Question must be on its own line
- Explanation must be on the next line
- Use the prefix: "Why this improves accuracy:"
- Do NOT place question and explanation on the same line
- Keep explanations concise
"""
    else:
        return f"""
你是一名资深商业策略分析师。

目标：提出能够显著提升最终商业分析报告准确度的关键澄清问题。

业务背景：
【业务类型】{business_type}
【目标市场】{target_market}
【关键KPI变化】{kpi_changes}
【核心问题】{core_problem}
【行业环境变化】{industry_change}
【补充背景】{extra}

任务步骤：
1）基于以上信息，先生成5个候选澄清问题。
2）从以下维度评估每个问题：
- 该问题的答案是否会实质性改变策略建议
- 问题是否具体且可以通过数据验证（避免空泛）
- 问题是否指向根因，而非仅停留在表面现象
3）筛选出最关键的3个问题。

输出规则：
- 不要重复报告标题
- 只输出最终筛选后的3个问题
- 问题必须具体、可执行、与当前业务情境强相关

输出格式（严格遵守）：
**1.关键问题**
- 原因

**2.关键问题**
- 原因

**3.关键问题**
- 原因

要求：
- 问题单独占一行
- 下一行用短句说明原因
- 原因使用“提高准确度原因：”作为前缀
- 不要把问题和解释写在同一行
- 保持简洁，避免长段落
"""
