from crewai import Agent
from tools.vision_tool import analyze_image

class ScoutAgent:
    def __init__(self, domain="generic"):
        self.domain = domain
        
        self.agent = Agent(
            role=f"Scout Sensorial - {domain.capitalize()}",
            goal=f"Observar y detectar de forma precisa todo lo relevante en el dominio {domain}",
            backstory=f"""Eres un observador experto con visión por computadora. 
            Tu trabajo es analizar imágenes o vídeo en tiempo real y detectar anomalías, 
            objetos o situaciones importantes en el contexto de {domain}.""",
            verbose=True,
            allow_delegation=False,
            tools=[analyze_image]
        )

    @property
    def task(self):
        return self.agent.task(
            description=f"""Analiza las imágenes actuales del entorno en el dominio {self.domain}.
            Detecta objetos, anomalías, estados o problemas relevantes.
            Devuelve una lista clara de detecciones con confianza, ubicación y descripción.""",
            expected_output="Lista detallada de detecciones con puntuación de confianza y coordenadas."
        )
