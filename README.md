# 📝 AI-Powered Resume Bullet Point Generator

An advanced Streamlit application that generates 20 tailored resume bullet points aligned with any job description using cognitive frameworks and AI.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-template.streamlit.app/)

## 🌟 Features

### Cognitive Framework Approach

This tool implements three advanced cognitive methodologies:

1. **Skeleton of Thoughts Method**
   - Maps core concepts from the job description
   - Identifies key competencies and requirements
   - Creates comprehensive framework of role demands

2. **Tree of Thoughts Method**
   - Branches out to explore connections
   - Identifies explicit and implicit requirements
   - Maps relationships between skill areas
   - Considers career progression elements

3. **Chain-of-Thought Reasoning**
   - Connects insights across branches
   - Ensures logical flow and coherence
   - Validates uniqueness and impact
   - Verifies keyword coverage

### Quality Criteria

Each of the 20 bullet points generated will:

✅ **Start with unique action verbs** (no repeats, past tense)  
✅ **Include quantification** (metrics, percentages, dollar figures)  
✅ **Align with JD requirements** (explicit and subtle)  
✅ **Emphasize impact** (achievements, not just duties)  
✅ **Incorporate JD keywords** (both obvious and subtle)  
✅ **Be concise** (1-2 lines each)  
✅ **Show progression** (collectively demonstrate growth)  
✅ **Exclude employer names** (maintain generality)  
✅ **Avoid repetition** (mutually exclusive content)  
✅ **Cover comprehensively** (collectively exhaustive)

### Validation System

- **80%+ Keyword Match**: Automatically validates that bullet points cover at least 80% of job description keywords
- **Iterative Refinement**: If validation fails, automatically regenerates with improvements
- **Real-time Feedback**: Shows match percentage and validation status

## 🚀 How to Use

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/account/api-keys))

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

4. Open your browser to the URL shown (typically `http://localhost:8501`)

### Using the Application

1. **Enter API Key**: Input your OpenAI API key in the sidebar
2. **Paste Job Description**: Copy and paste the complete job description
3. **Generate**: Click "🚀 Generate Bullet Points"
4. **Review**: Check the generated bullet points and keyword match percentage
5. **Export**: Download as text or JSON format

## 📊 Output Format

The application provides:

- **20 Tailored Bullet Points**: Ready to use in your resume
- **Keyword Match Analysis**: Percentage of JD keywords covered
- **Cognitive Framework Insights**: Explanation of the analysis process
- **Export Options**: Plain text and JSON formats

## 🎯 Example Use Case

**Input**: Job description for a Senior IFRS Consultant position requiring:
- 12+ years experience
- IFRS expertise (IFRS 17, 9, 15)
- Project management
- Client relationship management
- Team leadership
- Business development

**Output**: 20 unique bullet points like:
- "Orchestrated implementation of IFRS 17 insurance contracts standard for 15+ multinational clients, delivering $8M in compliance value"
- "Spearheaded cross-functional teams of 8-12 professionals across complex financial statement conversion projects, achieving 98% on-time delivery"
- etc.

## 🛠️ Technical Details

### Models Used
- **GPT-4 Turbo**: For advanced reasoning and bullet point generation
- **JSON Mode**: Ensures structured, parsable output

### Key Components

1. **Keyword Extraction**: Intelligent parsing of job descriptions
2. **Validation Loop**: Automatic regeneration until 80% match achieved
3. **Cognitive Framework Integration**: Systematic approach to content generation
4. **Quality Assurance**: Checks for uniqueness, quantification, and impact

### Files Structure

```
.
├── streamlit_app.py      # Main application
├── requirements.txt      # Python dependencies
├── README.md            # Documentation (this file)
└── LICENSE              # License information
```

## 📋 Requirements

```
streamlit
openai
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## 💡 Tips for Best Results

1. **Complete Job Descriptions**: Paste the full JD including responsibilities, requirements, qualifications
2. **Detailed JDs**: More detailed job descriptions yield better-tailored results
3. **Multiple Generations**: Try generating multiple times for variety
4. **Customization**: Review and customize the generated bullets to match your actual experience

## 🔧 Troubleshooting

**Issue**: Keyword match below 80%
- **Solution**: The app will automatically regenerate up to 3 times

**Issue**: API errors
- **Solution**: Verify your OpenAI API key is valid and has available credits

**Issue**: Generated fewer than 20 bullets
- **Solution**: The app will automatically retry generation

## 📞 Support

For issues or questions, please open an issue in the repository.

---

Built with ❤️ using Streamlit and OpenAI GPT-4
