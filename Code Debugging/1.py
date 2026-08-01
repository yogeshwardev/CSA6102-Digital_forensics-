custody_log = []

def add_entry(evidence_id, handler, action):
    entry = {
        'evidence_id': evidence_id,
        'handler': handler,
        'action': str(action)
    }
    custody_log.append(entry)

def print_log():
    for entry in custody_log:
        print(entry['evidence_id'] + " - " +
              entry['handler'] + " - " +
              str(entry['action']))

add_entry('EVD-101', 'A.Kumar', 'Collected')
add_entry('EVD-101', 'S.Rao', 'Analysed')

print_log()