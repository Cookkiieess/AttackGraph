from data.generator import (
    generate_attack_sequence,
    generate_normal_sequence
)

from app.ai.features import extract_features


def generate_dataset(number_of_sequences):

    dataset = []

    for _ in range(number_of_sequences):

        attack = generate_attack_sequence()
        attack_ip = attack[0].source_ip
        normal = generate_normal_sequence(source_ip=attack_ip)

        # -------------------------
        # POSITIVE ATTACK PAIRS
        # -------------------------

        for i in range(len(attack)):
            for j in range(i + 1, len(attack)):

                features = extract_features(
                    attack[i],
                    attack[j]
                )

                dataset.append({
                    "event1": attack[i],
                    "event2": attack[j],
                    "features": features,
                    "label": 1
                })

        # -------------------------
        # NORMAL PAIRS
        # -------------------------

        for i in range(len(normal)):
            for j in range(i + 1, len(normal)):

                features = extract_features(
                    normal[i],
                    normal[j]
                )

                dataset.append({
                    "event1": normal[i],
                    "event2": normal[j],
                    "features": features,
                    "label": 0
                })

        # -------------------------
        # CROSS-SEQUENCE PAIRS
        # -------------------------

        for attack_event in attack:
            for normal_event in normal:

                features = extract_features(
                    attack_event,
                    normal_event
                )

                dataset.append({
                    "event1": attack_event,
                    "event2": normal_event,
                    "features": features,
                    "label": 0
                })

    return dataset