import tkinter as tk
from tkinter import ttk, messagebox
import random
from flashcard_manager import load_flashcards, save_flashcard, get_topics

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        self.data = load_flashcards()

        self.cards = []
        self.index = 0
        self.current_card = None
        self.difficulty = "easy"

        
        notebook = ttk.Notebook(root)
        self.quiz_frame = tk.Frame(notebook, bg="#f0f0f0")
        self.add_frame = tk.Frame(notebook, bg="#f0f0f0")
        notebook.add(self.quiz_frame, text="Flashcards")
        notebook.add(self.add_frame, text="Add Flashcard")
        notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.build_flashcard_ui()
        self.build_add_ui()

    def build_flashcard_ui(self):
        """Build the flashcard UI components."""
        padding = {'padx': 10, 'pady': 5}

        
        ttk.Label(self.quiz_frame, text="Select Topic:", font=("Arial", 14), background="#f0f0f0").pack(**padding)

        
        self.subject_var = tk.StringVar()
        self.subject_menu = ttk.Combobox(self.quiz_frame, textvariable=self.subject_var, state="readonly", font=("Arial", 12))
        self.subject_menu["values"] = get_topics(self.data)
        self.subject_menu.pack(**padding)

        
        ttk.Label(self.quiz_frame, text="Select Difficulty:", font=("Arial", 14), background="#f0f0f0").pack(**padding)


        self.difficulty_var = tk.StringVar()
        self.difficulty_menu = ttk.Combobox(self.quiz_frame, textvariable=self.difficulty_var, state="readonly", font=("Arial", 12))
        self.difficulty_menu["values"] = ["easy", "medium", "hard"]
        self.difficulty_menu.set(self.difficulty)
        self.difficulty_menu.pack(**padding)


        self.start_button = ttk.Button(self.quiz_frame, text="Start Flashcards", command=self.start_flashcards)
        self.start_button.pack(**padding)

        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 16), wraplength=400, bg="#f0f0f0")
        self.question_label.pack(pady=20)


        self.show_answer_button = ttk.Button(self.quiz_frame, text="Show Answer", command=self.show_answer, state=tk.DISABLED)
        self.show_answer_button.pack(pady=10)


        self.answer_label = tk.Label(self.quiz_frame, text="", font=("Arial", 14), wraplength=400, bg="#f0f0f0")
        self.answer_label.pack(pady=10)


        self.next_button = ttk.Button(self.quiz_frame, text="Next Question", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

    def build_add_ui(self):
        """Build the add flashcard UI components."""
        padding = {'padx': 10, 'pady': 5}

        ttk.Label(self.add_frame, text="Topic:", font=("Arial", 14), background="#f0f0f0").pack(**padding)
        self.new_topic_var = tk.StringVar()
        self.new_topic_entry = ttk.Combobox(self.add_frame, textvariable=self.new_topic_var, font=("Arial", 12))
        self.new_topic_entry["values"] = get_topics(self.data)
        self.new_topic_entry.pack(**padding)

        ttk.Label(self.add_frame, text="Question:", font=("Arial", 14), background="#f0f0f0").pack(**padding)
        self.new_question_entry = tk.Entry(self.add_frame, font=("Arial", 12), width=40)
        self.new_question_entry.pack(**padding)

        ttk.Label(self.add_frame, text="Answer:", font=("Arial", 14), background="#f0f0f0").pack(**padding)
        self.new_answer_entry = tk.Entry(self.add_frame, font=("Arial", 12), width=40)
        self.new_answer_entry.pack(**padding)

        ttk.Label(self.add_frame, text="Difficulty:", font=("Arial", 14), background="#f0f0f0").pack(**padding)
        self.new_difficulty_var = tk.StringVar()
        self.difficulty_menu_add = ttk.Combobox(self.add_frame, textvariable=self.new_difficulty_var, font=("Arial", 12))
        self.difficulty_menu_add["values"] = ["easy", "medium", "hard"]
        self.difficulty_menu_add.set("easy")
        self.difficulty_menu_add.pack(**padding)

        self.save_button = ttk.Button(self.add_frame, text="Save Flashcard", command=self.save_flashcard)
        self.save_button.pack(pady=10)

    def start_flashcards(self):
        """Start showing flashcards based on selected topic and difficulty."""
        subject = self.subject_var.get()
        if subject not in self.data:
            messagebox.showwarning("Choose Topic", "Please select a valid topic.")
            return

     
        self.difficulty = self.difficulty_var.get()

        self.cards = self.filter_cards_by_topic_and_difficulty(self.data[subject])
        
        if not self.cards:
            messagebox.showinfo("No Cards", "No flashcards in this topic and difficulty level.")
            return

    
        random.shuffle(self.cards)
        
        self.index = 0
        self.show_answer_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)  
        self.show_question()


    def filter_cards_by_topic_and_difficulty(self, topic_data):
        """Filter flashcards by topic and difficulty level."""
        return topic_data.get(self.difficulty, [])

    def show_question(self):
        """Display the current question."""
        if self.index < len(self.cards):
            self.current_card = self.cards[self.index]
            self.question_label.config(text=f"Q{self.index + 1}: {self.current_card['question']}")
            self.answer_label.config(text="")  
        else:
            self.end_flashcards() 

    def show_answer(self):
        """Display the answer to the current question."""
        if self.current_card:
            self.answer_label.config(text=f"Answer: {self.current_card['answer']}")
            self.show_answer_button.config(state=tk.DISABLED)  
            self.next_button.config(state=tk.NORMAL)  
    
    def next_question(self):
        """Move to the next question."""
        self.index += 1  
        if self.index < len(self.cards):
            self.show_question()  # Show the next question
            self.show_answer_button.config(state=tk.NORMAL)   
            self.answer_label.config(text="")  
            self.next_button.config(state=tk.DISABLED) 
        else:
            self.end_flashcards()  



    def end_flashcards(self):
        """End the flashcards session."""
        self.question_label.config(text="")
        self.answer_label.config(text="")
        messagebox.showinfo("Session Finished", "You've gone through all the flashcards!")
        self.reset_flashcards()

    def reset_flashcards(self):
        """Reset the flashcards session variables."""
        self.cards = []
        self.index = 0
        self.current_card = None
        self.show_answer_button.config(state=tk.DISABLED) 


    def save_flashcard(self):
        """Save a new flashcard to the data structure."""
        topic = self.new_topic_var.get().strip()
        question = self.new_question_entry.get().strip()
        answer = self.new_answer_entry.get().strip()
        difficulty = self.new_difficulty_var.get().strip()

     
        if not topic or not question or not answer or not difficulty:
            messagebox.showwarning("Missing Info", "Please fill all fields.")
            return

           
        if topic not in self.data:
            self.data[topic] = {'easy': [], 'medium': [], 'hard': []}

        self.data[topic][difficulty].append({"question": question, "answer": answer})
     
        save_flashcard(self.data)

    
        self.subject_menu["values"] = get_topics(self.data)
        self.new_topic_entry["values"] = get_topics(self.data)

        
        self.new_question_entry.delete(0, tk.END)
        self.new_answer_entry.delete(0, tk.END)

        messagebox.showinfo("Saved", "Flashcard added successfully!")

