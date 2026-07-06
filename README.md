
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
