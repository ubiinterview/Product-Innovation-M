import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Technical Vision - Data & GenAI Product Innovation",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark theme CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Open+Sans:wght@300;400;600&display=swap');

:root {
    --primary: #6366f1;
    --secondary: #8b5cf6;
    --accent1: #06b6d4;
    --accent2: #10b981;
    --dark-bg: #0f172a;
    --dark-card: #1e293b;
    --dark-text: #e2e8f0;
    --dark-border: #334155;
    --gradient: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
}

* {
    font-family: 'Open Sans', sans-serif;
    color: var(--dark-text);
    line-height: 1.6;
}

.stApp {
    background-color: var(--dark-bg);
}

/* Layout container */
.content-container {
    max-width: 1180px;
    margin: 0 auto;
    padding: 0 1rem;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: var(--dark-text);
}

.main-header {
    font-size: clamp(2.4rem, 4.5vw, 4.25rem);
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 3px solid;
    border-image: var(--gradient) 1;
}

.section-header {
    font-size: 2.2rem;
    color: var(--primary);
    margin-top: 2.5rem;
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--primary);
    position: relative;
}

.section-header:after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 60px;
    height: 2px;
    background: var(--secondary);
}

.project-card {
    background: var(--dark-card);
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    border-left: 5px solid var(--primary);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px -10px rgba(99, 102, 241, 0.2);
    border-left: 5px solid var(--secondary);
}

.project-title {
    font-size: 1.8rem;
    color: var(--primary);
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
}

.project-title-icon {
    margin-right: 12px;
    font-size: 1.5rem;
}

.tech-stack {
    background-color: rgba(99, 102, 241, 0.15);
    padding: 0.8rem 1rem;
    border-radius: 8px;
    font-family: 'Montserrat', monospace;
    font-weight: 600;
    color: var(--primary);
    margin: 1rem 0;
    border-left: 3px solid var(--primary);
}

.competitor-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 1.5rem 0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.competitor-table th {
    background: var(--gradient);
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}

.competitor-table td {
    padding: 1rem;
    border-bottom: 1px solid var(--dark-border);
    background-color: var(--dark-card);
}

.competitor-table tr:last-child td {
    border-bottom: none;
}

.next-steps {
    background: var(--gradient);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    margin-top: 2.5rem;
    box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
}

.next-steps ol {
    margin-left: 1.5rem;
    line-height: 1.8;
}

.next-steps li {
    margin-bottom: 0.8rem;
    font-size: 1.1rem;
}

.sidebar .sidebar-content {
    background: var(--dark-card);
    color: white;
}

.stRadio div[role="radiogroup"] {
    background-color: var(--dark-card);
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid var(--dark-border);
}

.stRadio label {
    font-weight: 600;
    padding: 0.8rem;
    color: var(--dark-text);
}

.icon-bullet {
    display: flex;
    align-items: flex-start;
    margin-bottom: 1rem;
}

.icon-bullet .icon {
    margin-right: 12px;
    font-size: 1.2rem;
    color: var(--primary);
    min-width: 24px;
}

.timeline {
    position: relative;
    margin: 2rem 0;
    padding-left: 2rem;
}

.timeline:before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 4px;
    background: var(--gradient);
    border-radius: 4px;
}

.timeline-item {
    position: relative;
    margin-bottom: 2rem;
    padding-left: 1.5rem;
}

.timeline-item:before {
    content: '';
    position: absolute;
    left: -2.5rem;
    top: 0.5rem;
    height: 16px;
    width: 16px;
    border-radius: 50%;
    background: var(--primary);
    border: 3px solid var(--dark-bg);
    box-shadow: 0 0 0 2px var(--primary);
}

.timeline-date {
    font-weight: 600;
    color: var(--primary);
    margin-bottom: 0.5rem;
}

