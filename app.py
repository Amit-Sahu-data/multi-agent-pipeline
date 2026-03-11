# app.py
# Streamlit UI for Multi-Agent Pipeline

import streamlit as st
from pipeline import run_pipeline

# Page config
st.set_page_config(
    page_title="Multi-Agent Pipeline",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Multi-Agent Research Pipeline")
st.caption("Enter a topic → Agent 1 researches → Agent 2 summarizes → Agent 3 writes email")

# Show pipeline flow
st.markdown("""
```
Researcher Agent → Summarizer Agent → Email Writer Agent
```
""")

st.divider()

# Input
topic = st.text_input(
    "Enter a topic to research:",
    placeholder="e.g. AI agents trends 2025"
)

# Run button
if st.button("🚀 Run Pipeline", type="primary"):
    if not topic:
        st.warning("Please enter a topic first!")
    else:
        # Run all 3 agents with progress indicators
        with st.status("Running Multi-Agent Pipeline...", expanded=True) as status:

            st.write("🔍 Researcher Agent searching the web...")
            from researcher import research_topic
            research = research_topic(topic)
            st.write("✅ Research complete!")

            st.write("📝 Summarizer Agent condensing research...")
            from summarizer import summarize_research
            summary = summarize_research(research, topic)
            st.write("✅ Summary complete!")

            st.write("📧 Email Writer Agent drafting email...")
            from email_writer import write_email
            email = write_email(summary, topic)
            st.write("✅ Email complete!")

            status.update(label="Pipeline Complete!", state="complete")

        st.divider()

        # Show results in tabs
        tab1, tab2, tab3 = st.tabs(["🔍 Research", "📝 Summary", "📧 Email"])

        with tab1:
            st.subheader("Research Notes")
            st.markdown(research)

        with tab2:
            st.subheader("Summary")
            st.markdown(summary)

        with tab3:
            st.subheader("Email Draft")
            st.markdown(email)
            st.divider()
            # Copy button
            st.code(email, language=None)
            st.caption("Copy the email above and paste it anywhere!")