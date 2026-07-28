import subprocess
import sys
import os

scripts = [
    "Exp-17-Digital-Evidence-Collection.py",
    "Exp-18-Volatile-vs-Non-Volatile.py",
    "Exp-19-Physical-Logical-Sparse-Acquisition.py",
    "Exp-20-Live-vs-Dead-Acquisition.py",
    "Exp-21-Imaging-vs-Duplication.py",
    "Exp-22-Bit-Stream-Copy-Verification.py",
    "Exp-23-Hashing-and-Avalanche.py",
    "Exp-24-File-Carving.py",
    "Exp-25-File-System-Feature-Simulation.py",
    "Exp-26-Slack-Space-Calculation.py",
    "Exp-27-End-to-End-Forensic-Workflow.py"
]

def run_all():
    print("Running all experiments 17 through 27...\n")
    all_passed = True
    for script in scripts:
        print(f"=== Running {script} ===")
        if not os.path.exists(script):
            print(f"Error: {script} not found in the current directory.")
            all_passed = False
            continue
            
        result = subprocess.run([sys.executable, script], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error executing {script}:\n{result.stderr}")
            all_passed = False
        else:
            print(result.stdout)
            
    if all_passed:
        print("\nAll 11 experiments passed their test cases successfully.")
    else:
        print("\nSome experiments failed.")

if __name__ == "__main__":
    run_all()
