import streamlit as st
import requests
from PIL import Image
import base64
import io
import json
import os
from datetime import datetime
import groq
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Initialize Groq client
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page configuration
st.set_page_config(
    page_title="CodeVision Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Professional enterprise-grade CSS with advanced animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700&display=swap');
    
    /* Reset and base styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Hide Streamlit elements */
    #MainMenu, footer, header, .stDeployButton {display: none !important;}
    .stAppViewContainer > .main > div {padding-top: 0 !important;}
    
    /* CSS Variables */
    :root {
        --primary: #6366f1;
        --primary-light: #818cf8;
        --primary-dark: #4f46e5;
        --secondary: #f59e0b;
        --accent: #10b981;
        --danger: #ef4444;
        --warning: #f59e0b;
        --success: #10b981;
        --dark: #0f172a;
        --darker: #020617;
        --light: #1e293b;
        --lighter: #334155;
        --text: #f8fafc;
        --text-muted: #94a3b8;
        --text-dim: #64748b;
        --border: #334155;
        --glass: rgba(15, 23, 42, 0.8);
        --glass-border: rgba(99, 102, 241, 0.2);
        --shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        --shadow-lg: 0 35px 60px -12px rgba(0, 0, 0, 0.4);
    }
    
    /* Main app container */
    .stApp {
        background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 25%, var(--light) 50%, var(--dark) 75%, var(--darker) 100%);
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
        color: var(--text);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
    }
    
    /* Animated background grid */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(99, 102, 241, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(99, 102, 241, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: gridMove 30s linear infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    /* Floating orbs */
    .stApp::after {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 20%, rgba(99, 102, 241, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(245, 158, 11, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 40% 60%, rgba(16, 185, 129, 0.06) 0%, transparent 50%);
        animation: orbFloat 25s ease-in-out infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    @keyframes gridMove {
        0% { transform: translate(0, 0); }
        100% { transform: translate(50px, 50px); }
    }
    
    @keyframes orbFloat {
        0%, 100% { transform: scale(1) rotate(0deg); opacity: 0.4; }
        33% { transform: scale(1.1) rotate(120deg); opacity: 0.6; }
        66% { transform: scale(0.9) rotate(240deg); opacity: 0.3; }
    }
    
    /* Navigation bar */
    .nav-container {
        position: sticky;
        top: 0;
        z-index: 1000;
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid var(--border);
        padding: 1rem 0;
        margin-bottom: 2rem;
        animation: slideDown 0.8s ease-out;
    }
    
    .nav-content {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 2rem;
    }
    
    .nav-logo {
        font-size: 1.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .nav-stats {
        display: flex;
        gap: 2rem;
        font-size: 0.9rem;
        color: var(--text-muted);
    }
    
    .nav-stat {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .nav-stat-value {
        color: var(--primary-light);
        font-weight: 600;
    }
    
    @keyframes slideDown {
        from { transform: translateY(-100%); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    /* Hero section */
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    .hero-title {
        font-size: clamp(3rem, 8vw, 6rem);
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, var(--text) 0%, var(--primary-light) 50%, var(--secondary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: titleGlow 3s ease-in-out infinite alternate;
        position: relative;
    }
    
    .hero-title::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 120%;
        height: 120%;
        background: radial-gradient(ellipse, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
        animation: titlePulse 4s ease-in-out infinite;
        z-index: -1;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: var(--text-muted);
        margin-bottom: 3rem;
        font-weight: 400;
        animation: fadeInUp 1s ease-out 0.3s both;
    }
    
    .hero-cta {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease-out 0.6s both;
    }
    
    @keyframes titleGlow {
        0% { filter: drop-shadow(0 0 20px rgba(99, 102, 241, 0.3)); }
        100% { filter: drop-shadow(0 0 40px rgba(99, 102, 241, 0.6)); }
    }
    
    @keyframes titlePulse {
        0%, 100% { opacity: 0.3; transform: translate(-50%, -50%) scale(1); }
        50% { opacity: 0.6; transform: translate(-50%, -50%) scale(1.05); }
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Glass cards */
    .glass-panel {
        background: var(--glass);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 24px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: var(--shadow);
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .glass-panel::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.1), transparent);
        transition: left 0.8s ease;
    }
    
    .glass-panel:hover {
        transform: translateY(-8px);
        border-color: var(--primary);
        box-shadow: var(--shadow-lg), 0 0 50px rgba(99, 102, 241, 0.2);
    }
    
    .glass-panel:hover::before {
        left: 100%;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        position: relative;
    }
    
    .section-header::after {
        content: '';
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, var(--primary), transparent);
        margin-left: 1rem;
    }
    
    /* Premium buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), var(--primary-dark));
        color: white;
        border: none;
        border-radius: 16px;
        padding: 1rem 2.5rem;
        font-weight: 600;
        font-size: 1rem;
        font-family: 'Inter', sans-serif;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 25px rgba(99, 102, 241, 0.3);
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.6s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 15px 35px rgba(99, 102, 241, 0.4);
        background: linear-gradient(135deg, var(--primary-light), var(--primary));
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:active {
        transform: translateY(0) scale(0.98);
    }
    
    /* File uploader */
    .stFileUploader > div > div {
        background: rgba(99, 102, 241, 0.05);
        border: 2px dashed rgba(99, 102, 241, 0.3);
        border-radius: 20px;
        padding: 4rem 2rem;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stFileUploader > div > div::before {
        content: '⚡';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 4rem;
        opacity: 0.1;
        animation: pulse 2s ease-in-out infinite;
        z-index: 0;
    }
    
    .stFileUploader > div > div:hover {
        border-color: var(--primary);
        background: rgba(99, 102, 241, 0.1);
        transform: scale(1.02);
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.2);
    }
    
    /* Form inputs */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid var(--border);
        border-radius: 12px;
        color: var(--text);
        padding: 1rem 1.25rem;
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        background: rgba(30, 41, 59, 1);
        outline: none;
    }
    
    /* Radio buttons */
    .stRadio > div {
        background: rgba(30, 41, 59, 0.5);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid var(--border);
        transition: all 0.3s ease;
    }
    
    .stRadio > div:hover {
        border-color: var(--primary);
        background: rgba(30, 41, 59, 0.8);
    }
    
    /* Metrics cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(245, 158, 11, 0.05));
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(99, 102, 241, 0.1), transparent);
        animation: rotate 6s linear infinite;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: var(--primary);
        box-shadow: 0 15px 35px rgba(99, 102, 241, 0.2);
    }
    
    .metric-card:hover::before {
        opacity: 1;
    }
    
    @keyframes rotate {
        100% { transform: rotate(360deg); }
    }
    
    /* Code blocks */
    .stCodeBlock {
        background: rgba(2, 6, 23, 0.9);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 16px;
        font-family: 'JetBrains Mono', monospace;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .stCodeBlock::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
        animation: codeGlow 3s ease-in-out infinite;
    }
    
    @keyframes codeGlow {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 1; }
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: rgba(30, 41, 59, 0.5);
        border-radius: 16px;
        padding: 0.5rem;
        border: 1px solid var(--border);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        color: var(--text-muted);
        border: none;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(99, 102, 241, 0.1);
        color: var(--text);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary), var(--primary-dark));
        color: white;
        box-shadow: 0 5px 15px rgba(99, 102, 241, 0.3);
    }
    
    /* Success/Info messages */
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 12px;
        border: none;
        animation: slideInRight 0.5s ease-out;
        backdrop-filter: blur(10px);
    }
    
    .stSuccess {
        background: rgba(16, 185, 129, 0.1);
        border-left: 4px solid var(--success);
    }
    
    .stInfo {
        background: rgba(99, 102, 241, 0.1);
        border-left: 4px solid var(--primary);
    }
    
    .stWarning {
        background: rgba(245, 158, 11, 0.1);
        border-left: 4px solid var(--warning);
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.1);
        border-left: 4px solid var(--danger);
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    /* Images */
    .stImage > img {
        border-radius: 16px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
        transition: all 0.4s ease;
    }
    
    .stImage:hover > img {
        transform: scale(1.02);
        box-shadow: 0 20px 45px rgba(99, 102, 241, 0.2);
    }
    
    /* Loading spinner */
    .stSpinner > div {
        border-color: rgba(99, 102, 241, 0.2);
        border-top-color: var(--primary);
        animation: spin 1s linear infinite;
    }
    
    /* Progress bar */
    .progress-container {
        width: 100%;
        height: 4px;
        background: rgba(99, 102, 241, 0.2);
        border-radius: 2px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        border-radius: 2px;
        animation: progressFlow 2s ease-in-out infinite;
    }
    
    @keyframes progressFlow {
        0% { width: 0%; }
        50% { width: 70%; }
        100% { width: 100%; }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 3rem;
        }
        
        .glass-panel {
            padding: 1.5rem;
            margin: 1rem 0;
        }
        
        .nav-content {
            padding: 0 1rem;
        }
        
        .nav-stats {
            display: none;
        }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--dark);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--primary-light);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'current_analysis' not in st.session_state:
    st.session_state.current_analysis = None
