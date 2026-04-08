from crewai import Agent
from tools.hardware_bridge import execute_command

class ExecutorAgent:
    def __init__(self, domain="generic"):
        self.domain = domain
        
        self.agent = Agent(
            role=f"Executor Físico - {domain.capitalize()}",
            goal=f"Ejecutar acciones físicas o digitales de forma precisa y segura",
            backstory=f"""Eres el agente que lleva las decisiones a la realidad física.
            Controlas robots, actuadores, cámaras PTZ o sistemas externos en el dominio {domain}.
            Siempre priorizas la seguridad y eficiencia.""",
            verbose=True,
            allow_delegation=False,
            tools=[execute_command]
        )

    @property
    def task(self):
        return self.agent.task(
            description=f"""Recibe el plan del Planner Agent para el dominio {self.domain}.
            Ejecuta las acciones necesarias de forma ordenada y segura.
            Confirma la ejecución y reporta cualquier problema encontrado.""",
            expected_output="Confirmación de ejecución con resultados y estado final."
        )
