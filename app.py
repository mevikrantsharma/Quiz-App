import tkinter as tk
from tkinter import messagebox
import json

TIME_LIMIT=10
class QuizApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Quiz App with Timer")
        self.root.geometry("700x350")
        self.root['bg']='light blue'
        self.questions=self.load_questions("questions.json")
        self.score=0
        self.q_index=0
        self.selected_option=tk.StringVar()
        self.time_left=TIME_LIMIT
        self.timer_label=None
        self.timer_id=None
        self.create_widgets()
        self.display_question()
        
    def create_widgets(self):
        self.question_label=tk.Label(self.root,font=("Arial",15))
        self.radiobuttons=[]
        self.question_label.pack(pady=20)
        for _ in range(4):
            rb=tk.Radiobutton(self.root,text="",variable=self.selected_option,value="",font=("Arial",14))
            rb.pack()
            self.radiobuttons.append(rb)
        self.timer_label=tk.Label(self.root,text='',font=("Arial",15),fg="white", bg='red')
        self.timer_label.place(x=10, y=10)
        self.next_button=tk.Button(self.root,text="Next",font=("Arial",15),command=self.next_question)
        self.next_button.pack(pady=20)  
    def display_question(self):
        self.time_left=TIME_LIMIT
        self.update_timer()
        q=self.questions[self.q_index]
        self.question_label.config(text=f'{self.q_index+1}.{q["question"]}')
        self.selected_option.set(None)
        for i,option in enumerate(q['options']):
            self.radiobuttons[i].config(text=option,value=option)
    def update_timer(self):
        self.timer_label.config(text=f"TimeLeft:{self.time_left}s")
        if self.time_left>0:
            self.time_left-=1
            self.timer_id=self.root.after(1000,self.update_timer)
        else:
            messagebox.showinfo("Time's Up","Moving to next Question")
            self.auto_next()
    def auto_next(self):
        selected=self.selected_option.get()
        if selected==self.questions[self.q_index]['answer']:
            self.score+=1
        self.q_index+=1
        if self.q_index<len(self.questions):
            self.display_question()
        else:
            self.show_result()
# ====================================================================================
    # def load_questions(self,file):
    #     f=open(file,"r")
    #     Q=json.load(f)
    #     return Q
    def load_questions(self, file):
        with open(file, "r", encoding="utf-8") as f:
            Q = json.load(f)
        return Q
# =====================================================================================

    def next_question(self):
        self.root.after_cancel(self.timer_id)
        selected=self.selected_option.get()
        if selected=='None':
            messagebox.showwarning("Warning","Please Select Answer")
            return
        if selected==self.questions[self.q_index]['answer']:
            self.score+=1
        self.q_index+=1
        if self.q_index<len(self.questions):
            self.display_question()
        else:
            self.show_result()
    def show_result(self):
        messagebox.showinfo("Quiz Completed",f'Your Score: {self.score}/{len(self.questions)}')
        self.root.destroy()     
                            


root=tk.Tk() # Creating Window
app=QuizApp(root)



 