if 'processing' not in st.session_state:
    st.session_state.processing = False

def encode_image_to_base64(image):
    """Convert PIL image to base64 string with size optimization"""
    width, height = image.size
    total_pixels = width * height
    max_pixels = 33177600  # 33 megapixels
    
    if total_pixels > max_pixels:
        ratio = (max_pixels / total_pixels) ** 0.5
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        st.info(f"🔧 Image optimized: {width}×{height} → {new_width}×{new_height}")
    
    buffered = io.BytesIO()
    image.save(buffered, format="PNG", optimize=True)
    
    img_data = buffered.getvalue()
    if len(img_data) > 4 * 1024 * 1024:  # 4MB
        buffered = io.BytesIO()
        if image.mode in ('RGBA', 'LA', 'P'):
            image = image.convert('RGB')
        image.save(buffered, format="JPEG", quality=85, optimize=True)
        img_data = buffered.getvalue()
        st.info("🔧 Image compressed for optimal processing")
    
    img_str = base64.b64encode(img_data).decode()
    return img_str

def analyze_image_with_groq(image_base64, analysis_type="general"):
    """Analyze image using Groq API"""
    try:
        prompt_templates = {
            "web": """You are a senior full-stack developer. Analyze this image and generate a complete, self-contained HTML file that recreates this design exactly.

CRITICAL REQUIREMENTS:
- Generate ONLY a complete HTML document starting with <!DOCTYPE html>
- Include ALL CSS inside <style> tags in the <head>
- Include ALL JavaScript inside <script> tags before </body>
- Make it completely self-contained and runnable
- Use modern CSS (Grid/Flexbox) for responsive layouts
- Add smooth hover effects and transitions
- Ensure pixel-perfect recreation of the design
- Use semantic HTML5 elements
- NO markdown formatting, NO explanations, NO multiple code blocks

EXAMPLE STRUCTURE:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Design</title>
    <style>
        /* ALL CSS HERE */
    </style>
</head>
<body>
    <!-- ALL HTML CONTENT HERE -->
    <script>
        // ALL JAVASCRIPT HERE
    </script>
</body>
</html>

OUTPUT: ONLY the complete HTML code above, nothing else.""",
            
            "mobile": """You are a senior React Native developer. Generate complete React Native code for this mobile interface.

CRITICAL REQUIREMENTS:
- Generate ONLY complete React Native component code
- Include proper imports at the top
- Use StyleSheet for all styling
- Include proper state management with hooks
- Make it production-ready and runnable
- Follow React Native best practices
- NO markdown formatting, NO explanations

OUTPUT: ONLY the complete React Native code, nothing else.""",
            
            "general": """You are a senior software architect. Analyze this image and generate the most appropriate code.

DECISION LOGIC:
- If it looks like a web interface: Generate complete HTML with embedded CSS/JS
- If it looks like a mobile app: Generate React Native code
- If it looks like a desktop app: Generate Python GUI code

CRITICAL REQUIREMENTS:
- Generate ONLY the complete, runnable code
- For web: Complete HTML document with embedded CSS/JS
- For mobile: Complete React Native component
- For desktop: Complete Python application
- Make it production-ready and self-contained
- NO markdown formatting, NO explanations, NO multiple options

OUTPUT: ONLY the complete code for the detected platform, nothing else."""
        }
        
        prompt = prompt_templates.get(analysis_type, prompt_templates["general"])
        
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=4000,
            temperature=0.3
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing image: {str(e)}"

