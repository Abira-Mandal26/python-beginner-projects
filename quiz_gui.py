import tkinter as tk
from tkinter import messagebox

# Quiz Data
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "define", "def", "lambda"],
        "answer": "def"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    }
]

question_index = 0
score = 0


def next_question():
    global question_index

    if question_index < len(questions):
        q = questions[question_index]

        question_label.config(text=q["question"])

        for i in range(4):
            options[i].config(text=q["options"][i])

        selected_option.set(None)
    else:
        messagebox.showinfo("Quiz Finished", f"Your Score: {score}/{len(questions)}")
        root.quit()


def check_answer():
    global score, question_index

    selected = selected_option.get()

    if selected == questions[question_index]["answer"]:
        score += 1

    score_label.config(text=f"Score: {score}")

    question_index += 1
    next_question()


# Window
root = tk.Tk()
root.title("Python Quiz App")
root.geometry("500x350")
root.config(bg="#f0f8ff")

# Question Label
question_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f8ff")
question_label.pack(pady=20)

selected_option = tk.StringVar()

options = []

for i in range(4):
    rb = tk.Radiobutton(
        root,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 12),
        bg="#f0f8ff"
    )
    rb.pack(anchor="w", padx=100)
    options.append(rb)

# Update radio button values dynamically
def update_values():
    for i in range(4):
        options[i].config(value=questions[question_index]["options"][i])


# Submit Button
submit_button = tk.Button(root, text="Next Question", command=lambda:[check_answer(), update_values()], bg="#4CAF50", fg="white")
submit_button.pack(pady=20)

# Score Label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 12), bg="#f0f8ff")
score_label.pack()

next_question()
update_values()

root.mainloop()