import random
from collections import defaultdict

# Define disorders and symptoms
disorders = {
    "Generalized Anxiety Disorder": ["Restlessness", "Overthinking", "Irritability", "Muscle tension", "Sleep disturbances"],
    "Panic Disorder": ["Rapid heartbeat", "Chest pain", "Dizziness", "Shortness of breath", "Feeling of doom"],
    "Acute Stress Disorder": ["Flashbacks", "Nightmares", "Detachment", "Trouble sleeping", "Anxiety"],
    "Insomnia Disorder": ["Trouble sleeping", "Fatigue", "Irritability", "Trouble concentrating", "Mood changes"],
    "Hyperactivity Disorder (ADHD)": ["Inattention", "Impulsivity", "Fidgeting", "Interrupting others", "Poor time management"],
    "Major Depressive Disorder": ["Persistent sadness", "Loss of interest", "Fatigue", "Suicidal thoughts", "Appetite changes"],
    "Adjustment Disorder": ["Irritability", "Sadness", "Difficulty concentrating", "Withdrawal", "Sleep problems"],
    "Anorexia Nervosa": ["Extreme weight loss", "Food restriction", "Body image distortion", "Excessive exercise", "Denial of hunger"],
    "Oppositional Defiant Disorder": ["Arguing with authority", "Refusal to follow rules", "Blaming others", "Anger outbursts", "Spitefulness"],
    "Post-Traumatic Stress Disorder": ["Nightmares", "Flashbacks", "Avoidance", "Hypervigilance", "Emotional numbness"]
}

# Reverse map symptoms to disorders
symptom_to_disorders = defaultdict(list)
for disorder, symptoms in disorders.items():
    for symptom in symptoms:
        symptom_to_disorders[symptom].append(disorder)

# Generate questions
symptom_questions = [{"symptom": s, "question": f"Do you experience {s.lower()}?"}
                     for s in symptom_to_disorders]
random.shuffle(symptom_questions)

# Run diagnosis
def run_chatbot():
    print("Welcome to the AI Mental Health Assistant!\nPlease answer with Yes / No / Not Sure\n")
    scores = {d: 0 for d in disorders}
    selected_yes = []

    for i, q in enumerate(symptom_questions[:10], 1):
        print(f"Q{i}: {q['question']}")
        ans = input("Your answer: ").strip().lower()
        if ans == "yes":
            selected_yes.append(q["symptom"])
            for d in symptom_to_disorders[q["symptom"]]:
                scores[d] += 1
        elif ans == "not sure":
            for d in symptom_to_disorders[q["symptom"]]:
                scores[d] += 0.5

    diagnosis = max(scores, key=scores.get)
    print("\n✅ Based on your answers, the most likely condition is:", diagnosis)
    print("📝 Symptoms you confirmed:", ', '.join(selected_yes))
    print("📊 Confidence score:", scores[diagnosis])

# Entry point
if __name__ == "__main__":
    run_chatbot()