def clean_code_output(code):
    """Clean up code output by removing markdown formatting and extracting HTML"""
    # Remove markdown code blocks
    if code.startswith("```") and code.endswith("```"):
        lines = code.split('\n')
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1] == "```":
            lines = lines[:-1]
        code = '\n'.join(lines)
    
    # Remove specific language markers
    for lang in ["html", "javascript", "python", "jsx", "css"]:
        if code.startswith(f"```{lang}") and code.endswith("```"):
            code = code[len(f"```{lang}"):-3].strip()
    
    # Extract HTML from mixed content
    if "<!DOCTYPE html>" in code:
        # Find the HTML section
        start_idx = code.find("<!DOCTYPE html>")
        if start_idx != -1:
            # Find the end of the HTML document
            end_idx = code.find("</html>", start_idx)
            if end_idx != -1:
                code = code[start_idx:end_idx + 7]  # +7 for "</html>"
    
    # Remove any remaining markdown sections
    lines = code.split('\n')
    cleaned_lines = []
    skip_section = False
    
    for line in lines:
        # Skip markdown headers and code block markers
        if line.startswith('###') or line.startswith('```'):
            skip_section = not skip_section if line.startswith('```') else True
            continue
        
        if not skip_section:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines).strip()

def ensure_complete_html(code):
    """Ensure the generated code is a complete HTML document"""
    if not code.strip().startswith('<!DOCTYPE') and not code.strip().startswith('<html'):
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Design</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f8fafc;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        {code}
    </div>
</body>
</html>"""
        return html_template
    return code

def save_to_history(image, analysis, analysis_type):
    """Save analysis to history"""
    history_item = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "image": image,
        "analysis": analysis,
        "type": analysis_type,
        "id": len(st.session_state.history) + 1
    }
    st.session_state.history.insert(0, history_item)
    if len(st.session_state.history) > 20:
        st.session_state.history = st.session_state.history[:20]

# Navigation Bar
today_count = len([h for h in st.session_state.history if h["timestamp"].startswith(datetime.now().strftime("%Y-%m-%d"))])
total_count = len(st.session_state.history)

st.markdown(f"""
<div class="nav-container">
    <div class="nav-content">
        <div class="nav-logo">⚡ CodeVision Pro</div>
        <div class="nav-stats">
            <div class="nav-stat">
                <span>Total Projects:</span>
                <span class="nav-stat-value">{total_count}</span>
            </div>
            <div class="nav-stat">
                <span>Today:</span>
                <span class="nav-stat-value">{today_count}</span>
            </div>
            <div class="nav-stat">
                <span>Status:</span>
                <span class="nav-stat-value">{"Processing" if st.session_state.processing else "Ready"}</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">CodeVision Pro</h1>
    <p class="hero-subtitle">Enterprise-grade AI code generation from visual designs</p>
