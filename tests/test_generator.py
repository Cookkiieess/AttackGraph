from data.generator import generate_attack_sequence, generate_normal_sequence


attack = generate_attack_sequence()
normal = generate_normal_sequence()

print("ATTACK:")
for event in attack:
    print(event)

print("\nNORMAL:")
for event in normal:
    print(event)