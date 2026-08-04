import subprocess
import sys
import os

scripts = [
    "Exp-29-Windows-Event-Log-Brute-Force.py",
    "Exp-30-Windows-Registry-USB-History.py",
    "Exp-31-Linux-SSH-Auth-Log.py",
    "Exp-32-File-Timestamp-Timestomping.py",
    "Exp-33-Port-Scan-Detector.py",
    "Exp-34-DNS-Tunneling-Detector.py",
    "Exp-35-Signature-Based-IDS.py",
    "Exp-36-Mobile-SMS-Recovery.py",
    "Exp-37-Cloud-Audit-Log-Anomaly.py",
]

def run_all():
    print("Running all experiments 29 through 37...\n")
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
        print("\nAll 9 experiments passed their test cases successfully.")
    else:
        print("\nSome experiments failed.")

if __name__ == "__main__":
    run_all()
