# AI Study Planner

## 📌 Overview

AI Study Planner is a **Command Line Interface (CLI)** application that
generates a personalized study schedule based on user inputs such as
subjects, deadlines, difficulty levels, and required study hours.

The project uses **rule-based AI logic** (priority calculation and
scheduling) and works completely offline without any external APIs.

------------------------------------------------------------------------

## 🚀 Features

-   Add subjects with deadline, difficulty, and required hours\
-   Automatic priority calculation\
-   Smart study plan generation\
-   Balanced daily time allocation\
-   Actionable study suggestions\
-   Lightweight and fast (CLI-based)

------------------------------------------------------------------------

## ⚙️ How It Works

1.  User inputs subject details\
2.  System calculates priority using:
    -   Deadline proximity\
    -   Difficulty level\
    -   Required study hours\
3.  Subjects are sorted by priority\
4.  Time is distributed across available days\
5.  Final study plan is generated

------------------------------------------------------------------------

## 🛠️ Installation

``` bash
git clone https://github.com/your-username/ai-study-planner-cli.git
cd ai-study-planner-cli
python main.py
```

------------------------------------------------------------------------

## ▶️ Usage

``` bash
python main.py
```

Follow the CLI menu: - Add subjects\
- Generate study plan

------------------------------------------------------------------------

## 🧪 Input Example

Subject: Math\
Deadline: 2026-04-10\
Difficulty: 5\
Hours Required: 10

------------------------------------------------------------------------

## 📊 Output Example

Study Plan:

2026-04-01 - Math: 2 hour(s)

2026-04-02 - Physics: 2 hour(s)

Suggestions: - Focus more on difficult subjects - Start early for near
deadlines

------------------------------------------------------------------------

## 🧠 AI Logic

Priority = (Difficulty × 2) + (10 / Days Left)

### Scheduling Rules

-   Higher priority subjects scheduled first\
-   Maximum 2 hours per subject per day\
-   Balanced workload distribution

------------------------------------------------------------------------

## 🧰 Technologies Used

-   Python\
-   CLI Interface\
-   DateTime Module\
-   Rule-Based AI Logic

------------------------------------------------------------------------

## 📁 Project Structure

ai-study-planner-cli/ │── main.py │── README.md

------------------------------------------------------------------------

## ⚠️ Limitations

-   No GUI (CLI only)\
-   Uses rule-based logic (not machine learning)\
-   Assumes fixed daily availability

------------------------------------------------------------------------


## 📚 Learning Outcomes

-   Implemented AI logic without external APIs\
-   Built a CLI-based application\
-   Designed a scheduling algorithm\
-   Improved problem-solving and system design skills

------------------------------------------------------------------------

## 👨‍💻 Author

Your Name

------------------------------------------------------------------------

## ⭐ Acknowledgment

This project was developed as part of the Bring Your Own Project (BYOP)
capstone activity.
Author

Your Name

------------------------------------------------------------------------

## ⭐ Acknowledgment

This project was developed as part of the Bring Your Own Project (BYOP)
capstone activity.
