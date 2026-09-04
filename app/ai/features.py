from app.ai.embeddings import compare_events


def extract_features(event1, event2):
    similarity = compare_events(event1, event2)
    same_ip = 0
    if event1.source_ip == event2.source_ip:
        same_ip = 1
    time_difference = event2.timestamp - event1.timestamp
    same_target = 0
    if event1.target == event2.target:
        same_target = 1

    return {
        "similarity": similarity.item(),
        "same_ip": same_ip,
        "time_difference": time_difference.total_seconds(),
        "same_target": same_target
    }
