from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('all-MiniLM-L6-v2')
_embedding_cache = {}

def event_to_text(event):
    return f"{event.event_type} using {event.source_app} by {event.user or 'unknown user'} against {event.target}: {event.status}"

def get_event_embedding(event):
    text = event_to_text(event)
    if text not in _embedding_cache:
        _embedding_cache[text] = model.encode(
            text,
            convert_to_tensor=True
        )

    return _embedding_cache[text]

def compare_events(event1, event2):
    embedding1 = get_event_embedding(event1)
    embedding2 = get_event_embedding(event2)
    similarity = util.cos_sim(embedding1, embedding2)
    return similarity

def correlation_score(event1, event2):
    simialrity  = compare_events(event1, event2)
    same_ip = False
    if event1.source_ip == event2.source_ip:
        same_ip = True
    time_difference = event2.timestamp - event1.timestamp
    same_target = False
    if event1.target == event2.target:
        same_target = True

    return {
        "similarity": simialrity.item(),
        "same_ip": same_ip,
        "time_difference": time_difference,
        "same_target": same_target
    }