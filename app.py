import streamlit as st
import time

# Page config
st.set_page_config(page_title="Domestika AI Career Assistant", layout="wide")

# Session state setup
if "show_assistant" not in st.session_state:
    st.session_state["show_assistant"] = False

# --- LANDING PAGE ---
if not st.session_state["show_assistant"]:
    st.markdown("""
    <style>
        .banner {
            background: #ffe7e1;
            padding: 2rem;
            border-radius: 12px;
        }
        .course-box {
            display: flex;
            gap: 1.5rem;
            margin-top: 2rem;
        }
        .course-tile {
            width: 300px;
        }
        .chat-popup {
            position: fixed;
            bottom: 40px;
            right: 40px;
            background-color: white;
            border: 2px solid #7b2ff7;
            border-radius: 12px;
            padding: 1rem;
            width: 280px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            z-index: 100;
        }
        .chat-popup button {
            background-color: #7b2ff7;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            margin-top: 10px;
            cursor: pointer;
        }
    </style>
    """, unsafe_allow_html=True)

    # Content
    st.markdown("""
    <div class='banner'>
        <h1 style='color:#d72d1f;'>🔥 SALE: All courses from ₹74.00 each!</h1>
        <p style='font-size:1.2rem;'>Explore our most popular creative courses and learn from world-class professionals.</p>
    </div>

    <h2>📈 Popular Courses</h2>
    <div class="course-box">
        <div class="course-tile">
            <img src="https://img-c.udemycdn.com/course/240x135/4823468_1c98_3.jpg" width="100%" />
            <b>Canva for Beginners: Create Professional Designs</b><br/>
            <small>A course by Clàudia Cánovas</small>
        </div>
        <div class="course-tile">
            <img src="https://img-c.udemycdn.com/course/240x135/4825112_1f63_3.jpg" width="100%" />
            <b>Using ChatGPT for Work</b><br/>
            <small>A course by Víctor Mollá</small>
        </div>
        <div class="course-tile">
            <img src="https://img-c.udemycdn.com/course/240x135/4824744_a10a_2.jpg" width="100%" />
            <b>Drawing for Beginners Level -1</b><br/>
            <small>A course by Puño</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Chatbot popup
    st.markdown("""
    <div class="chat-popup">
        <b>🤖 Botestika:</b><br/>
        Hi, I'm Botestika! How can I help you with your creative journey?
        <br/>
        <form>
            <button name="start" value="yes">Launch Assistant</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

    # Trigger assistant
    if st.query_params.get("start") == "yes":
        st.session_state["show_assistant"] = True
        st.rerun()

    st.stop()

# --- ASSISTANT UI (After Launch) ---

# Header
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(to right, #7b2ff7, #f107a3); border-radius: 16px; color: white;'>
    <h1>Domestika AI Career Assistant</h1>
    <p>Personalized guidance for your creative career growth</p>
</div>
""", unsafe_allow_html=True)

# Tabs for assistant features
tab1, tab2 = st.tabs(["🧠 SkillScope", "🧑‍🤝‍🧑 Domestika Crew"])

# === Tab 1: SkillScope (for Nandu) ===
with tab1:
    st.header("🧠 SkillScope – Upskill with a Purpose")
    st.subheader("Upload your resume to get started")
    resume_file = st.file_uploader("📄 Upload Resume", type=["pdf", "docx"])

    if resume_file:
        st.success("✅ Resume uploaded!")
        with st.spinner("Generating learning roadmap..."):
            time.sleep(2)

        st.markdown("### 📘 6-Month Learning Plan")
        st.markdown("""
        - **Month 1-2**: AI Tools for Designers  
        - **Month 3-4**: Blender for 3D  
        - **Month 5-6**: Interactive Design with TouchDesigner
        """)

        st.markdown("### 📚 Recommended Domestika Courses")
        cols = st.columns(3)
        with cols[0]:
            st.image("https://www.domestika.org/en/courses/3159-kawaii-character-creation-in-3d-with-blender/cover.jpg", width=200)
            st.caption("🎨 Content Creation with AI – Núria Mañé")
        with cols[1]:
            st.image("https://www.domestika.org/en/courses/92-introduction-to-3d-design-and-modeling-with-blender/cover.jpg", width=200)
            st.caption("🧱 3D Design with Blender – Luis Arizaga")
        with cols[2]:
            st.image("https://www.domestika.org/en/courses/5560-creating-ai-generated-visuals-for-creative-inspiration/cover.jpg", width=200)
            st.caption("💡 AI Visuals – Ben Mornin")

        st.markdown("### ✨ AI Feedback on Your Work")
        project = st.text_area("Describe your recent creative project:")
        if project:
            with st.spinner("Analyzing..."):
                time.sleep(2)
            st.success("AI Feedback:")
            st.write("- Strong creativity, but needs refinement in shading")
            st.write("- Try stylized lighting in Blender")

# === Tab 2: Domestika Crew (for Nandita) ===
with tab2:
    st.header("🧑‍🤝‍🧑 Domestika Crew – Discover Your Path")
    st.subheader("Choose your interests")
    interests = st.multiselect("🎯 I'm curious about:", [
        "Illustration", "3D Modeling", "Motion Design", "UI Design", "AI Tools"
    ])

    if interests:
        with st.spinner("Curating recommendations..."):
            time.sleep(2)

        st.markdown("### 👩‍🏫 Mentors")
        st.markdown("- Sara Lopez – Illustrator ($35/session)\n- Mike Dawson – 3D Mentor ($50/session)")

        st.markdown("### 🎓 Suggested Courses")
        st.markdown("- AI for Creatives\n- Beginner's Blender\n- Design Portfolio Bootcamp")

        st.markdown("### 💬 Share Your Idea for Feedback")
        idea = st.text_area("I'm thinking of creating...")
        if idea:
            with st.spinner("AI is reviewing..."):
                time.sleep(2)
            st.success("Here's what we think:")
            st.write("- Nice concept! Try enhancing contrast.")
            st.write("- Consider a style moodboard first.")
