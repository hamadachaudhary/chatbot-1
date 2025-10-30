import streamlit as st
from openai import OpenAI
import re
import json
from typing import List, Dict, Set

# Page configuration
st.set_page_config(
    page_title="AI Resume Bullet Point Generator",
    page_icon="📝",
    layout="wide"
)

# Title and description
st.title("📝 AI-Powered Resume Bullet Point Generator")
st.write(
    """
    This advanced tool generates 20 tailored resume bullet points aligned with your target job description.
    Using cognitive frameworks (Skeleton of Thoughts, Tree of Thoughts, and Chain-of-Thought reasoning),
    it creates mutually exclusive, collectively exhaustive bullet points that match 80%+ of JD keywords.
    """
)

# Sidebar for API key
with st.sidebar:
    st.header("⚙️ Configuration")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This tool uses:
    - **Skeleton of Thoughts**: Initial framework generation
    - **Tree of Thoughts**: Deep analysis and branching
    - **Chain-of-Thought**: Fine-tuning and validation
    """)

def extract_keywords_from_jd(job_description: str) -> Set[str]:
    """Extract meaningful keywords from job description."""
    # Remove common words and extract meaningful terms
    stop_words = {'the', 'and', 'or', 'to', 'of', 'a', 'in', 'on', 'for', 'with', 'is', 'as', 'by', 'at', 'be', 'this', 'that'}
    
    # Convert to lowercase and split into words
    words = re.findall(r'\b[a-zA-Z]+\b', job_description.lower())
    
    # Filter out stop words and short words
    keywords = {word for word in words if word not in stop_words and len(word) > 3}
    
    # Also extract phrases (2-3 word combinations)
    text = job_description.lower()
    phrases = re.findall(r'\b(?:[a-z]+\s+){1,2}[a-z]+\b', text)
    keywords.update(phrase.strip() for phrase in phrases if len(phrase.strip()) > 10)
    
    return keywords

def calculate_keyword_match(bullet_points: List[str], jd_keywords: Set[str]) -> float:
    """Calculate percentage of JD keywords covered by bullet points."""
    bullet_text = ' '.join(bullet_points).lower()
    matched_keywords = sum(1 for keyword in jd_keywords if keyword in bullet_text)
    match_percentage = (matched_keywords / len(jd_keywords)) * 100 if jd_keywords else 0
    return match_percentage

def generate_system_prompt() -> str:
    """Generate the comprehensive system prompt with cognitive frameworks."""
    return """You are a highly knowledgeable cognitive scientist and expert resume writer with expertise in advanced problem-solving techniques, natural language processing, and thought organization methods. You possess deep understanding of various cognitive frameworks and are skilled at integrating these methodologies.

COGNITIVE FRAMEWORK APPROACH:

1. **Skeleton of Thoughts Method** (Initial Framework):
   - Map out core concepts from the job description
   - Identify key competencies, skills, and requirements
   - Create a comprehensive framework of what the role demands

2. **Tree of Thoughts Method** (Deep Analysis):
   - Branch out from initial concepts to explore connections
   - Identify explicit and implicit requirements
   - Map relationships between different skill areas
   - Consider career progression elements

3. **Chain-of-Thought Reasoning** (Fine-tuning):
   - Connect insights across different branches
   - Ensure logical flow and coherence
   - Validate uniqueness and impact of each bullet point
   - Verify keyword coverage and alignment

Your task is to generate resume bullet points that are professional, impactful, and perfectly aligned with the job description."""

def generate_user_prompt(job_description: str) -> str:
    """Generate the detailed user prompt."""
    return f"""Generate 20 unique and impactful resume bullet points aligned with the job description below.

CRITICAL REQUIREMENTS:

1. **Unique Action Verbs**: Start each bullet with a DIFFERENT strong action verb in past tense (no repeats)
2. **Quantification**: Include metrics, dollar figures, or percentages in each bullet
3. **Alignment**: Match skills and experiences to the JD requirements
4. **Impact Focus**: Emphasize major contributions and positive results
5. **Keyword Integration**: Incorporate BOTH obvious and subtle keywords from the JD
6. **Conciseness**: Keep each bullet to 1-2 lines maximum
7. **Career Progression**: Collectively demonstrate growth relevant to the role
8. **No Employer Names**: Exclude specific company names
9. **No Repetition**: Ensure no overlap in content or meaning
10. **Mutually Exclusive & Collectively Exhaustive**: Each bullet is unique, together they cover all JD aspects

