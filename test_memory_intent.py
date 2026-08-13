from app.brain.memory_intent_detector import MemoryIntentDetector


detector = MemoryIntentDetector()


tests = [
    "hola ev",
    "recuerda que estoy aprendiendo Python",
    "¿qué recuerdas sobre Python?",
    "¿qué recuerdas de Django?",
    "¿qué recuerdos tienes?",
    "qué recuerdas",
    "cómo estás"
]


for message in tests:

    intent = detector.detect(message)

    print(
        f"{message} -> {intent}"
    )