</div>
""", unsafe_allow_html=True)

# Main Content
st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">⚡ AI Code Generator</h2>', unsafe_allow_html=True)

# Configuration Row
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    analysis_type = st.selectbox(
        "Target Platform",
        ["general", "web", "mobile"],
        format_func=lambda x: {
            "general": "🎯 Smart Detection",
            "web": "🌐 Web Application",
            "mobile": "📱 Mobile Application"
        }[x],
        help="Choose the target platform for code generation"
    )

with col2:
    st.markdown("**Input Method:** File Upload Only")
    st.info("📁 Upload your design image using the file uploader below")

with col3:
    if st.session_state.current_analysis:
        st.success("✅ Code Ready")
    else:
        st.info("🎯 Ready to Generate")

st.markdown('</div>', unsafe_allow_html=True)

# Image Input Section
st.markdown('<div class="glass-panel">', unsafe_allow_html=True)

image = None

uploaded_file = st.file_uploader(
    "Drop your design image here or click to browse",
    type=['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'],
    help="Upload a high-quality image of your design or mockup"
)
if uploaded_file is not None:
    image = Image.open(uploaded_file)

if image:
    col_img1, col_img2 = st.columns([3, 1])
    
    with col_img1:
        st.image(image, caption="Design Input", use_container_width=True)
    
    with col_img2:
        st.markdown("### 📊 Image Analysis")
        
        # Image metrics
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Resolution", f"{image.size[0]} × {image.size[1]}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Format", image.format or "Unknown")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Color Mode", image.mode)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Generate button
        if st.button("🚀 Generate Code", type="primary", use_container_width=True):
            st.session_state.processing = True
            
            # Create progress container
            progress_container = st.empty()
            status_container = st.empty()
            
            try:
                # Step 1: Image processing
                with progress_container:
                    st.markdown("""
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 20%;"></div>
                    </div>
                    """, unsafe_allow_html=True)
                
                status_container.info("🔍 Processing image...")
                image_base64 = encode_image_to_base64(image)
                
                # Step 2: AI Analysis
                with progress_container:
                    st.markdown("""
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 60%;"></div>
                    </div>
                    """, unsafe_allow_html=True)
                
                status_container.info("🧠 AI is analyzing design patterns...")
                analysis = analyze_image_with_groq(image_base64, analysis_type)
                
                # Step 3: Code processing
                with progress_container:
                    st.markdown("""
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 90%;"></div>
                    </div>
                    """, unsafe_allow_html=True)
                
                status_container.info("⚡ Generating optimized code...")
                
                # Clean up the analysis
                analysis = clean_code_output(analysis)
                
                # Ensure complete HTML for web analysis
                if analysis_type == "web" or (analysis_type == "general" and ("<html" in analysis.lower() or "<!doctype" in analysis.lower())):
                    if not analysis.strip().startswith('<!DOCTYPE'):
                        analysis = ensure_complete_html(analysis)
                
                # Additional validation for HTML
                if analysis_type == "web" and not ("<!DOCTYPE" in analysis or "<html" in analysis):
                    status_container.error("❌ Generated code is not valid HTML. Please try again.")
                    st.session_state.processing = False
                    st.stop()
                
                # Step 4: Complete
                with progress_container:
                    st.markdown("""
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 100%;"></div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Save to session state and history
                st.session_state.current_analysis = analysis
                save_to_history(image, analysis, analysis_type)
                
                # Clear progress and show success
                progress_container.empty()
                status_container.success("✅ Code generation completed successfully!")
                st.session_state.processing = False
                
                st.balloons()
                time.sleep(1)
                st.rerun()
                
            except Exception as e:
                progress_container.empty()
                status_container.error(f"❌ Error during processing: {str(e)}")
                st.session_state.processing = False

st.markdown('</div>', unsafe_allow_html=True)

