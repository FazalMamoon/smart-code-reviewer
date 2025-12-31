"""
Smart Code Reviewer - AI-Powered Code Review Assistant
A Streamlit app that reviews code for readability, structure, and maintainability.
"""

import streamlit as st
import google.generativeai as genai
import os
import json

# Page config
st.set_page_config(
    page_title="Smart Code Reviewer",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stTextArea textarea {
        font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
        font-size: 14px;
    }
    .score-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
    .improvement-card {
        background: #f8f9fa;
        padding: 15px;
        border-left: 4px solid #667eea;
        margin: 10px 0;
        border-radius: 0 8px 8px 0;
    }
    .positive-card {
        background: #d4edda;
        padding: 15px;
        border-left: 4px solid #28a745;
        margin: 10px 0;
        border-radius: 0 8px 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🔍 Smart Code Reviewer")
st.markdown("*AI-powered code review for readability, structure, and maintainability*")

# Sidebar for API key and settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    demo_mode = st.checkbox("🎮 Demo Mode (no API key needed)", value=False,
                           help="Use mock data to preview the app")
    
    api_key = st.text_input("Google AI API Key", type="password", 
                            help="Get your free API key from https://makersuite.google.com/app/apikey",
                            disabled=demo_mode)
    
    st.markdown("---")
    
    language = st.selectbox("Programming Language", 
                           ["Python", "JavaScript", "TypeScript", "Java", "C++", "Go", "Rust", "Other"])
    
    review_focus = st.multiselect("Review Focus", 
                                  ["Readability", "Performance", "Security", "Best Practices", "Testing"],
                                  default=["Readability", "Best Practices"])
    
    experience_level = st.select_slider("Developer Level",
                                        options=["Junior", "Mid-Level", "Senior"],
                                        value="Mid-Level")
    
    st.markdown("---")
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. Enter your Google AI API key
    2. Paste your code snippet
    3. Click 'Review Code'
    4. Get instant feedback!
    """)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Your Code")
    
    # Sample code for demo
    sample_code = '''def calc(x,y,z):
    if x > 0:
        if y > 0:
            if z > 0:
                return x*y*z
            else:
                return 0
        else:
            return 0
    else:
        return 0'''
    
    code_input = st.text_area("Paste your code here:", 
                              value=sample_code,
                              height=400,
                              help="Paste the code snippet you want reviewed")
    
    context = st.text_input("Context (optional)", 
                           placeholder="e.g., This function calculates shipping costs")
    
    review_button = st.button("🚀 Review Code", type="primary", use_container_width=True)

with col2:
    st.subheader("📊 Review Results")
    
    if review_button:
        if not api_key and not demo_mode:
            st.error("⚠️ Please enter your Google AI API key in the sidebar or enable Demo Mode")
        elif not code_input.strip():
            st.error("⚠️ Please paste some code to review")
        elif demo_mode:
            # Demo mode - show mock results
            with st.spinner("🔍 Analyzing your code..."):
                import time
                time.sleep(1.5)  # Simulate API call
            
            # Mock results
            result = {
                "positive": "The function correctly handles the edge case of returning 0 when any input is non-positive, showing defensive programming awareness.",
                "scores": {"readability": 4, "maintainability": 5, "best_practices": 3},
                "improvements": [
                    {
                        "title": "Unclear Naming",
                        "problem": "Function name 'calc' and parameters 'x', 'y', 'z' don't describe their purpose",
                        "impact": "Other developers can't understand intent without reading the implementation",
                        "fix": "def calculate_volume(length: float, width: float, height: float) -> float:"
                    },
                    {
                        "title": "Nested Conditionals (Arrow Anti-pattern)",
                        "problem": "3 levels of nesting reduces readability significantly",
                        "impact": "Hard to trace logic flow, increases cognitive load and bug potential",
                        "fix": "def calculate_volume(length, width, height):\n    if length <= 0 or width <= 0 or height <= 0:\n        return 0\n    return length * width * height"
                    },
                    {
                        "title": "Missing Type Hints & Documentation",
                        "problem": "No type hints, docstring, or comments explaining the function",
                        "impact": "IDE can't provide autocomplete, unclear what types are expected",
                        "fix": 'def calculate_volume(length: float, width: float, height: float) -> float:\n    """Calculate volume of a rectangular prism."""\n    ...'
                    }
                ],
                "pro_tip": "Use guard clauses to handle edge cases early and keep your main logic at the lowest indentation level. This 'fail fast' pattern makes code easier to read and test."
            }
            
            # Display scores
            st.markdown("### 📈 Scores")
            score_cols = st.columns(3)
            scores = result.get("scores", {})
            
            with score_cols[0]:
                st.metric("Readability", f"{scores.get('readability', 'N/A')}/10")
            with score_cols[1]:
                st.metric("Maintainability", f"{scores.get('maintainability', 'N/A')}/10")
            with score_cols[2]:
                st.metric("Best Practices", f"{scores.get('best_practices', 'N/A')}/10")
            
            st.markdown("### ✅ What You Did Well")
            st.success(result.get("positive", "No positive feedback available"))
            
            st.markdown("### 🔧 Improvements")
            for i, imp in enumerate(result.get("improvements", []), 1):
                with st.expander(f"**{i}. {imp.get('title', 'Improvement')}**", expanded=True):
                    st.markdown(f"**Problem:** {imp.get('problem', '')}")
                    st.markdown(f"**Impact:** {imp.get('impact', '')}")
                    st.markdown("**Suggested Fix:**")
                    st.code(imp.get('fix', ''), language=language.lower())
            
            st.markdown("### 💡 Pro Tip")
            st.info(result.get("pro_tip", "Keep learning and practicing!"))
            
            st.warning("⚠️ Demo Mode: This is sample output. Use a real API key for actual code review.")
        else:
            try:
                # Configure Gemini - try multiple models
                genai.configure(api_key=api_key)
                
                # Try different models in order of preference
                models_to_try = ['gemini-1.5-flash-latest', 'gemini-1.5-pro-latest', 'gemini-pro']
                model = None
                for model_name in models_to_try:
                    try:
                        model = genai.GenerativeModel(model_name)
                        break
                    except:
                        continue
                
                if not model:
                    model = genai.GenerativeModel('gemini-pro')
                
                # Build the prompt
                prompt = f"""You are an expert code reviewer. Review this {language} code and provide feedback.

Developer Level: {experience_level}
Focus Areas: {', '.join(review_focus)}
Context: {context if context else 'Not provided'}

CODE TO REVIEW:
```{language.lower()}
{code_input}
```

Provide your review in this EXACT JSON format (no markdown, just raw JSON):
{{
    "positive": "One specific thing done well",
    "scores": {{
        "readability": 7,
        "maintainability": 6,
        "best_practices": 5
    }},
    "improvements": [
        {{
            "title": "Issue title",
            "problem": "What's wrong",
            "impact": "Why it matters",
            "fix": "Corrected code snippet"
        }},
        {{
            "title": "Issue title 2",
            "problem": "What's wrong",
            "impact": "Why it matters", 
            "fix": "Corrected code snippet"
        }},
        {{
            "title": "Issue title 3",
            "problem": "What's wrong",
            "impact": "Why it matters",
            "fix": "Corrected code snippet"
        }}
    ],
    "pro_tip": "One actionable tip to improve"
}}

Return ONLY valid JSON, no other text."""

                with st.spinner("🔍 Analyzing your code..."):
                    response = model.generate_content(prompt)
                    result_text = response.text.strip()
                    
                    # Clean up response if needed
                    if result_text.startswith("```"):
                        result_text = result_text.split("```")[1]
                        if result_text.startswith("json"):
                            result_text = result_text[4:]
                    
                    result = json.loads(result_text)
                
                # Display scores
                st.markdown("### 📈 Scores")
                score_cols = st.columns(3)
                scores = result.get("scores", {})
                
                with score_cols[0]:
                    st.metric("Readability", f"{scores.get('readability', 'N/A')}/10")
                with score_cols[1]:
                    st.metric("Maintainability", f"{scores.get('maintainability', 'N/A')}/10")
                with score_cols[2]:
                    st.metric("Best Practices", f"{scores.get('best_practices', 'N/A')}/10")
                
                # Positive note
                st.markdown("### ✅ What You Did Well")
                st.success(result.get("positive", "No positive feedback available"))
                
                # Improvements
                st.markdown("### 🔧 Improvements")
                for i, imp in enumerate(result.get("improvements", []), 1):
                    with st.expander(f"**{i}. {imp.get('title', 'Improvement')}**", expanded=True):
                        st.markdown(f"**Problem:** {imp.get('problem', '')}")
                        st.markdown(f"**Impact:** {imp.get('impact', '')}")
                        st.markdown("**Suggested Fix:**")
                        st.code(imp.get('fix', ''), language=language.lower())
                
                # Pro tip
                st.markdown("### 💡 Pro Tip")
                st.info(result.get("pro_tip", "Keep learning and practicing!"))
                
            except json.JSONDecodeError as e:
                st.error(f"Failed to parse AI response. Raw response:\n{response.text}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.info("👈 Paste your code and click 'Review Code' to get started!")
        
        # Show example output
        with st.expander("📋 Example Output Preview"):
            st.markdown("""
            **Scores:** Readability 4/10 | Maintainability 5/10 | Best Practices 3/10
            
            **✅ Positive:** The function correctly handles edge cases.
            
            **🔧 Improvements:**
            1. Use descriptive names instead of `calc`, `x`, `y`, `z`
            2. Flatten nested conditionals with guard clauses
            3. Add type hints and docstrings
            
            **💡 Pro Tip:** Use guard clauses for early returns!
            """)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit & Google Gemini AI | [Get API Key](https://makersuite.google.com/app/apikey)")
