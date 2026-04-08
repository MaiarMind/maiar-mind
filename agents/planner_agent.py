from crewai import Agent

class PlannerAgent:
    def __init__(self, domain="generic"):
        self.domain = domain
        
        self.agent = Agent(
            role=f"Planner Estratégico - {domain.capitalize()}",
            goal=f"Analizar las detecciones y crear un plan de acción óptimo y prioritizado",
            backstory=f"""Eres un estratega experto en {domain}. 
            Tu trabajo es recibir las observaciones del Scout y decidir las mejores acciones 
            a tomar, priorizando según gravedad, eficiencia y recursos disponibles.""",
            verbose=True,
            allow_delegation=False
        )

    @property
    def task(self):
        return self.agent.task(
            description=f"""Recibe las detecciones del Scout Agent en el dominio {self.domain}.
            Analiza la situación, prioriza las acciones según urgencia e impacto.
            Crea un plan claro y secuencial de qué debe hacer el Executor.""",
            expected_output="Plan de acción detallado con prioridades, pasos y justificación."
        )
