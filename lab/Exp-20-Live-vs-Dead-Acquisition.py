import time
import psutil
import json

def live_acquisition():
    return {
        "timestamp": time.time(),
        "running_processes": len(psutil.pids()),
        "cpu_percent": psutil.cpu_percent(interval=0.1),
    }

def dead_acquisition(snapshot_file):
    with open(snapshot_file) as f:
        return json.load(f)

dead_snapshot_path = "system_snapshot.json"
static_snapshot = {"hard_disk_files": ["a.txt", "b.txt"], "ram_data": None}
with open(dead_snapshot_path, "w") as f:
    json.dump(static_snapshot, f)

live_result = live_acquisition()
dead_result = dead_acquisition(dead_snapshot_path)

print("Live acquisition:", live_result)
print("Dead acquisition:", dead_result)

def test_experiment20():
    assert live_result["running_processes"] > 0, "Live acquisition must capture running processes"
    assert isinstance(live_result["cpu_percent"], float), "Live acquisition should return live CPU usage"
    assert dead_result["ram_data"] is None, "Dead acquisition can never recover RAM data"
    assert dead_result == static_snapshot, "Dead acquisition should exactly match the stored snapshot"
    print("Experiment 20: All test cases passed.")

test_experiment20()
