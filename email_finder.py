import os

def find_email_in_files(email, folder_path):
    found_in = []

    # Walk through all .txt files in the given folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        for i, line in enumerate(f, start=1):
                            if email in line:
                                found_in.append((file_path, i, line.strip()))
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return found_in


def main():
    print('''
 _____   __  __      _      ___   _          _____ ___ _   _ ____  _____ ____  
| ____| |  \/  |    / \    |_ _| | |        |  ___|_ _| \ | |  _ \| ____|  _ \ 
|  _|   | |\/| |   / _ \    | |  | |   _____| |_   | ||  \| | | | |  _| | |_) |
| |___  | |  | |  / ___ \   | |  | |__|_____|  _|  | || |\  | |_| | |___|  _ < 
|_____| |_|  |_| /_/   \_\ |___| |_____|    |_|   |___|_| \_|____/|_____|_| \_\

''')

    # ✅ Correct indentation here
    email = input("Enter the email to search for: ").strip()
    folder_path = input("Enter the folder path containing .txt files: ").strip()

    print(f"\nSearching for '{email}' in '{folder_path}'...\n")
    results = find_email_in_files(email, folder_path)

    if results:
        print(f"✅ Found {len(results)} matches:\n")
        for file_path, line_num, line_text in results:
            print(f"📄 File: {file_path}")
            print(f"   Line {line_num}: {line_text}\n")
    else:
        print("❌ No matches found.")


if __name__ == "__main__":
    main()
