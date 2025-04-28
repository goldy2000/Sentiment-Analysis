
import gradio as gr
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive 😀"
    elif polarity < -0.1:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    
    return sentiment

iface = gr.Interface(
    fn=analyze_sentiment,
    inputs="text",
    outputs="text",
    title="Sentiment Analyzer",
    description="Enter a sentence to know its sentiment."
)

iface.launch(server_name="0.0.0.0", server_port=8080)
