import streamlit as st

from okf.answer import generate_answer


st.set_page_config(
    page_title="OpsMind",
    page_icon="🧠",
    layout="wide"
)


st.title("🧠 OpsMind")
st.subheader("Internal Engineering Knowledge Assistant")

st.write(
    "Ask questions about company services, incidents, "
    "runbooks, architecture, and policies."
)


query = st.text_input(
    "Ask your question",
    placeholder="Example: Why are orders failing?"
)


if st.button("Ask OpsMind"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching knowledge base..."):
            answer = generate_answer(query)

        st.markdown("### Answer")
        st.write(answer)