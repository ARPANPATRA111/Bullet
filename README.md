# 📝 AI Resume Bullet Point Enhancer
**A minimalistic Streamlit application that transforms rough work descriptions into professional, ATS-friendly resume bullet points using AI.**

<a href="https://github.com/ARPANPATRA111/Bullet">
<img width="1919" height="1075" alt="Screenshot 2026-01-23 044903" src="https://github.com/user-attachments/assets/c93812c1-59e8-4d95-98f5-16ba2dfa7400" />
</a>

## ✨ Features

- **Generate Bullets**: Convert raw descriptions into 2-5 polished resume bullets
- **Style Selection**: Choose from ATS Optimized, Concise, or Impact-Focused styles
- **Length Control**: Short (<15 words), Medium (15-25), or Long (25+) bullets
- **Rewrite Option**: Refine individual bullets (shorter, more technical, or impact-focused)
- **12+ Quick Start Examples**: Pre-configured templates for different roles
- **Premium UI**: Glass-morphism design with smooth animations
- **Theme Support**: Dark/Light mode toggle with session persistence
- **Mobile Responsive**: Works seamlessly on all screen sizes
- **Copy & Reset**: Easy copying and session reset functionality

## 🚀 Setup

### 1. Clone or Download

```bash
cd Bullet
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

1. Copy the example environment file:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```

   Get your API key at: https://console.groq.com/

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 Usage

1. **Describe Your Work**: Enter what you did on a project or job
2. **Add Context**: Specify tech stack, target role, and experience level
3. **Choose Style**: Select a bullet style (ATS Optimized, Concise, or Impact-Focused)
4. **Set Preferences**: Adjust bullet count (2-5) and length in sidebar
5. **Generate**: Click "Generate Bullets" to get professional bullets
6. **Refine**: Click ✏️ on any bullet to rewrite it in a different style
7. **Copy**: Copy all bullets from the text area to your clipboard

## 📁 Project Structure

```
Bullet/
├── app.py              # Main Streamlit application
├── config.py           # Configuration constants
├── prompts.py          # AI prompt templates
├── ai_client.py        # Groq API integration
├── schemas.py          # Pydantic validation models
├── validators.py       # Input validation
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
├── report.md           # Project documentation for PPT
└── README.md           # This file
```

## 🎨 Bullet Styles

| Style | Description |
|-------|-------------|
| **ATS Optimized** | Keyword-rich bullets designed to pass Applicant Tracking Systems |
| **Concise** | Short, punchy bullets that get straight to the point |
| **Impact-Focused** | Emphasizes outcomes and contributions over tasks |

## 🔄 Rewrite Options

| Option | Effect |
|--------|--------|
| **Shorter** | Condense bullet to under 15 words |
| **More Technical** | Adds technical depth, tools, and methodology |
| **More Impact-Focused** | Emphasizes outcomes and business value |

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit with Custom CSS |
| AI Model | LLaMA 3.3 70B Versatile |
| API | Groq (High-speed inference) |
| Validation | Pydantic |
| API Client | OpenAI SDK |

## 📝 Notes

- The AI never invents metrics or statistics
- Each bullet starts with an action verb
- Bullets are adapted to your experience level
- Pydantic validation ensures consistent JSON output

## ❓ Troubleshooting

**"GROQ_API_KEY not found"**
- Make sure you've created a `.env` file with your API key
- Ensure the key is correct and active

**"Failed to generate bullets"**
- Check your internet connection
- Verify your API key has available credits
- Try again - transient errors happen

**Bullets seem weak**
- Provide more specific details in your description
- Include concrete tasks and technologies
- Describe what YOU specifically did

## 📄 License

MIT License - Use freely for personal and commercial projects.