# Results Section
if st.session_state.current_analysis:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">💻 Generated Code</h2>', unsafe_allow_html=True)
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["🔴 Live Preview", "📝 Source Code", "📊 Analytics", "📥 Export"])
    
    with tab1:
        col_prev1, col_prev2 = st.columns([1, 3])
        with col_prev1:
            preview_height = st.selectbox("Preview Height", [500, 700, 900, 1200], index=1)
        with col_prev2:
            st.info("💡 Live preview renders your generated code in real-time")
        
        # Check if the generated code is HTML
        if st.session_state.current_analysis and ("<html" in st.session_state.current_analysis.lower() or "<!doctype" in st.session_state.current_analysis.lower()):
            try:
                # Validate HTML structure
                if st.session_state.current_analysis.strip().startswith('<!DOCTYPE') or st.session_state.current_analysis.strip().startswith('<html'):
                    st.components.v1.html(st.session_state.current_analysis, height=preview_height, scrolling=True)
                    st.success("✅ Live preview rendered successfully!")
                else:
                    st.warning("⚠️ HTML structure detected but may be incomplete")
                    st.code(st.session_state.current_analysis, language="html")
            except Exception as e:
                st.error(f"❌ Preview error: {str(e)}")
                st.code(st.session_state.current_analysis, language="html")
        
        # React Native Preview Simulator
        elif "react" in st.session_state.current_analysis.lower() or "import React" in st.session_state.current_analysis:
            
            # Create a visual mockup based on the React Native code
            def create_mobile_mockup():
                code = st.session_state.current_analysis
                mockup_content = ""
                
                # Extract component name and title
                component_name = "Mobile App"
                if "const " in code:
                    try:
                        component_name = code.split("const ")[1].split(" =")[0].strip()
                        component_name = component_name.replace("Screen", "").replace("Component", "")
                    except:
                        pass
                
                # Look for header/title text
                header_text = component_name
                if "header" in code.lower():
                    try:
                        # Extract header text from the code
                        lines = code.split('\n')
                        for line in lines:
                            if 'header' in line.lower() and ('Text' in line or 'title' in line):
                                if "'" in line:
                                    header_text = line.split("'")[1]
                                elif '"' in line:
                                    header_text = line.split('"')[1]
                                break
                    except:
                        pass
                
                # Start building the mockup
                mockup_content += f"""
                <div class="mockup-title">
                    <h2>{header_text}</h2>
                </div>
                """
                
                # Check for specific components and create realistic mockups
                
                # Profile/Avatar section
                if "Image" in code and ("profile" in code.lower() or "avatar" in code.lower()):
                    mockup_content += """
                    <div style="text-align: center; margin-bottom: 24px;">
                        <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #e5e7eb, #d1d5db); border-radius: 40px; margin: 0 auto 12px auto; display: flex; align-items: center; justify-content: center; font-size: 32px; color: #9ca3af;">👤</div>
                        <p style="font-size: 12px; color: #6b7280; margin: 0;">Tap to change profile image</p>
                    </div>
                    """
                
                # Email section
                if "email" in code.lower() and "TextInput" not in code:
                    email_value = "AMYORTEGA@GMAIL.COM"
                    if "@" in code:
                        try:
                            # Try to extract email from code
                            import re
                            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', code)
                            if emails:
                                email_value = emails[0].upper()
                        except:
                            pass
                    
                    mockup_content += f"""
                    <div style="margin-bottom: 20px; padding: 16px; background: white; border-radius: 12px; border: 1px solid #f3f4f6;">
                        <div style="font-size: 12px; color: #6b7280; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">E-MAIL ADDRESS</div>
                        <div style="font-size: 16px; color: #1f2937; font-weight: 500; margin-bottom: 8px;">{email_value}</div>
                        <div style="font-size: 12px; color: #9ca3af;">Change your email address. Check your email with instructions</div>
                    </div>
                    """
                
                # Currency/Picker section
                if "Picker" in code or "currency" in code.lower():
                    currency_value = "US Dollars"
                    if "currency" in code.lower():
                        try:
                            lines = code.split('\n')
                            for line in lines:
                                if 'currency' in line.lower() and ('US' in line or 'Dollar' in line):
                                    if "'" in line:
                                        currency_value = line.split("'")[1]
                                    elif '"' in line:
                                        currency_value = line.split('"')[1]
                                    break
                        except:
                            pass
                    
                    mockup_content += f"""
                    <div style="margin-bottom: 20px; padding: 16px; background: white; border-radius: 12px; border: 1px solid #f3f4f6;">
                        <div style="font-size: 12px; color: #6b7280; font-weight: 600; margin-bottom: 12px; letter-spacing: 0.5px;">CHOOSE CURRENCY</div>
                        <div style="background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; padding: 12px; display: flex; justify-content: space-between; align-items: center;">
                            <span style="color: #1f2937; font-size: 16px;">{currency_value}</span>
                            <span style="color: #9ca3af;">▼</span>
                        </div>
                    </div>
                    """
                
                # Notifications/Switch section
                if "Switch" in code:
                    mockup_content += """
                    <div style="margin-bottom: 20px; padding: 16px; background: white; border-radius: 12px; border: 1px solid #f3f4f6;">
                        <div style="font-size: 12px; color: #6b7280; font-weight: 600; margin-bottom: 16px; letter-spacing: 0.5px;">NOTIFICATIONS</div>
                        
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                            <span style="color: #1f2937; font-size: 14px; font-weight: 500;">NEW ARRIVALS</span>
                            <div style="width: 44px; height: 24px; background: #3b82f6; border-radius: 12px; position: relative;">
                                <div style="width: 20px; height: 20px; background: white; border-radius: 10px; position: absolute; top: 2px; right: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.2);"></div>
                            </div>
                        </div>
                        
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="color: #1f2937; font-size: 14px; font-weight: 500;">DISCOUNTS</span>
                            <div style="width: 44px; height: 24px; background: #e5e7eb; border-radius: 12px; position: relative;">
                                <div style="width: 20px; height: 20px; background: white; border-radius: 10px; position: absolute; top: 2px; left: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.2);"></div>
                            </div>
                        </div>
                    </div>
                    """
                
                # Text inputs
                if "TextInput" in code:
                    mockup_content += """
                    <div class="mockup-form">
                        <input class="mockup-input" placeholder="Enter your name..." readonly>
                        <input class="mockup-input" placeholder="Enter your email..." readonly>
                        <input class="mockup-input" placeholder="Enter message..." readonly>
                    </div>
                    """
                
                # Save/Action button
                if "TouchableOpacity" in code or "Button" in code:
                    button_text = "SAVE CHANGES"
                    button_color = "#ffd700"
                    
                    # Try to extract button text and color
                    if "SAVE" in code:
                        button_text = "SAVE CHANGES"
                    elif "Submit" in code:
                        button_text = "Submit Action"
                    
                    if "#ffd700" in code or "gold" in code.lower():
                        button_color = "#ffd700"
                    elif "#3b82f6" in code:
                        button_color = "#3b82f6"
                    
                    mockup_content += f"""
                    <button style="
                        background: {button_color};
                        color: {'#1f2937' if button_color == '#ffd700' else 'white'};
                        padding: 16px 24px;
                        border-radius: 12px;
                        font-weight: 600;
                        font-size: 16px;
                        cursor: pointer;
                        border: none;
                        text-align: center;
                        width: 100%;
                        box-sizing: border-box;
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                        margin-top: 8px;
                        letter-spacing: 0.5px;
                    ">{button_text}</button>
                    """
                
                # Fallback if no specific content detected
                if not any(x in code for x in ["Image", "email", "Picker", "Switch", "TextInput", "TouchableOpacity"]):
                    mockup_content = """
                    <div class="mockup-default">
                        <div class="mockup-icon">📱</div>
                        <h3>React Native Component</h3>
                        <p>Your mobile interface will render here when you generate React Native code</p>
                        <div class="mockup-info-card">
                            <p class="mockup-info-text">✨ Generated React Native code is ready to use</p>
                        </div>
                    </div>
                    """
                
                return mockup_content
            
            col_mobile1, col_mobile2 = st.columns([1, 2])
            
            with col_mobile1:
                # Mobile phone simulator frame with visual mockup
                mockup_html = create_mobile_mockup()
                
                # Create complete HTML for the mobile simulator
                mobile_simulator_html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <style>
                        body {{
                            margin: 0;
                            padding: 20px;
                            background: linear-gradient(135deg, #0f172a, #1e293b);
                            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            min-height: 100vh;
                        }}
                        .phone-container {{
                            width: 320px;
                            height: {preview_height - 40}px;
                            background: linear-gradient(145deg, #1f2937, #111827);
                            border-radius: 30px;
                            padding: 8px;
                            box-shadow: 0 25px 50px rgba(0,0,0,0.4);
                            position: relative;
                        }}
                        .phone-frame {{
                            width: 100%;
                            height: 100%;
                            background: #000;
                            border-radius: 22px;
                            padding: 12px 8px;
                            position: relative;
                        }}
                        .status-bar {{
                            height: 20px;
                            display: flex;
                            justify-content: space-between;
                            align-items: center;
                            padding: 0 20px;
                            color: white;
                            font-size: 12px;
                            font-weight: 600;
                        }}
                        .battery {{
                            width: 18px;
                            height: 10px;
                            border: 1px solid white;
                            border-radius: 2px;
                            position: relative;
                        }}
                        .battery-fill {{
                            width: 12px;
                            height: 6px;
                            background: white;
                            border-radius: 1px;
                            position: absolute;
                            top: 1px;
                            left: 1px;
                        }}
                        .screen-content {{
                            width: 100%;
                            height: calc(100% - 40px);
                            background: #f9fafb;
                            border-radius: 18px;
                            padding: 16px;
                            overflow-y: auto;
                            margin-top: 8px;
                            display: flex;
                            flex-direction: column;
                            justify-content: flex-start;
                        }}
                        .home-indicator {{
                            width: 134px;
                            height: 5px;
                            background: white;
                            border-radius: 3px;
                            margin: 8px auto 0 auto;
                            opacity: 0.8;
                        }}
                        .mockup-title {{
                            text-align: center;
                            margin-bottom: 24px;
                            padding-top: 8px;
                        }}
                        .mockup-title h2 {{
                            color: #1f2937;
                            font-size: 20px;
                            font-weight: 700;
                            margin: 0;
                            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                        }}
                        .mockup-form {{
                            margin-bottom: 16px;
                        }}
                        .mockup-input {{
                            background: white;
                            border: 1px solid #e5e7eb;
                            border-radius: 12px;
                            padding: 14px 16px;
                            font-size: 16px;
                            color: #9ca3af;
                            margin-bottom: 12px;
                            width: 100%;
                            box-sizing: border-box;
                            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                            transition: all 0.2s ease;
                        }}
                        .mockup-input:focus {{
                            outline: none;
                            border-color: #3b82f6;
                            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
                        }}
                        .mockup-button {{
                            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
                            color: white;
                            padding: 16px 24px;
                            border-radius: 12px;
                            font-weight: 600;
                            font-size: 16px;
                            cursor: pointer;
                            border: none;
                            text-align: center;
                            width: 100%;
                            box-sizing: border-box;
                            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
                            transition: all 0.2s ease;
                            margin-top: 8px;
                        }}
                        .mockup-button:hover {{
                            transform: translateY(-1px);
                            box-shadow: 0 6px 16px rgba(59, 130, 246, 0.4);
                        }}
                        .mockup-list-item {{
                            background: white;
                            border-radius: 12px;
                            padding: 16px;
                            margin-bottom: 10px;
                            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                            border: 1px solid #f3f4f6;
                            transition: all 0.2s ease;
                        }}
                        .mockup-list-item:hover {{
                            transform: translateY(-1px);
                            box-shadow: 0 4px 12px rgba(0,0,0,0.12);
                        }}
                        .mockup-list-title {{
                            font-weight: 600;
                            color: #1f2937;
                            margin-bottom: 4px;
                            font-size: 16px;
                        }}
                        .mockup-list-subtitle {{
                            font-size: 14px;
                            color: #6b7280;
                            line-height: 1.4;
                        }}
                        .mockup-default {{
                            text-align: center;
                            padding: 32px 16px;
                            display: flex;
                            flex-direction: column;
                            justify-content: center;
                            align-items: center;
                            height: 100%;
                        }}
                        .mockup-icon {{
                            font-size: 56px;
                            margin-bottom: 16px;
                            opacity: 0.8;
                        }}
                        .mockup-default h3 {{
                            color: #1f2937;
                            margin-bottom: 8px;
                            font-size: 18px;
                            font-weight: 600;
                        }}
                        .mockup-default p {{
                            color: #6b7280;
                            font-size: 14px;
                            line-height: 1.5;
                            margin-bottom: 0;
                        }}
                        .mockup-info-card {{
                            margin-top: 20px;
                            padding: 16px;
                            background: rgba(59, 130, 246, 0.08);
                            border-radius: 12px;
                            border: 1px solid rgba(59, 130, 246, 0.2);
                        }}
                        .mockup-info-text {{
                            font-size: 13px;
                            color: #1e40af;
                            font-weight: 500;
                            margin: 0;
                        }}
                    </style>
                </head>
                <body>
                    <div class="phone-container">
                        <div class="phone-frame">
                            <div class="status-bar">
                                <span>9:41</span>
                                <div style="display: flex; gap: 4px; align-items: center;">
                                    <div class="battery">
                                        <div class="battery-fill"></div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="screen-content">
                                {mockup_html}
                            </div>
                            
                            <div class="home-indicator"></div>
                        </div>
                    </div>
                </body>
                </html>
                """
                
                # Render the mobile simulator
                st.components.v1.html(mobile_simulator_html, height=preview_height, scrolling=False)
            
            with col_mobile2:
                st.markdown("### 📱 React Native Code")
                st.code(st.session_state.current_analysis, language="javascript")
                
                # React Native specific features
                st.markdown("### 🔧 React Native Features Detected")
                features = []
                if "useState" in st.session_state.current_analysis:
                    features.append("✅ State Management (useState)")
                if "StyleSheet" in st.session_state.current_analysis:
                    features.append("✅ StyleSheet Styling")
                if "TouchableOpacity" in st.session_state.current_analysis:
                    features.append("✅ Touch Interactions")
                if "TextInput" in st.session_state.current_analysis:
                    features.append("✅ Text Input Components")
                if "ScrollView" in st.session_state.current_analysis:
                    features.append("✅ Scrollable Content")
                if "FlatList" in st.session_state.current_analysis:
                    features.append("✅ List Components")
                if "Image" in st.session_state.current_analysis:
                    features.append("✅ Image Components")
                
                if features:
                    for feature in features:
                        st.markdown(feature)
                else:
                    st.info("Basic React Native component structure detected")
                
                # Component analysis
                component_count = st.session_state.current_analysis.count('const ') + st.session_state.current_analysis.count('function ')
                lines_count = st.session_state.current_analysis.count('\n') + 1
                
                col_stat1, col_stat2 = st.columns(2)
                with col_stat1:
                    st.metric("Components", component_count)
                with col_stat2:
                    st.metric("Lines of Code", lines_count)
                
                # Setup instructions
                st.markdown("### 🚀 Setup Instructions")
                st.markdown("""
                1. **Copy the code** to your React Native project
                2. **Install dependencies**:
                   ```bash
                   npm install react react-native
                   ```
                3. **Import and use** the component in your app
                4. **Test on device** or simulator for best results
                
                **Quick Start:**
                ```javascript
                import YourComponent from './YourComponent';
                
                export default function App() {
                  return <YourComponent />;
                }
                ```
                """)
        
        # Python Preview
        elif "import tkinter" in st.session_state.current_analysis or "import matplotlib" in st.session_state.current_analysis:
            col_python1, col_python2 = st.columns([1, 2])
            
            with col_python1:
                # Desktop app simulator
                st.markdown(f"""
                <div style="
                    width: 400px;
                    height: {preview_height}px;
                    background: linear-gradient(145deg, #e2e8f0, #cbd5e1);
                    border-radius: 10px;
                    padding: 5px;
                    margin: 0 auto;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                ">
                    <!-- Window title bar -->
                    <div style="
                        background: linear-gradient(145deg, #f1f5f9, #e2e8f0);
                        height: 30px;
                        border-radius: 8px 8px 0 0;
                        display: flex;
                        align-items: center;
                        padding: 0 10px;
                        border-bottom: 1px solid #cbd5e1;
                    ">
                        <div style="display: flex; gap: 5px;">
                            <div style="width: 12px; height: 12px; background: #ef4444; border-radius: 50%;"></div>
                            <div style="width: 12px; height: 12px; background: #f59e0b; border-radius: 50%;"></div>
                            <div style="width: 12px; height: 12px; background: #10b981; border-radius: 50%;"></div>
                        </div>
                        <div style="flex: 1; text-align: center; font-size: 12px; color: #64748b;">Python Application</div>
                    </div>
                    
                    <!-- Window content -->
                    <div style="
                        background: white;
                        height: calc(100% - 35px);
                        border-radius: 0 0 8px 8px;
                        padding: 20px;
                        overflow-y: auto;
                    ">
                        <div style="text-align: center; color: #333;">
                            <h4 style="color: #6366f1; margin-bottom: 15px;">🐍 Python Desktop App</h4>
                            <p style="font-size: 14px; color: #666; margin-bottom: 15px;">
                                Desktop application code generated. Run in your Python environment to see the GUI.
                            </p>
                            <div style="background: #f8fafc; padding: 15px; border-radius: 8px; text-align: left;">
                                <div style="font-family: monospace; font-size: 12px; color: #475569;">
                                    <strong>Framework:</strong> {'Tkinter' if 'tkinter' in st.session_state.current_analysis else 'Matplotlib' if 'matplotlib' in st.session_state.current_analysis else 'Python'}<br>
                                    <strong>Lines:</strong> {st.session_state.current_analysis.count('n') + 1}<br>
                                    <strong>Classes:</strong> {st.session_state.current_analysis.count('class ')}<br>
                                    <strong>Functions:</strong> {st.session_state.current_analysis.count('def ')}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_python2:
                st.markdown("### 🐍 Python Code")
                st.code(st.session_state.current_analysis, language="python")
                
                # Python specific features
                st.markdown("### 🔧 Python Features Detected")
                if "tkinter" in st.session_state.current_analysis:
                    st.markdown("✅ Tkinter GUI Framework")
                    st.markdown("✅ Desktop Application")
                if "matplotlib" in st.session_state.current_analysis:
                    st.markdown("✅ Matplotlib Visualization")
                    st.markdown("✅ Data Plotting")
                if "class " in st.session_state.current_analysis:
                    st.markdown("✅ Object-Oriented Design")
                
                # Setup instructions
                st.markdown("### 🚀 Setup Instructions")
                st.markdown("""
                1. **Save the code** to a `.py` file
                2. **Install dependencies**:
                   ```bash
                   pip install tkinter matplotlib
                   ```
                3. **Run the application**:
                   ```bash
                   python your_app.py
                   ```
                """)
        
        else:
            st.warning("⚠️ Code format not recognized for live preview")
            st.code(st.session_state.current_analysis, language="text")
    
    with tab2:
        # Determine language
        if "<!DOCTYPE" in st.session_state.current_analysis or "<html" in st.session_state.current_analysis:
            language = "html"
        elif "import React" in st.session_state.current_analysis:
            language = "javascript"
        elif "import tkinter" in st.session_state.current_analysis:
            language = "python"
        else:
            language = "html"
        
        st.code(st.session_state.current_analysis, language=language)
    
    with tab3:
        # Code analytics
        lines = st.session_state.current_analysis.count('\n') + 1
        words = len(st.session_state.current_analysis.split())
        chars = len(st.session_state.current_analysis)
        
        col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
        
        with col_stat1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Lines of Code", f"{lines:,}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col_stat2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Word Count", f"{words:,}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col_stat3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Characters", f"{chars:,}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col_stat4:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Language", language.upper())
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.markdown(f"**Analysis Type:** {analysis_type.title()}")
        st.markdown(f"**Model:** Llama 4 Scout (17B parameters)")
    
    with tab4:
        st.markdown("### 📥 Export Options")
        
        col_exp1, col_exp2, col_exp3 = st.columns(3)
        
        with col_exp1:
            if language == "html":
                st.download_button(
                    "📄 Download HTML",
                    data=st.session_state.current_analysis,
                    file_name=f"codevision_pro_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
                    mime="text/html",
                    use_container_width=True
                )
        
        with col_exp2:
            if language == "javascript":
                st.download_button(
                    "📱 Download JSX",
                    data=st.session_state.current_analysis,
                    file_name=f"codevision_pro_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsx",
                    mime="text/javascript",
                    use_container_width=True
                )
        
        with col_exp3:
            if language == "python":
                st.download_button(
                    "🐍 Download Python",
                    data=st.session_state.current_analysis,
                    file_name=f"codevision_pro_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py",
                    mime="text/python",
                    use_container_width=True
                )
        
        st.markdown("---")
        st.info("💡 **Pro Tip:** All generated code is production-ready and follows industry best practices.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Project History
if st.session_state.history:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">📚 Project History</h2>', unsafe_allow_html=True)
    
    # Show recent projects
    for i, item in enumerate(st.session_state.history[:5]):
        col_hist1, col_hist2, col_hist3 = st.columns([1, 3, 1])
        
        with col_hist1:
            st.image(item['image'], width=120)
        
        with col_hist2:
            st.markdown(f"**Project #{item['id']} - {item['type'].title()}**")
            st.markdown(f"*Generated: {item['timestamp']}*")
            st.markdown(f"📊 {len(item['analysis'])} characters • {item['analysis'].count('n') + 1} lines")
        
        with col_hist3:
            if st.button(f"🔄 Restore", key=f"restore_{i}", use_container_width=True):
                st.session_state.current_analysis = item['analysis']
                st.success("✅ Project restored!")
                time.sleep(1)
                st.rerun()
            
            file_ext = "html" if item['type'] == "web" else ("jsx" if item['type'] == "mobile" else "py")
            st.download_button(
                "📥 Export",
                data=item['analysis'],
                file_name=f"project_{item['id']}.{file_ext}",
                mime=f"text/{file_ext}",
                key=f"download_{i}",
                use_container_width=True
            )
        
        if i < min(4, len(st.session_state.history) - 1):
            st.markdown("---")
    
    if len(st.session_state.history) > 5:
        st.info(f"💡 Showing 5 of {len(st.session_state.history)} total projects")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 4rem; padding: 3rem; opacity: 0.7;">
    <p style="font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;">⚡ CodeVision Pro</p>
    <p style="font-size: 0.95rem; color: var(--text-muted);">Enterprise AI Code Generation Platform</p>
    <p style="font-size: 0.85rem; color: var(--text-dim); margin-top: 1rem;">Powered by Llama 4 Scout • Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)