import streamlit as st
from config import *
from ai_client import get_ai_service

st.set_page_config(
    page_title=APP_TITLE, 
    page_icon="*", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

def inject_custom_css(is_dark_theme: bool):
    if is_dark_theme:
        bg_main = "#0F1117"
        bg_card = "rgba(30, 41, 59, 0.8)"
        text_primary = "#F8FAFC"
        text_secondary = "#94A3B8"
        text_placeholder = "#64748B"
        border_color = "rgba(255, 255, 255, 0.1)"
        input_bg = "rgba(15, 23, 42, 0.8)"
        sidebar_bg = "rgba(15, 23, 42, 0.95)"
        dropdown_bg = "#1E293B"
        dropdown_hover = "rgba(99, 102, 241, 0.4)"
        dropdown_hover_text = "#FFFFFF"
        toggle_btn_bg = "rgba(255, 255, 255, 0.1)"
        toggle_btn_border = "rgba(255, 255, 255, 0.2)"
        toggle_btn_text = "#F8FAFC"
        gradient_bg = """
            radial-gradient(at 0% 0%, rgba(99,102,241,0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(168,85,247,0.15) 0px, transparent 50%)
        """
        select_text = "#F8FAFC"
        select_bg = "rgba(30, 41, 59, 0.9)"
    else:
        bg_main = "#F1F5F9"
        bg_card = "rgba(255, 255, 255, 0.95)"
        text_primary = "#1E293B"
        text_secondary = "#475569"
        text_placeholder = "#94A3B8"
        border_color = "rgba(0, 0, 0, 0.15)"
        input_bg = "#FFFFFF"
        sidebar_bg = "#FFFFFF"
        dropdown_bg = "#FFFFFF"
        dropdown_hover = "rgba(99, 102, 241, 0.2)"
        dropdown_hover_text = "#1E293B"
        toggle_btn_bg = "#6366F1"
        toggle_btn_border = "#6366F1"
        toggle_btn_text = "#FFFFFF"
        gradient_bg = """
            radial-gradient(at 0% 0%, rgba(99,102,241,0.08) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(168,85,247,0.08) 0px, transparent 50%)
        """
        select_text = "#1E293B"
        select_bg = "#FFFFFF"

    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');
        
        @keyframes slideUpFade {{
            0% {{ opacity: 0; transform: translateY(20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}

        :root {{
            --primary: #6366F1;
            --bg-main: {bg_main};
            --bg-card: {bg_card};
            --text-primary: {text_primary};
            --text-secondary: {text_secondary};
            --text-placeholder: {text_placeholder};
            --border-color: {border_color};
            --input-bg: {input_bg};
            --sidebar-bg: {sidebar_bg};
            --select-text: {select_text};
            --select-bg: {select_bg};
            --dropdown-bg: {dropdown_bg};
            --dropdown-hover: {dropdown_hover};
            --dropdown-hover-text: {dropdown_hover_text};
            --toggle-btn-bg: {toggle_btn_bg};
            --toggle-btn-border: {toggle_btn_border};
            --toggle-btn-text: {toggle_btn_text};
        }}

        .stApp {{ 
            background-color: var(--bg-main) !important;
            background-image: {gradient_bg};
            background-attachment: fixed;
        }}
        
        /* Text styling */
        .stApp p, .stApp span, .stApp div {{
            color: var(--text-primary);
        }}
        
        /* Font family - exclude icon fonts */
        .stApp .stMarkdown, .stApp .stTextInput, .stApp .stTextArea, 
        .stApp .stSelectbox, .stApp .stButton {{
            font-family: 'Inter', sans-serif !important;
        }}
        
        .block-container {{ padding-top: 1.5rem !important; padding-bottom: 3rem !important; }}
        div[data-testid="stVerticalBlock"] {{ gap: 0.6rem; }}

        /* SIDEBAR TOGGLE - Let Streamlit handle icons */
        header[data-testid="stHeader"] {{ 
            background: transparent !important; 
        }}
        
        /* Sidebar styling */
        section[data-testid="stSidebar"] {{
            background: var(--sidebar-bg) !important;
            border-right: 1px solid var(--border-color);
        }}
        section[data-testid="stSidebar"] .stMarkdown,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label {{
            color: var(--text-primary) !important;
        }}
        section[data-testid="stSidebar"] .stCaption {{
            color: var(--text-secondary) !important;
        }}

        .main-header {{
            text-align: center;
            padding: 0.5rem 0 1.5rem 0;
            animation: slideUpFade 0.8s ease-out;
        }}
        .main-header h1 {{
            background: linear-gradient(to right, #818CF8, #C084FC, #F472B6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
        }}
        .main-header p {{ 
            color: var(--text-secondary) !important; 
            font-size: 1.1rem; 
            margin-top: 0.5rem;
            letter-spacing: 0.02em;
        }}

        /* Input fields with full theme support */
        .stTextInput input, .stTextArea textarea {{
            background-color: var(--input-bg) !important;
            border: 1px solid var(--border-color) !important;

            border-radius: 10px !important;
            color: var(--text-primary) !important;
            transition: all 0.2s ease;
        }}
        
        /* Placeholder text */
        .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
            color: var(--text-placeholder) !important;
            opacity: 1 !important;
        }}
        
        .stTextInput input:focus, .stTextArea textarea:focus {{
            border-color: var(--primary) !important;
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.2) !important;
        }}
        
        /* Selectbox styling */
        .stSelectbox div[data-baseweb="select"] {{
            background-color: var(--select-bg) !important;
        }}
        .stSelectbox div[data-baseweb="select"] > div {{
            background-color: var(--select-bg) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 10px !important;
            color: var(--select-text) !important;
        }}
        .stSelectbox svg {{
            fill: var(--text-primary) !important;
        }}
        
        /* Dropdown menu */
        div[data-baseweb="popover"] {{
            background-color: var(--bg-card) !important;
        }}
        div[data-baseweb="popover"] li {{
            color: var(--text-primary) !important;
        }}
        div[data-baseweb="popover"] li:hover {{
            background-color: var(--primary) !important;
        }}
        
        /* Labels */
        .stTextInput label, .stTextArea label, .stSelectbox label {{
            color: var(--text-secondary) !important;
            font-weight: 500 !important;
        }}
        
        /* Slider */
        .stSlider label, .stSlider p {{
            color: var(--text-primary) !important;
        }}

        /* Buttons - All buttons including form buttons */
        button[kind="primary"], 
        button[data-testid="stFormSubmitButton"],
        .stFormSubmitButton button {{
            background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%) !important;
            border: none !important;
            transition: transform 0.2s !important;
            font-weight: 600 !important;
            color: white !important;
        }}
        button[kind="primary"]:hover, 
        .stFormSubmitButton button:hover {{ 
            transform: translateY(-2px); 
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4); 
        }}
        
        button[kind="secondary"] {{
            background: var(--bg-card) !important;
            border: 1px solid var(--border-color) !important;
            color: #EF4444 !important;
        }}
        button[kind="secondary"]:hover {{ 
            border-color: #EF4444 !important; 
        }}
        
        /* All other buttons (Edit, Example buttons) */
        .stButton button {{
            background: var(--bg-card) !important;
            border: 1px solid var(--border-color) !important;
            color: var(--text-primary) !important;
        }}
        .stButton button:hover {{
            border-color: var(--primary) !important;
            background: var(--input-bg) !important;
        }}

        /* Bullet cards and edit button row */
        .bullet-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.25rem;
            animation: slideUpFade 0.6s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
            opacity: 0;
            margin-bottom: 0.75rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .bullet-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            border-color: var(--primary);
        }}
        .bullet-content {{
            color: var(--text-primary) !important;
            font-size: 1rem;
            line-height: 1.6;
            font-weight: 500;
        }}
        
        /* Edit button in column - vertically centered */
        div[data-testid="stHorizontalBlock"]:has(.bullet-card) {{
            align-items: center !important;
        }}
        div[data-testid="stHorizontalBlock"]:has(.bullet-card) .stButton button {{
            background: rgba(99, 102, 241, 0.1) !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.5rem !important;
            font-size: 1.1rem !important;
            color: var(--primary) !important;
            opacity: 0.7;
            transition: all 0.2s ease !important;
            min-height: auto !important;
            width: 100% !important;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        div[data-testid="stHorizontalBlock"]:has(.bullet-card) .stButton button:hover {{
            opacity: 1;
            background: rgba(99, 102, 241, 0.2) !important;
            transform: scale(1.05);
        }}
        
        /* Form Container Styling */
        .form-container {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
        }}
        
        /* Copy textarea */
        .stTextArea[data-testid="stTextArea"] textarea {{
            background-color: var(--input-bg) !important;
            color: var(--text-primary) !important;
        }}

        
        /* Caption */
        .stCaption, small {{
            color: var(--text-secondary) !important;
        }}
        
        /* Markdown headers in main area */
        .stMarkdown h3, .stMarkdown h4 {{
            color: var(--text-primary) !important;
        }}
        
        /* Dialog/Modal styling */
        div[data-testid="stModal"], 
        div[role="dialog"] {{
            background-color: var(--bg-card) !important;
        }}
        div[data-testid="stModal"] .stMarkdown,
        div[role="dialog"] .stMarkdown {{
            color: var(--text-primary) !important;
        }}
        div[data-testid="stModal"] p,
        div[role="dialog"] p {{
            color: var(--text-primary) !important;
        }}
        
        /* Dialog backdrop */
        div[data-testid="stModal"]::before {{
            background-color: rgba(0, 0, 0, 0.5) !important;
        }}
        
        /* Dropdown/Select Menu popover - comprehensive styling */
        div[data-baseweb="popover"],
        ul[role="listbox"],
        div[data-baseweb="menu"],
        div[data-baseweb="select"] ul,
        div[data-baseweb="popover"] > div {{
            background-color: var(--dropdown-bg) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 8px !important;
        }}
        div[data-baseweb="popover"] li,
        ul[role="listbox"] li,
        div[data-baseweb="menu"] li,
        li[role="option"],
        div[role="option"] {{
            color: var(--text-primary) !important;
            background-color: var(--dropdown-bg) !important;
        }}
        div[data-baseweb="popover"] li:hover,
        ul[role="listbox"] li:hover,
        div[data-baseweb="menu"] li:hover,
        li[role="option"]:hover,
        div[role="option"]:hover {{
            background-color: var(--primary) !important;
            color: #FFFFFF !important;
        }}
        li[aria-selected="true"],
        div[aria-selected="true"] {{
            background-color: var(--dropdown-hover) !important;
        }}
        
        /* Toggle switch styling - make visible in light mode */
        .stToggle label {{
            color: var(--text-primary) !important;
        }}
        .stToggle > div {{
            color: var(--text-primary) !important;
        }}
        
        /* Sidebar toggle button styling */
        button[data-testid="stSidebarCollapseButton"],
        button[data-testid="stBaseButton-header"],
        button[data-testid="stBaseButton-headerNoPadding"] {{
            background-color: var(--toggle-btn-bg) !important;
            border: 1px solid var(--toggle-btn-border) !important;
            color: var(--toggle-btn-text) !important;
        }}
        
        /* Radio buttons in dialogs */
        .stRadio label {{
            color: var(--text-primary) !important;
        }}
        .stRadio div[role="radiogroup"] label {{
            color: var(--text-primary) !important;
        }}
        
        /* Info/Warning/Error boxes */
        .stAlert {{
            background-color: var(--bg-card) !important;
            color: var(--text-primary) !important;
        }}

        /* Form submit buttons */
        .stFormSubmitButton button {{
            border-radius: 10px !important;
        }}

        /* Mobile */
        @media (max-width: 768px) {{
            .main-header h1 {{ font-size: 1.75rem; }}
            .main-header p {{ font-size: 0.9rem; }}
            .block-container {{ 
                padding-left: 0.75rem !important; 
                padding-right: 0.75rem !important; 
            }}
            /* Keep bullet row together on mobile */
            div[data-testid="stHorizontalBlock"]:has(.bullet-card) {{
                flex-wrap: nowrap !important;
                gap: 0.25rem !important;
            }}
            div[data-testid="stHorizontalBlock"]:has(.bullet-card) > div:first-child {{
                flex: 1 1 auto !important;
                min-width: 0 !important;
            }}
            div[data-testid="stHorizontalBlock"]:has(.bullet-card) > div:last-child {{
                flex: 0 0 40px !important;
                min-width: 40px !important;
            }}
            /* Form inputs stack vertically on mobile */
            div[data-testid="stHorizontalBlock"]:not(:has(.bullet-card)) {{ 
                flex-wrap: wrap !important; 
                gap: 0.5rem !important; 
            }}
            div[data-testid="stHorizontalBlock"]:not(:has(.bullet-card)) > div[data-testid="column"] {{ 
                min-width: 100% !important; 
                flex: 1 1 100% !important; 
            }}
            /* Ensure text areas are fully visible */
            .stTextArea textarea {{
                min-height: 100px !important;
            }}
        }}

        #MainMenu, footer, .stDeployButton {{ visibility: hidden; }}
    </style>
    """, unsafe_allow_html=True)

def init_state():
    defaults = {
        "bullets": [],
        "form_role": "",
        "form_tech": "",
        "form_exp": "Intermediate",
        "form_desc": "",
        "trigger_gen": False,
        "dark_theme": True
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def clear_form():
    st.session_state.form_role = ""
    st.session_state.form_tech = ""
    st.session_state.form_exp = "Intermediate"
    st.session_state.form_desc = ""
    st.session_state.bullets = []
    st.toast("Form cleared!")

@st.dialog("Refine Bullet")
def open_edit_modal(index, current_text, ai_service):
    st.markdown("**Original:**")
    st.info(current_text)
    
    new_style = st.radio("Refinement Goal", list(REWRITE_OPTIONS.keys()), 
                        format_func=lambda x: f"**{x}** - {REWRITE_OPTIONS[x]}")
    
    if st.button("Apply Changes", type="primary", use_container_width=True):
        with st.spinner("Polishing..."):
            try:
                new_val = ai_service.rewrite_bullet(current_text, new_style)
                st.session_state.bullets[index] = new_val
                st.rerun()
            except Exception as e:
                st.error(str(e))

def validate_inputs(desc, length_mode):
    word_count = len(desc.split())
    
    if word_count < 5:
        return False, "Description is too short. Please add at least 5 words."
    
    if length_mode == "Long" and word_count < 15:
        return False, f"For 'Long' bullets, please provide more detail (at least 15 words). You currently have {word_count}."
        
    return True, ""

def render_sidebar():
    with st.sidebar:
        st.markdown("#### Settings")
        
        theme_mode = st.toggle(
            "Dark Mode", 
            value=st.session_state.dark_theme,
            key="theme_toggle_switch",
            help="Toggle between dark and light theme"
        )
        if theme_mode != st.session_state.dark_theme:
            st.session_state.dark_theme = theme_mode
            st.rerun()
        
        st.markdown("---")
        
        st.markdown("#### Controls")
        b_count = st.slider("Number of Bullets", 2, 5, DEFAULT_COUNT)
        b_length_key = st.select_slider("Bullet Length", options=list(BULLET_LENGTHS.keys()), value="Medium")
        
        st.markdown("---")
        
        st.markdown("#### Quick Start Examples")
        st.caption("Click to auto-fill the form")
        
        for name, data in EXAMPLE_INPUTS.items():
            if st.button(name, key=f"ex_{name}", use_container_width=True):
                st.session_state.form_role = data["role"]
                st.session_state.form_tech = data["tech"]
                st.session_state.form_exp = data["exp"]
                st.session_state.form_desc = data["desc"]
                st.session_state.trigger_gen = True
                st.rerun()
        
        st.markdown("---")
        st.caption("Tip: Be specific about YOUR contributions and include metrics when possible.")
                
    return b_count, b_length_key

def main():
    init_state()
    inject_custom_css(st.session_state.dark_theme)
    ai_service = get_ai_service()
    
    st.markdown("""
    <div class="main-header">
        <h1>Resume Bullet Enhancer</h1>
        <p>Turn rough notes into hired results.</p>
    </div>
    """, unsafe_allow_html=True)

    count, length_key = render_sidebar()
    length_instruction = BULLET_LENGTHS[length_key]

    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        with st.form("main_form", border=False):
            
            st.markdown("### 📝 Describe Your Work")
            
            c1, c2 = st.columns([2, 1]) 
            with c1:
                role = st.text_input("Target Role", key="form_role", placeholder="e.g. Senior Backend Engineer")
            with c2:
                exp = st.selectbox("Experience Level", options=EXPERIENCE_LEVELS, key="form_exp")
            
            c3, c4 = st.columns([2, 1])
            with c3:
                tech = st.text_input("Tech Stack", key="form_tech", placeholder="e.g. Python, AWS, Docker")
            with c4:
                style = st.selectbox("Bullet Style", options=list(BULLET_STYLES.keys()))

            desc = st.text_area(
                "Work Description", 
                key="form_desc",
                height=120, 
                placeholder="I built the authentication system using JWT tokens. It improved security and reduced login issues by 20%..."
            )

            b_col1, b_col2 = st.columns([3, 1])
            with b_col1:
                submitted = st.form_submit_button("✨ Generate Bullets", type="primary", use_container_width=True)
            with b_col2:
                clear_clicked = st.form_submit_button("🗑️ Clear", type="secondary", use_container_width=True, on_click=clear_form)
        
        st.markdown('</div>', unsafe_allow_html=True)

    should_generate = (submitted or st.session_state.trigger_gen) and not clear_clicked
    
    if should_generate and ai_service:
        st.session_state.trigger_gen = False
        
        is_valid, err_msg = validate_inputs(desc, length_key)
        
        if not is_valid:
            st.warning(err_msg)
        else:
            with st.spinner("Generating professional bullets..."):
                try:
                    bullets = ai_service.generate_bullets(
                        description=desc,
                        tech_stack=tech,
                        experience_level=exp,
                        target_role=role,
                        style=style,
                        count=count,
                        length=length_instruction
                    )
                    st.session_state.bullets = bullets
                    if not submitted: st.rerun()
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    if st.session_state.bullets:
        st.markdown("### Optimized Results")
        st.caption("Click Edit to refine any bullet point")
        
        for i, bullet in enumerate(st.session_state.bullets):
            cols = st.columns([15, 1], gap="small")
            with cols[0]:
                st.markdown(f"""
                <div class="bullet-card" style="animation-delay: {i * 0.1}s">
                    <div class="bullet-content">{bullet}</div>
                </div>
                """, unsafe_allow_html=True)
            with cols[1]:
                if st.button("✏️", key=f"edit_{i}", help="Edit"):
                    open_edit_modal(i, bullet, ai_service)

        st.markdown("---")
        final_text = "\n\n".join(st.session_state.bullets)
        
        line_count = len(st.session_state.bullets)
        char_count = len(final_text)
        dynamic_height = max(120, min(300, line_count * 60 + char_count // 10))
        
        st.markdown("#### Final Output")
        st.text_area(
            "Copy to Clipboard", 
            value=final_text, 
            height=dynamic_height,
            key=f"copy_area_{len(st.session_state.bullets)}_{hash(final_text)}"
        )
        st.caption("Click inside the box and press Ctrl+A then Ctrl+C to copy all")

    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem 0; border-top: 1px solid var(--border-color); color: var(--text-secondary);">
        <small>Powered by <b>Groq</b> & <b>LLaMA 3.3</b> • Built with Streamlit</small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
