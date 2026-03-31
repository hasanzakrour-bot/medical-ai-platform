import torch
from transformers import AutoModel, AutoTokenizer

class AIModelManager:
    def __init__(self):
        self.models = {}  # name -> (model, tokenizer)

    def add_model(self, name: str, hf_model_name: str):
        """
        إضافة نموذج جديد من Hugging Face
        """
        model = AutoModel.from_pretrained(hf_model_name)
        tokenizer = AutoTokenizer.from_pretrained(hf_model_name)
        self.models[name] = (model, tokenizer)
        print(f"Model {name} loaded from Hugging Face: {hf_model_name}")

    def get_model(self, name: str):
        """
        استدعاء نموذج معين
        """
        return self.models.get(name)