
# How To Build AI Agent To Solve Complex Question Using 'Decomposition and Aggregation'


## Introduction

Full Article : [https://medium.com/@learn-simplified/how-to-build-ai-agent-to-solve-complex-question-using-decomposition-and-aggregation-7dee6f0373a3

Have you ever thought about how AI can handle really tough questions that even experts find challenging? We're about to explore AI agents that can solve complex problems, step by step, like a chef following a detailed recipe. This isn't just another tech discussion - it's a look into how AI is shaping the future of problem-solving, not just by giving answers, but by creating well-thought-out solutions.

## What's This Project About?
This article is your backstage pass to building an AI agent that's like a Swiss Army knife for complex questions. We're talking about a system that doesn't just stare blankly at tough queries but breaks them down into bite-sized chunks. It's all about the art of 'decomposition and aggregation' - fancy words for splitting big problems into smaller ones and then putting the answers back together.
We'll walk through creating a SubQuestionQueryEngine that's like a team of mini-experts working together. It takes a big question, like "How have electric vehicles impacted urban traffic from 2015 to 2023?", and turns it into a series of smaller questions. Then, it hunts for answers in a treasure trove of PDF reports, each covering a different year. Finally, it weaves all these answers into one coherent response. It's like watching a jigsaw puzzle solve itself!

## Why Use This Project?
In today's business world, AI isn't just a buzzword - it's becoming as essential as your morning coffee. Companies are drowning in data and complex problems, and they need smart solutions fast. This article shows you how a fictional company (let's call them "EcoCity Planners") could use AI to make sense of years of data on electric vehicles and urban traffic.

## Architecture
![Design Diagram](design_docs/design.png)


# Tutorial: Lets Build Agentic RAG From Scratch

## Prerequisites
- Python installed on your system.
- A basic understanding of virtual environments and command-line tools.

## Steps

1. **Virtual Environment Setup:**
   - Create a dedicated virtual environment for our project:
   
     ```bash
     python -m venv AI_Agents_Take_Strategic_Decision_In_Complex_Scenarios
     ```
   - Activate the environment:
   
     - Windows:
       ```bash
       AI_Agents_Take_Strategic_Decision_In_Complex_Scenarios\Scripts\activate
       ```
     - Unix/macOS:
       ```bash
       source AI_Agents_Take_Strategic_Decision_In_Complex_Scenarios/bin/activate
       ```

2. **Install Project Dependencies:**

   - Navigate to your project directory and install required packages using `pip`:
   
     ```bash        
     cd path/to/your/project
     pip install -r requirements.txt
     ```
3. **Install Ollama**
    
    Ollama is a powerful tool for running large language models locally on your machine. Let's walk through the installation process step-by-step.
    
    Step 1: Download Ollama
     - Visit the official Ollama website at https://ollama.com/ and click the "Download" button. The website will automatically detect your operating system and offer the appropriate installer
    
    Step 2: Install Ollama
      - For Windows and Mac users: Double-click the downloaded installer file (.exe for Windows, .dmg for Mac) and follow the on-screen instructions
      - For Linux users: Open a terminal and run the following command:

4. **Run - AI Agent To Strategic decision for complex business scenario**

   ```bash 
   # Run AI Agent To Strategic decision for complex business scenario   
   streamlit run ui.py   
   ```






