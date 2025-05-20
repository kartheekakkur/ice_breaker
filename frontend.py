import streamlit as st
import requests

name = st.text_area("Enter the name of person you want break ice with")
if st.button("Get Ice Breaker"):
    # Make a request to the FastAPI backend
    response = requests.get(f"http://localhost:8000/ice_break/{name}")
    
    if response.status_code == 200:
        data = response.json()
        summary_and_facts = data.get("summary_and_facts", {})
        summary = summary_and_facts.get("summary", "")
        facts = summary_and_facts.get("facts", [])

        st.markdown("**Summary:**")
        st.write(summary)
        st.markdown("**Facts:**")
        for fact in facts:
            st.write(f"- {fact}")
    else:
        st.error("Error fetching data from the API.")