"""
mini-contacts v1 — Enhanced Version
Student: Esmanur Ceviz (251478077)

V1 TASK LIST:
1. 'list' command: Formatted listing of all contacts using loops.
2. 'search' command: Keyword-based search functionality on names.
3. 'clear' command: Database reset feature as defined in SPEC.
"""
import sys
import os

DB_PATH = ".minicontacts/contacts.dat"

def initialize():
    if os.path.exists(".minicontacts"):
        return "Already initialized"
    os.mkdir(".minicontacts")
    open(DB_PATH, "w").close()
    return "Initialized empty minicontacts in .minicontacts/"

def add_contact(name, phone, email):
    if not os.path.exists(".minicontacts"):
        return "Not initialized. Run: python solution_v1.py init"
    with open(DB_PATH, "r") as f:
        lines = f.readlines()
    contact_id = len(lines) + 1
    with open(DB_PATH, "a") as f:
        f.write(f"{contact_id}|{name}|{phone}|{email}\n")
    return f"Added contact #{contact_id}: {name}"

def list_contacts():
    if not os.path.exists(DB_PATH): return "Not initialized."
    with open(DB_PATH, "r") as f:
        lines = f.readlines()
    if not lines: return "No contacts found."
    output = ""
    for line in lines:
        cid, name, phone, email = line.strip().split("|")
        output += f"  [{cid}] {name} - {phone} ({email})\n"
    return output.strip()

def search_contact(keyword):
    if not os.path.exists(DB_PATH): return "Not initialized."
    with open(DB_PATH, "r") as f:
        lines = f.readlines()
    results = [l for l in lines if keyword.lower() in l.split("|")[1].lower()]
    if not results: return "No match found."
    output = ""
    for line in results:
        cid, name, phone, email = line.strip().split("|")
        output += f"  [{cid}] {name} - {phone} ({email})\n"
    return output.strip()

def clear_contacts():
    """Yeni eklenen görev [cite: 21]"""
    if not os.path.exists(DB_PATH): return "Not initialized."
    open(DB_PATH, "w").close()
    return "All contacts cleared."

# --- Main Program ---
if len(sys.argv) < 2:
    print("Usage: python solution_v1.py <command>")
else:
    cmd = sys.argv[1]
    if cmd == "init": print(initialize())
    elif cmd == "add":
        if len(sys.argv) < 5: print("Usage: add <name> <phone> <email>")
        else: print(add_contact(sys.argv[2], sys.argv[3], sys.argv[4]))
    elif cmd == "list": print(list_contacts())
    elif cmd == "search":
        if len(sys.argv) < 3: print("Usage: search <keyword>")
        else: print(search_contact(sys.argv[2]))
    elif cmd == "clear": print(clear_contacts())
    else: print(f"Unknown command: {cmd}")