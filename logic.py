from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    if not text.strip():
        return None
    result = classifier(text)[0] 
    label = result['label']
    score = round(result['score'] * 100, 2)
    return label, score
