lecture_text = """
Artificial Intelligence is a branch of computer science.
Machine Learning helps computers learn from data.
Deep Learning uses neural networks.
AI is used in healthcare and education.
"""

print("AI-Powered Real-Time Lecture Analysis")
print("-" * 40)

sentences = lecture_text.split(".")

notes = []
for sentence in sentences:
    if sentence.strip():
        notes.append("• " + sentence.strip())

with open("study_notes.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(notes))

print("\nGenerated Notes:")
print("\n".join(notes))

print("\nStudy Notes Saved Successfully!")