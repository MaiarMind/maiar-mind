from ultralytics import YOLO
import cv2
from typing import List, Dict

class VisionTool:
    def __init__(self, model_path: str = "yolov11n.pt", domain: str = "generic"):
        print(f"🔄 Cargando modelo YOLO para dominio: {domain}")
        self.model = YOLO(model_path)
        self.domain = domain

    def analyze_image(self, image_path: str) -> List[Dict]:
        """
        Analiza una imagen y devuelve las detecciones.
        """
        results = self.model(image_path, verbose=False)
        detections = []

        for result in results:
            for box in result.boxes:
                detection = {
                    "class": result.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "bbox": box.xyxy[0].tolist(),  # [x1, y1, x2, y2]
                    "domain": self.domain
                }
                detections.append(detection)

        return detections

# Instancia global
vision_tool = VisionTool()

def analyze_image(image_path: str):
    """Función que usan los agentes"""
    return vision_tool.analyze_image(image_path)
