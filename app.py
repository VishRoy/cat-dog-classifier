
import gradio as gr
import torch
from PIL import Image
from transformers import ViTForImageClassification, ViTImageProcessor

MODEL_ID = "VishRoy/cat-dog-classifier"
processor = ViTImageProcessor.from_pretrained(MODEL_ID)
model = ViTForImageClassification.from_pretrained(MODEL_ID)
model.eval()

def classify_image(image):
    inputs = processor(
        images=image.convert("RGB"),
        return_tensors="pt"
    )
    with torch.no_grad():
        probs = torch.softmax(
            model(**inputs).logits, dim=-1
        )[0]
    return {
        "Cat": float(probs[0]),
        "Dog": float(probs[1])
    }

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil", label="Upload Photo"),
    outputs=gr.Label(num_top_classes=2, label="Result"),
    title="Cat vs Dog Classifier",
    description="Photo Description",
    theme="soft"
)

demo.launch()
