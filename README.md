# 📝 AI Resume Bullet Point Enhancer

A minimalistic Streamlit application that transforms rough work descriptions into professional, ATS-friendly resume bullet points using AI.

## Features

- **Generate Bullets**: Convert raw descriptions into 3 polished resume bullets
- **Style Selection**: Choose from ATS Optimized, Concise, or Impact-Focused styles
- **Rewrite Option**: Refine individual bullets (shorter, more technical, or impact-focused)
- **Copy & Reset**: Easy copying and session reset functionality

## Setup

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

2. Edit `.env` and add your Grok API key:
   ```
   XAI_API_KEY=your_actual_api_key_here
   ```

   Get your API key at: https://console.x.ai/

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

1. **Describe Your Work**: Enter what you did on a project or job
2. **Add Context**: Specify tech stack, target role, and experience level
3. **Choose Style**: Select a bullet style (ATS Optimized, Concise, or Impact-Focused)
4. **Generate**: Click "Generate Bullets" to get 3 professional bullets
5. **Refine**: Select any bullet and rewrite it in a different style
6. **Copy**: Copy all bullets to your clipboard

## Project Structure

```
Bullet/
├── app.py              # Main Streamlit application
├── config.py           # Configuration constants
├── prompts.py          # AI prompt templates
├── ai_client.py        # API integration
├── validators.py       # Input validation
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
└── README.md           # This file
```

## Bullet Styles

| Style | Description |
|-------|-------------|
| **ATS Optimized** | Keyword-rich bullets designed to pass Applicant Tracking Systems |
| **Concise** | Short, punchy bullets that get straight to the point |
| **Impact-Focused** | Emphasizes outcomes and contributions over tasks |

## Rewrite Options

| Option | Effect |
|--------|--------|
| **Shorter** | Reduces bullet to under 15 words |
| **More Technical** | Adds technical depth and terminology |
| **More Impact-Focused** | Emphasizes outcomes and value delivered |

## Notes

- The AI never invents metrics or statistics
- Each bullet starts with an action verb
- Bullets are adapted to your experience level
- Quality checks ensure consistent output

## Troubleshooting

**"XAI_API_KEY not found"**
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

## License

MIT License - Use freely for personal and commercial projects.
