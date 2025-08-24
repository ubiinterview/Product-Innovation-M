import streamlit as st
import graphviz as graphviz
import re

#IMPROVED UI/UX EXPERIENCE

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
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border-radius: 20px;
    padding: 2.5rem;
    color: #1a202c;
    margin-bottom: 2rem;
    box-shadow: 0 20px 60px rgba(0,0,0,0.08);
    position: relative;
    overflow: hidden;
    border: 1px solid #e2e8f0;
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
}

/* Professional styling for project card content */
.project-card h4 {
    color: #2d3748 !important;
    font-size: 1.375rem !important;
    font-weight: 700 !important;
    margin-bottom: 1.5rem !important;
    font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
    letter-spacing: -0.025em !important;
}

.project-card div {
    color: #4a5568 !important;
    font-weight: 500 !important;
    font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
}

.project-title {
    color: #0f172a !important;
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.8rem;
    position: relative;
    z-index: 1;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background: rgba(255, 255, 255, 0.9);
    padding: 1rem;
    border-radius: 12px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.project-title span {
    color: #0f172a !important;
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
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background: rgba(15, 23, 42, 0.95);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--dark-border);
    padding: 0.75rem 1rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
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
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 20px 60px rgba(102, 126, 234, 0.15);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
}

.grid-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
    transform: translateX(-100%);
    transition: transform 0.8s ease;
}

.grid-card:hover::before {
    transform: translateX(100%);
}

.grid-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 30px 80px rgba(102, 126, 234, 0.25);
}

/* Enhanced readability for grid card text */
.grid-card .title {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: white !important;
    margin-bottom: 0.75rem !important;
    text-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
    font-family: 'Inter', sans-serif !important;
    letter-spacing: -0.025em !important;
}

.grid-card div {
    color: rgba(255,255,255,0.95) !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    text-shadow: 0 1px 4px rgba(0,0,0,0.2) !important;
    font-family: 'Inter', sans-serif !important;
    line-height: 1.6 !important;
}

.grid-card .description {
    color: rgba(255,255,255,0.9) !important;
    font-size: 0.9375rem !important;
    font-weight: 400 !important;
    margin-bottom: 1.5rem !important;
    line-height: 1.5 !important;
}

.grid-card .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1rem;
}

.grid-card .tag {
    background: rgba(255,255,255,0.2);
    color: white;
    padding: 0.375rem 0.75rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 0.025em;
}

