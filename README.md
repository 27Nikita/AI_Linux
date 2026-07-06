
# Automated Log Summarizer

This project reads Linux system logs and generates a human-readable summary using AI (Hugging Face Transformers).

## Features
- Reads logs from `/var/log/syslog` or custom files
- Summarizes logs into concise daily reports
- Easy to extend with cron jobs for automation

## Setup
```bash
git clone https://github.com/yourusername/automated-log-summarizer.git
cd automated-log-summarizer
pip install -r requirements.txt


Project Structure
============================
automated-log-summarizer/
│── README.md          # Project documentation
│── requirements.txt   # Python dependencies (transformers, torch)
│── summarizer.py      # Main script to read & summarize logs
│── data/
│    └── sample_logs.txt   # Example log file for testing
│── .gitignore         # Ignore cache, venv, logs, temp files

How to Use
===============================
1. Install dependencies
pip install -r requirements.txt

2. Run summarizer on sample logs
python summarizer.py data/sample_logs.txt

3. Run on real system logs
python summarizer.py /var/log/syslog
Output  
The script prints a short AI‑generated summary of the logs, e.g.:

Summary:
- System boot completed successfully
- Network service restarted
- 2 warnings related to disk usage