PROCESS:
- Start with Skeleton of Thoughts: Map all JD requirements
- Apply Tree of Thoughts: Branch out to explore connections
- Use Chain-of-Thought: Fine-tune for impact and coherence
- Verify: Ensure 80%+ JD keyword coverage

JOB DESCRIPTION:
{job_description}

OUTPUT FORMAT:
Return ONLY a JSON object with this exact structure:
{{
    "bullet_points": [
        "Bullet point 1",
        "Bullet point 2",
        ...
        "Bullet point 20"
    ],
    "analysis": {{
        "skeleton_insights": "Brief description of initial framework",
        "tree_analysis": "Brief description of branching analysis",
        "cot_refinement": "Brief description of refinements made"
    }}
}}

Generate exactly 20 bullet points that are achievement-focused and collectively represent the candidate as an outstanding performer, not just a task-completer."""

def validate_and_regenerate(client: OpenAI, job_description: str, max_attempts: int = 3) -> Dict:
    """Generate bullet points with validation loop."""
    jd_keywords = extract_keywords_from_jd(job_description)
    
    system_prompt = generate_system_prompt()
    user_prompt = generate_user_prompt(job_description)
    
    for attempt in range(max_attempts):
        with st.spinner(f"🧠 Generating bullet points (Attempt {attempt + 1}/{max_attempts})..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4-turbo-preview",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.7,
                    response_format={"type": "json_object"}
                )
                
                result = json.loads(response.choices[0].message.content)
                bullet_points = result.get("bullet_points", [])
                
                if len(bullet_points) != 20:
                    st.warning(f"⚠️ Attempt {attempt + 1}: Generated {len(bullet_points)} bullets instead of 20. Retrying...")
                    continue
                
                # Calculate keyword match
                match_percentage = calculate_keyword_match(bullet_points, jd_keywords)
                
                st.info(f"📊 Attempt {attempt + 1}: Keyword match = {match_percentage:.1f}%")
                
                if match_percentage >= 80:
                    st.success(f"✅ Successfully generated bullet points with {match_percentage:.1f}% keyword match!")
                    result["match_percentage"] = match_percentage
                    result["keywords_total"] = len(jd_keywords)
                    return result
                else:
                    if attempt < max_attempts - 1:
                        st.warning(f"⚠️ Keyword match {match_percentage:.1f}% is below 80%. Regenerating...")
                        # Add feedback to improve next attempt
                        user_prompt += f"\n\nPREVIOUS ATTEMPT FEEDBACK: The previous attempt only matched {match_percentage:.1f}% of keywords. Please incorporate more keywords from the job description, especially focusing on: {', '.join(list(jd_keywords)[:20])}"
                    else:
                        st.warning(f"⚠️ Final attempt reached {match_percentage:.1f}% match. Proceeding with best result.")
                        result["match_percentage"] = match_percentage
                        result["keywords_total"] = len(jd_keywords)
                        return result
                        
            except Exception as e:
                st.error(f"❌ Error on attempt {attempt + 1}: {str(e)}")
                if attempt == max_attempts - 1:
                    raise
    
    return None

# Main application
if openai_api_key:
    client = OpenAI(api_key=openai_api_key)
    
    # Input section
    st.header("1️⃣ Input Job Description")
    
    # Example JD in expander
    with st.expander("📋 View Example Job Description"):
        st.code("""Manage multiple day-to-day roles that include project delivery, client relationship management, team building, and business development. Support and guide the planning, budgeting, quality management, and resource management of consulting (client) and internal (within KPMG) projects; Stay abreast on current business and economic developments relevant to the client's business, and use current technology and tools to enhance the effectiveness of services provided; Provide technical guidance on client assignments including preparation of reports, position papers, and manage the implementation/ adoption of IFRS and ensure projects are delivered according to client specifications and within set timelines; Lead projects which require specialist technical accounting advice and support on accounting for proposed and actual transactions; Assist clients in preparing for and completing audits, and liaising with the auditor; Contribute to review(s) on completion of projects to identify lessons learned and enhance future quality and commercial planning Assist on financial statement conversions projects to and from IFRS; Provide IFRS training to clients and KPMG personnel; Continuously review project's performance against preset objectives and milestones to ensure quality control throughout its life cycle while identifying and addressing key challenges/lessons learnt; Ensure effective operation of projects by managing and facilitating flow of essential information and feedback among project stakeholders; regularly and effectively communicate project expectations and updates; As a key member of the team, the role includes wider practice management responsibilities such as market and brand initiatives, including the development of new service offerings/competency development, including supporting the delivery of annual IFRS Update Training; Build presence in the marketplace, network and build relationships, and identify opportunities for work; from lead identification to the presentation of pitches and proposals; and Supervise, coach and mentor junior staff. Conduct performance reviews and contribute to performance feedback and training.""")
    
    job_description = st.text_area(
        "Paste the complete job description here:",
        height=300,
        placeholder="Paste the full job description including responsibilities, requirements, qualifications, etc."
    )
    
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        generate_button = st.button("🚀 Generate Bullet Points", type="primary", use_container_width=True)
    
    with col2:
        if st.button("🔄 Clear", use_container_width=True):
            st.session_state.clear()
            st.rerun()
    
    # Generation and display section
    if generate_button:
        if not job_description or len(job_description.strip()) < 100:
            st.error("❌ Please provide a complete job description (at least 100 characters).")
        else:
            try:
                result = validate_and_regenerate(client, job_description)
                
                if result:
                    st.session_state['result'] = result
                    st.session_state['job_description'] = job_description
                else:
                    st.error("❌ Failed to generate bullet points. Please try again.")
                    
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
    
    # Display results if available
    if 'result' in st.session_state:
        result = st.session_state['result']
        
        st.markdown("---")
        st.header("2️⃣ Generated Resume Bullet Points")
        
        # Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Bullet Points", len(result['bullet_points']))
        with col2:
            st.metric("Keyword Match", f"{result.get('match_percentage', 0):.1f}%")
        with col3:
            status = "✅ Passed" if result.get('match_percentage', 0) >= 80 else "⚠️ Below Target"
            st.metric("Validation Status", status)
        
        # Bullet points
        st.subheader("📝 Your Tailored Bullet Points")
        
        for i, bullet in enumerate(result['bullet_points'], 1):
            st.markdown(f"**{i}.** {bullet}")
        
        # Analysis section
        st.markdown("---")
        st.header("3️⃣ Cognitive Framework Analysis")
        
        if 'analysis' in result:
            analysis = result['analysis']
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.subheader("🌱 Skeleton of Thoughts")
                st.write(analysis.get('skeleton_insights', 'N/A'))
            
            with col2:
                st.subheader("🌳 Tree of Thoughts")
                st.write(analysis.get('tree_analysis', 'N/A'))
            
            with col3:
                st.subheader("⛓️ Chain-of-Thought")
                st.write(analysis.get('cot_refinement', 'N/A'))
        
        # Export options
        st.markdown("---")
        st.header("4️⃣ Export Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Plain text export
            bullet_text = "\n".join([f"{i}. {bullet}" for i, bullet in enumerate(result['bullet_points'], 1)])
            st.download_button(
                label="📄 Download as Text",
                data=bullet_text,
                file_name="resume_bullet_points.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col2:
            # JSON export
            json_export = json.dumps(result, indent=2)
            st.download_button(
                label="📊 Download as JSON",
                data=json_export,
                file_name="resume_bullet_points.json",
                mime="application/json",
                use_container_width=True
            )

else:
    st.info("👈 Please enter your OpenAI API key in the sidebar to begin.", icon="🗝️")
    
    # Show features
    st.markdown("---")
    st.header("✨ Key Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Cognitive Frameworks
        - **Skeleton of Thoughts**: Initial mapping
        - **Tree of Thoughts**: Deep analysis
        - **Chain-of-Thought**: Fine-tuning
        
        ### Quality Assurance
        - ✅ 80%+ keyword match validation
        - ✅ Unique action verbs (no repeats)
        - ✅ Quantified achievements
        - ✅ No content overlap
        """)
    
    with col2:
        st.markdown("""
        ### Bullet Point Criteria
        - 🎯 Aligned with JD requirements
        - 📊 Quantified with metrics
        - 💪 Impact-focused language
        - 🔑 Keyword-optimized
        
        ### Output Quality
        - ✅ 20 unique bullet points
        - ✅ Mutually exclusive content
        - ✅ Collectively exhaustive coverage
        - ✅ Achievement-oriented tone
        """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
    Built with Streamlit • Powered by OpenAI GPT-4 • Using Advanced Cognitive Frameworks
    </div>
    """,
    unsafe_allow_html=True
)