.grid-card .tag:hover {
    background: rgba(255,255,255,0.3);
    transform: scale(1.05);
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

.pill:hover {
    background: rgba(255,255,255,0.3);
    transform: scale(1.05);
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

    # Executive Summary Banner
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1e40af 0%, #3730a3 100%); padding: 2.5rem; border-radius: 20px; margin-bottom: 2.5rem; box-shadow: 0 12px 40px rgba(30, 64, 175, 0.25); border: 1px solid rgba(255,255,255,0.15); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.08) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 4s infinite;"></div>
            <div style="position: relative; z-index: 1;">
                <div style="display: flex; align-items: center; gap: 1.2rem; margin-bottom: 1.5rem;">
                    <div style="background: rgba(255,255,255,0.25); padding: 0.75rem; border-radius: 12px; backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.3); box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                        <span style="font-size: 1.6rem;">📋</span>
                    </div>
                    <h2 style="color: white; margin: 0; font-size: 1.7rem; font-weight: 700; letter-spacing: -0.025em;">Executive Summary</h2>
                </div>
                <p style="color: rgba(255,255,255,0.95); font-size: 1.15rem; line-height: 1.7; margin: 0; font-weight: 500; text-shadow: 0 1px 2px rgba(0,0,0,0.1);">
                    This strategic technical roadmap presents a comprehensive vision for enterprise-grade data and GenAI product innovation. 
                    Our approach delivers <strong style="color: #fbbf24;">40% faster time-to-market</strong>, <strong style="color: #fbbf24;">60% reduction in operational costs</strong>, and 
                    <strong style="color: #fbbf24;">enterprise-grade security</strong> across all solutions. We propose 6 strategic initiatives that will position 
                    the organization as a leader in AI-powered data solutions.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Enhanced header with gradient background and better typography
    st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 4rem 2rem; border-radius: 24px; margin-bottom: 3rem; box-shadow: 0 20px 60px rgba(102, 126, 234, 0.15); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 3s infinite;"></div>
            <div style="position: relative; z-index: 1;">
                <h1 style="color: white; font-size: 3.5rem; font-weight: 700; text-align: center; margin-bottom: 1.5rem; text-shadow: 0 4px 12px rgba(0,0,0,0.3); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">
                    🚀 Enterprise Data & GenAI Innovation Platform
                </h1>
                <div style="text-align: center; margin-bottom: 2.5rem;">
                    <h3 style="color: rgba(255,255,255,0.95); margin-bottom: 0.5rem; font-size: 1.6rem; font-weight: 600;">Umesh Rathod – Senior Solutions Architect</h3>
                    <p style="font-size: 1.3rem; color: rgba(255,255,255,0.8); margin: 0; font-weight: 500;">Strategic Technical Roadmap & Enterprise Architecture | Q1 2025</p>
                </div>
                <div style="text-align: center;">
                    <div style="display: inline-flex; align-items: center; gap: 1.5rem; background: rgba(255,255,255,0.15); padding: 1rem 2rem; border-radius: 25px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <span style="font-size: 1.3rem;">🏢</span>
                        <span style="font-weight: 600; font-size: 1.1rem;">Enterprise-Grade Solutions</span>
                        <span style="font-size: 1.3rem;">🔒</span>
                        <span style="font-weight: 600; font-size: 1.1rem;">•</span>
                        <span style="font-size: 1.3rem;">⚡</span>
                        <span style="font-weight: 600; font-size: 1.1rem;">AI-Powered Automation</span>
                        <span style="font-size: 1.3rem;">🌐</span>
                    </div>
                </div>
            </div>
        </div>

        <style>
        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        </style>
    """, unsafe_allow_html=True)

    # Enhanced content section with better layout
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
            <div style="padding-right: 2rem;">
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3.5rem; border-radius: 24px; box-shadow: 0 20px 60px rgba(102, 126, 234, 0.25); border: 1px solid rgba(255,255,255,0.15); margin-bottom: 2.5rem; position: relative; overflow: hidden; transition: all 0.4s ease; cursor: pointer;" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 28px 80px rgba(102, 126, 234, 0.35)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 60px rgba(102, 126, 234, 0.25)'">
                    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.12) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 4s infinite;"></div>
                    <div style="position: relative; z-index: 1;">
                        <h3 style="color: white; margin-bottom: 2rem; font-size: 2rem; font-weight: 700; display: flex; align-items: center; gap: 1rem; letter-spacing: -0.025em;">
                            <span style="font-size: 2.2rem;">🎯</span>
                            <span>Strategic Vision</span>
                        </h3>
                        <p style="font-size: 1.25rem; line-height: 1.8; color: rgba(255,255,255,0.95); margin-bottom: 2rem; font-weight: 500; text-shadow: 0 1px 2px rgba(0,0,0,0.1);">
                            We envision a future where data and AI work seamlessly together to drive unprecedented business value. 
                            Our platform transforms complex data operations into intelligent, automated processes that scale with 
                            your business needs while maintaining enterprise-grade security and compliance.
                        </p>
                        <div style="background: rgba(255,255,255,0.15); padding: 2rem; border-radius: 20px; backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.25); box-shadow: 0 8px 24px rgba(0,0,0,0.1);">
                            <h4 style="color: white; margin-bottom: 1.5rem; font-size: 1.3rem; font-weight: 600; letter-spacing: -0.025em;">Key Value Propositions:</h4>
                            <ul style="color: rgba(255,255,255,0.95); margin: 0; padding-left: 1.8rem; line-height: 1.7; font-size: 1.1rem;">
                                <li style="margin-bottom: 0.8rem;"><strong style="color: #fbbf24;">40% faster time-to-market</strong> through modular, reusable frameworks</li>
                                <li style="margin-bottom: 0.8rem;"><strong style="color: #fbbf24;">60% reduction in operational costs</strong> via AI-powered automation</li>
                                <li style="margin-bottom: 0.8rem;"><strong style="color: #fbbf24;">Zero vendor lock-in</strong> with cloud-agnostic architecture</li>
                                <li style="margin-bottom: 0;"><strong style="color: #fbbf24;">Enterprise-grade security</strong> built into every component</li>
                            </ul>
                            </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Enhanced stat cards section
        st.markdown("""
            <div style="padding-right: 2rem;">
                <h3 style="color: #1a202c; margin-bottom: 1.5rem; font-size: 1.4rem; font-weight: 600; display: flex; align-items: center; gap: 0.5rem;">
                    <span>📊</span>
                    <span>Strategic Impact Metrics</span>
                </h3>
                <div class="stat-cards" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 1.5rem;">
                    <div class="stat-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2.5rem; border-radius: 24px; text-align: center; color: white; box-shadow: 0 16px 48px rgba(102, 126, 234, 0.2); transition: all 0.4s ease; border: 1px solid rgba(255,255,255,0.15); cursor: pointer; position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-10px) scale(1.03)'; this.style.boxShadow='0 24px 72px rgba(102, 126, 234, 0.35)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 16px 48px rgba(102, 126, 234, 0.2)'">
                        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.12) 50%, transparent 70%); transform: translateX(-100%); transition: transform 0.8s ease;"></div>
                        <div style="position: relative; z-index: 1;">
                            <div class="icon" style="font-size: 3rem; margin-bottom: 1.5rem; text-shadow: 0 2px 8px rgba(0,0,0,0.2);">📈</div>
                            <div class="value" style="font-size: 3rem; font-weight: 700; margin-bottom: 0.8rem; text-shadow: 0 2px 8px rgba(0,0,0,0.2);">6</div>
                            <div class="label" style="font-size: 1.1rem; opacity: 0.95; font-weight: 600; margin-bottom: 0.5rem;">Strategic Initiatives</div>
                            <div style="font-size: 0.9rem; opacity: 0.85; background: rgba(255,255,255,0.15); padding: 0.5rem 1rem; border-radius: 12px; backdrop-filter: blur(10px);">Revenue Impact: $2M+</div>
                        </div>
                    </div>
                    <div class="stat-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 2.5rem; border-radius: 24px; text-align: center; color: white; box-shadow: 0 16px 48px rgba(240, 147, 251, 0.2); transition: all 0.4s ease; border: 1px solid rgba(255,255,255,0.15); cursor: pointer; position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-10px) scale(1.03)'; this.style.boxShadow='0 24px 72px rgba(240, 147, 251, 0.35)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 16px 48px rgba(240, 147, 251, 0.2)'">
                        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.12) 50%, transparent 70%); transform: translateX(-100%); transition: transform 0.8s ease;"></div>
                        <div style="position: relative; z-index: 1;">
                            <div class="icon" style="font-size: 3rem; margin-bottom: 1.5rem; text-shadow: 0 2px 8px rgba(0,0,0,0.2);">⚡</div>
                            <div class="value" style="font-size: 3rem; font-weight: 700; margin-bottom: 0.8rem; text-shadow: 0 2px 8px rgba(0,0,0,0.2);">40%</div>
                            <div class="label" style="font-size: 1.1rem; opacity: 0.95; font-weight: 600; margin-bottom: 0.5rem;">Faster Delivery</div>
                            <div style="font-size: 0.9rem; opacity: 0.85; background: rgba(255,255,255,0.15); padding: 0.5rem 1rem; border-radius: 12px; backdrop-filter: blur(10px);">Time-to-Market</div>
                        </div>
                    </div>
                    <div class="stat-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 2.5rem; border-radius: 24px; text-align: center; color: white; box-shadow: 0 16px 48px rgba(79, 172, 254, 0.2); transition: all 0.4s ease; border: 1px solid rgba(255,255,255,0.15); cursor: pointer; position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-10px) scale(1.03)'; this.style.boxShadow='0 24px 72px rgba(79, 172, 254, 0.35)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 16px 48px rgba(79, 172, 254, 0.2)'">
                        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.12) 50%, transparent 70%); transform: translateX(-100%); transition: transform 0.8s ease;"></div>
                        <div style="position: relative; z-index: 1;">
                            <div class="icon" style="font-size: 3rem; margin-bottom: 1.5rem; text-shadow: 0 2px 8px rgba(0,0,0,0.2);">💰</div>
                            <div class="value" style="font-size: 3rem; font-weight: 700; margin-bottom: 0.8rem; text-shadow: 0 2px 8px rgba(0,0,0,0.2);">60%</div>
                            <div class="label" style="font-size: 1.1rem; opacity: 0.95; font-weight: 600; margin-bottom: 0.5rem;">Cost Reduction</div>
                            <div style="font-size: 0.9rem; opacity: 0.85; background: rgba(255,255,255,0.15); padding: 0.5rem 1rem; border-radius: 12px; backdrop-filter: blur(10px);">Operational Efficiency</div>
                        </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); padding: 3.5rem; border-radius: 24px; color: white; box-shadow: 0 20px 60px rgba(99, 102, 241, 0.3); border: 1px solid rgba(255,255,255,0.15); position: relative; overflow: hidden; transition: all 0.4s ease; cursor: pointer;" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 28px 80px rgba(99, 102, 241, 0.4)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 60px rgba(99, 102, 241, 0.3)'">
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.08) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 4s infinite;"></div>
                <div style="position: relative; z-index: 1;">
                    <h3 style="color: white; margin-top: 0; margin-bottom: 3rem; font-size: 2rem; font-weight: 700; display: flex; align-items: center; gap: 1rem; letter-spacing: -0.025em;">
                        <span style="font-size: 2.2rem;">🏆</span>
                        <span>Competitive Advantages</span>
                    </h3>
                    <div class="icon-bullet" style="display: flex; align-items: center; margin-bottom: 2rem; padding: 1.5rem; background: rgba(255,255,255,0.18); border-radius: 20px; backdrop-filter: blur(15px); transition: all 0.4s ease; cursor: pointer; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 4px 16px rgba(0,0,0,0.1);" onmouseover="this.style.background='rgba(255,255,255,0.28)'; this.style.transform='translateX(16px) translateY(-4px)'; this.style.boxShadow='0 12px 32px rgba(0,0,0,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.18)'; this.style.transform='translateX(0) translateY(0)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.1)'">
                        <span class="icon" style="margin-right: 1.5rem; font-size: 1.8rem; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">🤖</span>
                        <span style="font-weight: 600; font-size: 1.2rem; letter-spacing: -0.025em;">GenAI Integration Across All Solutions</span>
                    </div>
                    <div class="icon-bullet" style="display: flex; align-items: center; margin-bottom: 2rem; padding: 1.5rem; background: rgba(255,255,255,0.18); border-radius: 20px; backdrop-filter: blur(15px); transition: all 0.4s ease; cursor: pointer; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 4px 16px rgba(0,0,0,0.1);" onmouseover="this.style.background='rgba(255,255,255,0.28)'; this.style.transform='translateX(16px) translateY(-4px)'; this.style.boxShadow='0 12px 32px rgba(0,0,0,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.18)'; this.style.transform='translateX(0) translateY(0)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.1)'">
                        <span class="icon" style="margin-right: 1.5rem; font-size: 1.8rem; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">🔧</span>
                        <span style="font-weight: 600; font-size: 1.2rem; letter-spacing: -0.025em;">Multi-Cloud, Multi-Orchestrator Support</span>
                    </div>
                    <div class="icon-bullet" style="display: flex; align-items: center; margin-bottom: 2rem; padding: 1.5rem; background: rgba(255,255,255,0.18); border-radius: 20px; backdrop-filter: blur(15px); transition: all 0.4s ease; cursor: pointer; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 4px 16px rgba(0,0,0,0.1);" onmouseover="this.style.background='rgba(255,255,255,0.28)'; this.style.transform='translateX(16px) translateY(-4px)'; this.style.boxShadow='0 12px 32px rgba(0,0,0,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.18)'; this.style.transform='translateX(0) translateY(0)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.1)'">
                        <span class="icon" style="margin-right: 1.5rem; font-size: 1.8rem; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">🔒</span>
                        <span style="font-weight: 600; font-size: 1.2rem; letter-spacing: -0.025em;">Enterprise Security & Compliance Built-In</span>
                    </div>
                    <div class="icon-bullet" style="display: flex; align-items: center; margin-bottom: 0; padding: 1.5rem; background: rgba(255,255,255,0.18); border-radius: 20px; backdrop-filter: blur(15px); transition: all 0.4s ease; cursor: pointer; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 4px 16px rgba(0,0,0,0.1);" onmouseover="this.style.background='rgba(255,255,255,0.28)'; this.style.transform='translateX(16px) translateY(-4px)'; this.style.boxShadow='0 12px 32px rgba(0,0,0,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.18)'; this.style.transform='translateX(0) translateY(0)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.1)'">
                        <span class="icon" style="margin-right: 1.5rem; font-size: 1.8rem; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">🚀</span>
                        <span style="font-weight: 600; font-size: 1.2rem; letter-spacing: -0.025em;">Modular Architecture for Rapid Deployment</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Additional section below
    st.markdown("""
        <div style="margin-top: 3rem; background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 3rem; border-radius: 24px; box-shadow: 0 16px 48px rgba(0,0,0,0.25); border: 1px solid #475569; position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.08) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 4s infinite;"></div>
            <div style="position: relative; z-index: 1;">
                <h3 style="color: #6366f1; margin-bottom: 2.5rem; font-size: 2rem; font-weight: 700; display: flex; align-items: center; gap: 0.8rem; letter-spacing: -0.025em;">
                    <span style="font-size: 2.2rem;">🎯</span>
                    <span>Strategic Approach & Business Impact</span>
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
                    <div style="background: rgba(255, 255, 255, 0.12); padding: 2.5rem; border-radius: 20px; box-shadow: 0 12px 32px rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.15); transition: all 0.4s ease; cursor: pointer; backdrop-filter: blur(15px);" onmouseover="this.style.transform='translateY(-8px)'; this.style.background='rgba(255,255,255,0.18)'; this.style.boxShadow='0 16px 40px rgba(0,0,0,0.35)'" onmouseout="this.style.transform='translateY(0)'; this.style.background='rgba(255,255,255,0.12)'; this.style.boxShadow='0 12px 32px rgba(0,0,0,0.25)'">
                        <h4 style="color: #fbbf24; margin-bottom: 1rem; font-size: 1.4rem; font-weight: 600; display: flex; align-items: center; gap: 0.8rem; letter-spacing: -0.025em;">
                            <span style="font-size: 1.6rem;">🤖</span>
                            <span>AI-First Design</span>
                        </h4>
                        <p style="color: #e2e8f0; line-height: 1.8; margin: 0; font-size: 1.1rem; margin-bottom: 1.5rem;">Integrating artificial intelligence and machine learning capabilities into every aspect of our solutions, automating complex processes and enhancing decision-making.</p>
                        <div style="padding: 1rem; background: rgba(99, 102, 241, 0.25); border-radius: 12px; border-left: 4px solid #6366f1; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                            <div style="font-size: 1rem; color: #fbbf24; font-weight: 600; margin-bottom: 0.5rem;">Business Impact:</div>
                            <div style="font-size: 0.9rem; color: #cbd5e1; line-height: 1.5;">Automated operations, improved accuracy, competitive advantage</div>
                    </div>
                    </div>
                    <div style="background: rgba(255, 255, 255, 0.12); padding: 2.5rem; border-radius: 20px; box-shadow: 0 12px 32px rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.15); transition: all 0.4s ease; cursor: pointer; backdrop-filter: blur(15px);" onmouseover="this.style.transform='translateY(-8px)'; this.style.background='rgba(255,255,255,0.18)'; this.style.boxShadow='0 16px 40px rgba(0,0,0,0.35)'" onmouseout="this.style.transform='translateY(0)'; this.style.background='rgba(255,255,255,0.12)'; this.style.boxShadow='0 12px 32px rgba(0,0,0,0.25)'">
                        <h4 style="color: #fbbf24; margin-bottom: 1rem; font-size: 1.4rem; font-weight: 600; display: flex; align-items: center; gap: 0.8rem; letter-spacing: -0.025em;">
                            <span style="font-size: 1.6rem;">☁️</span>
                            <span>Cloud Agnostic</span>
                        </h4>
                        <p style="color: #e2e8f0; line-height: 1.8; margin: 0; font-size: 1.1rem; margin-bottom: 1.5rem;">Designing solutions that work seamlessly across multiple cloud platforms without vendor lock-in, providing flexibility and cost optimization opportunities.</p>
                        <div style="padding: 1rem; background: rgba(99, 102, 241, 0.25); border-radius: 12px; border-left: 4px solid #6366f1; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                            <div style="font-size: 1rem; color: #fbbf24; font-weight: 600; margin-bottom: 0.5rem;">Business Impact:</div>
                            <div style="font-size: 0.9rem; color: #cbd5e1; line-height: 1.5;">Reduced cloud costs, increased bargaining power, risk mitigation</div>
                    </div>
                    </div>
                    <div style="background: rgba(255, 255, 255, 0.12); padding: 2.5rem; border-radius: 20px; box-shadow: 0 12px 32px rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.15); transition: all 0.4s ease; cursor: pointer; backdrop-filter: blur(15px);" onmouseover="this.style.transform='translateY(-8px)'; this.style.background='rgba(255,255,255,0.18)'; this.style.boxShadow='0 16px 40px rgba(0,0,0,0.35)'" onmouseout="this.style.transform='translateY(0)'; this.style.background='rgba(255,255,255,0.12)'; this.style.boxShadow='0 12px 32px rgba(0,0,0,0.25)'">
                        <h4 style="color: #fbbf24; margin-bottom: 1rem; font-size: 1.4rem; font-weight: 600; display: flex; align-items: center; gap: 0.8rem; letter-spacing: -0.025em;">
                            <span style="font-size: 1.6rem;">🏗️</span>
                            <span>Modular Architecture</span>
                        </h4>
                        <p style="color: #e2e8f0; line-height: 1.8; margin: 0; font-size: 1.1rem; margin-bottom: 1.5rem;">Building reusable components that can be easily integrated and scaled across different projects and environments, reducing development time by 40% and maintenance costs by 60%.</p>
                        <div style="padding: 1rem; background: rgba(99, 102, 241, 0.25); border-radius: 12px; border-left: 4px solid #6366f1; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                            <div style="font-size: 1rem; color: #fbbf24; font-weight: 600; margin-bottom: 0.5rem;">Business Impact:</div>
                            <div style="font-size: 0.9rem; color: #cbd5e1; line-height: 1.5;">Faster product launches, reduced technical debt, improved team productivity</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_architecture_goals():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    # Enhanced header with gradient background
    st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3rem 2rem; border-radius: 20px; margin-bottom: 3rem; box-shadow: 0 20px 60px rgba(102, 126, 234, 0.15); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 3s infinite;"></div>
            <div style="position: relative; z-index: 1; text-align: center;">
                <h1 style="color: white; font-size: 2.5rem; font-weight: 700; margin-bottom: 1rem; text-shadow: 0 4px 12px rgba(0,0,0,0.3); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">
                    🎯 Architecture Goals
                </h1>
                <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin: 0; font-weight: 500;">
                    Building the foundation for scalable, future-proof solutions
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Enhanced goals with better styling and layout
    goals = [
        {
            "icon": "🤖",
            "title": "GenAI Integration",
            "text": "Integrate GenAI for RCA, Documentation, Testing",
            "gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"
        },
        {
            "icon": "☁️",
            "title": "Cloud Agnostic",
            "text": "Multi-orchestrator support (Databricks, Airflow, Glue, ADF, Synapse)",
            "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
        },
        {
            "icon": "🔒",
            "title": "Enterprise Security",
            "text": "Ensure CI/CD, security, compliance, and observability from day one",
            "gradient": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)"
        },
        {
            "icon": "🧩",
            "title": "Modular Frameworks",
            "text": "Build reusable, modular frameworks (plug and play)",
            "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        }
    ]

    # Create a modern UI grid layout for goals
    st.markdown("""
        <style>
        .goals-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .goal-card {
            background: white;
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #e2e8f0;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .goal-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--card-gradient);
        }

        .goal-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
            border-color: #cbd5e1;
        }

        .goal-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .goal-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            background: var(--card-gradient);
            color: white;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }

                .goal-title {
            font-size: 1.1rem;
            font-weight: 700;
            color: #0f172a;
            margin: 0;
        }

        .goal-description {
            color: #374151;
            font-size: 0.95rem;
            line-height: 1.6;
            margin: 0;
            font-weight: 500;
        }
        </style>

        <div class="goals-container">
    """, unsafe_allow_html=True)

    for goal in goals:
        st.markdown(f"""
            <div class="goal-card" style="--card-gradient: {goal['gradient']};">
                <div class="goal-header">
                    <div class="goal-icon">{goal['icon']}</div>
                    <h3 style="font-size: 1.1rem; font-weight: 700; color: #0f172a; margin: 0;">{goal['title']}</h3>
                </div>
                <p style="color: #374151; font-size: 0.95rem; line-height: 1.6; margin: 0; font-weight: 500;">{goal['text']}</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Enhanced Architecture Philosophy section
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 3rem; border-radius: 20px; box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2); margin-top: 3rem; border: 1px solid #475569; position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.05) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 4s infinite;"></div>
            <div style="position: relative; z-index: 1;">
                <h3 style="color: #6366f1; margin-top: 0; margin-bottom: 1.5rem; font-size: 1.8rem; font-weight: 600; display: flex; align-items: center; gap: 0.5rem;">
                    <span>🏗️</span>
                    <span>Our Architecture Philosophy</span>
                </h3>
                <p style="line-height: 1.8; font-size: 1.1rem; color: #e2e8f0; margin-bottom: 0; font-weight: 400;">
                    Our architecture philosophy centers on creating flexible, future-proof systems that can 
                    adapt to changing business needs and technological advancements. We prioritize clean interfaces, 
                    well-defined contracts, and comprehensive documentation to ensure long-term maintainability 
                    and extensibility of all solutions.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_projects():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    # Enhanced Professional Header with Executive Summary
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 4rem 3rem; border-radius: 24px; margin-bottom: 3rem; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15); position: relative; overflow: hidden; border: 1px solid #475569;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.05) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 4s infinite;"></div>
            <div style="position: relative; z-index: 1; text-align: center;">
                <h1 style="color: white; font-size: 3rem; font-weight: 800; margin-bottom: 1.5rem; text-shadow: 0 4px 12px rgba(0,0,0,0.4); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">
                    🚀 Enterprise Solutions Portfolio
                </h1>
                <p style="color: rgba(255,255,255,0.9); font-size: 1.25rem; margin-bottom: 2rem; font-weight: 500; line-height: 1.6; max-width: 800px; margin-left: auto; margin-right: auto;">
                    Comprehensive suite of AI-powered, cloud-native solutions designed for enterprise-scale data operations, 
                    automation, and intelligence. Each solution is built with security, scalability, and operational excellence at its core.
                </p>
                <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 2rem;">
                    <div style="background: rgba(255,255,255,0.1); padding: 1rem 1.5rem; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #10b981; margin-bottom: 0.25rem;">6</div>
                        <div style="font-size: 0.875rem; color: rgba(255,255,255,0.8); font-weight: 500;">Enterprise Solutions</div>
                </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 1rem 1.5rem; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #3b82f6; margin-bottom: 0.25rem;">100%</div>
                        <div style="font-size: 0.875rem; color: rgba(255,255,255,0.8); font-weight: 500;">Cloud Native</div>
            </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 1rem 1.5rem; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #f59e0b; margin-bottom: 0.25rem;">AI-First</div>
                        <div style="font-size: 0.875rem; color: rgba(255,255,255,0.8); font-weight: 500;">Design Philosophy</div>
                </div>
            </div>
                </div>
            </div>
    """, unsafe_allow_html=True)

    # Professional Solutions Overview Grid with Enhanced Design
    st.markdown("""
        <div style="margin-bottom: 3rem;">
            <h2 style="color: #1e293b; font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 2rem; font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">
                🎯 Core Enterprise Solutions
            </h2>
            <p style="color: #64748b; font-size: 1.125rem; text-align: center; margin-bottom: 3rem; font-weight: 400; line-height: 1.6; max-width: 800px; margin-left: auto; margin-right: auto;">
                Our comprehensive portfolio addresses the most critical challenges in modern data operations, 
                providing intelligent automation, enhanced security, and operational excellence.
            </p>
                </div>
    """, unsafe_allow_html=True)

    # Enhanced Professional Overview Grid
    st.markdown("""
        <div class="projects-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(380px, 1fr)); gap: 2.5rem; margin-bottom: 4rem;">
            <div class="grid-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 60px rgba(102, 126, 234, 0.15); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);" onmouseover="this.style.transform='translateY(-12px) scale(1.03)'; this.style.boxShadow='0 30px 80px rgba(102, 126, 234, 0.25)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 20px 60px rgba(102, 126, 234, 0.15)'">
                <div class="title" style="font-size: 1.75rem; font-weight: 800; color: white; margin-bottom: 1rem; text-shadow: 0 2px 8px rgba(0,0,0,0.3); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">🤖 AutoOps</div>
                <div class="description" style="color: rgba(255,255,255,0.95); font-size: 1rem; font-weight: 500; margin-bottom: 2rem; line-height: 1.6;">Self-healing ETL pipelines with intelligent root cause analysis and automated remediation</div>
                <div class="tags" style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem;">
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">Python</span>
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">Spark</span>
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">LLM</span>
            </div>
                </div>
            <div class="grid-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 60px rgba(240, 147, 251, 0.15); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);" onmouseover="this.style.transform='translateY(-12px) scale(1.03)'; this.style.boxShadow='0 30px 80px rgba(240, 147, 251, 0.25)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 20px 60px rgba(240, 147, 251, 0.15)'">
                <div class="title" style="font-size: 1.75rem; font-weight: 800; color: white; margin-bottom: 1rem; text-shadow: 0 2px 8px rgba(0,0,0,0.3); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">📄 Document Intelligence</div>
                <div class="description" style="color: rgba(255,255,255,0.95); font-size: 1rem; font-weight: 500; margin-bottom: 2rem; line-height: 1.6;">Automated documentation generation with LLM enhancement and intelligent summarization</div>
                <div class="tags" style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem;">
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">LangChain</span>
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">Graph</span>
            </div>
            </div>
            <div class="grid-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 60px rgba(79, 172, 254, 0.15); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);" onmouseover="this.style.transform='translateY(-12px) scale(1.03)'; this.style.boxShadow='0 30px 80px rgba(79, 172, 254, 0.25)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 20px 60px rgba(79, 172, 254, 0.15)'">
                <div class="title" style="font-size: 1.75rem; font-weight: 800; color: white; margin-bottom: 1rem; text-shadow: 0 2px 8px rgba(0,0,0,0.3); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">🌐 Virtual DataLake</div>
                <div class="description" style="color: rgba(255,255,255,0.95); font-size: 1rem; font-weight: 500; margin-bottom: 2rem; line-height: 1.6;">Federated data access with natural language queries and unified data governance</div>
                <div class="tags" style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem;">
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">Trino</span>
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">Presto</span>
                </div>
            </div>
            <div class="grid-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 60px rgba(67, 233, 123, 0.15); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);" onmouseover="this.style.transform='translateY(-12px) scale(1.03)'; this.style.boxShadow='0 30px 80px rgba(67, 233, 123, 0.25)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 20px 60px rgba(67, 233, 123, 0.15)'">
                <div class="title" style="font-size: 1.75rem; font-weight: 800; color: white; margin-bottom: 1rem; text-shadow: 0 2px 8px rgba(0,0,0,0.3); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">🧪 Synthetic Data Generator</div>
                <div class="description" style="color: rgba(255,255,255,0.95); font-size: 1rem; font-weight: 500; margin-bottom: 2rem; line-height: 1.6;">AI-powered synthetic data generation at scale with industry-specific templates</div>
                <div class="tags" style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem;">
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">PySpark</span>
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">LLM</span>
                </div>
            </div>
            <div class="grid-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 60px rgba(250, 112, 154, 0.15); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);" onmouseover="this.style.transform='translateY(-12px) scale(1.03)'; this.style.boxShadow='0 30px 80px rgba(250, 112, 154, 0.25)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 20px 60px rgba(250, 112, 154, 0.15)'">
                <div class="title" style="font-size: 1.75rem; font-weight: 800; color: white; margin-bottom: 1rem; text-shadow: 0 2px 8px rgba(0,0,0,0.3); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">✅ DQM & ETL Testing</div>
                <div class="description" style="color: rgba(255,255,255,0.95); font-size: 1rem; font-weight: 500; margin-bottom: 2rem; line-height: 1.6;">Comprehensive data quality management framework with automated testing</div>
                <div class="tags" style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem;">
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">GX</span>
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">LangChain</span>
                </div>
            </div>
            <div class="grid-card" style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 60px rgba(168, 237, 234, 0.15); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);" onmouseover="this.style.transform='translateY(-12px) scale(1.03)'; this.style.boxShadow='0 30px 80px rgba(168, 237, 234, 0.25)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 20px 60px rgba(168, 237, 234, 0.15)'">
                <div class="title" style="font-size: 1.75rem; font-weight: 800; color: white; margin-bottom: 1rem; text-shadow: 0 2px 8px rgba(0,0,0,0.3); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">🚀 Deployment Framework</div>
                <div class="description" style="color: rgba(255,255,255,0.95); font-size: 1rem; font-weight: 500; margin-bottom: 2rem; line-height: 1.6;">Multi-cloud infrastructure automation platform with enterprise security</div>
                <div class="tags" style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem;">
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">Terraform</span>
                    <span class="tag" style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.025em;">Pulumi</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Enhanced Professional Section Header
    st.markdown("""
        <div style="text-align: center; margin: 4rem 0 3rem 0; padding: 2rem; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 20px; border: 1px solid #e2e8f0; box-shadow: 0 8px 32px rgba(0,0,0,0.05);">
            <h3 style="color: #1e293b; font-size: 2.25rem; font-weight: 700; margin-bottom: 1rem; font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">📋 Detailed Solution Specifications</h3>
            <p style="color: #64748b; font-size: 1.125rem; margin: 0; font-weight: 500; line-height: 1.6; max-width: 700px; margin-left: auto; margin-right: auto;">
                Explore comprehensive technical details, architecture diagrams, and implementation specifications for each enterprise solution
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Check if user wants to view AutoOps architecture
    if 'show_autoops_arch' not in st.session_state:
        st.session_state.show_autoops_arch = False

    # Check if user wants to view Document Intelligence architecture
    if 'show_doc_intel_arch' not in st.session_state:
        st.session_state.show_doc_intel_arch = False

    # Check if user wants to view Virtual DataLake architecture
    if 'show_virtual_dl_arch' not in st.session_state:
        st.session_state.show_virtual_dl_arch = False

    # Check if user wants to view Synthetic Data Generator architecture
    if 'show_synthetic_data_arch' not in st.session_state:
        st.session_state.show_synthetic_data_arch = False

    # Check if user wants to view DQM & ETL Testing Framework architecture
    if 'show_dqm_etl_arch' not in st.session_state:
        st.session_state.show_dqm_etl_arch = False

    # Check if user wants to view Deployment Framework architecture
    if 'show_deployment_framework_arch' not in st.session_state:
        st.session_state.show_deployment_framework_arch = False

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
            "deploy": "Docker + K8s / ECS / AKS",
            "is_autoops": True
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
            "deploy": "CLI + SaaS",
            "is_doc_intel": True
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
            "deploy": "Cloud Function / Container",
            "is_virtual_dl": True
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
            "deploy": "Databricks Job + API",
            "is_synthetic_data": True
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
            "deploy": "Python Library + SaaS",
            "is_dqm_etl": True
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
            "deploy": "CLI + Templates",
            "is_deployment_framework": True
        },
    ]

    for card in cards:
        tags_html = "".join([
            f'<span class="pill" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.8rem; margin-right: 0.5rem; display: inline-block; margin-bottom: 0.5rem;">{t}</span>'
            for t in card["tags"]])
        feats_html = "".join(
            [
                f'<li class="feature-item" style="display: flex; align-items: center; margin-bottom: 0.8rem; padding: 0.75rem; background: #475569; border-radius: 8px; border-left: 4px solid #6366f1; border: 1px solid #64748b; box-shadow: 0 2px 8px rgba(0,0,0,0.2);"><span class="icon" style="margin-right: 0.8rem; font-size: 1.2rem; color: #10b981;">{icon}</span><span style="color: #f1f5f9; font-weight: 600; font-size: 1rem; line-height: 1.4;">{text}</span></li>'
                for text, icon in
                card["features"]])
        metrics_html = "".join(
            [
                f'<div class="metric" style="background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); color: white; padding: 1rem; border-radius: 12px; text-align: center; margin: 0.5rem; box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);"><div class="label" style="font-size: 0.8rem; opacity: 0.9; margin-bottom: 0.3rem;">{k}</div><div class="value" style="font-size: 1.2rem; font-weight: 700;">{v}</div></div>'
                for k, v in
                card["metrics"]])

        # Special handling for AutoOps card
        if card.get("is_autoops", False):
            # Create a custom expandable section for AutoOps
            with st.expander(f"{card['emoji']} {card['title']}", expanded=False):
                # Enhanced project card content
                st.markdown(f"""
                <div class="project-card" style="background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); border-radius: 16px; padding: 2rem; color: #1a202c; margin-bottom: 1.5rem; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid #e2e8f0;">
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-bottom: 2rem;">{metrics_html}</div>
                    <div style="background: #000000; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid #333333; box-shadow: 0 2px 12px rgba(0,0,0,0.3);">
                        <h4 style="color: #ffffff; margin-bottom: 1.25rem; font-size: 1.2rem; font-weight: 700; display: flex; align-items: center; gap: 0.5rem;">
                            <span style="font-size: 1.3rem;">✨</span>
                            <span>Key Features</span>
                        </h4>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #ffffff;">{feats_html}</ul>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                        <div style="background: #475569; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #64748b; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                            <div style="font-size: 0.9rem; color: #e2e8f0; margin-bottom: 0.3rem; font-weight: 600;">Tech Stack</div>
                            <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">{card['stack']}</div>
                        </div>
                        <div style="background: #475569; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #64748b; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                            <div style="font-size: 0.9rem; color: #e2e8f0; margin-bottom: 0.3rem; font-weight: 600;">Deployment</div>
                            <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">{card['deploy']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Add Streamlit buttons for AutoOps architecture and repo inside the card
                st.markdown('<div style="margin: 1.5rem 0;">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏗️ View Architecture", key="autoops_arch_btn",
                                 help="Click to view the detailed architecture diagram"):
                        st.session_state.show_autoops_arch = not st.session_state.show_autoops_arch
                        st.rerun()
                with col2:
                    if st.button("📂 Explore Repository", key="autoops_repo_btn",
                                 help="Click to explore the project repository"):
                        st.info("Repository link would open here")
                st.markdown('</div>', unsafe_allow_html=True)

                # Show architecture if button is clicked
                if st.session_state.show_autoops_arch:
                    st.markdown("---")
                    st.markdown('<h3 style="color: #6366f1; margin-top: 1rem;">AutoOps Architecture Diagram</h3>',
                                unsafe_allow_html=True)
                    st.markdown("""
                    This diagram illustrates the architecture of the AutoOps (Self-Healing + RCA) system, showing how logs are collected from various sources, 
                    processed through a data lineage graph, analyzed by an LLM-powered RCA engine, and how self-healing actions are executed.
                    """)

                    # Create the architecture diagram
                    with st.expander("Architecture Diagram", expanded=True):
                        # Create a graphlib graph
                        dot = graphviz.Digraph(comment='AutoOps Architecture')
                        dot.attr(rankdir='LR', size='12,8')

                        # Define nodes with styles
                        dot.attr('node', shape='box', style='filled', fillcolor='lightblue', fontname='Arial')

                        # Log Sources
                        with dot.subgraph(name='cluster_log_sources') as c:
                            c.attr(label='Log Sources', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('databricks', 'Databricks Workflow')
                            c.node('airflow', 'Airflow')
                            c.node('glue', 'AWS Glue')
                            c.node('adf', 'Azure Data Factory')
                            c.node('synapse', 'Azure Synapse')
                            c.node('fabric', 'Fabric')

                        # Log Collector
                        dot.node('log_collector', 'Log Collector\n(Universal Interface)', shape='component',
                                 fillcolor='lightyellow')

                        # Data Lineage
                        dot.node('lineage', 'Data Lineage\nGraph Builder', shape='cylinder', fillcolor='lightgreen')

                        # RCA Engine
                        dot.node('rca', 'LLM-Powered\nRCA Engine', shape='ellipse', fillcolor='lightcoral')

                        # Self-Heal Executor
                        dot.node('self_heal', 'Self-Heal Executor', shape='component', fillcolor='lightpink')

                        # Actions
                        with dot.subgraph(name='cluster_actions') as c:
                            c.attr(label='Remediation Actions', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('rollback', 'Rollback')
                            c.node('retry', 'Retry')
                            c.node('fallback', 'Fallback')

                        # Define edges
                        dot.edges([
                            ('databricks', 'log_collector'),
                            ('airflow', 'log_collector'),
                            ('glue', 'log_collector'),
                            ('adf', 'log_collector'),
                            ('synapse', 'log_collector'),
                            ('fabric', 'log_collector')
                        ])

                        dot.edge('log_collector', 'lineage', label='Parsed Logs')
                        dot.edge('lineage', 'rca', label='Lineage Graph')
                        dot.edge('rca', 'self_heal', label='Root Cause Analysis')
                        dot.edge('self_heal', 'rollback', label='Execute')
                        dot.edge('self_heal', 'retry', label='Execute')
                        dot.edge('self_heal', 'fallback', label='Execute')

                        # Feedback loop
                        dot.edge('self_heal', 'rca', label='Action Results', style='dashed')

                        # Render the graph
                        st.graphviz_chart(dot)

                    # Detailed component descriptions
                    st.markdown("---")
                    st.markdown('<h4 style="color: #6366f1;">Component Details</h4>', unsafe_allow_html=True)

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("### Log Collector")
                        st.markdown("""
                        **Universal interface for multiple data platforms:**
                        - Databricks Workflow
                        - Apache Airflow
                        - AWS Glue
                        - Azure Data Factory (ADF)
                        - Azure Synapse
                        - Microsoft Fabric

                        **Functions:**
                        - Normalizes log formats across platforms
                        - Extracts key metadata and error information
                        - Provides real-time monitoring capabilities
                        """)

                        st.markdown("### Data Lineage Graph Builder")
                        st.markdown("""
                        **Creates comprehensive data lineage:**
                        - Maps dependencies between data assets
                        - Tracks data flow across systems
                        - Identifies impact of failures
                        - Provides visual representation of data pipelines
                        """)

                    with col2:
                        st.markdown("### LLM-Powered RCA Engine")
                        st.markdown("""
                        **Intelligent root cause analysis:**
                        - Uses large language models for pattern recognition
                        - Correlates events across systems
                        - Identifies root causes from symptoms
                        - Learns from historical incidents
                        - Provides natural language explanations
                        """)

                        st.markdown("### Self-Heal Executor")
                        st.markdown("""
                        **Automated remediation actions:**
                        - **Rollback:** Reverts to last known good state
                        - **Retry:** Re-executes failed operations
                        - **Fallback:** Uses alternative processing paths
                        - **Feedback loop:** Improves based on action results
                        """)

                        # Data flow explanation
                    st.markdown("---")
                    st.markdown('<h4 style="color: #6366f1;">Data Flow Process</h4>', unsafe_allow_html=True)
                    st.markdown("""
                     1. **Log Collection:** Various data platforms generate logs that are collected and normalized
                     2. **Lineage Building:** The system builds a comprehensive graph of data dependencies
                     3. **RCA Analysis:** When failures occur, the LLM engine analyzes patterns to identify root causes
                     4. **Remediation:** The system executes appropriate self-healing actions based on the analysis
                     5. **Learning:** Results from actions are fed back to improve future RCA accuracy
                     """)
        elif card.get("is_doc_intel", False):
            # Create a custom expandable section for Document Intelligence
            with st.expander(f"{card['emoji']} {card['title']}", expanded=False):
                # Enhanced project card content
                st.markdown(f"""
                <div class="project-card" style="background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); border-radius: 16px; padding: 2rem; color: #1a202c; margin-bottom: 1.5rem; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid #e2e8f0;">
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-bottom: 2rem;">{metrics_html}</div>
                    <div style="background: #000000; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid #333333; box-shadow: 0 2px 12px rgba(0,0,0,0.3);">
                        <h4 style="color: #ffffff; margin-bottom: 1.25rem; font-size: 1.2rem; font-weight: 700; display: flex; align-items: center; gap: 0.5rem;">
                            <span style="font-size: 1.3rem;">✨</span>
                            <span>Key Features</span>
                        </h4>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #ffffff;">{feats_html}</ul>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                        <div style="background: #475569; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #64748b; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                            <div style="font-size: 0.9rem; color: #e2e8f0; margin-bottom: 0.3rem; font-weight: 600;">Tech Stack</div>
                            <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">{card['stack']}</div>
                        </div>
                        <div style="background: #475569; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #64748b; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                            <div style="font-size: 0.9rem; color: #e2e8f0; margin-bottom: 0.3rem; font-weight: 600;">Deployment</div>
                            <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">{card['deploy']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Add Streamlit buttons for Document Intelligence architecture and repo inside the card
                st.markdown('<div style="margin: 1.5rem 0;">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏗️ View Architecture", key="doc_intel_arch_btn",
                                 help="Click to view the detailed architecture diagram"):
                        st.session_state.show_doc_intel_arch = not st.session_state.show_doc_intel_arch
                        st.rerun()
                with col2:
                    if st.button("📂 Explore Repository", key="doc_intel_repo_btn",
                                 help="Click to explore the project repository"):
                        st.info("Repository link would open here")
                st.markdown('</div>', unsafe_allow_html=True)

                # Show architecture if button is clicked
                if st.session_state.show_doc_intel_arch:
                    st.markdown("---")
                    st.markdown(
                        '<h3 style="color: #6366f1; margin-top: 1rem;">Document Intelligence Architecture Diagram</h3>',
                        unsafe_allow_html=True)
                    st.markdown("""
                    This diagram illustrates the architecture of the Document Intelligence system, showing how it extracts pipeline definitions from various sources, 
                    generates documentation in multiple formats, enhances it with LLM summarization, and provides graph visualization capabilities.
                    """)

                    # Create the architecture diagram
                    with st.expander("Architecture Diagram", expanded=True):
                        # Create a graphlib graph
                        dot = graphviz.Digraph(comment='Document Intelligence Architecture')
                        dot.attr(rankdir='TB', size='12,10')

                        # Define nodes with styles
                        dot.attr('node', shape='box', style='filled', fontname='Arial')

                        # Pipeline Sources
                        with dot.subgraph(name='cluster_sources') as c:
                            c.attr(label='Pipeline Definition Sources', style='filled', fillcolor='lightgrey',
                                   fontname='Arial')
                            c.node('json', 'JSON Files', fillcolor='lightblue')
                            c.node('dag', 'DAG Files\n(Airflow)', fillcolor='lightblue')
                            c.node('config', 'Config Files\n(YAML/INI)', fillcolor='lightblue')
                            c.node('api', 'API Endpoints', fillcolor='lightblue')

                        # Extraction Engine
                        dot.node('extractor', 'Definition Extractor\n(Universal Parser)', shape='component',
                                 fillcolor='lightyellow')

                        # Intermediate Processing
                        dot.node('normalizer', 'Data Normalizer\n(Standard Format)', shape='ellipse',
                                 fillcolor='lightgreen')

                        # Documentation Generation
                        with dot.subgraph(name='cluster_docs') as c:
                            c.attr(label='Documentation Generation', style='filled', fillcolor='lightgrey',
                                   fontname='Arial')
                            c.node('markdown', 'Markdown\nGenerator', fillcolor='#FFD700')
                            c.node('confluence', 'Confluence\nGenerator', fillcolor='#FFD700')
                            c.node('word', 'Word Document\nGenerator', fillcolor='#FFD700')

                        # LLM Processing
                        dot.node('llm', 'LLM Summarization\n(Enhanced Documentation)', shape='ellipse',
                                 fillcolor='lightcoral')

                        # Graph Visualization
                        dot.node('visualization', 'Graph Visualization\n(Interactive Diagrams)', shape='component',
                                 fillcolor='lightpink')

                        # Output Formats
                        with dot.subgraph(name='cluster_outputs') as c:
                            c.attr(label='Output Formats', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('web_ui', 'Web UI', fillcolor='#90EE90')
                            c.node('export', 'Export Formats\n(PDF/HTML)', fillcolor='#90EE90')
                            c.node('api_out', 'API Endpoints', fillcolor='#90EE90')

                        # Define edges
                        dot.edges([
                            ('json', 'extractor'),
                            ('dag', 'extractor'),
                            ('config', 'extractor'),
                            ('api', 'extractor')
                        ])

                        dot.edge('extractor', 'normalizer', label='Raw Definitions')
                        dot.edge('normalizer', 'markdown', label='Normalized Data')
                        dot.edge('normalizer', 'confluence', label='Normalized Data')
                        dot.edge('normalizer', 'word', label='Normalized Data')

                        dot.edge('markdown', 'llm', label='Basic Documentation', style='dashed')
                        dot.edge('confluence', 'llm', label='Basic Documentation', style='dashed')
                        dot.edge('word', 'llm', label='Basic Documentation', style='dashed')

                        dot.edge('normalizer', 'visualization', label='Structured Data')
                        dot.edge('llm', 'visualization', label='Enhanced Documentation')

                        dot.edge('visualization', 'web_ui', label='Interactive Views')
                        dot.edge('visualization', 'export', label='Static Exports')
                        dot.edge('visualization', 'api_out', label='Data Access')

                        # Feedback loop
                        dot.edge('llm', 'extractor', label='Learning Feedback', style='dotted')

                        # Render the graph
                        st.graphviz_chart(dot)

                    # Detailed component descriptions
                    st.markdown("---")
                    st.markdown('<h4 style="color: #6366f1;">Component Details</h4>', unsafe_allow_html=True)

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("### Definition Extractor")
                        st.markdown("""
                        **Universal parser for multiple definition formats:**
                        - JSON pipeline definitions
                        - DAG files (Airflow)
                        - Configuration files (YAML, INI, etc.)
                        - API endpoints for pipeline metadata

                        **Functions:**
                        - Normalizes different definition formats
                        - Extracts key pipeline metadata and structure
                        - Handles version differences in definition formats
                        """)

                        st.markdown("### Data Normalizer")
                        st.markdown("""
                        **Standardizes pipeline information:**
                        - Creates unified data model across sources
                        - Extracts dependencies and relationships
                        - Identifies key components and parameters
                        - Prepares data for documentation and visualization
                        """)

                    with col2:
                        st.markdown("### LLM Summarization")
                        st.markdown("""
                        **Enhances documentation with AI:**
                        - Generates natural language summaries of complex pipelines
                        - Explains technical components in business terms
                        - Identifies potential issues and optimization opportunities
                        - Creates consistent documentation style across all pipelines
                        """)

                        st.markdown("### Graph Visualization")
                        st.markdown("""
                        **Interactive pipeline visualization:**
                        - Creates dependency graphs of data pipelines
                        - Provides interactive exploration capabilities
                        - Shows data flow and transformation steps
                        - Allows filtering and focusing on specific components
                        """)

                    # Documentation formats
                    st.markdown("---")
                    st.markdown('<h4 style="color: #6366f1;">Documentation Formats</h4>', unsafe_allow_html=True)

                    docs_col1, docs_col2, docs_col3 = st.columns(3)

                    with docs_col1:
                        st.markdown("### Markdown")
                        st.markdown("""
                        - **Format:** Standard Markdown (.md)
                        - **Use Cases:** 
                            - GitHub/GitLab documentation
                            - Developer reference
                            - Version-controlled documentation
                        - **Features:**
                            - Code snippets
                            - Table of contents
                            - Easy conversion to other formats
                        """)

                    with docs_col2:
                        st.markdown("### Confluence")
                        st.markdown("""
                        - **Format:** Atlassian Confluence pages
                        - **Use Cases:** 
                            - Team collaboration
                            - Business documentation
                            - Project documentation
                        - **Features:**
                            - Automatic page creation
                            - Version history
                            - Team commenting
                        """)

                    with docs_col3:
                        st.markdown("### Word Documents")
                        st.markdown("""
                        - **Format:** Microsoft Word (.docx)
                        - **Use Cases:** 
                            - Formal documentation
                            - Client deliverables
                            - Compliance documentation
                        - **Features:**
                            - Professional formatting
                            - Table of contents
                            - Custom templates
                        """)

                    # Data flow explanation
                    st.markdown("---")
                    st.markdown('<h4 style="color: #6366f1;">Data Flow Process</h4>', unsafe_allow_html=True)
                    st.markdown("""
                    1. **Extraction:** Pipeline definitions are extracted from various sources and formats
                    2. **Normalization:** Data is standardized into a unified model for processing
                    3. **Documentation Generation:** Basic documentation is created in multiple formats
                    4. **LLM Enhancement:** Documentation is enhanced with AI-powered summarization and analysis
                    5. **Visualization:** Interactive graphs are created to visualize pipeline dependencies
                    6. **Delivery:** Final documentation is delivered through various channels (UI, exports, APIs)
                    """)
        elif card.get("is_virtual_dl", False):
            # Create a custom expandable section for Virtual DataLake
            with st.expander(f"{card['emoji']} {card['title']}", expanded=False):
                # Enhanced project card content
                st.markdown(f"""
                <div class="project-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 16px; padding: 2rem; color: white; margin-bottom: 1.5rem; box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-bottom: 2rem;">{metrics_html}</div>
                    <div style="background: #000000; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid #333333; box-shadow: 0 2px 12px rgba(0,0,0,0.3);">
                        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.1rem; font-weight: 700;">✨ Key Features</h4>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #ffffff;">{feats_html}</ul>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                        <div style="background: rgba(255,255,255,0.1); padding: 0.8rem 1.2rem; border-radius: 8px; backdrop-filter: blur(10px);">
                            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.3rem;">Tech Stack</div>
                            <div style="font-weight: 600; color: #0f172a; font-size: 0.95rem;">{card['stack']}</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.1); padding: 0.8rem 1.2rem; border-radius: 8px; backdrop-filter: blur(10px);">
                            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.3rem;">Deployment</div>
                            <div style="font-weight: 600; color: #0f172a; font-size: 0.95rem;">{card['deploy']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Add Streamlit buttons for Virtual DataLake architecture and repo inside the card
                st.markdown('<div style="margin: 1.5rem 0;">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏗️ View Architecture", key="virtual_dl_arch_btn",
                                 help="Click to view the detailed architecture diagram"):
                        st.session_state.show_virtual_dl_arch = not st.session_state.show_virtual_dl_arch
                        st.rerun()
                with col2:
                    if st.button("📂 Explore Repository", key="virtual_dl_repo_btn",
                                 help="Click to explore the project repository"):
                        st.info("Repository link would open here")
                st.markdown('</div>', unsafe_allow_html=True)

                # Show architecture if button is clicked
                if st.session_state.show_virtual_dl_arch:
                    st.markdown("---")
                    st.markdown(
                        '<h3 style="color: #6366f1; margin-top: 1rem;">Virtual DataLake Architecture Diagram</h3>',
                        unsafe_allow_html=True)
                    st.markdown("""
                    This diagram illustrates the architecture of the Virtual DataLake system, showing how it processes natural language prompts, 
                    connects to various data sources through a federation layer, executes queries via Presto/Trino, and returns results in multiple formats.
                    """)

                    # Create the architecture diagram
                    with st.expander("Architecture Diagram", expanded=True):
                        # Create a graphlib graph
                        dot = graphviz.Digraph(comment='Virtual DataLake Architecture')
                        dot.attr(rankdir='TB', size='14,10')

                        # Define nodes with styles
                        dot.attr('node', shape='box', style='filled', fontname='Arial')

                        # User Input
                        dot.node('user', 'User\n(Natural Language Prompt)', shape='ellipse', fillcolor='lightblue')

                        # Prompt Processing
                        dot.node('nlp', 'Natural Language Processing\n(Prompt → SQL Translation)', shape='component',
                                 fillcolor='lightyellow')

                        # Query Optimization
                        dot.node('optimizer', 'Query Optimizer\n(Federation Planning)', shape='component',
                                 fillcolor='#FFD700')

                        # Data Sources
                        with dot.subgraph(name='cluster_sources') as c:
                            c.attr(label='Data Sources (100+ Connectors)', style='filled', fillcolor='lightgrey',
                                   fontname='Arial')

                            with dot.subgraph(name='cluster_databases') as c2:
                                c2.attr(label='Databases', style='filled', fillcolor='#E6E6FA')
                                c2.node('salesforce', 'Salesforce', fillcolor='#ADD8E6')
                                c2.node('postgres', 'PostgreSQL', fillcolor='#ADD8E6')
                                c2.node('snowflake', 'Snowflake', fillcolor='#ADD8E6')
                                c2.node('other_db', 'Other Databases\n(MySQL, Oracle, etc.)', fillcolor='#ADD8E6')

                            with dot.subgraph(name='cluster_storage') as c2:
                                c2.attr(label='Storage Systems', style='filled', fillcolor='#E6E6FA')
                                c2.node('s3', 'Amazon S3', fillcolor='#90EE90')
                                c2.node('adls', 'Azure Data Lake', fillcolor='#90EE90')
                                c2.node('gcs', 'Google Cloud Storage', fillcolor='#90EE90')

                            with dot.subgraph(name='cluster_apps') as c2:
                                c2.attr(label='Applications', style='filled', fillcolor='#E6E6FA')
                                c2.node('api_sources', 'APIs\n(REST, GraphQL, etc.)', fillcolor='#FFB6C1')
                                c2.node('file_sources', 'File Systems\n(CSV, JSON, Parquet)', fillcolor='#FFB6C1')

                        # Federation Engine
                        dot.node('presto', 'Federation Engine\n(Presto/Trino)', shape='cylinder',
                                 fillcolor='lightcoral')

                        # Result Processing
                        dot.node('results', 'Result Processor\n(Format Transformation)', shape='component',
                                 fillcolor='lightpink')

                        # Output Formats
                        with dot.subgraph(name='cluster_outputs') as c:
                            c.attr(label='Output Formats', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('dataframe', 'Data Frame\n(Pandas, Spark)', fillcolor='#90EE90')
                            c.node('csv', 'CSV File', fillcolor='#90EE90')
                            c.node('dashboard', 'Interactive Dashboard', fillcolor='#90EE90')
                            c.node('api', 'API Response', fillcolor='#90EE90')

                        # Define edges
                        dot.edge('user', 'nlp', label='Natural Language Query')
                        dot.edge('nlp', 'optimizer', label='Translated SQL')
                        dot.edge('optimizer', 'presto', label='Optimized Query Plan')

                        # Connections to data sources
                        dot.edge('presto', 'salesforce', label='Query', style='dashed')
                        dot.edge('presto', 'postgres', label='Query', style='dashed')
                        dot.edge('presto', 'snowflake', label='Query', style='dashed')
                        dot.edge('presto', 'other_db', label='Query', style='dashed')
                        dot.edge('presto', 's3', label='Query', style='dashed')
                        dot.edge('presto', 'adls', label='Query', style='dashed')
                        dot.edge('presto', 'gcs', label='Query', style='dashed')
                        dot.edge('presto', 'api_sources', label='Query', style='dashed')
                        dot.edge('presto', 'file_sources', label='Query', style='dashed')

                        # Data flow from sources
                        dot.edge('salesforce', 'presto', label='Results', style='dashed')
                        dot.edge('postgres', 'presto', label='Results', style='dashed')
                        dot.edge('snowflake', 'presto', label='Results', style='dashed')
                        dot.edge('other_db', 'presto', label='Results', style='dashed')
                        dot.edge('s3', 'presto', label='Results', style='dashed')
                        dot.edge('adls', 'presto', label='Results', style='dashed')
                        dot.edge('gcs', 'presto', label='Results', style='dashed')
                        dot.edge('api_sources', 'presto', label='Results', style='dashed')
                        dot.edge('file_sources', 'presto', label='Results', style='dashed')

                        dot.edge('presto', 'results', label='Query Results')
                        dot.edge('results', 'dataframe', label='Formatted Output')
                        dot.edge('results', 'csv', label='Formatted Output')
                        dot.edge('results', 'dashboard', label='Formatted Output')
                        dot.edge('results', 'api', label='Formatted Output')

                        # Feedback loop
                        dot.edge('results', 'nlp', label='Query Results Feedback', style='dotted')

                        # Render the graph
                        st.graphviz_chart(dot)

                    # Detailed component descriptions
                    st.markdown("---")
                    st.markdown('<h4 style="color: #6366f1;">Component Details</h4>', unsafe_allow_html=True)

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("### Natural Language Processing")
                        st.markdown("""
                        **Translates prompts to SQL:**
                        - Understands natural language queries
                        - Converts business questions to technical queries
                        - Supports complex multi-source joins
                        - Learns from user feedback and query patterns

                        **Capabilities:**
                        - Schema awareness across all connected sources
                        - Contextual understanding of business domains
                        - Query validation and safety checks
                        """)

                        st.markdown("### Query Optimizer")
                        st.markdown("""
                        **Creates efficient execution plans:**
                        - Analyzes query across all connected sources
                        - Determines optimal execution strategy
                        - Pushes down operations to source systems when possible
                        - Minimizes data movement across networks
                        """)

                    with col2:
                        st.markdown("### Federation Engine (Presto/Trino)")
                        st.markdown("""
                        **Distributed SQL query engine:**
                        - Executes queries across multiple data sources
                        - Provides unified SQL interface to diverse systems
                        - Handles query federation and joins across sources
                        - Scales horizontally for performance
                        """)

                        st.markdown("### Result Processor")
                        st.markdown("""
                        **Transforms and delivers results:**
                        - Formats data for different output types
                        - Handles large result sets efficiently
                        - Provides pagination and streaming where needed
                        - Applies post-processing and transformations
                        """)

                    # Connector types
                    st.markdown("---")
                    st.markdown('<h4 style="color: #6366f1;">Connector Types</h4>', unsafe_allow_html=True)

                    connector_col1, connector_col2, connector_col3 = st.columns(3)

                    with connector_col1:
                        st.markdown("### Database Connectors")
                        st.markdown("""
                        - **Relational Databases:**
                            - PostgreSQL, MySQL, SQL Server
                            - Oracle, DB2, Teradata
                        - **Cloud Data Warehouses:**
                            - Snowflake, BigQuery, Redshift
                            - Azure Synapse, Databricks SQL
                        - **NoSQL Databases:**
                            - MongoDB, Cassandra, DynamoDB
                        """)

                    with connector_col2:
                        st.markdown("### Storage Connectors")
                        st.markdown("""
                        - **Cloud Storage:**
                            - Amazon S3
                            - Azure Data Lake Storage
                            - Google Cloud Storage
                        - **File Formats:**
                            - Parquet, ORC, Avro
                            - JSON, CSV, XML
                        - **Data Lakes:**
                            - Delta Lake, Iceberg, Hudi
                        """)

                    with connector_col3:
                        st.markdown("### Application Connectors")
                        st.markdown("""
                        - **SaaS Applications:**
                            - Salesforce, ServiceNow
                            - HubSpot, Marketo
                        - **APIs:**
                            - REST APIs
                            - GraphQL endpoints
                            - SOAP services
                        - **Streaming Sources:**
                            - Kafka, Kinesis
                            - Event Hubs, Pub/Sub
                        """)

                    # Output formats
                    st.markdown("---")
                    st.markdown('<h4 style="color: #6366f1;">Output Formats</h4>', unsafe_allow_html=True)

                    output_col1, output_col2, output_col3, output_col4 = st.columns(4)

                    with output_col1:
                        st.markdown("### Data Frames")
                        st.markdown("""
                        - **Formats:** Pandas, Spark, Dask
                        - **Use Cases:** 
                            - Data science workflows
                            - Further processing in Python
                            - Machine learning pipelines
                        - **Features:**
                            - Preserves data types
                            - Supports large datasets
                            - Easy integration with analytics libraries
                        """)

                    with output_col2:
                        st.markdown("### CSV Files")
                        st.markdown("""
                        - **Formats:** Standard CSV, compressed formats
                        - **Use Cases:** 
                            - Data exchange
                            - Import into spreadsheets
                            - Simple data sharing
                        - **Features:**
                            - Configurable delimiters
                            - Header options
                            - Chunked downloads for large files
                        """)

                    with output_col3:
                        st.markdown("### Dashboards")
                        st.markdown("""
                        - **Formats:** Interactive web UI
                        - **Use Cases:** 
                            - Business intelligence
                            - Data exploration
                            - Real-time monitoring
                        - **Features:**
                            - Charts and visualizations
                            - Filtering and drilling
                            - Export capabilities
                        """)

                    with output_col4:
                        st.markdown("### API Responses")
                        st.markdown("""
                        - **Formats:** JSON, XML, Protocol Buffers
                        - **Use Cases:** 
                            - Application integration
                            - Automated workflows
                            - Microservices architecture
                        - **Features:**
                            - Standard HTTP REST API
                            - Authentication and rate limiting
                            - Pagination and cursors
                        """)

                    # Data flow explanation
                    st.markdown("---")
                    st.markdown('<h4 style="color: #6366f1;">Query Execution Process</h4>', unsafe_allow_html=True)
                    st.markdown("""
                    1. **Input:** User provides natural language prompt or direct SQL query
                    2. **Translation:** NLP engine converts prompt to optimized SQL
                    3. **Planning:** Query optimizer creates execution plan across sources
                    4. **Execution:** Presto/Trino executes the query across connected systems
                    5. **Federation:** Results are combined from multiple sources
                    6. **Processing:** Result processor formats data for output
                    7. **Delivery:** Results are returned in requested format
                    8. **Learning:** System learns from query patterns and results
                    """)
        elif card.get("is_synthetic_data", False):
            # Create a custom expandable section for Synthetic Data Generator
            with st.expander(f"{card['emoji']} {card['title']}", expanded=False):
                # Enhanced project card content
                st.markdown(f"""
                <div class="project-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 16px; padding: 2rem; color: white; margin-bottom: 1.5rem; box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-bottom: 2rem;">{metrics_html}</div>
                    <div style="background: #000000; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid #333333; box-shadow: 0 2px 12px rgba(0,0,0,0.3);">
                        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.1rem; font-weight: 700;">✨ Key Features</h4>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #ffffff;">{feats_html}</ul>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                        <div style="background: rgba(255,255,255,0.1); padding: 0.8rem 1.2rem; border-radius: 8px; backdrop-filter: blur(10px);">
                            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.3rem;">Tech Stack</div>
                            <div style="font-weight: 600; color: #0f172a; font-size: 0.95rem;">{card['stack']}</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.1); padding: 0.8rem 1.2rem; border-radius: 8px; backdrop-filter: blur(10px);">
                            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.3rem;">Deployment</div>
                            <div style="font-weight: 600; color: #0f172a; font-size: 0.95rem;">{card['deploy']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Add Streamlit buttons for Synthetic Data Generator architecture and repo inside the card
                st.markdown('<div style="margin: 1.5rem 0;">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏗️ View Architecture", key="synthetic_data_arch_btn",
                                 help="Click to view the detailed architecture diagram"):
                        st.session_state.show_synthetic_data_arch = not st.session_state.show_synthetic_data_arch
                        st.rerun()
                with col2:
                    if st.button("📂 Explore Repository", key="synthetic_data_repo_btn",
                                 help="Click to explore the project repository"):
                        st.info("Repository link would open here")
                st.markdown('</div>', unsafe_allow_html=True)

                # Show architecture if button is clicked
                if st.session_state.show_synthetic_data_arch:
                    st.markdown("---")
                    st.markdown(
                        '<h3 style="color: #6366f1; margin-top: 1rem;">Synthetic Data Generator Architecture Diagram</h3>',
                        unsafe_allow_html=True)
                    st.markdown("""
                    This diagram illustrates the architecture of the Synthetic Data Generator system, showing how it uses seed data and metadata, 
                    applies constraints and business rules, and scales to generate large synthetic datasets using PySpark and LLM technologies.
                    """)

                    # Create the architecture diagram
                    with st.expander("Architecture Diagram", expanded=True):
                        # Create a graphlib graph
                        dot = graphviz.Digraph(comment='Synthetic Data Generator Architecture')
                        dot.attr(rankdir='TB', size='14,12')

                        # Define nodes with styles
                        dot.attr('node', shape='box', style='filled', fontname='Arial')

                        # Input Sources
                        with dot.subgraph(name='cluster_inputs') as c:
                            c.attr(label='Input Sources', style='filled', fillcolor='lightgrey', fontname='Arial')

                            with dot.subgraph(name='cluster_seed_data') as c2:
                                c2.attr(label='Seed Data', style='filled', fillcolor='#E6E6FA')
                                c2.node('sample_data', 'Sample Datasets\n(CSV, Parquet, JSON)', fillcolor='#ADD8E6')
                                c2.node('db_snapshot', 'Database Snapshots', fillcolor='#ADD8E6')
                                c2.node('api_data', 'API Data Sources', fillcolor='#ADD8E6')

                            with dot.subgraph(name='cluster_metadata') as c2:
                                c2.attr(label='Metadata', style='filled', fillcolor='#E6E6FA')
                                c2.node('schema_def', 'Schema Definitions', fillcolor='#90EE90')
                                c2.node('data_dict', 'Data Dictionaries', fillcolor='#90EE90')
                                c2.node('profiling', 'Data Profiling Results', fillcolor='#90EE90')

                        # Configuration
                        with dot.subgraph(name='cluster_config') as c:
                            c.attr(label='Generation Configuration', style='filled', fillcolor='lightgrey',
                                   fontname='Arial')
                            c.node('constraints', 'Constraints & Rules', fillcolor='#FFD700')
                            c.node('null_ratios', 'Null Ratios & Distributions', fillcolor='#FFD700')
                            c.node('industry', 'Industry Templates', fillcolor='#FFD700')

                        # Core Engine
                        dot.node('generator', 'Synthetic Data Generator\n(PySpark + LLM)', shape='component',
                                 fillcolor='lightcoral')

                        # LLM Components
                        with dot.subgraph(name='cluster_llm') as c:
                            c.attr(label='LLM Enhancement', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('pattern_learning', 'Pattern Learning', fillcolor='#FFB6C1')
                            c.node('realism', 'Realism Enhancement', fillcolor='#FFB6C1')
                            c.node('anonymization', 'Smart Anonymization', fillcolor='#FFB6C1')

                        # Processing
                        dot.node('distributed', 'Distributed Processing\n(Spark Cluster)', shape='cylinder',
                                 fillcolor='lightyellow')

                        # Output
                        with dot.subgraph(name='cluster_output') as c:
                            c.attr(label='Output Formats', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('synthetic_data', 'Synthetic Datasets', fillcolor='#90EE90')
                            c.node('quality_report', 'Data Quality Reports', fillcolor='#90EE90')
                            c.node('api_out', 'API Endpoints', fillcolor='#90EE90')

                        # Scale & Performance
                        with dot.subgraph(name='cluster_scale') as c:
                            c.attr(label='Scale & Performance', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('parallel', 'Parallel Generation', fillcolor='#ADD8E6')
                            c.node('incremental', 'Incremental Generation', fillcolor='#ADD8E6')
                            c.node('monitoring', 'Performance Monitoring', fillcolor='#ADD8E6')

                        # Define edges
                        # Input flows
                        dot.edges([
                            ('sample_data', 'generator'),
                            ('db_snapshot', 'generator'),
                            ('api_data', 'generator'),
                            ('schema_def', 'generator'),
                            ('data_dict', 'generator'),
                            ('profiling', 'generator')
                        ])

                        # Configuration flows
                        dot.edges([
                            ('constraints', 'generator'),
                            ('null_ratios', 'generator'),
                            ('industry', 'generator')
                        ])

                        # Processing flows
                        dot.edge('generator', 'pattern_learning', label='Data Patterns')
                        dot.edge('generator', 'realism', label='Realism Requirements')
                        dot.edge('generator', 'anonymization', label='Anonymization Needs')

                        dot.edge('pattern_learning', 'generator', label='Learned Patterns', style='dashed')
                        dot.edge('realism', 'generator', label='Realism Enhancements', style='dashed')
                        dot.edge('anonymization', 'generator', label='Anonymization Rules', style='dashed')

                        dot.edge('generator', 'distributed', label='Generation Plan')
                        dot.edge('distributed', 'generator', label='Processing Results', style='dashed')

                        # Output flows
                        dot.edges([
                            ('generator', 'synthetic_data'),
                            ('generator', 'quality_report'),
                            ('generator', 'api_out')
                        ])

                        # Scale flows
                        dot.edges([
                            ('parallel', 'distributed'),
                            ('incremental', 'distributed'),
                            ('monitoring', 'distributed')
                        ])

                        # Render the graph
                        st.graphviz_chart(dot)

                    # Detailed component descriptions
                    st.markdown("---")
                    st.header("Component Details")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("Input Sources")
                        st.markdown("""
                        **Seed data and metadata inputs:**
                        - **Sample Datasets:** Real data samples in various formats (CSV, Parquet, JSON)
                        - **Database Snapshots:** Schema and data from production databases
                        - **API Data Sources:** Data extracted from various APIs
                        - **Schema Definitions:** Formal schema specifications
                        - **Data Dictionaries:** Business definitions of data elements
                        - **Profiling Results:** Statistical analysis of source data

                        **Purpose:** Provide the foundation for generating realistic synthetic data
                        that maintains statistical properties of original data.
                        """)

                        st.subheader("Generation Configuration")
                        st.markdown("""
                        **Rules and constraints for data generation:**
                        - **Constraints & Rules:** Business rules, foreign key relationships, value constraints
                        - **Null Ratios & Distributions:** Control over null values and data distributions
                        - **Industry Templates:** Pre-configured templates for specific industries
                          (Healthcare, Finance, Retail, etc.)

                        **Purpose:** Ensure synthetic data meets specific requirements and maintains
                        data quality standards.
                        """)

                    with col2:
                        st.subheader("Core Engine (PySpark + LLM)")
                        st.markdown("""
                        **Advanced data generation capabilities:**
                        - **PySpark Foundation:** Distributed processing for large-scale data generation
                        - **LLM Integration:** Enhanced realism through language model capabilities
                        - **Pattern Recognition:** Identifies and replicates complex data patterns
                        - **Statistical Modeling:** Maintains statistical properties of source data

                        **Capabilities:**
                        - Generates data with same statistical properties as source
                        - Maintains referential integrity across tables
                        - Handles complex data types and relationships
                        """)

                        st.subheader("Scale & Performance")
                        st.markdown("""
                        **Enterprise-scale data generation:**
                        - **Parallel Generation:** Simultaneous generation of multiple datasets
                        - **Incremental Generation:** Add to existing datasets without full regeneration
                        - **Performance Monitoring:** Track generation speed and resource utilization

                        **Scalability:**
                        - Handles datasets from MB to PB scale
                        - Distributed across Spark clusters
                        - Optimized for cloud and on-premise deployment
                        """)

                    # Industry templates
                    st.markdown("---")
                    st.header("Industry Templates")

                    industry_col1, industry_col2, industry_col3 = st.columns(3)

                    with industry_col1:
                        st.subheader("Healthcare")
                        st.markdown("""
                        - **HIPAA Compliance:** PHI anonymization
                        - **Medical Codes:** ICD-10, CPT, LOINC
                        - **Patient Data:** Demographics, medical history
                        - **Clinical Data:** Lab results, vitals, medications
                        - **Provider Data:** Hospitals, physicians, pharmacies
                        """)

                    with industry_col2:
                        st.subheader("Finance")
                        st.markdown("""
                        - **PCI Compliance:** Financial data protection
                        - **Transaction Data:** Payments, transfers, purchases
                        - **Customer Data:** Accounts, profiles, KYC information
                        - **Market Data:** Stock prices, exchange rates
                        - **Risk Data:** Credit scores, fraud patterns
                        """)

                    with industry_col3:
                        st.subheader("Retail & E-commerce")
                        st.markdown("""
                        - **Customer Data:** Profiles, preferences, behavior
                        - **Product Data:** Catalog, inventory, pricing
                        - **Transaction Data:** Purchases, returns, reviews
                        - **Supply Chain:** Inventory, logistics, suppliers
                        - **Web Analytics:** Clicks, sessions, conversions
                        """)

                    # Output formats
                    st.markdown("---")
                    st.header("Output Formats & Features")

                    output_col1, output_col2 = st.columns(2)

                    with output_col1:
                        st.subheader("Data Generation Features")
                        st.markdown("""
                        - **Maintains Statistical Properties:** Mean, median, mode, distribution
                        - **Referential Integrity:** Maintains relationships between tables
                        - **Data Variety:** Structured, semi-structured, and unstructured data
                        - **Temporal Consistency:** Time-series data with proper sequencing
                        - **Geographic Data:** Realistic locations with proper spatial relationships
                        - **Synthetic PII:** Realistic but fake personal identifiable information
                        """)

                    with output_col2:
                        st.subheader("Output Options")
                        st.markdown("""
                        - **File Formats:** Parquet, CSV, JSON, Avro, ORC
                        - **Database Load:** Direct loading to SQL, NoSQL databases
                        - **Cloud Storage:** S3, ADLS, GCS compatible outputs
                        - **Data Size:** From small samples to petabyte-scale datasets
                        - **API Access:** RESTful API for on-demand generation
                        - **Integration:** Compatible with major data platforms
                        """)

                    # Data generation process
                    st.markdown("---")
                    st.header("Data Generation Process")
                    st.markdown("""
                    1. **Input Analysis:** System analyzes seed data and metadata to understand structure and patterns
                    2. **Pattern Learning:** LLM components identify and learn complex data patterns and relationships
                    3. **Constraint Application:** Business rules, null ratios, and constraints are applied
                    4. **Distribution Planning:** System plans distributed generation across Spark cluster
                    5. **Data Generation:** Parallel generation of synthetic data maintaining statistical properties
                    6. **Quality Validation:** Automated checks ensure data quality and constraint adherence
                    7. **Output Delivery:** Data delivered in requested formats with quality reports
                    8. **Feedback Loop:** System learns from generation results to improve future outputs
                    """)

                    # Use cases
                    st.markdown("---")
                    st.header("Use Cases")
                    use_case_col1, use_case_col2, use_case_col3 = st.columns(3)

                    with use_case_col1:
                        st.subheader("Development & Testing")
                        st.markdown("""
                        - **Application Development:** Realistic test data for development
                        - **Quality Assurance:** Comprehensive test scenarios
                        - **Performance Testing:** Large-scale data for load testing
                        - **Training:** Data for training new team members
                        """)

                    with use_case_col2:
                        st.subheader("Data Science & AI")
                        st.markdown("""
                        - **Model Training:** Data for machine learning models
                        - **Algorithm Development:** Test algorithms without sensitive data
                        - **Data Augmentation:** Expand limited datasets for better models
                        - **Research:** Data for academic and commercial research
                        """)

                    with use_case_col3:
                        st.subheader("Compliance & Security")
                        st.markdown("""
                        - **Data Anonymization:** Replace sensitive data with synthetic equivalents
                        - **Regulatory Compliance:** Meet GDPR, HIPAA, CCPA requirements
                        - **Data Sharing:** Share data with partners without exposing sensitive information
                        - **Demo Environments:** Realistic data for sales demonstrations
                        """)
        elif card.get("is_dqm_etl", False):
            # Create a custom expandable section for DQM & ETL Testing Framework
            with st.expander(f"{card['emoji']} {card['title']}", expanded=False):
                # Enhanced project card content
                st.markdown(f"""
                <div class="project-card" style="background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); border-radius: 16px; padding: 2rem; color: #1a202c; margin-bottom: 1.5rem; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid #e2e8f0;">
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-bottom: 2rem;">{metrics_html}</div>
                    <div style="background: #000000; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid #333333; box-shadow: 0 2px 12px rgba(0,0,0,0.3);">
                        <h4 style="color: #ffffff; margin-bottom: 1.25rem; font-size: 1.2rem; font-weight: 700; display: flex; align-items: center; gap: 0.5rem;">
                            <span style="font-size: 1.3rem;">✨</span>
                            <span>Key Features</span>
                        </h4>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #ffffff;">{feats_html}</ul>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                        <div style="background: #475569; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #64748b; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                            <div style="font-size: 0.9rem; color: #e2e8f0; margin-bottom: 0.3rem; font-weight: 600;">Tech Stack</div>
                            <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">{card['stack']}</div>
                        </div>
                        <div style="background: #475569; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #64748b; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                            <div style="font-size: 0.9rem; color: #e2e8f0; margin-bottom: 0.3rem; font-weight: 600;">Deployment</div>
                            <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">{card['deploy']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Add Streamlit buttons for DQM & ETL Testing Framework architecture and repo inside the card
                st.markdown('<div style="margin: 1.5rem 0;">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏗️ View Architecture", key="dqm_etl_arch_btn",
                                 help="Click to view the detailed architecture diagram"):
                        st.session_state.show_dqm_etl_arch = not st.session_state.show_dqm_etl_arch
                        st.rerun()
                with col2:
                    if st.button("📂 Explore Repository", key="dqm_etl_repo_btn",
                                 help="Click to explore the project repository"):
                        st.info("Repository link would open here")
                st.markdown('</div>', unsafe_allow_html=True)

                # Show architecture if button is clicked
                if st.session_state.show_dqm_etl_arch:
                    st.markdown("---")
                    st.markdown(
                        '<h3 style="color: #6366f1; margin-top: 1rem;">DQM & ETL Testing Framework Architecture Diagram</h3>',
                        unsafe_allow_html=True)
                    st.markdown("""
                    This diagram illustrates the architecture of the DQM (Data Quality Management) & ETL Testing Framework, showing how it performs 
                    schema validation, null/constraint checks, reconciliation across stages, and automated regression tests using Great Expectations, PySpark, and LangChain.
                    """)

                    # Create the architecture diagram
                    with st.expander("Architecture Diagram", expanded=True):
                        # Create a graphlib graph
                        dot = graphviz.Digraph(comment='DQM & ETL Testing Framework Architecture')
                        dot.attr(rankdir='TB', size='14,12')

                        # Define nodes with styles
                        dot.attr('node', shape='box', style='filled', fontname='Arial')

                        # Data Sources
                        with dot.subgraph(name='cluster_sources') as c:
                            c.attr(label='Data Sources', style='filled', fillcolor='lightgrey', fontname='Arial')

                            with dot.subgraph(name='cluster_etl_stages') as c2:
                                c2.attr(label='ETL Pipeline Stages', style='filled', fillcolor='#E6E6FA')
                                c2.node('source', 'Source Systems', fillcolor='#ADD8E6')
                                c2.node('staging', 'Staging Area', fillcolor='#ADD8E6')
                                c2.node('processed', 'Processed Data', fillcolor='#ADD8E6')
                                c2.node('target', 'Target Data Warehouse', fillcolor='#ADD8E6')

                        # Test Configuration
                        with dot.subgraph(name='cluster_config') as c:
                            c.attr(label='Test Configuration', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('test_def', 'Test Definitions\n(YAML/JSON)', fillcolor='#FFD700')
                            c.node('expectations', 'Data Expectations', fillcolor='#FFD700')
                            c.node('rules', 'Business Rules', fillcolor='#FFD700')

                        # Core Testing Engine
                        dot.node('test_engine', 'Testing Engine\n(Great Expectations + PySpark)', shape='component',
                                 fillcolor='lightcoral')

                        # AI Components
                        with dot.subgraph(name='cluster_ai') as c:
                            c.attr(label='AI Components (LangChain)', style='filled', fillcolor='lightgrey',
                                   fontname='Arial')
                            c.node('test_gen', 'Test Case Generation', fillcolor='#FFB6C1')
                            c.node('anomaly_detection', 'Anomaly Detection', fillcolor='#FFB6C1')
                            c.node('root_cause', 'Root Cause Analysis', fillcolor='#FFB6C1')

                        # Testing Components
                        with dot.subgraph(name='cluster_testing') as c:
                            c.attr(label='Testing Components', style='filled', fillcolor='lightgrey', fontname='Arial')

                            with dot.subgraph(name='cluster_validation') as c2:
                                c2.attr(label='Validation Tests', style='filled', fillcolor='#E6E6FA')
                                c2.node('schema_val', 'Schema Validation', fillcolor='#90EE90')
                                c2.node('null_check', 'Null/Constraint Checks', fillcolor='#90EE90')
                                c2.node('data_type', 'Data Type Validation', fillcolor='#90EE90')

                            with dot.subgraph(name='cluster_reconciliation') as c2:
                                c2.attr(label='Reconciliation Tests', style='filled', fillcolor='#E6E6FA')
                                c2.node('reconciliation', 'Cross-Stage Reconciliation', fillcolor='#ADD8E6')
                                c2.node('count_check', 'Record Count Validation', fillcolor='#ADD8E6')
                                c2.node('sum_check', 'Sum/Amount Validation', fillcolor='#ADD8E6')

                            with dot.subgraph(name='cluster_regression') as c2:
                                c2.attr(label='Regression Tests', style='filled', fillcolor='#E6E6FA')
                                c2.node('regression', 'Automated Regression', fillcolor='#FFB6C1')
                                c2.node('history_compare', 'Historical Comparison', fillcolor='#FFB6C1')
                                c2.node('perf_test', 'Performance Testing', fillcolor='#FFB6C1')

                        # Results & Reporting
                        with dot.subgraph(name='cluster_results') as c:
                            c.attr(label='Results & Reporting', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('results', 'Test Results Storage', fillcolor='#90EE90')
                            c.node('dashboard', 'Quality Dashboard', fillcolor='#90EE90')
                            c.node('alerts', 'Alert System', fillcolor='#90EE90')
                            c.node('reports', 'Quality Reports', fillcolor='#90EE90')

                        # Integration
                        with dot.subgraph(name='cluster_integration') as c:
                            c.attr(label='CI/CD Integration', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('github', 'GitHub Actions', fillcolor='#ADD8E6')
                            c.node('ado', 'Azure DevOps', fillcolor='#ADD8E6')
                            c.node('jenkins', 'Jenkins', fillcolor='#ADD8E6')

                        # Define edges
                        # Data flows
                        dot.edges([
                            ('source', 'test_engine'),
                            ('staging', 'test_engine'),
                            ('processed', 'test_engine'),
                            ('target', 'test_engine')
                        ])

                        # Configuration flows
                        dot.edges([
                            ('test_def', 'test_engine'),
                            ('expectations', 'test_engine'),
                            ('rules', 'test_engine')
                        ])

                        # Testing component flows
                        dot.edges([
                            ('test_engine', 'schema_val'),
                            ('test_engine', 'null_check'),
                            ('test_engine', 'data_type'),
                            ('test_engine', 'reconciliation'),
                            ('test_engine', 'count_check'),
                            ('test_engine', 'sum_check'),
                            ('test_engine', 'regression'),
                            ('test_engine', 'history_compare'),
                            ('test_engine', 'perf_test')
                        ])

                        # AI component flows
                        dot.edges([
                            ('test_engine', 'test_gen'),
                            ('test_engine', 'anomaly_detection'),
                            ('test_engine', 'root_cause')
                        ])

                        dot.edges([
                            ('test_gen', 'test_engine'),
                            ('anomaly_detection', 'test_engine'),
                            ('root_cause', 'test_engine')
                        ])

                        # Results flows
                        dot.edges([
                            ('schema_val', 'results'),
                            ('null_check', 'results'),
                            ('data_type', 'results'),
                            ('reconciliation', 'results'),
                            ('count_check', 'results'),
                            ('sum_check', 'results'),
                            ('regression', 'results'),
                            ('history_compare', 'results'),
                            ('perf_test', 'results')
                        ])

                        dot.edges([
                            ('results', 'dashboard'),
                            ('results', 'alerts'),
                            ('results', 'reports')
                        ])

                        # Integration flows
                        dot.edges([
                            ('results', 'github'),
                            ('results', 'ado'),
                            ('results', 'jenkins')
                        ])

                        # Render the graph
                        st.graphviz_chart(dot)

                    # Detailed component descriptions
                    st.markdown("---")
                    st.header("Component Details")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("Testing Engine (Great Expectations + PySpark)")
                        st.markdown("""
                        **Core testing capabilities:**
                        - **Great Expectations Integration:** Declarative data testing framework
                        - **PySpark Foundation:** Distributed testing for large datasets
                        - **Validation Suite Execution:** Runs comprehensive test suites
                        - **Data Profiling:** Automated profiling to understand data characteristics

                        **Capabilities:**
                        - Executes tests across different data environments
                        - Handles batch and streaming data testing
                        - Provides detailed test results and metrics
                        - Supports custom test development
                        """)

                        st.subheader("Validation Tests")
                        st.markdown("""
                        **Data quality validation:**
                        - **Schema Validation:** Ensures data structure matches expectations
                        - **Null/Constraint Checks:** Validates null ratios and business constraints
                        - **Data Type Validation:** Confirms data types are as expected
                        - **Format Validation:** Checks data formatting (email, phone, etc.)

                        **Purpose:** Ensure data conforms to defined standards and structures
                        before processing continues.
                        """)

                    with col2:
                        st.subheader("AI Components (LangChain)")
                        st.markdown("""
                        **Intelligent testing capabilities:**
                        - **Test Case Generation:** AI-powered creation of test scenarios
                        - **Anomaly Detection:** Identifies unusual patterns in data
                        - **Root Cause Analysis:** Helps identify sources of data quality issues
                        - **Predictive Testing:** Anticipates potential data quality problems

                        **Benefits:**
                        - Reduces manual test creation effort
                        - Identifies subtle data quality issues
                        - Provides intelligent insights into data problems
                        - Learns from historical test results
                        """)

                        st.subheader("Reconciliation Tests")
                        st.markdown("""
                        **Cross-stage validation:**
                        - **Cross-Stage Reconciliation:** Ensures data consistency across ETL stages
                        - **Record Count Validation:** Verifies no records are lost during processing
                        - **Sum/Amount Validation:** Confirms numerical integrity through pipelines
                        - **Referential Integrity:** Validates relationship consistency

                        **Purpose:** Ensure data remains consistent and accurate as it moves
                        through different processing stages.
                        """)

                    # Testing types
                    st.markdown("---")
                    st.header("Testing Types")

                    testing_col1, testing_col2, testing_col3 = st.columns(3)

                    with testing_col1:
                        st.subheader("Schema Validation")
                        st.markdown("""
                        - **Column Existence:** All expected columns are present
                        - **Data Types:** Column data types match expectations
                        - **Constraints:** Primary key, unique constraints are maintained
                        - **Defaults:** Default values are correctly applied
                        - **Nested Structures:** Complex types are properly structured
                        """)

                    with testing_col2:
                        st.subheader("Data Quality Checks")
                        st.markdown("""
                        - **Null Checks:** Validate null ratios and patterns
                        - **Value Ranges:** Ensure values fall within expected ranges
                        - **Pattern Matching:** Validate formats (email, phone, etc.)
                        - **Uniqueness:** Confirm unique constraints are maintained
                        - **Consistency:** Ensure consistent values across related fields
                        """)

                    with testing_col3:
                        st.subheader("Reconciliation Tests")
                        st.markdown("""
                        - **Record Counts:** Compare counts between source and target
                        - **Data Completeness:** Ensure no data loss during processing
                        - **Numerical Accuracy:** Validate sums, averages, and other aggregates
                        - **Business Logic:** Verify business rules are correctly applied
                        - **Temporal Consistency:** Ensure time-based logic works correctly
                        """)

                    # Regression testing
                    st.markdown("---")
                    st.header("Regression Testing")
                    regression_col1, regression_col2 = st.columns(2)

                    with regression_col1:
                        st.subheader("Automated Regression Tests")
                        st.markdown("""
                        - **Test Suite Management:** Organized collection of regression tests
                        - **Historical Comparison:** Compare current results with historical baselines
                        - **Performance Testing:** Measure and validate processing performance
                        - **Change Impact Analysis:** Assess impact of schema or logic changes
                        - **Version Control:** Track test changes and results over time
                        """)

                    with regression_col2:
                        st.subheader("CI/CD Integration")
                        st.markdown("""
                        - **GitHub Actions:** Automated testing in GitHub workflows
                        - **Azure DevOps:** Integration with Azure pipelines
                        - **Jenkins:** Plugin-based integration with Jenkins
                        - **Quality Gates:** Automated promotion based on test results
                        - **Deployment Blocking:** Prevent deployment on test failures
                        """)

                    # Results & reporting
                    st.markdown("---")
                    st.header("Results & Reporting")
                    results_col1, results_col2 = st.columns(2)

                    with results_col1:
                        st.subheader("Reporting Features")
                        st.markdown("""
                        - **Quality Dashboard:** Visual representation of data quality metrics
                        - **Alert System:** Notifications for quality issues and test failures
                        - **Quality Reports:** Detailed reports for stakeholders
                        - **Trend Analysis:** Track quality metrics over time
                        - **Drill-Down Capability:** Investigate specific quality issues
                        """)

                    with results_col2:
                        st.subheader("Integration Options")
                        st.markdown("""
                        - **API Access:** RESTful API for integrating with other systems
                        - **Webhooks:** Event-based notifications for test results
                        - **Export Formats:** CSV, JSON, PDF exports of test results
                        - **Data Lake Integration:** Store results in data lakes for analysis
                        - **BI Tool Integration:** Connect with Tableau, Power BI, etc.
                        """)

                    # Testing process
                    st.markdown("---")
                    st.header("Testing Process")
                    st.markdown("""
                    1. **Test Definition:** Define tests using YAML/JSON configuration or UI
                    2. **Test Execution:** Automated execution of tests against data sources
                    3. **Validation:** Comprehensive validation of schema, constraints, and quality
                    4. **Reconciliation:** Cross-stage validation to ensure data consistency
                    5. **Regression Testing:** Automated regression testing against historical baselines
                    6. **Results Collection:** Aggregation of test results and metrics
                    7. **Reporting:** Generation of dashboards, alerts, and reports
                    8. **Integration:** Feedback into CI/CD pipelines and alerting systems
                    """)

                    # Benefits
                    st.markdown("---")
                    st.header("Benefits")
                    benefits_col1, benefits_col2, benefits_col3 = st.columns(3)

                    with benefits_col1:
                        st.subheader("Data Quality")
                        st.markdown("""
                        - **Early Detection:** Catch issues before they impact downstream systems
                        - **Comprehensive Coverage:** Test all aspects of data quality
                        - **Consistent Standards:** Apply uniform quality standards across projects
                        - **Proactive Monitoring:** Continuous monitoring of data quality
                        """)

                    with benefits_col2:
                        st.subheader("Efficiency")
                        st.markdown("""
                        - **Automation:** Reduce manual testing effort
                        - **Reusability:** Reuse test patterns across projects
                        - **Scalability:** Handle testing at any data scale
                        - **Integration:** Seamless integration with existing workflows
                        """)

                    with benefits_col3:
                        st.subheader("Reliability")
                        st.markdown("""
                        - **Trustworthy Data:** Ensure data can be trusted for decision making
                        - **Audit Trail:** Complete history of test executions and results
                        - **Compliance:** Meet regulatory and compliance requirements
                        - **Risk Reduction:** Minimize business risks from poor data quality
                        """)
        elif card.get("is_deployment_framework", False):
            # Create a custom expandable section for Deployment Framework
            with st.expander(f"{card['emoji']} {card['title']}", expanded=False):
                # Enhanced project card content
                st.markdown(f"""
                <div class="project-card" style="background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); border-radius: 16px; padding: 2rem; color: #1a202c; margin-bottom: 1.5rem; box-shadow: 0 8px 32px rgba(0,0,0,0.08); border: 1px solid #e2e8f0;">
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-bottom: 2rem;">{metrics_html}</div>
                    <div style="background: #000000; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid #333333; box-shadow: 0 2px 12px rgba(0,0,0,0.3);">
                        <h4 style="color: #ffffff; margin-bottom: 1.25rem; font-size: 1.2rem; font-weight: 700; display: flex; align-items: center; gap: 0.5rem;">
                            <span style="font-size: 1.3rem;">✨</span>
                            <span>Key Features</span>
                        </h4>
                        <ul style="list-style: none; padding: 0; margin: 0; color: #ffffff;">{feats_html}</ul>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                        <div style="background: #475569; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #64748b; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                            <div style="font-size: 0.9rem; color: #e2e8f0; margin-bottom: 0.3rem; font-weight: 600;">Tech Stack</div>
                            <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">{card['stack']}</div>
                        </div>
                        <div style="background: #475569; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #64748b; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                            <div style="font-size: 0.9rem; color: #e2e8f0; margin-bottom: 0.3rem; font-weight: 600;">Deployment</div>
                            <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">{card['deploy']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Add Streamlit buttons for Deployment Framework architecture and repo inside the card
                st.markdown('<div style="margin: 1.5rem 0;">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏗️ View Architecture", key="deployment_framework_arch_btn",
                                 help="Click to view the detailed architecture diagram"):
                        st.session_state.show_deployment_framework_arch = not st.session_state.show_deployment_framework_arch
                        st.rerun()
                with col2:
                    if st.button("📂 Explore Repository", key="deployment_framework_repo_btn",
                                 help="Click to explore the project repository"):
                        st.info("Repository link would open here")
                st.markdown('</div>', unsafe_allow_html=True)

                # Show architecture if button is clicked
                if st.session_state.show_deployment_framework_arch:
                    st.markdown("---")
                    st.markdown(
                        '<h3 style="color: #6366f1; margin-top: 1rem;">Deployment Framework Architecture Diagram</h3>',
                        unsafe_allow_html=True)
                    st.markdown("""
                    This diagram illustrates the architecture of the Deployment Framework, showing how it uses infrastructure as code, 
                    provisions resources via Terraform/CDK/ARM, manages jobs and IAM roles, and integrates with CI/CD systems like GitHub and Azure DevOps.
                    """)

                    # Create the architecture diagram
                    with st.expander("Architecture Diagram", expanded=True):
                        # Create a graphlib graph
                        dot = graphviz.Digraph(comment='Deployment Framework Architecture')
                        dot.attr(rankdir='TB', size='14,12')

                        # Define nodes with styles
                        dot.attr('node', shape='box', style='filled', fontname='Arial')

                        # Infrastructure as Code
                        with dot.subgraph(name='cluster_iac') as c:
                            c.attr(label='Infrastructure as Code', style='filled', fillcolor='lightgrey',
                                   fontname='Arial')

                            with dot.subgraph(name='cluster_definitions') as c2:
                                c2.attr(label='Definition Files', style='filled', fillcolor='#E6E6FA')
                                c2.node('yaml_def', 'YAML Definitions', fillcolor='#ADD8E6')
                                c2.node('json_def', 'JSON Definitions', fillcolor='#ADD8E6')
                                c2.node('templates', 'Template Library', fillcolor='#ADD8E6')

                        # Provisioning Tools
                        with dot.subgraph(name='cluster_provisioning') as c:
                            c.attr(label='Provisioning Tools', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('terraform', 'Terraform', fillcolor='#FFD700')
                            c.node('cdk', 'AWS CDK', fillcolor='#FFD700')
                            c.node('arm', 'ARM Templates', fillcolor='#FFD700')
                            c.node('pulumi', 'Pulumi', fillcolor='#FFD700')

                        # Core Engine
                        dot.node('orchestrator', 'Deployment Orchestrator', shape='component', fillcolor='lightcoral')

                        # Resource Management
                        with dot.subgraph(name='cluster_resources') as c:
                            c.attr(label='Resource Management', style='filled', fillcolor='lightgrey', fontname='Arial')

                            with dot.subgraph(name='cluster_jobs') as c2:
                                c2.attr(label='Jobs & Services', style='filled', fillcolor='#E6E6FA')
                                c2.node('etl_jobs', 'ETL Jobs', fillcolor='#90EE90')
                                c2.node('api_services', 'API Services', fillcolor='#90EE90')
                                c2.node('batch_jobs', 'Batch Processing', fillcolor='#90EE90')
                                c2.node('streaming', 'Streaming Jobs', fillcolor='#90EE90')

                            with dot.subgraph(name='cluster_iam') as c2:
                                c2.attr(label='IAM & Security', style='filled', fillcolor='#E6E6FA')
                                c2.node('roles', 'IAM Roles', fillcolor='#ADD8E6')
                                c2.node('policies', 'Security Policies', fillcolor='#ADD8E6')
                                c2.node('secrets', 'Secrets Management', fillcolor='#ADD8E6')

                        # Cloud Providers
                        with dot.subgraph(name='cluster_cloud') as c:
                            c.attr(label='Cloud Providers', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('aws', 'Amazon Web Services', fillcolor='#FFB6C1')
                            c.node('azure', 'Microsoft Azure', fillcolor='#FFB6C1')
                            c.node('gcp', 'Google Cloud Platform', fillcolor='#FFB6C1')
                            c.node('multi_cloud', 'Multi-Cloud Deployment', fillcolor='#FFB6C1')

                        # CI/CD Integration
                        with dot.subgraph(name='cluster_cicd') as c:
                            c.attr(label='CI/CD Integration', style='filled', fillcolor='lightgrey', fontname='Arial')
                            c.node('github', 'GitHub Actions', fillcolor='#90EE90')
                            c.node('ado', 'Azure DevOps', fillcolor='#90EE90')
                            c.node('jenkins', 'Jenkins', fillcolor='#90EE90')
                            c.node('gitlab', 'GitLab CI/CD', fillcolor='#90EE90')

                        # Monitoring & Governance
                        with dot.subgraph(name='cluster_monitoring') as c:
                            c.attr(label='Monitoring & Governance', style='filled', fillcolor='lightgrey',
                                   fontname='Arial')
                            c.node('monitoring', 'Deployment Monitoring', fillcolor='#ADD8E6')
                            c.node('audit', 'Audit Logs', fillcolor='#ADD8E6')
                            c.node('compliance', 'Compliance Checks', fillcolor='#ADD8E6')

                        # Define edges
                        # Infrastructure as Code flows
                        dot.edges([
                            ('yaml_def', 'orchestrator'),
                            ('json_def', 'orchestrator'),
                            ('templates', 'orchestrator')
                        ])

                        # Provisioning tool flows
                        dot.edges([
                            ('orchestrator', 'terraform'),
                            ('orchestrator', 'cdk'),
                            ('orchestrator', 'arm'),
                            ('orchestrator', 'pulumi')
                        ])

                        # Resource management flows
                        dot.edges([
                            ('orchestrator', 'etl_jobs'),
                            ('orchestrator', 'api_services'),
                            ('orchestrator', 'batch_jobs'),
                            ('orchestrator', 'streaming'),
                            ('orchestrator', 'roles'),
                            ('orchestrator', 'policies'),
                            ('orchestrator', 'secrets')
                        ])

                        # Cloud provider flows
                        dot.edges([
                            ('terraform', 'aws'),
                            ('terraform', 'azure'),
                            ('terraform', 'gcp'),
                            ('terraform', 'multi_cloud'),
                            ('cdk', 'aws'),
                            ('arm', 'azure'),
                            ('pulumi', 'multi_cloud')
                        ])

                        # CI/CD integration flows
                        dot.edges([
                            ('github', 'orchestrator'),
                            ('ado', 'orchestrator'),
                            ('jenkins', 'orchestrator'),
                            ('gitlab', 'orchestrator')
                        ])

                        # Monitoring flows
                        dot.edges([
                            ('aws', 'monitoring'),
                            ('azure', 'monitoring'),
                            ('gcp', 'monitoring'),
                            ('multi_cloud', 'monitoring'),
                            ('monitoring', 'audit'),
                            ('monitoring', 'compliance')
                        ])

                        # Feedback loops
                        dot.edge('monitoring', 'orchestrator', label='Health Status', style='dashed')
                        dot.edge('compliance', 'orchestrator', label='Policy Validation', style='dashed')

                        # Render the graph
                        st.graphviz_chart(dot)

                    # Detailed component descriptions
                    st.markdown("---")
                    st.header("Component Details")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("Infrastructure as Code")
                        st.markdown("""
                        **Declarative infrastructure definition:**
                        - **YAML Definitions:** Human-readable configuration format
                        - **JSON Definitions:** Structured configuration format
                        - **Template Library:** Reusable infrastructure patterns
                        - **Version Control:** Git-based management of infrastructure code

                        **Benefits:**
                        - Repeatable and consistent deployments
                        - Version-controlled infrastructure changes
                        - Collaborative infrastructure management
                        - Audit trail of all changes
                        """)

                        st.subheader("Provisioning Tools")
                        st.markdown("""
                        **Multi-tool provisioning support:**
                        - **Terraform:** Cloud-agnostic infrastructure provisioning
                        - **AWS CDK:** AWS-specific infrastructure as code using programming languages
                        - **ARM Templates:** Azure Resource Manager templates for Azure deployments
                        - **Pulumi:** General-purpose infrastructure as code using programming languages

                        **Capabilities:**
                        - Support for multiple cloud providers
                        - Modular and reusable components
                        - State management for infrastructure
                        - Dependency management between resources
                        """)

                    with col2:
                        st.subheader("Deployment Orchestrator")
                        st.markdown("""
                        **Centralized deployment management:**
                        - **Workflow Coordination:** Manages deployment sequences and dependencies
                        - **Resource Provisioning:** Coordinates infrastructure provisioning
                        - **Configuration Management:** Handles application configuration
                        - **Rollback Management:** Manages deployment failures and rollbacks

                        **Features:**
                        - Parallel deployment execution where possible
                        - Dependency resolution between components
                        - Health checks and validation
                        - Automated rollback on failures
                        """)

                        st.subheader("Resource Management")
                        st.markdown("""
                        **Comprehensive resource provisioning:**
                        - **Jobs & Services:** ETL jobs, API services, batch processing, streaming jobs
                        - **IAM & Security:** Roles, policies, and secrets management
                        - **Networking:** VPCs, subnets, security groups, and load balancers
                        - **Storage:** Databases, object storage, and file systems

                        **Security Focus:**
                        - Principle of least privilege for IAM roles
                        - Automated security policy application
                        - Secrets management and rotation
                        - Compliance validation
                        """)

                    # Provisioning tools comparison
                    st.markdown("---")
                    st.header("Provisioning Tools Comparison")

                    tools_col1, tools_col2, tools_col3, tools_col4 = st.columns(4)

                    with tools_col1:
                        st.subheader("Terraform")
                        st.markdown("""
                        - **Provider:** HashiCorp
                        - **Language:** HCL (HashiCorp Configuration Language)
                        - **Cloud Support:** Multi-cloud (AWS, Azure, GCP, etc.)
                        - **State Management:** Terraform State files
                        - **Strengths:** Mature ecosystem, large community
                        """)

                    with tools_col2:
                        st.subheader("AWS CDK")
                        st.markdown("""
                        - **Provider:** AWS
                        - **Language:** TypeScript, Python, Java, etc.
                        - **Cloud Support:** AWS only
                        - **State Management:** AWS CloudFormation
                        - **Strengths:** AWS-native, programming language support
                        """)

                    with tools_col3:
                        st.subheader("ARM Templates")
                        st.markdown("""
                        - **Provider:** Microsoft
                        - **Language:** JSON
                        - **Cloud Support:** Azure only
                        - **State Management:** Azure Resource Manager
                        - **Strengths:** Azure-native, deep Azure integration
                        """)

                    with tools_col4:
                        st.subheader("Pulumi")
                        st.markdown("""
                        - **Provider:** Pulumi
                        - **Language:** TypeScript, Python, Go, etc.
                        - **Cloud Support:** Multi-cloud (AWS, Azure, GCP, etc.)
                        - **State Management:** Pulumi Service or self-managed
                        - **Strengths:** Programming language support, multi-cloud
                        """)

                    # CI/CD integration
                    st.markdown("---")
                    st.header("CI/CD Integration")

                    cicd_col1, cicd_col2, cicd_col3, cicd_col4 = st.columns(4)

                    with cicd_col1:
                        st.subheader("GitHub Actions")
                        st.markdown("""
                        - **Workflow Definition:** YAML files in repository
                        - **Triggers:** Push, pull request, schedule, etc.
                        - **Integration:** Native GitHub integration
                        - **Runners:** GitHub-hosted or self-hosted
                        - **Marketplace:** Extensive action ecosystem
                        """)

                    with cicd_col2:
                        st.subheader("Azure DevOps")
                        st.markdown("""
                        - **Workflow Definition:** YAML or classic editor
                        - **Triggers:** Various git events and schedules
                        - **Integration:** Native Azure integration
                        - **Agents:** Microsoft-hosted or self-hosted
                        - **Features:** Boards, Repos, Pipelines, Test Plans
                        """)

                    with cicd_col3:
                        st.subheader("Jenkins")
                        st.markdown("""
                        - **Workflow Definition:** Jenkinsfile (Groovy)
                        - **Triggers:** Various plugins and webhooks
                        - **Integration:** Extensive plugin ecosystem
                        - **Agents:** Master/agent architecture
                        - **Flexibility:** Highly customizable and extensible
                        """)

                    with cicd_col4:
                        st.subheader("GitLab CI/CD")
                        st.markdown("""
                        - **Workflow Definition:** .gitlab-ci.yml in repository
                        - **Triggers:** Push, merge request, schedule, etc.
                        - **Integration:** Native GitLab integration
                        - **Runners:** GitLab-hosted or self-hosted
                        - **Features:** Built-in container registry, package registry
                        """)

                    # Deployment process
                    st.markdown("---")
                    st.header("Deployment Process")
                    st.markdown("""
                    1. **Infrastructure Definition:** Define infrastructure using YAML/JSON templates
                    2. **CI/CD Trigger:** Code commit or manual trigger initiates deployment pipeline
                    3. **Validation:** Infrastructure code validated for syntax and security
                    4. **Planning:** Deployment plan generated showing what will be created/changed
                    5. **Approval:** Manual or automated approval of deployment plan
                    6. **Provisioning:** Infrastructure provisioned using selected tool (Terraform/CDK/ARM)
                    7. **Configuration:** Applications and services configured and deployed
                    8. **Testing:** Automated tests verify deployment success
                    9. **Monitoring:** Deployment health monitored and alerts configured
                    10. **Documentation:** Deployment artifacts and documentation updated
                    """)

                    # Deployment strategies
                    st.markdown("---")
                    st.header("Deployment Strategies")
                    strategy_col1, strategy_col2, strategy_col3, strategy_col4 = st.columns(4)

                    with strategy_col1:
                        st.subheader("Blue-Green")
                        st.markdown("""
                        - **Description:** Two identical environments, switch traffic between them
                        - **Benefits:** Zero downtime, easy rollback
                        - **Use Cases:** Critical production applications
                        - **Complexity:** Higher infrastructure cost
                        """)

                    with strategy_col2:
                        st.subheader("Canary")
                        st.markdown("""
                        - **Description:** Gradually roll out to small percentage of users
                        - **Benefits:** Risk mitigation, performance testing
                        - **Use Cases:** New features, major changes
                        - **Complexity:** Requires traffic routing capabilities
                        """)

                    with strategy_col3:
                        st.subheader("Rolling")
                        st.markdown("""
                        - **Description:** Gradually replace instances with new version
                        - **Benefits:** No additional infrastructure cost
                        - **Use Cases:** Most standard deployments
                        - **Complexity:** Moderate, requires health checks
                        """)

                    with strategy_col4:
                        st.subheader("Recreate")
                        st.markdown("""
                        - **Description:** Terminate old version and deploy new version
                        - **Benefits:** Simple to implement
                        - **Use Cases:** Non-critical applications, development environments
                        - **Complexity:** Low, but causes downtime
                        """)

                    # Benefits
                    st.markdown("---")
                    st.header("Benefits")
                    benefits_col1, benefits_col2, benefits_col3 = st.columns(3)

                    with benefits_col1:
                        st.subheader("Consistency & Reliability")
                        st.markdown("""
                        - **Repeatable Deployments:** Same process every time
                        - **Reduced Errors:** Automation minimizes human error
                        - **Version Control:** Track changes to infrastructure
                        - **Audit Trail:** Complete history of deployments
                        """)

                    with benefits_col2:
                        st.subheader("Speed & Efficiency")
                        st.markdown("""
                        - **Faster Deployments:** Automation speeds up processes
                        - **Parallel Execution:** Deploy multiple components simultaneously
                        - **Self-Service:** Teams can deploy without operations overhead
                        - **Resource Optimization:** Efficient resource utilization
                        """)

                    with benefits_col3:
                        st.subheader("Security & Compliance")
                        st.markdown("""
                        - **Security by Default:** Built-in security practices
                        - **Policy Enforcement:** Automated compliance checks
                        - **Secrets Management:** Secure handling of credentials
                        - **Access Control:** Role-based deployment permissions
                        """)
        else:
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
            <div class="project-card" style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); border-radius: 16px; padding: 2rem; color: #f1f5f9; margin-bottom: 1.5rem; box-shadow: 0 8px 32px rgba(0,0,0,0.15); border: 1px solid #475569;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-bottom: 2rem;">{metrics_html}</div>
                <div style="background: #000000; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid #333333; box-shadow: 0 2px 12px rgba(0,0,0,0.3);">
                    <h4 style="color: #ffffff; margin-bottom: 1.25rem; font-size: 1.2rem; font-weight: 700; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="font-size: 1.3rem;">✨</span>
                        <span>Key Features</span>
                    </h4>
                    <ul style="list-style: none; padding: 0; margin: 0; color: #ffffff;">{feats_html}</ul>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div style="background: #334155; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #475569;">
                        <div style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 0.3rem; font-weight: 600;">Tech Stack</div>
                        <div style="font-weight: 600; color: #f1f5f9; font-size: 0.95rem;">{card['stack']}</div>
                    </div>
                    <div style="background: #334155; padding: 0.8rem 1.2rem; border-radius: 8px; border: 1px solid #475569;">
                        <div style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 0.3rem; font-weight: 600;">Deployment</div>
                        <div style="font-weight: 600; color: #f1f5f9; font-size: 0.95rem;">{card['deploy']}</div>
                    </div>
                </div>
            </div>
        </details>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Add enhanced CSS styling for the project section
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        /* Enhanced Project Section Styling */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .grid-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.15);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }

        .grid-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
            transform: translateX(-100%);
            transition: transform 0.8s ease;
        }

        .grid-card:hover::before {
            transform: translateX(100%);
        }

        .grid-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 30px 80px rgba(102, 126, 234, 0.25);
        }

        /* Improved readability for grid card text */
        .grid-card .title {
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            color: white !important;
            margin-bottom: 0.75rem !important;
            text-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
            font-family: 'Inter', sans-serif !important;
            letter-spacing: -0.025em !important;
        }

        .grid-card div {
            color: rgba(255,255,255,0.95) !important;
            font-size: 1rem !important;
            font-weight: 500 !important;
            text-shadow: 0 1px 4px rgba(0,0,0,0.2) !important;
            font-family: 'Inter', sans-serif !important;
            line-height: 1.6 !important;
        }

        .grid-card .description {
            color: rgba(255,255,255,0.9) !important;
            font-size: 0.9375rem !important;
            font-weight: 400 !important;
            margin-bottom: 1.5rem !important;
            line-height: 1.5 !important;
        }

        .grid-card .tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .grid-card .tag {
            background: rgba(255,255,255,0.2);
            color: white;
            padding: 0.375rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 0.025em;
        }

        .grid-card .tag:hover {
            background: rgba(255,255,255,0.3);
            transform: scale(1.05);
        }

        .project-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 16px;
            padding: 2rem;
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="75" cy="75" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="50" cy="10" r="0.5" fill="rgba(255,255,255,0.1)"/><circle cx="10" cy="60" r="0.5" fill="rgba(255,255,255,0.1)"/><circle cx="90" cy="40" r="0.5" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }

        /* Improved readability for project card content */
        .project-card h4 {
            color: white !important;
            font-size: 1.2rem !important;
            font-weight: 700 !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
        }

        .project-card div {
            color: rgba(255,255,255,0.95) !important;
            font-weight: 500 !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }

        .feature-item {
            display: flex;
            align-items: center;
            margin-bottom: 0.8rem;
            padding: 0.8rem;
            background: rgba(255,255,255,0.15);
            border-radius: 8px;
            border-left: 3px solid rgba(255,255,255,0.4);
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .feature-item:hover {
            background: rgba(255,255,255,0.2);
            transform: translateX(5px);
        }

        .feature-item span {
            color: white !important;
            font-weight: 500 !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }

        .metric {
            background: rgba(255,255,255,0.15);
            padding: 1rem;
            border-radius: 12px;
            text-align: center;
            margin: 0.5rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            transition: all 0.3s ease;
        }

        .metric:hover {
            background: rgba(255,255,255,0.2);
            transform: scale(1.05);
        }

        .metric .label {
            font-size: 0.9rem !important;
            opacity: 0.95 !important;
            font-weight: 600 !important;
            color: white !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }

        .metric .value {
            font-size: 1.3rem !important;
            font-weight: 700 !important;
            color: white !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
        }

        .pill {
            background: rgba(255,255,255,0.25);
            color: white;
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            margin-right: 0.5rem;
            display: inline-block;
            margin-bottom: 0.5rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            transition: all 0.3s ease;
            font-weight: 600;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        }

        .pill:hover {
            background: rgba(255,255,255,0.35);
            transform: scale(1.05);
        }

        /* Enhanced button styling */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 1rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
            font-size: 1rem;
            width: 100%;
            margin: 0.75rem 0;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;
            text-transform: uppercase;
            letter-spacing: 0.025em;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 35px rgba(102, 126, 234, 0.3);
            background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
        }

        /* Button container styling for better layout */
        [data-testid="column"] {
            padding: 0 0.5rem;
        }

        /* Ensure buttons have equal width and proper spacing */
        .stButton {
            width: 100%;
            margin: 0.25rem 0;
        }

        /* Enhanced expander styling */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 12px;
            padding: 1rem 1.5rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
            font-size: 1.1rem;
        }

        .streamlit-expanderHeader:hover {
            background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
        }

        /* Architecture diagram styling */
        .stGraph {
            border: 2px solid #e6e6e6;
            border-radius: 16px;
            padding: 2rem;
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }

        /* Section headers */
        .section-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 2rem;
        }

        /* Introduction section stat cards - Improved readability */
        .stat-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        }

        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            color: white;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }

        .stat-card .icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .stat-card .value {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .stat-card .label {
            font-size: 0.9rem;
            font-weight: 600;
            opacity: 0.95;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        }

        /* Key advantages card - Improved readability */
        .icon-bullet {
            display: flex;
            align-items: flex-start;
            margin-bottom: 1rem;
        }

        .icon-bullet .icon {
            margin-right: 12px;
            font-size: 1.2rem;
            color: white;
            min-width: 24px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .icon-bullet span:last-child {
            color: white !important;
            font-weight: 500 !important;
            font-size: 1rem !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
            line-height: 1.5 !important;
        }

        /* CRITICAL: Dark theme for expanded project content */
        .streamlit-expanderContent {
            background: #0a0a0a !important;
            color: #ffffff !important;
            padding: 2rem !important;
            border-radius: 16px !important;
            margin-top: 1rem !important;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
            border: 1px solid #333333 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        /* Enhanced typography for expanded content */
        .streamlit-expanderContent h1,
        .streamlit-expanderContent h2,
        .streamlit-expanderContent h3,
        .streamlit-expanderContent h4,
        .streamlit-expanderContent h5,
        .streamlit-expanderContent h6 {
            color: #ffffff !important;
            font-weight: 700 !important;
            margin-bottom: 1rem !important;
            line-height: 1.4 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.5) !important;
        }

        .streamlit-expanderContent h1 { font-size: 2rem !important; }
        .streamlit-expanderContent h2 { font-size: 1.75rem !important; }
        .streamlit-expanderContent h3 { font-size: 1.5rem !important; }
        .streamlit-expanderContent h4 { font-size: 1.25rem !important; }
        .streamlit-expanderContent h5 { font-size: 1.1rem !important; }
        .streamlit-expanderContent h6 { font-size: 1rem !important; }

        /* Enhanced paragraph and text styling */
        .streamlit-expanderContent p {
            color: #e0e0e0 !important;
            font-size: 1rem !important;
            line-height: 1.7 !important;
            margin-bottom: 1rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent strong,
        .streamlit-expanderContent b {
            color: #ffffff !important;
            font-weight: 700 !important;
        }

        .streamlit-expanderContent ul,
        .streamlit-expanderContent ol {
            color: #e0e0e0 !important;
            font-size: 1rem !important;
            line-height: 1.6 !important;
            margin-bottom: 1rem !important;
            padding-left: 1.5rem !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent li {
            color: #e0e0e0 !important;
            font-size: 1rem !important;
            line-height: 1.6 !important;
            margin-bottom: 0.5rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent code {
            background: #1a1a1a !important;
            color: #00ff88 !important;
            padding: 0.2rem 0.4rem !important;
            border-radius: 4px !important;
            font-family: 'Fira Code', 'Courier New', monospace !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            border: 1px solid #333333 !important;
        }

        .streamlit-expanderContent pre {
            background: #1a1a1a !important;
            color: #e0e0e0 !important;
            padding: 1rem !important;
            border-radius: 8px !important;
            border: 1px solid #333333 !important;
            overflow-x: auto !important;
            font-family: 'Fira Code', 'Courier New', monospace !important;
            font-size: 0.9rem !important;
            line-height: 1.5 !important;
        }

        /* Enhanced blockquote styling */
        .streamlit-expanderContent blockquote {
            background: #1a1a1a !important;
            border-left: 4px solid #6366f1 !important;
            padding: 1rem !important;
            margin: 1rem 0 !important;
            border-radius: 0 8px 8px 0 !important;
            color: #e0e0e0 !important;
            font-style: italic !important;
        }

        /* Enhanced table styling */
        .streamlit-expanderContent table {
            background: #1a1a1a !important;
            border-collapse: collapse !important;
            width: 100% !important;
            margin: 1rem 0 !important;
            border-radius: 8px !important;
            overflow: hidden !important;
            box-shadow: 0 4px 16px rgba(0,0,0,0.3) !important;
            border: 1px solid #333333 !important;
        }

        .streamlit-expanderContent th {
            background: #6366f1 !important;
            color: white !important;
            padding: 0.75rem !important;
            text-align: left !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
        }

        .streamlit-expanderContent td {
            padding: 0.75rem !important;
            border-bottom: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            font-size: 0.9rem !important;
        }

        .streamlit-expanderContent tr:nth-child(even) {
            background: #0f0f0f !important;
        }

        .streamlit-expanderContent tr:hover {
            background: #1f1f1f !important;
        }

        /* Enhanced hr styling */
        .streamlit-expanderContent hr {
            border: none !important;
            height: 2px !important;
            background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
            margin: 2rem 0 !important;
            border-radius: 1px !important;
        }

        /* Enhanced mark styling */
        .streamlit-expanderContent mark {
            background: linear-gradient(120deg, #fbbf24 0%, #f59e0b 100%) !important;
            color: #000000 !important;
            padding: 0.1rem 0.3rem !important;
            border-radius: 4px !important;
            font-weight: 600 !important;
        }

        /* CRITICAL: Fix for Streamlit markdown content inside expanders */
        .streamlit-expanderContent .stMarkdown {
            background: #0a0a0a !important;
            color: #ffffff !important;
            padding: 1rem !important;
            border-radius: 8px !important;
            margin: 0.5rem 0 !important;
        }

        .streamlit-expanderContent .stMarkdown h1,
        .streamlit-expanderContent .stMarkdown h2,
        .streamlit-expanderContent .stMarkdown h3,
        .streamlit-expanderContent .stMarkdown h4,
        .streamlit-expanderContent .stMarkdown h5,
        .streamlit-expanderContent .stMarkdown h6 {
            color: #ffffff !important;
            font-weight: 700 !important;
            margin-bottom: 1rem !important;
            line-height: 1.4 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.5) !important;
        }

        .streamlit-expanderContent .stMarkdown p {
            color: #e0e0e0 !important;
            font-size: 1rem !important;
            line-height: 1.7 !important;
            margin-bottom: 1rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent .stMarkdown ul,
        .streamlit-expanderContent .stMarkdown ol {
            color: #e0e0e0 !important;
            font-size: 1rem !important;
            line-height: 1.6 !important;
            margin-bottom: 1rem !important;
            padding-left: 1.5rem !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent .stMarkdown li {
            color: #e0e0e0 !important;
            font-size: 1rem !important;
            line-height: 1.6 !important;
            margin-bottom: 0.5rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent .stMarkdown strong,
        .streamlit-expanderContent .stMarkdown b {
            color: #ffffff !important;
            font-weight: 700 !important;
        }

        /* Additional fix for any markdown content */
        .streamlit-expanderContent div[data-testid="stMarkdown"] {
            background: #0a0a0a !important;
            color: #ffffff !important;
            padding: 1rem !important;
            border-radius: 8px !important;
            margin: 0.5rem 0 !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] h1,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h2,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h3,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h4,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h5,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h6 {
            color: #ffffff !important;
            font-weight: 700 !important;
            margin-bottom: 1rem !important;
            line-height: 1.4 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.5) !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] p {
            color: #e0e0e0 !important;
            font-size: 1rem !important;
            line-height: 1.7 !important;
            margin-bottom: 1rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] ul,
        .streamlit-expanderContent div[data-testid="stMarkdown"] ol {
            color: #e0e0e0 !important;
            font-size: 1rem !important;
            line-height: 1.6 !important;
            margin-bottom: 1rem !important;
            padding-left: 1.5rem !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] li {
            color: #e0e0e0 !important;
            font-size: 1rem !important;
            line-height: 1.6 !important;
            margin-bottom: 0.5rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] strong,
        .streamlit-expanderContent div[data-testid="stMarkdown"] b {
            color: #ffffff !important;
            font-weight: 700 !important;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .projects-grid {
                grid-template-columns: 1fr;
            }

            .project-card {
                padding: 1.5rem;
            }

            .section-header {
                font-size: 2rem;
            }
        }

        /* CRITICAL: Professional enterprise-grade styling for expanded project content */
        .streamlit-expanderContent {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
            color: #1a202c !important;
            padding: 2.5rem !important;
            border-radius: 20px !important;
            margin-top: 1.5rem !important;
            box-shadow: 0 20px 60px rgba(0,0,0,0.08) !important;
            border: 1px solid #e2e8f0 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            position: relative !important;
            overflow: hidden !important;
        }

        .streamlit-expanderContent::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        }

        /* Professional typography for expanded content */
        .streamlit-expanderContent h1,
        .streamlit-expanderContent h2,
        .streamlit-expanderContent h3,
        .streamlit-expanderContent h4,
        .streamlit-expanderContent h5,
        .streamlit-expanderContent h6 {
            color: #1a202c !important;
            font-weight: 700 !important;
            margin-bottom: 1.5rem !important;
            line-height: 1.3 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            letter-spacing: -0.025em !important;
        }

        .streamlit-expanderContent h1 { 
            font-size: 2.25rem !important; 
            color: #2d3748 !important;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.75rem;
        }
        .streamlit-expanderContent h2 { 
            font-size: 1.875rem !important; 
            color: #2d3748 !important;
        }
        .streamlit-expanderContent h3 { 
            font-size: 1.5rem !important; 
            color: #4a5568 !important;
        }
        .streamlit-expanderContent h4 { 
            font-size: 1.25rem !important; 
            color: #4a5568 !important;
        }
        .streamlit-expanderContent h5 { 
            font-size: 1.125rem !important; 
            color: #4a5568 !important;
        }
        .streamlit-expanderContent h6 { 
            font-size: 1rem !important; 
            color: #4a5568 !important;
        }

        /* Professional paragraph and text styling */
        .streamlit-expanderContent p {
            color: #4a5568 !important;
            font-size: 1.0625rem !important;
            line-height: 1.75 !important;
            margin-bottom: 1.25rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent strong,
        .streamlit-expanderContent b {
            color: #2d3748 !important;
            font-weight: 600 !important;
        }

        .streamlit-expanderContent ul,
        .streamlit-expanderContent ol {
            color: #4a5568 !important;
            font-size: 1.0625rem !important;
            line-height: 1.7 !important;
            margin-bottom: 1.5rem !important;
            padding-left: 1.75rem !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent li {
            color: #4a5568 !important;
            font-size: 1.0625rem !important;
            line-height: 1.7 !important;
            margin-bottom: 0.75rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent code {
            background: #f7fafc !important;
            color: #e53e3e !important;
            padding: 0.25rem 0.5rem !important;
            border-radius: 6px !important;
            font-family: 'Fira Code', 'Courier New', monospace !important;
            font-size: 0.875rem !important;
            font-weight: 500 !important;
            border: 1px solid #e2e8f0 !important;
        }

        .streamlit-expanderContent pre {
            background: #f7fafc !important;
            color: #2d3748 !important;
            padding: 1.5rem !important;
            border-radius: 12px !important;
            border: 1px solid #e2e8f0 !important;
            overflow-x: auto !important;
            font-family: 'Fira Code', 'Courier New', monospace !important;
            font-size: 0.875rem !important;
            line-height: 1.6 !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.06) !important;
        }

        /* Professional blockquote styling */
        .streamlit-expanderContent blockquote {
            background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%) !important;
            border-left: 4px solid #667eea !important;
            padding: 1.5rem !important;
            margin: 2rem 0 !important;
            border-radius: 0 12px 12px 0 !important;
            color: #4a5568 !important;
            font-style: italic !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
        }

        /* Professional table styling */
        .streamlit-expanderContent table {
            background: white !important;
            border-collapse: collapse !important;
            width: 100% !important;
            margin: 2rem 0 !important;
            border-radius: 12px !important;
            overflow: hidden !important;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08) !important;
            border: 1px solid #e2e8f0 !important;
        }

        .streamlit-expanderContent th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            padding: 1rem 1.25rem !important;
            text-align: left !important;
            font-weight: 600 !important;
            font-size: 0.875rem !important;
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
        }

        .streamlit-expanderContent td {
            padding: 1rem 1.25rem !important;
            border-bottom: 1px solid #f1f5f9 !important;
            color: #4a5568 !important;
            font-size: 0.9375rem !important;
        }

        .streamlit-expanderContent tr:nth-child(even) {
            background: #f8fafc !important;
        }

        .streamlit-expanderContent tr:hover {
            background: #f1f5f9 !important;
        }

        /* Professional hr styling */
        .streamlit-expanderContent hr {
            border: none !important;
            height: 1px !important;
            background: linear-gradient(90deg, transparent, #e2e8f0, transparent) !important;
            margin: 3rem 0 !important;
        }

        /* Professional mark styling */
        .streamlit-expanderContent mark {
            background: linear-gradient(120deg, #fef5e7 0%, #fed7aa 100%) !important;
            color: #c05621 !important;
            padding: 0.125rem 0.375rem !important;
            border-radius: 4px !important;
            font-weight: 600 !important;
        }

        /* CRITICAL: Fix for Streamlit markdown content inside expanders */
        .streamlit-expanderContent .stMarkdown {
            background: transparent !important;
            color: #1a202c !important;
            padding: 0 !important;
            border-radius: 0 !important;
            margin: 0 !important;
        }

        .streamlit-expanderContent .stMarkdown h1,
        .streamlit-expanderContent .stMarkdown h2,
        .streamlit-expanderContent .stMarkdown h3,
        .streamlit-expanderContent .stMarkdown h4,
        .streamlit-expanderContent .stMarkdown h5,
        .streamlit-expanderContent .stMarkdown h6 {
            color: #1a202c !important;
            font-weight: 700 !important;
            margin-bottom: 1.5rem !important;
            line-height: 1.3 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            letter-spacing: -0.025em !important;
        }

        .streamlit-expanderContent .stMarkdown p {
            color: #4a5568 !important;
            font-size: 1.0625rem !important;
            line-height: 1.75 !important;
            margin-bottom: 1.25rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent .stMarkdown ul,
        .streamlit-expanderContent .stMarkdown ol {
            color: #4a5568 !important;
            font-size: 1.0625rem !important;
            line-height: 1.7 !important;
            margin-bottom: 1.5rem !important;
            padding-left: 1.75rem !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent .stMarkdown li {
            color: #4a5568 !important;
            font-size: 1.0625rem !important;
            line-height: 1.7 !important;
            margin-bottom: 0.75rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent .stMarkdown strong,
        .streamlit-expanderContent .stMarkdown b {
            color: #2d3748 !important;
            font-weight: 600 !important;
        }

        /* Additional fix for any markdown content */
        .streamlit-expanderContent div[data-testid="stMarkdown"] {
            background: transparent !important;
            color: #1a202c !important;
            padding: 0 !important;
            border-radius: 0 !important;
            margin: 0 !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] h1,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h2,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h3,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h4,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h5,
        .streamlit-expanderContent div[data-testid="stMarkdown"] h6 {
            color: #1a202c !important;
            font-weight: 700 !important;
            margin-bottom: 1.5rem !important;
            line-height: 1.3 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            letter-spacing: -0.025em !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] p {
            color: #4a5568 !important;
            font-size: 1.0625rem !important;
            line-height: 1.75 !important;
            margin-bottom: 1.25rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] ul,
        .streamlit-expanderContent div[data-testid="stMarkdown"] ol {
            color: #4a5568 !important;
            font-size: 1.0625rem !important;
            line-height: 1.7 !important;
            margin-bottom: 1.5rem !important;
            padding-left: 1.75rem !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] li {
            color: #4a5568 !important;
            font-size: 1.0625rem !important;
            line-height: 1.7 !important;
            margin-bottom: 0.75rem !important;
            font-weight: 400 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
        }

        .streamlit-expanderContent div[data-testid="stMarkdown"] strong,
        .streamlit-expanderContent div[data-testid="stMarkdown"] b {
            color: #2d3748 !important;
            font-weight: 600 !important;
        }

        /* Professional styling for expanded project content */
        .streamlit-expanderContent {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
            border-radius: 12px !important;
            padding: 2rem !important;
            margin: 1rem 0 !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
            border: 1px solid #e2e8f0 !important;
        }

        .streamlit-expanderContent h1, .streamlit-expanderContent h2, .streamlit-expanderContent h3, 
        .streamlit-expanderContent h4, .streamlit-expanderContent h5, .streamlit-expanderContent h6 {
            color: #1a202c !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            font-weight: 600 !important;
            margin-bottom: 1rem !important;
            line-height: 1.4 !important;
        }

        .streamlit-expanderContent p {
            color: #374151 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            font-size: 1rem !important;
            line-height: 1.7 !important;
            margin-bottom: 1rem !important;
        }

        .streamlit-expanderContent ul, .streamlit-expanderContent ol {
            color: #374151 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            line-height: 1.6 !important;
            margin-bottom: 1rem !important;
        }

        .streamlit-expanderContent li {
            color: #374151 !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif !important;
            margin-bottom: 0.5rem !important;
        }

        .streamlit-expanderContent strong, .streamlit-expanderContent b {
            color: #1a202c !important;
            font-weight: 600 !important;
        }

        .streamlit-expanderContent code, .streamlit-expanderContent pre {
            background: #f1f5f9 !important;
            color: #1e293b !important;
            font-family: 'Fira Code', 'Monaco', 'Consolas', monospace !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 6px !important;
            padding: 0.25rem 0.5rem !important;
        }

        .streamlit-expanderContent blockquote {
            background: #f8fafc !important;
            border-left: 4px solid #6366f1 !important;
            color: #374151 !important;
            padding: 1rem !important;
            margin: 1rem 0 !important;
            border-radius: 0 8px 8px 0 !important;
        }

        .streamlit-expanderContent table {
            background: white !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 8px !important;
            overflow: hidden !important;
        }

        .streamlit-expanderContent th {
            background: #f8fafc !important;
            color: #1a202c !important;
            font-weight: 600 !important;
            border-bottom: 1px solid #e2e8f0 !important;
        }

        .streamlit-expanderContent td {
            color: #374151 !important;
            border-bottom: 1px solid #f1f5f9 !important;
        }

        .streamlit-expanderContent hr {
            border: none !important;
            border-top: 2px solid #e2e8f0 !important;
            margin: 2rem 0 !important;
        }

        .streamlit-expanderContent mark {
            background: #fef3c7 !important;
            color: #92400e !important;
            padding: 0.125rem 0.25rem !important;
            border-radius: 4px !important;
        }

        .streamlit-expanderContent .stMarkdown {
            color: #374151 !important;
        }
    </style>
    """, unsafe_allow_html=True)


def render_security():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    # Enhanced Professional Header with Executive Summary
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 4rem 3rem; border-radius: 24px; margin-bottom: 3rem; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15); position: relative; overflow: hidden; border: 1px solid #475569;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.05) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 4s infinite;"></div>
            <div style="position: relative; z-index: 1; text-align: center;">
                <h1 style="color: white; font-size: 3rem; font-weight: 800; margin-bottom: 1.5rem; text-shadow: 0 4px 12px rgba(0,0,0,0.4); font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">
                    🔒 Enterprise Security & Compliance
                </h1>
                <p style="color: rgba(255,255,255,0.9); font-size: 1.25rem; margin-bottom: 2rem; font-weight: 500; line-height: 1.6; max-width: 800px; margin-left: auto; margin-right: auto;">
                    Comprehensive security framework designed to protect enterprise data, ensure regulatory compliance, 
                    and maintain operational integrity across all solutions and environments.
                </p>
                <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 2rem;">
                    <div style="background: rgba(255,255,255,0.1); padding: 1rem 1.5rem; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #10b981; margin-bottom: 0.25rem;">100%</div>
                        <div style="font-size: 0.875rem; color: rgba(255,255,255,0.8); font-weight: 500;">Compliance Ready</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 1rem 1.5rem; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #3b82f6; margin-bottom: 0.25rem;">Zero</div>
                        <div style="font-size: 0.875rem; color: rgba(255,255,255,0.8); font-weight: 500;">Security Breaches</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 1rem 1.5rem; border-radius: 12px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #f59e0b; margin-bottom: 0.25rem;">24/7</div>
                        <div style="font-size: 0.875rem; color: rgba(255,255,255,0.8); font-weight: 500;">Monitoring</div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Professional Security Framework Overview
    st.markdown("""
        <div style="margin-bottom: 3rem;">
            <h2 style="color: #1e293b; font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 2rem; font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">
                🛡️ Comprehensive Security Framework
            </h2>
            <p style="color: #64748b; font-size: 1.125rem; text-align: center; margin-bottom: 3rem; font-weight: 400; line-height: 1.6; max-width: 800px; margin-left: auto; margin-right: auto;">
                Our multi-layered security approach ensures data protection, regulatory compliance, and operational security 
                across all enterprise solutions and cloud environments.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Enhanced Security and Compliance Grid
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <style>
            .security-card {
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                padding: 3rem;
                border-radius: 24px;
                color: white;
                box-shadow: 0 20px 60px rgba(240, 147, 251, 0.2);
                border: 1px solid rgba(255,255,255,0.1);
                margin-bottom: 2rem;
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                cursor: pointer;
                position: relative;
                overflow: hidden;
                backdrop-filter: blur(10px);
            }

            .security-card:hover {
                transform: translateY(-12px) scale(1.03);
                box-shadow: 0 30px 80px rgba(240, 147, 251, 0.3);
            }

            .security-item {
                display: flex;
                align-items: center;
                margin-bottom: 1.5rem;
                padding: 1.25rem;
                background: rgba(255,255,255,0.15);
                border-radius: 16px;
                backdrop-filter: blur(15px);
                transition: all 0.3s ease;
                border: 1px solid rgba(255,255,255,0.2);
                box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            }

            .security-item:hover {
                background: rgba(255,255,255,0.25);
                transform: translateX(8px) scale(1.02);
                box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            }
            </style>

            <div class="security-card">
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%); transform: translateX(-100%); transition: transform 0.8s ease;"></div>
                <div style="position: relative; z-index: 1;">
                    <h3 style="color: white; margin-top: 0; margin-bottom: 2rem; font-size: 1.75rem; font-weight: 700; display: flex; align-items: center; gap: 0.75rem; letter-spacing: -0.025em;">
                        <span style="font-size: 2rem;">🔒</span>
                        <span>Security Measures</span>
                    </h3>
        """, unsafe_allow_html=True)

        security_items = [
            {"icon": "👥", "text": "Identity & Access Management (IAM)",
             "desc": "Role-based access control with least privilege principles"},
            {"icon": "🔐", "text": "Secrets Management",
             "desc": "Centralized credential and key management with rotation"},
            {"icon": "📝", "text": "Comprehensive Audit Logging",
             "desc": "Full traceability of all system activities and changes"},
            {"icon": "🛡️", "text": "Data Protection & PII Redaction",
             "desc": "Automated sensitive data identification and protection"},
            {"icon": "🔍", "text": "Real-time Threat Detection",
             "desc": "Advanced monitoring and alerting for security incidents"},
            {"icon": "🔄", "text": "Encryption at Rest & Transit",
             "desc": "End-to-end encryption for all data and communications"}
        ]

        for item in security_items:
            st.markdown(f"""
                <div class="security-item">
                    <span style="margin-right: 1rem; font-size: 1.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">{item['icon']}</span>
                    <div>
                        <div style="font-weight: 600; font-size: 1.1rem; margin-bottom: 0.25rem; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">{item['text']}</div>
                        <div style="font-size: 0.9rem; opacity: 0.9; font-weight: 400;">{item['desc']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <style>
            .compliance-card {
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                padding: 3rem;
                border-radius: 24px;
                color: white;
                box-shadow: 0 20px 60px rgba(79, 172, 254, 0.2);
                border: 1px solid rgba(255,255,255,0.1);
                margin-bottom: 2rem;
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                cursor: pointer;
                position: relative;
                overflow: hidden;
                backdrop-filter: blur(10px);
            }

            .compliance-card:hover {
                transform: translateY(-12px) scale(1.03);
                box-shadow: 0 30px 80px rgba(79, 172, 254, 0.3);
            }

            .compliance-item {
                display: flex;
                align-items: center;
                margin-bottom: 1.5rem;
                padding: 1.25rem;
                background: rgba(255,255,255,0.15);
                border-radius: 16px;
                backdrop-filter: blur(15px);
                transition: all 0.3s ease;
                border: 1px solid rgba(255,255,255,0.2);
                box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            }

            .compliance-item:hover {
                background: rgba(255,255,255,0.25);
                transform: translateX(8px) scale(1.02);
                box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            }
            </style>

            <div class="compliance-card">
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%); transform: translateX(-100%); transition: transform 0.8s ease;"></div>
                <div style="position: relative; z-index: 1;">
                    <h3 style="color: white; margin-top: 0; margin-bottom: 2rem; font-size: 1.75rem; font-weight: 700; display: flex; align-items: center; gap: 0.75rem; letter-spacing: -0.025em;">
                        <span style="font-size: 2rem;">📋</span>
                        <span>Compliance Standards</span>
                    </h3>
        """, unsafe_allow_html=True)

        compliance_items = [
            {"icon": "🌐", "text": "GDPR Compliance", "desc": "EU data protection and privacy regulations"},
            {"icon": "🏥", "text": "HIPAA Certification", "desc": "Healthcare data security and privacy standards"},
            {"icon": "🏢", "text": "SOC 2 Type II", "desc": "Security, availability, and processing integrity"},
            {"icon": "💳", "text": "PCI DSS", "desc": "Payment card industry data security standards"},
            {"icon": "🏭", "text": "ISO 27001", "desc": "Information security management systems"},
            {"icon": "⚖️", "text": "SOX Compliance", "desc": "Sarbanes-Oxley financial reporting controls"}
        ]

        for item in compliance_items:
            st.markdown(f"""
                <div class="compliance-item">
                    <span style="margin-right: 1rem; font-size: 1.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">{item['icon']}</span>
                    <div>
                        <div style="font-weight: 600; font-size: 1.1rem; margin-bottom: 0.25rem; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">{item['text']}</div>
                        <div style="font-size: 0.9rem; opacity: 0.9; font-weight: 400;">{item['desc']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # Enhanced Security Architecture Section
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 3.5rem; border-radius: 24px; margin: 3rem 0; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15); position: relative; overflow: hidden; border: 1px solid #475569;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.05) 50%, transparent 70%); transform: translateX(-100%); animation: shimmer 4s infinite;"></div>
            <div style="position: relative; z-index: 1;">
                <h3 style="color: #6366f1; margin-top: 0; margin-bottom: 2rem; font-size: 2.25rem; font-weight: 700; display: flex; align-items: center; gap: 1rem; letter-spacing: -0.025em;">
                    <span style="font-size: 2.5rem;">🛡️</span>
                    <span>Security Architecture & Approach</span>
                </h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;">
                    <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 16px; backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.2);">
                        <h4 style="color: #10b981; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">🔐 Defense in Depth</h4>
                        <p style="color: #e2e8f0; line-height: 1.7; font-size: 1rem; margin: 0; font-weight: 400;">
                            Multi-layered security approach with network, application, and data protection at every level. 
                            Each layer provides independent security controls to prevent single points of failure.
                        </p>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 16px; backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.2);">
                        <h4 style="color: #3b82f6; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">🔍 Continuous Monitoring</h4>
                        <p style="color: #e2e8f0; line-height: 1.7; font-size: 1rem; margin: 0; font-weight: 400;">
                            24/7 security monitoring with real-time threat detection, automated incident response, 
                            and comprehensive logging for forensic analysis and compliance reporting.
                        </p>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 16px; backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.2);">
                        <h4 style="color: #f59e0b; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">⚡ Zero Trust Model</h4>
                        <p style="color: #e2e8f0; line-height: 1.7; font-size: 1rem; margin: 0; font-weight: 400;">
                            Never trust, always verify approach with identity verification, device validation, 
                            and continuous authentication for all access requests and data transactions.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Security Metrics and KPIs Section
    st.markdown("""
        <div style="margin: 3rem 0;">
            <h2 style="color: #1e293b; font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 2rem; font-family: 'Inter', sans-serif; letter-spacing: -0.025em;">
                📊 Security Performance Metrics
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 2rem;">
                <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 2.5rem; border-radius: 20px; text-align: center; color: white; box-shadow: 0 16px 48px rgba(16, 185, 129, 0.2); border: 1px solid rgba(255,255,255,0.15);">
                    <div style="font-size: 3rem; font-weight: 700; margin-bottom: 0.5rem;">99.99%</div>
                    <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">Uptime SLA</div>
                    <div style="font-size: 0.9rem; opacity: 0.9;">Infrastructure Availability</div>
                </div>
                <div style="background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); padding: 2.5rem; border-radius: 20px; text-align: center; color: white; box-shadow: 0 16px 48px rgba(59, 130, 246, 0.2); border: 1px solid rgba(255,255,255,0.15);">
                    <div style="font-size: 3rem; font-weight: 700; margin-bottom: 0.5rem;">< 5min</div>
                    <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">Response Time</div>
                    <div style="font-size: 0.9rem; opacity: 0.9;">Security Incident Response</div>
                </div>
                <div style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); padding: 2.5rem; border-radius: 20px; text-align: center; color: white; box-shadow: 0 16px 48px rgba(245, 158, 11, 0.2); border: 1px solid rgba(255,255,255,0.15);">
                    <div style="font-size: 3rem; font-weight: 700; margin-bottom: 0.5rem;">100%</div>
                    <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">Data Encryption</div>
                    <div style="font-size: 0.9rem; opacity: 0.9;">At Rest & In Transit</div>
                </div>
                <div style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); padding: 2.5rem; border-radius: 20px; text-align: center; color: white; box-shadow: 0 16px 48px rgba(139, 92, 246, 0.2); border: 1px solid rgba(255,255,255,0.15);">
                    <div style="font-size: 3rem; font-weight: 700; margin-bottom: 0.5rem;">0</div>
                    <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">Security Breaches</div>
                    <div style="font-size: 0.9rem; opacity: 0.9;">Zero Compromise Record</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_competitive():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    # Enhanced Professional Header with Executive Summary
    import streamlit.components.v1 as components

    header_html = """
    <div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 3.5rem; border-radius: 24px; color: white; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15); margin-bottom: 3rem; border: 1px solid #475569;">
        <h1 style="color: #6366f1; margin: 0; font-size: 2.75rem; font-weight: 700; display: flex; align-items: center; gap: 1rem; letter-spacing: -0.025em;">
            <span style="font-size: 3rem;">🏆</span>
            <span>Competitive Landscape Analysis</span>
                </h1>
        <p style="font-size: 1.3rem; margin: 1.5rem 0 0 0; opacity: 0.95; line-height: 1.7; font-weight: 400; color: #e2e8f0;">
            Strategic market positioning and competitive differentiation analysis across our comprehensive data engineering portfolio
                </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin-top: 2.5rem;">
            <div style="background: rgba(99, 102, 241, 0.2); padding: 1.5rem; border-radius: 16px; text-align: center; border: 1px solid rgba(99, 102, 241, 0.3);">
                <div style="font-size: 2.5rem; font-weight: 700; color: #6366f1; margin-bottom: 0.5rem;">6</div>
                <div style="font-size: 1rem; font-weight: 600; color: #e2e8f0;">Core Solutions</div>
            </div>
            <div style="background: rgba(16, 185, 129, 0.2); padding: 1.5rem; border-radius: 16px; text-align: center; border: 1px solid rgba(16, 185, 129, 0.3);">
                <div style="font-size: 2.5rem; font-weight: 700; color: #10b981; margin-bottom: 0.5rem;">18+</div>
                <div style="font-size: 1rem; font-weight: 600; color: #e2e8f0;">Competitors Analyzed</div>
        </div>
            <div style="background: rgba(245, 158, 11, 0.2); padding: 1.5rem; border-radius: 16px; text-align: center; border: 1px solid rgba(245, 158, 11, 0.3);">
                <div style="font-size: 2.5rem; font-weight: 700; color: #f59e0b; margin-bottom: 0.5rem;">40%</div>
                <div style="font-size: 1rem; font-weight: 600; color: #e2e8f0;">Cost Advantage</div>
            </div>
        </div>
    </div>
    """
    components.html(header_html, height=500)

    # Professional Competitive Analysis Overview
    framework_html = """
    <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); padding: 3rem; border-radius: 24px; margin: 3rem 0; box-shadow: 0 16px 48px rgba(0, 0, 0, 0.08); border: 1px solid rgba(255, 255, 255, 0.8);">
        <h2 style="color: #1e293b; font-size: 2.25rem; font-weight: 700; margin-bottom: 1.5rem; text-align: center; letter-spacing: -0.025em;">
            📊 Market Analysis Framework
        </h2>
        <p style="color: #475569; font-size: 1.2rem; line-height: 1.7; text-align: center; margin-bottom: 2.5rem; font-weight: 400;">
            Our comprehensive competitive analysis evaluates market leaders across six core data engineering domains, 
            identifying strategic opportunities and differentiation vectors for enterprise success.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;">
            <div style="background: rgba(255, 255, 255, 0.9); padding: 2rem; border-radius: 16px; border: 1px solid rgba(99, 102, 241, 0.2); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);">
                <h3 style="color: #6366f1; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                    <span>🎯</span>
                    <span>Market Positioning</span>
                </h3>
                <p style="color: #475569; line-height: 1.6; margin: 0; font-size: 1rem;">
                    Integrated platform approach vs. point solutions, offering superior cost efficiency and operational simplicity
                </p>
            </div>
            <div style="background: rgba(255, 255, 255, 0.9); padding: 2rem; border-radius: 16px; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);">
                <h3 style="color: #10b981; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                    <span>⚡</span>
                    <span>Competitive Advantages</span>
                </h3>
                <p style="color: #475569; line-height: 1.6; margin: 0; font-size: 1rem;">
                    Enterprise-grade security, GenAI integration, cloud-agnostic architecture, and modular deployment frameworks
                </p>
            </div>
            <div style="background: rgba(255, 255, 255, 0.9); padding: 2rem; border-radius: 16px; border: 1px solid rgba(245, 158, 11, 0.2); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);">
                <h3 style="color: #f59e0b; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                    <span>📈</span>
                    <span>Value Proposition</span>
                </h3>
                <p style="color: #475569; line-height: 1.6; margin: 0; font-size: 1rem;">
                    40% cost reduction, 60% faster time-to-market, and 100% compliance readiness for enterprise environments
                </p>
            </div>
        </div>
    </div>
    """
    components.html(framework_html, height=600)

    competitors = {
        "AutoOps (Self-Healing ETL)": {
            "competitors": ["Monte Carlo", "Datafold", "Acceldata"],
            "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "icon": "🤖",
            "description": "Intelligent ETL monitoring and automated issue resolution",
            "advantage": "GenAI-powered root cause analysis and self-healing capabilities"
        },
        "Document Intelligence": {
            "competitors": ["Sifflet", "Manta", "Octopai"],
            "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
            "icon": "📄",
            "description": "Automated data lineage and documentation generation",
            "advantage": "GenAI-driven metadata extraction and real-time documentation updates"
        },
        "Virtual DataLake": {
            "competitors": ["Starburst (Trino)", "Dremio", "Denodo"],
            "gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
            "icon": "🌊",
            "description": "Unified data access layer across multiple sources",
            "advantage": "GenAI-powered multi-cloud orchestration with intelligent query optimization"
        },
        "Synthetic Data Generator": {
            "competitors": ["Mostly AI", "Gretel.ai", "Tonic.ai"],
            "gradient": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
            "icon": "🎲",
            "description": "Privacy-preserving synthetic data generation",
            "advantage": "GenAI-enhanced privacy controls with regulatory compliance"
        },
        "DQM & ETL Testing": {
            "competitors": ["Great Expectations", "Soda", "Deequ"],
            "gradient": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
            "icon": "✅",
            "description": "Comprehensive data quality management and testing",
            "advantage": "GenAI-powered testing framework with automated validation workflows"
        },
        "Deployment Framework": {
            "competitors": ["Terraform", "Pulumi", "dbt Cloud", "Astronomer"],
            "gradient": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
            "icon": "🚀",
            "description": "Unified deployment and orchestration platform",
            "advantage": "GenAI-integrated multi-orchestrator support with enterprise security"
        }
    }

    # Enhanced Competitive Analysis Grid
    competitive_cards_html = """
        <style>
        .competitive-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
        margin: 3rem 0;
        padding: 2rem 0;
        }

        .competitive-card {
        padding: 2.5rem;
        border-radius: 24px;
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.25);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
            position: relative;
            overflow: hidden;
        backdrop-filter: blur(15px);
        min-height: 350px;
        }

        .competitive-card:hover {
        transform: translateY(-12px) scale(1.03);
        box-shadow: 0 24px 64px rgba(0, 0, 0, 0.18);
        }

        .competitive-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
            transform: translateX(-100%);
            transition: transform 0.8s ease;
        }

        .competitive-card:hover::before {
            transform: translateX(100%);
        }

        .project-title {
            color: #1a202c;
        font-size: 1.75rem;
        font-weight: 800;
        margin-bottom: 2rem;
            display: flex;
            align-items: center;
        gap: 1rem;
            position: relative;
            z-index: 1;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        background: rgba(255, 255, 255, 0.95);
        padding: 1.5rem;
        border-radius: 16px;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        letter-spacing: -0.025em;
    }

    .project-title span {
        color: #0f172a !important;
    }

    .project-description {
        color: #1a202c;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
        line-height: 1.6;
            background: rgba(255, 255, 255, 0.9);
        padding: 1rem 1.5rem;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        position: relative;
        z-index: 1;
    }

    .competitive-advantage {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        padding: 1.25rem 1.75rem;
        border-radius: 16px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        position: relative;
        z-index: 1;
        box-shadow: 0 8px 24px rgba(5, 150, 105, 0.3);
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
        letter-spacing: -0.01em;
        backdrop-filter: blur(10px);
    }

    .competitive-advantage strong {
        color: #ffffff;
        font-weight: 800;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        margin-right: 0.5rem;
        }

        .competitors-container {
            position: relative;
            z-index: 1;
        }

    .competitors-header {
        color: #1a202c;
        font-weight: 700;
        font-size: 1.1rem;
        background: rgba(255, 255, 255, 0.95);
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        display: inline-block;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }

        .competitors-tags-wrapper {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        align-items: center;
        justify-content: flex-start;
        min-height: 3rem;
        }

        .competitor-tag {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: rgba(255, 255, 255, 0.98);
            color: #1a202c;
        padding: 0.65rem 1.25rem;
        border-radius: 20px;
            margin: 0;
            font-weight: 700;
            font-size: 0.9rem;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
            transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.6);
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
            white-space: nowrap;
        flex-shrink: 1;
        letter-spacing: -0.01em;
        height: 2.25rem;
        line-height: 1;
        min-width: 0;
        max-width: calc(33.33% - 0.34rem);
    }

    .competitor-tag:hover {
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        background: rgba(255, 255, 255, 1);
        }
        </style>
    """

    # Create enhanced competitive cards
    competitive_html = competitive_cards_html + '<div class="competitive-grid">'

    for project_name, project_data in competitors.items():
        gradient = project_data["gradient"]
        competitors_list = project_data["competitors"]
        icon = project_data["icon"]
        description = project_data["description"]
        advantage = project_data["advantage"]

        competitive_html += f"""
            <div class="competitive-card" style="background: {gradient};">
                <div class="project-title">
                    <span style="font-size: 2rem; color: #0f172a !important;">{icon}</span>
                    <span style="color: #0f172a !important;">{project_name}</span>
                </div>
                <div class="project-description">
                    {description}
                </div>
                <div class="competitive-advantage">
                    <strong>🏆 Key Advantage:</strong> {advantage}
                </div>
                <div class="competitors-container">
                    <div class="competitors-header">Key Competitors:</div>
                    <div class="competitors-tags-wrapper">
        """

        for competitor in competitors_list:
            competitive_html += f'<span class="competitor-tag">{competitor}</span>'

        competitive_html += '</div></div></div>'

    competitive_html += '</div>'

    components.html(competitive_html, height=1800)

    # Enhanced Market Positioning & Strategic Advantages Section
    positioning_html = """
    <div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 3.5rem; border-radius: 24px; color: white; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15); margin-top: 4rem; border: 1px solid #475569;">
        <h3 style="color: #6366f1; margin-top: 0; margin-bottom: 2rem; font-size: 2.25rem; font-weight: 700; display: flex; align-items: center; gap: 1rem; letter-spacing: -0.025em;">
            <span style="font-size: 2.5rem;">🎯</span>
            <span>Strategic Market Positioning</span>
                </h3>
        <p style="line-height: 1.8; font-size: 1.2rem; color: #e2e8f0; margin-bottom: 2.5rem; font-weight: 400;">
            Our integrated platform approach delivers superior value through unified data engineering capabilities, 
            offering significant cost advantages, operational efficiency, and enterprise-grade security compared to 
            fragmented point solutions in the market.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;">
            <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.2);">
                <h4 style="color: #10b981; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">💰 Cost Efficiency</h4>
                <p style="color: #e2e8f0; line-height: 1.7; font-size: 1rem; margin: 0; font-weight: 400;">
                    40% reduction in total cost of ownership through unified platform licensing, 
                    reduced infrastructure complexity, and streamlined operational overhead.
                </p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.2);">
                <h4 style="color: #3b82f6; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">⚡ Time-to-Market</h4>
                <p style="color: #e2e8f0; line-height: 1.7; font-size: 1rem; margin: 0; font-weight: 400;">
                    60% faster deployment and integration through pre-built connectors, 
                    modular architecture, and automated provisioning capabilities.
                </p>
        </div>
            <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.2);">
                <h4 style="color: #f59e0b; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">🛡️ Enterprise Security</h4>
                <p style="color: #e2e8f0; line-height: 1.7; font-size: 1rem; margin: 0; font-weight: 400;">
                    100% compliance readiness with built-in security controls, audit logging, 
                    and regulatory adherence across all platform components.
                </p>
            </div>
        </div>
    </div>
    """
    components.html(positioning_html, height=600)

    # Competitive Analysis Summary Section
    summary_html = """
    <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); padding: 3rem; border-radius: 24px; margin: 3rem 0; box-shadow: 0 16px 48px rgba(0, 0, 0, 0.08); border: 1px solid rgba(255, 255, 255, 0.8);">
        <h2 style="color: #1e293b; font-size: 2.25rem; font-weight: 700; margin-bottom: 1.5rem; text-align: center; letter-spacing: -0.025em;">
            📋 Competitive Analysis Summary
        </h2>
        <p style="color: #475569; font-size: 1.2rem; line-height: 1.7; text-align: center; margin-bottom: 2.5rem; font-weight: 400;">
            Our comprehensive analysis reveals significant opportunities for market disruption through integrated platform capabilities
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 2rem;">
            <div style="background: rgba(255, 255, 255, 0.9); padding: 2rem; border-radius: 16px; border: 1px solid rgba(99, 102, 241, 0.2); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06); text-align: center;">
                <div style="font-size: 3rem; font-weight: 700; color: #6366f1; margin-bottom: 1rem;">6</div>
                <h3 style="color: #1e293b; font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">Market Segments</h3>
                <p style="color: #475569; font-size: 1rem; margin: 0;">Core data engineering domains with high growth potential</p>
            </div>
            <div style="background: rgba(255, 255, 255, 0.9); padding: 2rem; border-radius: 16px; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06); text-align: center;">
                <div style="font-size: 3rem; font-weight: 700; color: #10b981; margin-bottom: 1rem;">18+</div>
                <h3 style="color: #1e293b; font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">Competitors Analyzed</h3>
                <p style="color: #475569; font-size: 1rem; margin: 0;">Leading vendors across all solution categories</p>
            </div>
            <div style="background: rgba(255, 255, 255, 0.9); padding: 2rem; border-radius: 16px; border: 1px solid rgba(245, 158, 11, 0.2); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06); text-align: center;">
                <div style="font-size: 3rem; font-weight: 700; color: #f59e0b; margin-bottom: 1rem;">$2.5B</div>
                <h3 style="color: #1e293b; font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">Market Opportunity</h3>
                <p style="color: #475569; font-size: 1rem; margin: 0;">Total addressable market across all segments</p>
            </div>
            <div style="background: rgba(255, 255, 255, 0.9); padding: 2rem; border-radius: 16px; border: 1px solid rgba(139, 92, 246, 0.2); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06); text-align: center;">
                <div style="font-size: 3rem; font-weight: 700; color: #8b5cf6; margin-bottom: 1rem;">40%</div>
                <h3 style="color: #1e293b; font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">Cost Advantage</h3>
                <p style="color: #475569; font-size: 1rem; margin: 0;">Reduction vs. point solution alternatives</p>
            </div>
        </div>
    </div>
    """
    components.html(summary_html, height=500)

    st.markdown('</div>', unsafe_allow_html=True)


def render_next_steps():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">Next Steps for Technical Team</h1>', unsafe_allow_html=True)

    # Add hover effects CSS
    st.markdown("""
        <style>
        .next-steps-list {
            padding: 2rem;
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            margin: 2rem 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .next-steps-list ol {
            margin: 0;
            padding-left: 2rem;
        }

        .next-steps-list li {
            margin-bottom: 1rem;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            transition: all 0.3s ease;
            font-size: 1.1rem;
            font-weight: 500;
            color: #1a202c;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            cursor: pointer;
        }

        .next-steps-list li:hover {
            transform: translateY(-4px) scale(1.02);
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
            border: 1px solid rgba(99, 102, 241, 0.3);
        }

                .timeline-section {
            margin-top: 3rem;
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
            border: 1px solid #475569;
            position: relative;
            overflow: hidden;
        }

        .timeline-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.05) 50%, transparent 70%);
            transform: translateX(-100%);
            animation: shimmer 4s infinite;
        }

        .timeline-header {
            font-size: 2rem;
            font-weight: 700;
            color: #6366f1;
            margin-bottom: 2.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            position: relative;
            z-index: 1;
        }

        .timeline {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            position: relative;
            z-index: 1;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 2rem;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(180deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%);
            border-radius: 2px;
        }

        .timeline-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 16px;
            color: white;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            position: relative;
            margin-left: 4rem;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            left: -3.5rem;
            top: 2rem;
            width: 1rem;
            height: 1rem;
            background: #6366f1;
            border-radius: 50%;
            border: 3px solid #1e293b;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.3);
        }

        .timeline-item:hover {
            transform: translateX(8px) translateY(-4px);
            background: rgba(255, 255, 255, 0.15);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(99, 102, 241, 0.3);
        }

        .timeline-item:hover::before {
            background: #8b5cf6;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.3);
        }

        .timeline-date {
            font-weight: 700;
            font-size: 1.1rem;
            margin-bottom: 0.8rem;
            color: #fbbf24;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .timeline-date::before {
            content: '📅';
            font-size: 1rem;
        }

        .timeline-content {
            font-weight: 500;
            line-height: 1.6;
            font-size: 1.05rem;
            opacity: 0.95;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="next-steps-list">', unsafe_allow_html=True)

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

    st.markdown("""
        <div class="timeline-section">
            <h3 class="timeline-header">
                <span>📅</span>
                <span>Proposed Timeline</span>
            </h3>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-date">Sept 1-15, 2025</div>
            <div class="timeline-content">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="background: #10b981; color: white; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Phase 1</span>
                    <span style="background: rgba(16, 185, 129, 0.2); color: #10b981; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Foundation</span>
                </div>
                Planning & Requirements Gathering
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">Sept 15 - Oct 15, 2025</div>
            <div class="timeline-content">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="background: #3b82f6; color: white; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Phase 2</span>
                    <span style="background: rgba(59, 130, 246, 0.2); color: #3b82f6; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Core Development</span>
                </div>
                AutoOps MVP Development
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">Sept 15 - Oct 1, 2025</div>
            <div class="timeline-content">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="background: #8b5cf6; color: white; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Phase 2</span>
                    <span style="background: rgba(139, 92, 246, 0.2); color: #8b5cf6; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Quick Win</span>
                </div>
                Document Intelligence POC
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">Oct 1 - Nov 15, 2025</div>
            <div class="timeline-content">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="background: #f59e0b; color: white; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Phase 3</span>
                    <span style="background: rgba(245, 158, 11, 0.2); color: #f59e0b; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Integration</span>
                </div>
                Connector Development
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">Oct 15 - Dec 1, 2025</div>
            <div class="timeline-content">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="background: #ef4444; color: white; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Phase 4</span>
                    <span style="background: rgba(239, 68, 68, 0.2); color: #ef4444; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">Deployment</span>
                </div>
                CI/CD Pipeline Implementation
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# Top brand bar
st.markdown("""
    <style>
    .top-nav {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid #334155;
        padding: 0.75rem 1rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }

    .sticky-tabs {
        position: fixed;
        top: 60px;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid #334155;
        padding: 0.5rem 1rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }

    .content-wrapper {
        padding-top: 140px;
    }
    </style>

    <div class="top-nav">
        <div class="content-container" style="display:flex; align-items:center; justify-content:center; gap:.75rem;">
            <span style="font-size:1.5rem;">🚀</span>
            <span class="brand-title" style="font-weight:700; letter-spacing:.3px; color:#cbd5e1;">Technical Vision Deck</span>
        </div>
    </div>

    <div class="sticky-tabs">
""", unsafe_allow_html=True)

# Enhanced top navigation tabs
st.markdown("""
    <style>
    /* Sticky navigation */
    .top-nav {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        z-index: 1000 !important;
        background: rgba(15, 23, 42, 0.95) !important;
        backdrop-filter: blur(12px) !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        position: fixed !important;
        top: 60px !important;
        left: 0 !important;
        right: 0 !important;
        z-index: 999 !important;
        gap: 0.5rem;
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 1rem;
        border-radius: 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        border: 1px solid #475569;
        margin: 0;
        backdrop-filter: blur(12px);
    }

    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 140px !important;
    }

    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin: 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        font-weight: 600;
        font-size: 1rem;
        color: #e2e8f0;
        min-width: 140px;
        text-align: center;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(99, 102, 241, 0.3);
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.3);
        transform: translateY(-2px);
    }

    .stTabs [aria-selected="true"]:hover {
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
        transform: translateY(-3px);
        box-shadow: 0 12px 32px rgba(99, 102, 241, 0.4);
    }

    /* Tab content area styling */
    .stTabs [data-baseweb="tab-panel"] {
        padding: 2rem 0;
    }

    /* Responsive design for smaller screens */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab"] {
            min-width: 120px;
            padding: 0.8rem 1rem;
            font-size: 0.9rem;
        }

        .stTabs [data-baseweb="tab-list"] {
            padding: 0.8rem;
            gap: 0.3rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

tab_labels = [
    "🚀 Introduction",
    "🏗️ Architecture Goals",
    "💼 Projects",
    "🛡️ Security & Compliance",
    "🏆 Competitive Landscape",
    "📋 Next Steps"
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
        <p>© 2025 Technical Vision Presentation By Umesh Rathod | For Stakeholder Review</p>
        <p>Confidential & Proprietary</p>
    </div>
""", unsafe_allow_html=True)

# Replace light gray text with darker, more readable colors
import re

# Read the file content
with open('app.py', 'r', encoding='utf-8') as file:
    content = file.read()

# Replace light gray text with darker colors
content = re.sub(r'color: #6b7280; margin-bottom: 0\.3rem;">Tech Stack',
                 'color: #374151; margin-bottom: 0.3rem; font-weight: 600;">Tech Stack', content)
content = re.sub(r'color: #6b7280; margin-bottom: 0\.3rem;">Deployment',
                 'color: #374151; margin-bottom: 0.3rem; font-weight: 600;">Deployment', content)
content = re.sub(r'font-weight: 600;">{card\[\'stack\'\]}',
                 'font-weight: 600; color: #0f172a; font-size: 0.95rem;">{card[\'stack\']}', content)
content = re.sub(r'font-weight: 600;">{card\[\'deploy\'\]}',
                 'font-weight: 600; color: #0f172a; font-size: 0.95rem;">{card[\'deploy\']}', content)

# Write the updated content back
with open('app.py', 'w', encoding='utf-8') as file:
    file.write(content)