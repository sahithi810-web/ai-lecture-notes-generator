import streamlit as st

st.title("AI-Powered Real-Time Lecture Analysis")
st.write("Personalized Study Notes Generator")

lecture_text = st.text_area(
    "Paste Lecture Text Here",
    height=200
)

if st.button("Generate Notes"):
    sentences = lecture_text.split(".")

    notes = []
    for sentence in sentences:
        if sentence.strip():
            notes.append("• " + sentence.strip())

    st.subheader("Generated Study Notes")
    st.write("\n".join(notes))

    with open("study_notes.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(notes))

    st.success("Study Notes Saved Successfully!")