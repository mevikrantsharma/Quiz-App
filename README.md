# Quiz-App

## Overview
The **Quiz App with Timer** is a Python-based interactive quiz application developed using **Tkinter** for the GUI and **JSON** for storing quiz questions and answers. The app displays a set of multiple-choice questions, where users can select answers and are given a set time to answer each question. The timer counts down for each question, and if the time runs out, the app automatically proceeds to the next question. At the end of the quiz, the app displays the final score.

---

## Features

- **Interactive GUI:** Built with Tkinter to present a user-friendly interface for answering quiz questions.
- **Timer Integration:** Each question has a countdown timer (10 seconds). The app auto-moves to the next question when time is up.
- **Dynamic Questions:** Quiz questions and options are loaded from a JSON file, allowing easy modifications and updates.
- **Score Display:** Shows the user's score after completing the quiz.
- **Responsive Design:** The app uses a light blue theme and a clean, minimalist design for better user experience.

---

## Use Cases

- **Education:** Can be used for creating timed quizzes or assessments in educational settings.
- **Practice:** Perfect for users who want to practice general knowledge or improve their time-bound answering skills.
- **Learning Tool:** Can be used as a tool for self-assessment in various domains like history, geography, and science.

---

## Installation

1. Clone this repository to your local machine:

   ```bash```
   git clone https://github.com/your-username/quiz-app-with-timer.git

2. Navigate into the project folder:

  ```bash```
   cd quiz-app-with-timer

3. Ensure you have Python installed (Python 3.x recommended).

4. Install necessary dependencies:

   ```bash```
    pip install -r requirements.txt
   
**How to Run**

1. Run the main application script:

  ```bash```
  python app.py
  
2. The quiz will start, displaying questions one by one with a countdown timer.

3. After completing the quiz, your final score will be displayed.

**Technologies Used**
  Python (3.x)
  Tkinter for GUI
  JSON for storing quiz questions and answers
  Messagebox for user alerts and score display
