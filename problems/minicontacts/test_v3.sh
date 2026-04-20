#!/usr/bin/env python3
import subprocess, os, shutil

def run(args):
    # Testing the solution_v3.py file
    return subprocess.run(["python3", "solution_v3.py"] + args, capture_output=True, text=True).stdout.strip()

def setup():
    if os.path.exists(".minicontacts"): shutil.rmtree(".minicontacts")

def test_v3_flow():
    setup()
    run(["init"])
    run(["add", "Esmanur", "555-123", "esma@email.com"])
    run(["add", "Zeynep", "444-987", "zeynep@email.com"])
    
    # 1. Count Test (New in v3)
    assert "Total contacts: 2" in run(["count"])
    
    # 2. Update Test (New in v3)
    run(["update", "1", "Esmanur", "999-999", "new@email.com"])
    assert "999-999" in run(["list"])
    
    # 3. Delete Test (New in v3)
    run(["delete", "2"])
    assert "Zeynep" not in run(["list"])
    
    # 4. Final Count Test
    assert "Total contacts: 1" in run(["count"])
    
    print("All v3 test scenarios passed successfully!")

if __name__ == "__main__": 
    test_v3_flow()