from pydantic import BaseModel

def group_by_ip(events):
    groups = {}
    for event in events:
        if event.source_ip not in groups:
            groups[event.source_ip] = []
        groups[event.source_ip].append(event)

    for ip in groups:
        groups[ip].sort(key=lambda x: x.timestamp)

    return groups
                