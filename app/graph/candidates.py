import datetime


def find_candidates(events, event):

    candidates = []
    max_gap = datetime.timedelta(seconds=60)

    for candidate in events:
        if candidate.timestamp > event.timestamp:
            if candidate.source_ip == event.source_ip:
                if candidate.timestamp - event.timestamp <= max_gap:
                    candidates.append(candidate)

    return candidates