.timeline-content {
    background: var(--dark-card);
    padding: 1.2rem;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.tag {
    display: inline-block;
    background: rgba(99, 102, 241, 0.15);
    color: var(--primary);
    padding: 0.4rem 0.8rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    margin: 0.3rem;
}

.footer {
    text-align: center;
    margin-top: 3rem;
    padding: 1.5rem;
    color: #94a3b8;
    font-size: 0.9rem;
    border-top: 1px solid var(--dark-border);
}

/* Streamlit component overrides */
.stExpander {
    background-color: var(--dark-card);
    border: 1px solid var(--dark-border);
}

.stExpander label {
    color: var(--primary) !important;
    font-weight: 600;
}

div[data-testid="stExpander"] div[role="button"] p {
    color: var(--primary) !important;
    font-weight: 600;
    font-size: 1.1rem;
}

/* Markdown text color override */
div[data-testid="stMarkdown"] p {
    color: var(--dark-text);
}

/* Code block styling */
code {
    background-color: rgba(99, 102, 241, 0.1) !important;
    color: var(--accent1) !important;
    border-radius: 4px;
    padding: 2px 4px;
}

pre {
    background-color: rgba(99, 102, 241, 0.1) !important;
    border-left: 3px solid var(--primary) !important;
    color: var(--dark-text) !important;
}

/* Horizontal rule styling */
hr {
    border-top: 1px solid var(--dark-border);
    margin: 2rem 0;
}

/* Column background */
div[data-testid="column"] {
    background-color: transparent;
}
/* Top navigation */
.top-nav {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid var(--dark-border);
    padding: 0.5rem 1rem;
    box-shadow: 0 6px 18px -14px rgba(0,0,0,.8);
}
.top-nav .brand-title {
    font-size: 1.35rem;
}
.top-nav .tabs {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    justify-content: center;
}
.top-nav .tab-btn {
    padding: 0.6rem 1rem;
    border: 1px solid var(--dark-border);
    border-radius: 999px;
    background: #0b1224;
    color: var(--dark-text);
    text-decoration: none;
    display: inline-block;
    transition: all 0.2s ease;
    cursor: pointer;
}
.top-nav .tab-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 20px -10px rgba(99,102,241,.6);
    border-color: var(--primary);
}
.top-nav .tab-btn.active {
    background: linear-gradient(135deg, rgba(99,102,241,.15), rgba(139,92,246,.15));
    border-color: var(--primary);
}

/* Enhanced project cards */
.project-card {
    position: relative;
    background: radial-gradient(1200px circle at 10% -10%, rgba(99,102,241,.12), transparent 40%),
                radial-gradient(1200px circle at 110% 110%, rgba(139,92,246,.12), transparent 40%),
                var(--dark-card);
    padding: 2rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    box-shadow: 0 12px 30px -10px rgba(0,0,0,.5);
    border: 1px solid var(--dark-border);
    outline: 1px solid rgba(99,102,241,.15);
    transition: transform .25s ease, box-shadow .25s ease, outline-color .25s ease;
    overflow: hidden;
}
.project-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 24px 48px -16px rgba(99,102,241,.35);
    outline-color: rgba(139,92,246,.35);
}
.project-hover {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 76px;
    display: flex;
    align-items: center;
    padding: 0 1.25rem;
    background: linear-gradient(135deg, rgba(99,102,241,.18), rgba(139,92,246,.18));
    border-bottom: 1px solid rgba(99,102,241,.35);
    opacity: 0;
    transform: translateY(-8px);
    transition: opacity .25s ease, transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    pointer-events: none;
}
.project-card:hover .project-hover {
    opacity: 1;
    transform: translateY(0);
    border-bottom-color: var(--primary);
    box-shadow: 0 14px 30px -16px rgba(99,102,241,.45);
}
.project-hover-title {
    display: flex;
    align-items: center;
    gap: .6rem;
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--dark-text);
}
.project-hover-title .emoji { font-size: 1.3rem; }
.project-title {
    font-size: 1.9rem;
}
.tech-stack {
    background: linear-gradient(90deg, rgba(99,102,241,.18), rgba(139,92,246,.18));
    border-left: 0;
    border: 1px dashed rgba(99,102,241,.35);
}
/* Tabs styled as navbar */
div[role="tablist"] {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.5rem 0.25rem 0.75rem 0.25rem;
    background: transparent;
    border-bottom: 1px solid var(--dark-border);
    margin-bottom: 1rem;
}
button[role="tab"] {
    border: 1px solid var(--dark-border) !important;
    background: #0b1224 !important;
    color: var(--dark-text) !important;
    border-radius: 999px !important;
    padding: 0.4rem 0.9rem !important;
    transition: all .2s ease !important;
}
button[role="tab"]:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 20px -10px rgba(99,102,241,.35);
    border-color: var(--primary) !important;
}
button[role="tab"][aria-selected="true"] {
    background: linear-gradient(135deg, rgba(99,102,241,.15), rgba(139,92,246,.15)) !important;
    border-color: var(--primary) !important;
}

