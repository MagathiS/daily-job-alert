import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

EMAIL = "magathisanjai@gmail.com"
APP_PASSWORD = "bjtj bwjx istr dues"

def fetch_jobs():
    # This will be replaced with live scraping next step
    jobs = [
        {
            "title": "Data Scientist",
            "company": "Example Corp",
            "location": "Remote",
            "salary": "12–18 LPA",
            "link": "https://example.com/job1"
        },
        {
            "title": "Data Analyst",
            "company": "Startup XYZ",
            "location": "Chennai",
            "salary": "8–12 LPA",
            "link": "https://example.com/job2"
        }
    ]
    return jobs

def send_email(jobs):
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg["Subject"] = "🔥 Fresh Data Jobs – Last 24 Hours"

    body = "Here are your best matches from the last 24 hours:\n\n"

    for i, job in enumerate(jobs, 1):
        body += f"{i}. {job['title']} – {job['company']} – {job['location']} – {job['salary']}\n"
        body += f"Apply: {job['link']}\n\n"

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
    server.quit()

def main():
    jobs = fetch_jobs()
    send_email(jobs)

if __name__ == "__main__":
    main()
