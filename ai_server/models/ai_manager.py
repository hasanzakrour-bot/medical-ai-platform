import os
import torch
from .model_loader import load_model
from pathlib import Path

MODELS_DIR = Path("models")  # كل النماذج تحفظ هنا

class AIModelManager:
    def init(self, models_dir=MODELS_DIR):
        self.models_dir = Path(models_dir)
        self.models = {}  # dict: name -> model object
        self.load_all_models()

    def load_all_models(self):
        """تحميل كل النماذج في مجلد models"""
        for model_file in self.models_dir.glob("*.pth"):
            model_name = model_file.stem
            self.models[model_name] = load_model(model_file)
        print(f"Loaded models: {list(self.models.keys())}")

    def add_model(self, name: str, model_path: str):
        """إضافة نموذج جديد"""
        model_path = Path(model_path)
        if not model_path.exists():
            raise FileNotFoundError(f"{model_path} not found")
        self.models[name] = load_model(model_path)
        # حفظ نسخة في مجلد models
        target = self.models_dir / f"{name}.pth"
        os.replace(model_path, target)
        print(f"Model {name} added and saved.")

    def get_model(self, name: str):
        """استدعاء نموذج معين"""
        return self.models.get(name)