/* Stat cards */
.stat-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1rem;
}
.stat-card {
    position: relative;
    background: linear-gradient(180deg, rgba(255,255,255,.04), rgba(255,255,255,.02));
    border: 1px solid var(--dark-border);
    border-radius: 16px;
    padding: 1.25rem 1rem;
    overflow: hidden;
    box-shadow: 0 8px 20px -12px rgba(0,0,0,.6);
    transition: transform .25s ease, box-shadow .25s ease;
}
.stat-card:before {
    content: '';
    position: absolute;
    inset: -1px;
    border-radius: 16px;
    padding: 1px;
    background: linear-gradient(135deg, rgba(99,102,241,.6), rgba(139,92,246,.4));
    -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask-composite: exclude;
}
.stat-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 36px -18px rgba(99,102,241,.35);
}
.stat-card .icon {
    font-size: 1.2rem;
    color: var(--primary);
}
.stat-card .value {
    font-family: 'Montserrat', sans-serif;
    font-size: 2.1rem;
    font-weight: 700;
    line-height: 1.1;
}
.stat-card .label {
    color: #94a3b8;
    font-size: 0.95rem;
}

/* Projects overview grid */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1rem;
    margin-bottom: 1.25rem;
}
.grid-card {
    background: var(--dark-card);
    border: 1px solid var(--dark-border);
    border-radius: 14px;
    padding: 1rem;
    transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}
