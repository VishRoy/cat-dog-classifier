# 🐱🐶 Cat vs Dog Classifier

A deep learning image classifier built with HuggingFace Transformers.
Upload any cat or dog photo — model will predict with confidence score!

## 🚀 Live Demo
👉 [Try it here](https://huggingface.co/spaces/VishRoy/cat-dog-app)

## 🛠️ Tech Stack
- **Model**: Google ViT (Vision Transformer) — fine-tuned
- **Framework**: HuggingFace Transformers + PyTorch
- **UI**: Gradio
- **Deployment**: HuggingFace Spaces (free)
- **Training**: Google Colab (free GPU)

## 📊 Results
- Training Accuracy : 100%
- Model Type        : Fine-tuned ViT (google/vit-base-patch16-224)
- Classes           : Cat, Dog
- Training Data     : Custom dataset

## 🏗️ Project Structure

cat-dog-classifier/
├── app.py                 # Gradio web app
├── requirements.txt       # Dependencies
├── training_notebook.py   # Full training code
└── README.md
