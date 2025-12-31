# 🔍 Smart Code Reviewer

An AI-powered code review assistant that analyzes code for readability, structure, and maintainability before human review.

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

## 📋 Features

- **Instant Code Analysis** - Get feedback in seconds
- **Structured Reviews** - Consistent format with scores, improvements, and positive notes
- **Multi-Language Support** - Python, JavaScript, TypeScript, Java, C++, Go, Rust
- **Customizable Focus** - Choose review priorities (readability, performance, security)
- **Developer-Level Aware** - Tailored feedback based on experience level

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 1.5 Flash (free tier)
- **Language**: Python 3.9+

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-code-reviewer.git
cd smart-code-reviewer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🔑 API Key Setup

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a free API key
3. Enter the key in the app sidebar

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main.png)

### Review Results
![Review Results](screenshots/results.png)

## 💡 How It Works

1. **Input**: Paste code snippet + optional context
2. **Process**: AI analyzes using structured prompt engineering
3. **Output**: 
   - 3 scores (readability, maintainability, best practices)
   - 1 positive note
   - 3 specific improvements with code fixes
   - 1 pro tip

## 🎯 Use Cases

- **Pre-PR Review**: Catch issues before human reviewers
- **Learning Tool**: Junior devs get instant feedback
- **Code Quality Gates**: Integrate into CI/CD workflows
- **Team Standards**: Enforce consistent coding practices

## 📄 License

MIT License

---

## 📝 100-Word Summary

**Smart Code Reviewer** is an AI-powered assistant that provides instant, structured code reviews before human review. Built with Streamlit and Google Gemini AI, it analyzes code snippets and delivers: readability/maintainability/best-practices scores (1-10), one positive reinforcement, three specific improvements with corrected code, and a pro tip. The tool supports multiple programming languages and adjusts feedback based on developer experience level. Users can customize review focus areas (security, performance, testing). This reduces review bottlenecks, catches issues early, and helps junior developers learn faster. The free-tier API makes it accessible to everyone, and the structured output ensures consistent, actionable feedback.
