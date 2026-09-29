
import streamlit as st

from okf.answer import generate_answer


st.set_page_config(
    page_title="OpsMind",
    page_icon="🧠"
)

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0f172a;
        color: #e5e7eb;
    }

    .main-title {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 18px;
        margin-bottom: 25px;
    }

    /* Question input box */
    .stTextArea textarea {
        background-color: #1e293b !important;
        color: #e5e7eb !important;
        border: 1px solid #475569 !important;
        border-radius: 10px !important;
    }

    .stTextArea textarea::placeholder {
        color: #94a3b8 !important;
    }

    /* Answer box */
    .answer-box {
        background-color: #1e293b;
        color: #e5e7eb;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #334155;
        margin-top: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-title">🧠 OpsMind</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Internal Engineering Knowledge Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Ask questions about services, incidents, runbooks, "
    "architecture, and company policies."
)

st.divider()


query = st.text_area(
    "Ask your question",
    placeholder="Example: Why are orders failing?"
)


if st.button("Ask OpsMind"):

    if not query.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching OpsMind..."):

            answer = generate_answer(query)

        st.subheader("Answer")

        st.markdown(
            f"""
            <div class="answer-box">
                {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

