from crewai import Agent

class ReporterAgent:
    def __init__(self):
        self.agent = Agent(
            role="Reporter y Analista Final",
            goal="Generar informes claros, útiles y accionables para el usuario",
            backstory="""Eres un analista profesional que resume toda la información del proceso.
            Transformas las detecciones, decisiones y ejecuciones en informes fáciles de entender
            para el agricultor, ganadero o técnico.""",
            verbose=True,
            allow_delegation=False
        )

    @property
    def task(self):
        return self.agent.task(
            description="""Recibe toda la información del flujo completo (Scout → Planner → Executor).
            Genera un informe claro que incluya:
            - Resumen de lo detectado
            - Decisiones tomadas
            - Acciones ejecutadas
            - Resultados y recomendaciones
            - Alertas importantes""",
            expected_output="Informe completo y bien estructurado listo para el usuario final."
        )
