import streamlit as st
from config import (
    EXPERIENCE_LEVELS, BULLET_STYLES, REWRITE_OPTIONS,
    BULLET_COUNT_OPTIONS, DEFAULT_BULLET_COUNT,
    BULLET_LENGTH_OPTIONS, DEFAULT_BULLET_LENGTH,
    EXAMPLE_INPUTS
)
from validators import validate_description, validate_tech_stack, validate_target_role, is_input_too_verbose
from ai_client import generate_bullets, rewrite_bullet


def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .stApp { background: linear-gradient(180deg, #0a0a1a 0%, #12122a 100%); }
    * { font-family: 'Inter', -apple-system, sans-serif; }
    #MainMenu, footer { visibility: hidden; }
    .stDeployButton { display: none; }
    
    /* Keep sidebar toggle button visible */
    header[data-testid="stHeader"] { background: transparent !important; }
    button[kind="header"] { visibility: visible !important; }
    [data-testid="collapsedControl"] { visibility: visible !important; display: flex !important; }
    
    /* Minimize top padding */
    .main .block-container { 
        padding: 0 2rem 2rem 2rem !important; 
        max-width: 950px; 
    }
    
    /* Remove empty elements */
    .main .block-container > div:first-child { margin-top: 0 !important; padding-top: 0 !important; }
    div[data-testid="stVerticalBlock"] > div:empty { display: none !important; }
    div[data-testid="stVerticalBlock"] > div:has(> div:empty):not(:has(*:not(:empty))) { display: none !important; }
    .element-container:has(> div:empty) { display: none !important; margin: 0 !important; padding: 0 !important; }
    .stMarkdown:empty { display: none !important; }
    .element-container:empty { display: none !important; }
    
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f25 0%, #1a1a3a 100%);
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    section[data-testid="stSidebar"] > div:first-child { padding-top: 1rem; }
    
    .main-header { text-align: center; padding: 0.5rem 0; margin: 0; }
    .main-title {
        font-size: 1.8rem; font-weight: 700;
        background: linear-gradient(135deg, #a78bfa 0%, #818cf8 50%, #6366f1 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin: 0; letter-spacing: -0.01em;
    }
    .main-subtitle { color: rgba(255,255,255,0.5); font-size: 0.85rem; margin-top: 0.25rem; }
    
    .section-label {
        color: rgba(255,255,255,0.9); font-weight: 600; font-size: 0.9rem;
        margin: 0.5rem 0; display: flex; align-items: center; gap: 0.4rem;
    }
    
    .stTextArea textarea, .stTextInput input {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 8px !important; color: white !important;
        font-size: 0.875rem !important; padding: 0.6rem !important;
    }
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: rgba(129,140,248,0.5) !important;
        box-shadow: 0 0 0 2px rgba(129,140,248,0.1) !important;
    }
    .stTextArea textarea::placeholder, .stTextInput input::placeholder { color: rgba(255,255,255,0.3) !important; }
    
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 8px !important;
    }
    
    .stButton > button {
        border-radius: 8px !important; font-weight: 500 !important;
        font-size: 0.875rem !important; padding: 0.5rem 1rem !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        border: none !important; color: white !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(99,102,241,0.4) !important;
    }
    .stButton > button[kind="secondary"] {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: rgba(255,255,255,0.8) !important;
    }
    
    .bullet-item {
        background: rgba(99,102,241,0.05);
        border: 1px solid rgba(99,102,241,0.15);
        border-radius: 8px; padding: 0.75rem 1rem; margin-bottom: 0.4rem;
        display: flex; align-items: flex-start; gap: 0.6rem;
    }
    .bullet-item:hover { border-color: rgba(99,102,241,0.3); background: rgba(99,102,241,0.08); }
    .bullet-item.selected { border-color: #818cf8; background: rgba(99,102,241,0.12); }
    .bullet-num {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white; font-size: 0.65rem; font-weight: 600;
        width: 18px; height: 18px; border-radius: 5px;
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0; margin-top: 2px;
    }
    .bullet-text { color: rgba(255,255,255,0.9); font-size: 0.875rem; line-height: 1.5; flex: 1; }
    
    .stTextArea label, .stTextInput label, .stSelectbox label, .stRadio label {
        color: rgba(255,255,255,0.7) !important; font-weight: 500 !important; font-size: 0.8rem !important;
    }
    .stRadio > div { gap: 0.4rem !important; }
    .stAlert { border-radius: 8px !important; padding: 0.6rem 0.8rem !important; }
    hr { border: none; height: 1px; background: rgba(255,255,255,0.06); margin: 0.75rem 0; }
    
    .rewrite-panel {
        background: rgba(168,85,247,0.05);
        border: 1px solid rgba(168,85,247,0.2);
        border-radius: 8px; padding: 0.75rem; margin-top: 0.5rem;
    }
    .pill {
        display: inline-block; background: rgba(99,102,241,0.1);
        border: 1px solid rgba(99,102,241,0.2); color: #a5b4fc;
        font-size: 0.7rem; padding: 0.2rem 0.4rem;
        border-radius: 4px; margin-top: 0.25rem;
    }
    .footer-text { 
        text-align: center; color: rgba(255,255,255,0.25); 
        font-size: 0.75rem; padding: 1rem 0 0.5rem 0; 
    }
    </style>
    """, unsafe_allow_html=True)


def init_session_state():
    defaults = {
        "bullets": [], "error": "", "warning": "",
        "selected_bullet_index": None, "description": "",
        "tech_stack": "", "target_role": "",
        "experience_level": "Intermediate", "bullet_style": "ATS Optimized",
        "bullet_count": DEFAULT_BULLET_COUNT, "bullet_length": DEFAULT_BULLET_LENGTH
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_app():
    st.session_state.bullets = []
    st.session_state.error = ""
    st.session_state.warning = ""
    st.session_state.selected_bullet_index = None


def load_example(example: dict):
    st.session_state.description = example["description"]
    st.session_state.tech_stack = example["tech_stack"]
    st.session_state.target_role = example["target_role"]
    st.session_state.experience_level = example["experience_level"]
    st.session_state.bullets = []
    st.session_state.error = ""


def format_bullets_for_copy(bullets: list[str]) -> str:
    return "\n".join([f"* {b}" for b in bullets])


def render_sidebar():
    with st.sidebar:
        st.markdown("### Settings")
        
        st.session_state.bullet_count = st.select_slider(
            "Number of bullets", options=BULLET_COUNT_OPTIONS,
            value=st.session_state.bullet_count
        )
        
        st.session_state.bullet_length = st.selectbox(
            "Bullet length", options=list(BULLET_LENGTH_OPTIONS.keys()),
            index=list(BULLET_LENGTH_OPTIONS.keys()).index(st.session_state.bullet_length)
        )
        
        st.divider()
        st.markdown("### Examples")
        
        for i, example in enumerate(EXAMPLE_INPUTS):
            if st.button(example["name"], key=f"ex_{i}", use_container_width=True):
                load_example(example)
                st.rerun()
        
        st.divider()
        st.caption("**Tip:** Be specific about YOUR contributions and include technologies used.")


def main():
    st.set_page_config(
        page_title="Resume Bullet Enhancer", 
        page_icon="*",
        layout="centered", 
        initial_sidebar_state="expanded"
    )
    
    inject_custom_css()
    init_session_state()
    render_sidebar()
    
    st.markdown("""
    <div class="main-header">
        <div class="main-title">Resume Bullet Enhancer</div>
        <div class="main-subtitle">Transform descriptions into polished, ATS-friendly resume bullets</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-label">Describe Your Work</div>', unsafe_allow_html=True)
    
    description = st.text_area(
        "desc", value=st.session_state.description,
        placeholder="I built REST APIs for checkout, fixed payment bugs, wrote tests using Python and PostgreSQL...",
        height=90, key="desc_input", label_visibility="collapsed"
    )
    st.session_state.description = description
    
    if description and is_input_too_verbose(description):
        st.warning("Description is long. Consider focusing on key achievements.")
    
    col1, col2 = st.columns(2)
    with col1:
        tech = st.text_input("Tech Stack", value=st.session_state.tech_stack, 
                            placeholder="Python, Flask, PostgreSQL", key="tech_input")
        st.session_state.tech_stack = tech
    with col2:
        role = st.text_input("Target Role", value=st.session_state.target_role, 
                            placeholder="Backend Engineer", key="role_input")
        st.session_state.target_role = role
    
    col3, col4 = st.columns(2)
    with col3:
        exp = st.selectbox("Experience Level", options=EXPERIENCE_LEVELS,
            index=EXPERIENCE_LEVELS.index(st.session_state.experience_level), key="exp_input")
        st.session_state.experience_level = exp
    with col4:
        style = st.selectbox("Bullet Style", options=list(BULLET_STYLES.keys()),
            index=list(BULLET_STYLES.keys()).index(st.session_state.bullet_style), key="style_input")
        st.session_state.bullet_style = style
    
    st.markdown(f'<span class="pill">{BULLET_STYLES[style]}</span>', unsafe_allow_html=True)
    
    col_gen, col_reset = st.columns([6, 1])
    with col_gen:
        generate_clicked = st.button("Generate Bullets", type="primary", use_container_width=True)
    with col_reset:
        if st.button("Reset", use_container_width=True):
            reset_app()
            st.rerun()
    
    if generate_clicked:
        st.session_state.error = ""
        st.session_state.warning = ""
        st.session_state.selected_bullet_index = None
        
        is_valid, error_msg = validate_description(description)
        if not is_valid:
            st.session_state.error = error_msg
            st.session_state.bullets = []
        else:
            clean_tech = validate_tech_stack(tech)
            clean_role = validate_target_role(role)
            
            with st.spinner("Generating..."):
                bullets, gen_error = generate_bullets(
                    description=description, tech_stack=clean_tech,
                    experience_level=exp, target_role=clean_role,
                    bullet_style=style, bullet_count=st.session_state.bullet_count,
                    bullet_length=st.session_state.bullet_length
                )
            
            if gen_error and not bullets:
                st.session_state.error = gen_error
                st.session_state.bullets = []
            else:
                st.session_state.bullets = bullets
                if gen_error:
                    st.session_state.warning = gen_error
    
    if st.session_state.error:
        st.error(st.session_state.error)
    if st.session_state.warning:
        st.warning(st.session_state.warning)
    
    # Results
    if st.session_state.bullets:
        st.divider()
        st.markdown('<div class="section-label">Generated Bullets</div>', unsafe_allow_html=True)
        
        for i, bullet in enumerate(st.session_state.bullets):
            is_selected = st.session_state.selected_bullet_index == i
            selected_class = "selected" if is_selected else ""
            
            col_b, col_s = st.columns([12, 1])
            with col_b:
                st.markdown(f'<div class="bullet-item {selected_class}"><span class="bullet-num">{i+1}</span><span class="bullet-text">{bullet}</span></div>', unsafe_allow_html=True)
            with col_s:
                if st.button("Edit", key=f"sel_{i}"):
                    st.session_state.selected_bullet_index = i if st.session_state.selected_bullet_index != i else None
                    st.rerun()
        
        if st.session_state.selected_bullet_index is not None:
            idx = st.session_state.selected_bullet_index
            st.markdown('<div class="rewrite-panel">', unsafe_allow_html=True)
            st.markdown(f"**Editing Bullet {idx + 1}**")
            
            rewrite_style = st.radio("Style:", options=list(REWRITE_OPTIONS.keys()), 
                                    horizontal=True, label_visibility="collapsed")
            
            col_rw, col_cn = st.columns([4, 1])
            with col_rw:
                if st.button("Apply Rewrite", type="primary", use_container_width=True):
                    with st.spinner("Rewriting..."):
                        rewritten, err = rewrite_bullet(st.session_state.bullets[idx], rewrite_style)
                    if err:
                        st.error(err)
                    else:
                        st.session_state.bullets[idx] = rewritten
                        st.session_state.selected_bullet_index = None
                        st.rerun()
            with col_cn:
                if st.button("Cancel", use_container_width=True):
                    st.session_state.selected_bullet_index = None
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        
        with st.expander("Copy Bullets"):
            st.code(format_bullets_for_copy(st.session_state.bullets), language=None)
    
    st.markdown('<p class="footer-text">Built for students who want their resume to stand out</p>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
