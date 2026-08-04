from datetime import datetime

def parse_usbstor(registry_data):
    """registry_data: {device_id: {"serial", "friendly_name",
    "first_connected", "last_connected"}}. Returns list of device dicts
    sorted by last_connected, most recent first."""
    devices = []
    for device_id, info in registry_data.items():
        entry = {"device_id": device_id}
        entry.update(info)
        devices.append(entry)
    devices.sort(
        key=lambda d: datetime.strptime(d["last_connected"], "%Y-%m-%d %H:%M:%S"),
        reverse=True,
    )
    return devices

def find_device_near_time(devices, target_time_str, window_minutes=30):
    """Return devices whose last_connected time is within window_minutes
    of target_time_str."""
    target = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")
    matches = []
    for d in devices:
        last = datetime.strptime(d["last_connected"], "%Y-%m-%d %H:%M:%S")
        delta_minutes = abs((target - last).total_seconds()) / 60
        if delta_minutes <= window_minutes:
            matches.append(d)
    return matches

def test_experiment30():
    registry_data = {
        "USB\\VID_0781&PID_5567\\4C531001234": {
            "serial": "4C531001234",
            "friendly_name": "SanDisk Cruzer Blade",
            "first_connected": "2025-11-01 09:00:00",
            "last_connected": "2026-02-10 17:42:00",
        },
        "USB\\VID_090C&PID_1000\\A1002233": {
            "serial": "A1002233",
            "friendly_name": "Kingston DataTraveler",
            "first_connected": "2024-06-01 10:00:00",
            "last_connected": "2024-06-01 10:15:00",
        },
    }
    devices = parse_usbstor(registry_data)
    assert devices[0]["friendly_name"] == "SanDisk Cruzer Blade"
    matches = find_device_near_time(devices, "2026-02-10 17:35:00", window_minutes=30)
    matched_names = [m["friendly_name"] for m in matches]
    assert "SanDisk Cruzer Blade" in matched_names
    assert "Kingston DataTraveler" not in matched_names
    print("Experiment 30: All test cases passed.")

test_experiment30()
