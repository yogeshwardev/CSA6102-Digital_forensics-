CLUSTER_SIZE = 4096 # typical disk cluster size in bytes

def calculate_slack_space(file_size, cluster_size=CLUSTER_SIZE):
    clusters_needed = -(-file_size // cluster_size) # ceiling division
    allocated_space = clusters_needed * cluster_size
    slack_space = allocated_space - file_size
    return allocated_space, slack_space

file_size = 5000 # bytes
allocated, slack = calculate_slack_space(file_size)
print(f"File size: {file_size} bytes -> allocated: {allocated} bytes, slack space: {slack} bytes")

def test_experiment26():
    assert allocated == 8192, "5000 bytes needs 2 clusters of 4096 bytes = 8192 bytes allocated"
    assert slack == 8192 - 5000, "Slack space should be the unused remainder of the last cluster"
    allocated2, slack2 = calculate_slack_space(4096)
    assert slack2 == 0, "A file that exactly fills a cluster should have zero slack space"
    print("Experiment 26: All test cases passed.")

test_experiment26()
