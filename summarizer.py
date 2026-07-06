import sys
from transformers import pipeline

def read_logs(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def summarize_logs(log_text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(log_text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarizer.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    logs = read_logs(log_file)
    print("\nSummary:\n")
    print(summarize_logs(logs))
