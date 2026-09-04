from app.models.event import SecurityEvent
from app.ai.features import extract_features
from data.sample_events import SE_1, SE_2, SE_3, SE_4

attack_sequence = [SE_1, SE_2, SE_3, SE_4]

for event in attack_sequence:
    print(event)

print("\nExtracted Features Between Events:")
print(f"Features between SE_1 and SE_2: {extract_features(SE_1, SE_2)}")
print(f"Features between SE_1 and SE_4: {extract_features(SE_1, SE_4)}")

