from transformers import pipeline
from huggingface_hub import login
import json

model = r"model\distilbert-news-sentiment"
labels = ["negative", "neutral", "positive"]

classifier = pipeline("sentiment-analysis", model=model)

data = []
with open('output.txt') as f:
    for line in f:
        data.append(json.loads(line)["description"])

output = classifier(
    data[:5]
)

print(output)