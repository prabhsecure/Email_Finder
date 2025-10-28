📧 Email Finder in Text Files

A simple Python script that searches for a specific email address in all .txt files inside a given folder (and its subfolders).
It lists all files, line numbers, and the exact lines where the email appears.

🧩 Features

🔍 Searches recursively through all .txt files in a folder

📄 Displays file path, line number, and line content for each match

⚙️ Ignores encoding errors automatically

💡 Simple command-line interface with ASCII art header

🚀 How to Use
🐍 Step 1: Clone the Repository

    git clone https://github.com/prabhsecure/Email_Finder.git
    cd Email_Finder
    chmod + email_finder.py
    python3 email_finder.py

⚙️ Step 2: Run the Script

    Make sure you have Python 3.6+ installed.

Then run:

    python email_finder.py

💬 Step 3: Enter Required Details

When prompted:

    Enter the email to search for: example@gmail.com
    Enter the folder path containing .txt files: /home/kali/Email_Finder
    

📊 Step 4: View Results

    Searching for 'john@example.com' in ' /home/kali/Email_Finder'...

    ✅ Found 2 matches:

    📄 File: /home/kali/Email_Finder\notes.txt
    Line 5: Please contact john@example.com for support.

    📄 File: /home/kali/Email_Finder/report.txt
    Line 12: Report sent to john@example.com