.grid-card:hover {
    transform: translateY(-4px);
    border-color: var(--primary);
    box-shadow: 0 14px 30px -16px rgba(99,102,241,.35);
}
.grid-card .title {
    display: flex;
    align-items: center;
    gap: .5rem;
    color: var(--primary);
    font-weight: 700;
}
.pill {
    display: inline-block;
    background: rgba(99,102,241,.15);
    color: var(--primary);
    border: 1px solid rgba(99,102,241,.35);
    padding: .15rem .5rem;
    border-radius: 999px;
    font-size: .8rem;
    margin: .15rem .25rem .15rem 0;
}
/* Accordion for projects */
.project-accordion {
    background: var(--dark-card);
    border: 1px solid var(--dark-border);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 12px 28px -14px rgba(0,0,0,.45);
    margin-bottom: 1rem;
}
.project-accordion summary {
    list-style: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: .75rem;
    padding: 0.9rem 1.1rem;
    cursor: pointer;
    background: linear-gradient(135deg, rgba(99,102,241,.14), rgba(139,92,246,.14));
    border-bottom: 1px solid rgba(99,102,241,.35);
}
.project-accordion summary::-webkit-details-marker { display: none; }
.summary-left { display:flex; align-items:center; gap:.65rem; }
.summary-icon { font-size: 1.1rem; }
.summary-title { font-weight: 700; color: var(--dark-text); }
.summary-tags { margin-left: auto; }
.chevron { color:#94a3b8; transition: transform .25s ease; }
.project-accordion[open] .chevron { transform: rotate(180deg); }

/* Rich content styles inside cards */
.feature-list { list-style: none; padding-left: 0; margin: .25rem 0 0 0; }
.feature-item { display:flex; align-items:flex-start; gap:.5rem; margin:.35rem 0; }
.feature-item .icon { color: var(--accent2); margin-top:.15rem; }

.metrics-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: .75rem;
    margin: .5rem 0 1rem 0;
}
.metric {
    background: linear-gradient(180deg, rgba(255,255,255,.04), rgba(255,255,255,.02));
    border: 1px solid var(--dark-border);
    border-radius: 12px;
    padding: .8rem;
}
.metric .label { color:#94a3b8; font-size:.8rem; }
.metric .value { font-weight:700; font-size:1.1rem; }

.button-row { margin-top: .75rem; }
.btn {
    display: inline-block;
    background: linear-gradient(135deg, rgba(99,102,241,.22), rgba(139,92,246,.22));
    border: 1px solid var(--primary);
    color: var(--dark-text);
    padding: .4rem .75rem;
    border-radius: 10px;
    text-decoration: none;
    margin-right: .5rem;
    transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}
.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 28px -18px rgba(99,102,241,.45);
    border-color: var(--secondary);
}
</style>
""", unsafe_allow_html=True)

def render_introduction():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-header">Technical Vision – Data & GenAI Product Innovation</h1>',
                unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <h3 style="color: #8b5cf6; margin-bottom: 0.5rem;">Umesh Rathod – Solutions Architect</h3>
                <p style="font-size: 1.2rem; color: #94a3b8;">Technical Roadmap & Architecture | August 2025</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
            <div style="padding-right: 2rem;">
                <p style="font-size: 1.1rem; line-height: 1.7;">
                    This presentation outlines our technical vision for building innovative data and GenAI products 
                    with a focus on modularity, cloud-agnostic architecture, and AI-powered automation. Our approach 
                    combines cutting-edge technologies with robust engineering practices to deliver exceptional value.
                </p>
                <div class="stat-cards" style="margin-top: 1.25rem;">
                    <div class="stat-card">
                        <div class="icon">📈</div>
                        <div class="value">6</div>
                        <div class="label">Strategic Projects</div>
                    </div>
                    <div class="stat-card">
                        <div class="icon">☁️</div>
                        <div class="value">4+</div>
                        <div class="label">Cloud Platforms</div>
                    </div>
                    <div class="stat-card">
                        <div class="icon">🤖</div>
                        <div class="value">AI</div>
                        <div class="label">Powered Solutions</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); padding: 2rem; border-radius: 16px; color: white;">
                <h3 style="color: white; margin-top: 0;">Key Advantages</h3>
                <div class="icon-bullet">
                    <span class="icon">🚀</span>
                    <span>Faster time-to-market with modular frameworks</span>
                </div>
                <div class="icon-bullet">
                    <span class="icon">🔧</span>
                    <span>Multi-cloud, multi-orchestrator support</span>
                </div>
                <div class="icon-bullet">
                    <span class="icon">🤖</span>
                    <span>GenAI integration across all solutions</span>
                </div>
                <div class="icon-bullet">
                    <span class="icon">🔒</span>
                    <span>Enterprise-grade security from day one</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_architecture_goals():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Architecture Goals</h1>', unsafe_allow_html=True)

    goals = [
        {"icon": "🧩", "text": "Build reusable, modular frameworks (plug and play)"},
        {"icon": "☁️", "text": "Cloud agnostic, Multi-orchestrator support (Databricks, Airflow, Glue, ADF, Synapse)"},
        {"icon": "🤖", "text": "Integrate GenAI for RCA, Documentation, Testing"},
        {"icon": "🔒", "text": "Ensure CI/CD, security, compliance, and observability from day one"}
    ]

    for goal in goals:
        st.markdown(f"""
            <div class="icon-bullet">
                <span class="icon">{goal['icon']}</span>
                <span style="font-size: 1.1rem;">{goal['text']}</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
        <div style="background: #1e293b; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); margin-top: 2rem;">
            <h3 style="color: #6366f1; margin-top: 0;">Our Architecture Philosophy</h3>
            <p style="line-height: 1.7;">
                Our architecture philosophy centers on creating flexible, future-proof systems that can 
                adapt to changing business needs and technological advancements. We prioritize clean interfaces, 
                well-defined contracts, and comprehensive documentation to ensure long-term maintainability 
                and extensibility of all solutions.
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_projects():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Projects Portfolio</h1>', unsafe_allow_html=True)

    # Overview grid
    st.markdown("""
        <div class="projects-grid">
            <div class="grid-card">
                <div class="title">🤖 AutoOps</div>
                <div style="margin-top:.25rem; color:#94a3b8;">Self-healing ETL + RCA</div>
                <div style="margin-top:.5rem;">
                    <span class="pill">Python</span>
                    <span class="pill">Spark</span>
                    <span class="pill">LLM</span>
                </div>
            </div>
            <div class="grid-card">
                <div class="title">📄 Document Intelligence</div>
                <div style="margin-top:.25rem; color:#94a3b8;">Docs from DAGs + Summaries</div>
                <div style="margin-top:.5rem;">
                    <span class="pill">LangChain</span>
                    <span class="pill">Graph</span>
                </div>
            </div>
            <div class="grid-card">
                <div class="title">🌐 Virtual DataLake</div>
                <div style="margin-top:.25rem; color:#94a3b8;">Prompt → SQL over federated data</div>
                <div style="margin-top:.5rem;">
                    <span class="pill">Trino</span>
                    <span class="pill">Presto</span>
                </div>
            </div>
            <div class="grid-card">
                <div class="title">🧪 Synthetic Data</div>
                <div style="margin-top:.25rem; color:#94a3b8;">Scale test data with constraints</div>
                <div style="margin-top:.5rem;">
                    <span class="pill">PySpark</span>
                    <span class="pill">LLM</span>
                </div>
            </div>
            <div class="grid-card">
                <div class="title">✅ DQM & ETL Testing</div>
                <div style="margin-top:.25rem; color:#94a3b8;">Validation, reconciliation, regression</div>
                <div style="margin-top:.5rem;">
                    <span class="pill">GX</span>
                    <span class="pill">LangChain</span>
                </div>
            </div>
            <div class="grid-card">
                <div class="title">🚀 Deployment Framework</div>
                <div style="margin-top:.25rem; color:#94a3b8;">Infra as code + CI/CD</div>
                <div style="margin-top:.5rem;">
                    <span class="pill">Terraform</span>
                    <span class="pill">Pulumi</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Polished accordions
    cards = [
        {
            "emoji": "🤖", "title": "AutoOps (Self-Healing + RCA)",
            "tags": ["Python", "Spark", "LLM"],
            "features": [
                ("Log collector for Glue/Airflow/ADF/Synapse", "✔️"),
                ("Data lineage graph builder", "✔️"),
                ("LLM-powered RCA engine", "✔️"),
                ("Self-heal executor (rollback/retry/fallback)", "✔️")
            ],
            "metrics": [("MTTR", "↓ 45%"), ("Coverage", "80%"), ("Incidents", "Auto 60%")],
            "stack": "Python + Spark + LLM APIs",
            "deploy": "Docker + K8s / ECS / AKS"
        },
        {
            "emoji": "📄", "title": "Document Intelligence",
            "tags": ["LangChain", "Graph"],
            "features": [
                ("Extract pipeline definitions (JSON/DAG/Config)", "✔️"),
                ("Generate documentation (Md/Confluence/Word)", "✔️"),
                ("Add LLM summarization", "✔️"),
                ("Graph visualization", "✔️")
            ],
            "metrics": [("Docs gen", "2m"), ("Accuracy", "~90%"), ("Formats", "3+")],
            "stack": "Python, Graph viz, LangChain",
            "deploy": "CLI + SaaS"
        },
        {
            "emoji": "🌐", "title": "Virtual DataLake",
            "tags": ["Trino", "Presto"],
            "features": [
                ("Prompt → SQL / Federated query", "✔️"),
                ("Connectors: Salesforce, Postgres, Snowflake, S3", "✔️"),
                ("Execution via Presto/Trino", "✔️"),
                ("Return DF/CSV/Dashboard", "✔️")
            ],
            "metrics": [("Latency", "<3s"), ("Sources", "4"), ("Cache", "Yes")],
            "stack": "LLM (prompt2SQL)",
            "deploy": "Cloud Function / Container"
        },
        {
            "emoji": "🧪", "title": "Synthetic Data Generator",
            "tags": ["PySpark", "LLM"],
            "features": [
                ("Seed data/metadata driven", "✔️"),
                ("Constraints, null ratios, business rules", "✔️"),
                ("Scale to large datasets", "✔️")
            ],
            "metrics": [("Scale", ">1B"), ("Templates", "Healthcare/Finance"), ("Speed", "Fast")],
            "stack": "PySpark + LLM",
            "deploy": "Databricks Job + API"
        },
        {
            "emoji": "✅", "title": "DQM & ETL Testing Framework",
            "tags": ["GX", "LangChain"],
            "features": [
                ("Schema validation", "✔️"),
                ("Null/constraint checks", "✔️"),
                ("Reconciliation across stages", "✔️"),
                ("Automated regression tests", "✔️")
            ],
            "metrics": [("Rules", "100+"), ("CI/CD", "Yes"), ("Coverage", "High")],
            "stack": "Great Expectations + PySpark + LangChain",
            "deploy": "Python Library + SaaS"
        },
        {
            "emoji": "🚀", "title": "Deployment Framework",
            "tags": ["Terraform", "Pulumi"],
            "features": [
                ("Infra as code (YAML/JSON)", "✔️"),
                ("Provision via Terraform/CDK/ARM", "✔️"),
                ("Jobs, IAM roles & policies", "✔️"),
                ("CI/CD (GitHub/ADO)", "✔️")
            ],
            "metrics": [("Time to deploy", "↓ 60%"), ("Templates", "10+"), ("Clouds", "Multi")],
            "stack": "Terraform / Pulumi / Bicep",
            "deploy": "CLI + Templates"
        },
    ]

    for card in cards:
        tags_html = "".join([f'<span class="pill">{t}</span>' for t in card["tags"]])
        feats_html = "".join([f'<li class="feature-item"><span class="icon">{icon}</span><span>{text}</span></li>' for text, icon in card["features"]])
        metrics_html = "".join([f'<div class="metric"><div class="label">{k}</div><div class="value">{v}</div></div>' for k, v in card["metrics"]])
        st.markdown(f"""
        <details class="project-accordion">
            <summary>
                <div class="summary-left">
                    <span class="summary-icon">{card['emoji']}</span>
                    <span class="summary-title">{card['title']}</span>
                </div>
                <div class="summary-tags">{tags_html}</div>
                <span class="chevron">▼</span>
            </summary>
            <div class="project-card">
                <div class="metrics-row">{metrics_html}</div>
                <ul class="feature-list">{feats_html}</ul>
                <div class="tech-stack">{card['stack']}</div>
                <div class="button-row">
                    <a class="btn" href="#">View Architecture</a>
                    <a class="btn" href="#">Explore Repo</a>
                </div>
                <div style="margin-top:.5rem; color:#94a3b8;">Deployment: {card['deploy']}</div>
            </div>
        </details>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_security():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Security & Compliance</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔒 Security Measures")
        security_items = [
            {"icon": "👥", "text": "IAM Roles, RBAC, Secrets Manager integration"},
            {"icon": "📝", "text": "Audit logging for all components"},
            {"icon": "🛡️", "text": "PII redaction for LLM-based tools"}
        ]

        for item in security_items:
            st.markdown(f"""
                <div class="icon-bullet">
                    <span class="icon">{item['icon']}</span>
                    <span>{item['text']}</span>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 📋 Compliance Standards")
        compliance_items = [
            {"icon": "🌐", "text": "GDPR"},
            {"icon": "🏥", "text": "HIPAA"},
            {"icon": "🏢", "text": "SOC2"}
        ]

        for item in compliance_items:
            st.markdown(f"""
                <div class="icon-bullet">
                    <span class="icon">{item['icon']}</span>
                    <span>{item['text']}</span>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
        <div style="background: #1e293b; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); margin-top: 2rem;">
            <h3 style="color: #6366f1; margin-top: 0;">Our Security Approach</h3>
            <p style="line-height: 1.7;">
                Security is integrated into every layer of our architecture, from infrastructure provisioning to 
                application logic. We follow the principle of least privilege, encrypt data in transit and at rest, 
                and maintain comprehensive audit trails for all operations. Our solutions are designed to meet 
                stringent compliance requirements across industries.
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_competitive():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Competitive Landscape</h1>', unsafe_allow_html=True)

    competitors = {
        "Project 1: AutoOps (Self-Healing ETL)": ["Monte Carlo", "Datafold", "Acceldata"],
        "Project 2: Document Intelligence": ["Sifflet", "Manta", "Octopai"],
        "Project 3: Virtual DataLake": ["Starburst (Trino)", "Dremio", "Denodo"],
        "Project 4: Synthetic Data Generator": ["Mostly AI", "Gretel.ai", "Tonic.ai"],
        "Project 5: DQM & ETL Testing": ["Great Expectations", "Soda", "Deequ"],
        "Project 6: Deployment Framework": ["Terraform", "Pulumi", "dbt Cloud", "Astronomer"]
    }

    for project, comps in competitors.items():
        st.markdown(f"**{project}**")
        comp_tags = "".join([f'<span class="tag">{comp}</span>' for comp in comps])
        st.markdown(f'<div>{comp_tags}</div>', unsafe_allow_html=True)
        st.markdown("")
    st.markdown('</div>', unsafe_allow_html=True)


def render_next_steps():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Next Steps for Technical Team</h1>', unsafe_allow_html=True)

    st.markdown('<div class="next-steps">', unsafe_allow_html=True)

    next_steps = [
        "Build AutoOps MVP → start with Databricks Workflow integration",
        "Parallel POC for Document Intelligence (quick win)",
        "Define connectors for Virtual DataLake (Salesforce + Postgres)",
        "Create shared DevOps pipeline (CI/CD + Testing)",
        "Biweekly demo checkpoints with Architect team"
    ]

    st.markdown("<ol>", unsafe_allow_html=True)
    for step in next_steps:
        st.markdown(f"<li>{step}</li>", unsafe_allow_html=True)
    st.markdown("</ol>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 📅 Proposed Timeline")

    st.markdown("""
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-date">Sept 1-15, 2025</div>
            <div class="timeline-content">Planning & Requirements Gathering</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">Sept 15 - Oct 15, 2025</div>
            <div class="timeline-content">AutoOps MVP Development</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">Sept 15 - Oct 1, 2025</div>
            <div class="timeline-content">Document Intelligence POC</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">Oct 1 - Nov 15, 2025</div>
            <div class="timeline-content">Connector Development</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">Oct 15 - Dec 1, 2025</div>
            <div class="timeline-content">CI/CD Pipeline Implementation</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# Top brand bar
st.markdown("""
    <div class="top-nav">
        <div class="content-container" style="display:flex; align-items:center; justify-content:center; gap:.75rem;">
            <span style="font-size:1.5rem;">🚀</span>
            <span class="brand-title" style="font-weight:700; letter-spacing:.3px; color:#cbd5e1;">Technical Vision Deck</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Top navigation via tabs (no URL change)
tab_labels = [
    "Introduction",
    "Architecture Goals",
    "Projects",
    "Security & Compliance",
    "Competitive Landscape",
    "Next Steps"
]

tabs = st.tabs(tab_labels)

with tabs[0]:
    render_introduction()
with tabs[1]:
    render_architecture_goals()
with tabs[2]:
    render_projects()
with tabs[3]:
    render_security()
with tabs[4]:
    render_competitive()
with tabs[5]:
    render_next_steps()

# Footer
st.markdown("---")
st.markdown("""
    <div class="footer">
        <p>© 2025 Technical Vision Presentation | For Stakeholder Review</p>
        <p>Confidential & Proprietary</p>
    </div>
""", unsafe_allow_html=True)