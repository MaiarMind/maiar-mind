def get_citricos_rules():
    """Reglas específicas para el dominio de cítricos"""
    return {
        "domain_name": "citricos",
        "critical_threshold": 0.75,           # Confianza mínima para alertas críticas
        "priority_classes": ["citrus_greening", "citrus_canker", "black_spot"],
        "action_rules": {
            "citrus_greening": "alta",        # Requiere acción inmediata
            "citrus_canker": "alta",
            "black_spot": "media",
            "orange_severe_stress": "media",
            "fruit_fly_damage": "media",
            "nutrient_deficiency": "baja"
        },
        "description": "Detección de plagas, enfermedades y estados de madurez en cítricos"
    }
