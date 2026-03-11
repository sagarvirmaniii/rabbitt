# Talking Rabbitt – Conversational Analytics MVP

A minimal web application that demonstrates conversational analytics on CSV datasets using natural language questions.

## Features

- Upload CSV files
- Ask questions in natural language
- Get instant insights with text answers
- Automatically generated visualizations (bar charts, line charts)

## Local Setup

### Prerequisites
- Python 3.7 or higher

### Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

### Try It Out

1. Upload the included `sample_sales.csv` file
2. Ask questions like:
   - "Which region has the highest revenue?"
   - "Show revenue trend by quarter"
   - "Which region performed best?"

## Deploy to Streamlit Cloud

1. Push this repository to GitHub

2. Go to [share.streamlit.io](https://share.streamlit.io)

3. Sign in with GitHub

4. Click "New app"

5. Select your repository, branch (main), and main file path (app.py)

6. Click "Deploy"

Your app will be live in minutes with a public URL!

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── sample_sales.csv      # Sample dataset
└── README.md             # This file
```

## How It Works

The app uses:
- **Streamlit** for the web interface
- **Pandas** for data processing
- **Matplotlib** for visualizations

When you ask a question, the app:
1. Analyzes keywords in your question
2. Processes the DataFrame accordingly
3. Returns a text answer and relevant chart
