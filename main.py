import argparse
import yaml
from crewai import Crew
from agents.scout_agent import ScoutAgent
from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from agents.reporter_agent import ReporterAgent

def load_config():
    with open("config/llm_config.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="MaiarMind - Physical AI Modular System")
    parser.add_argument("--domain", type=str, default="generic",
                        help="Dominio específico: citricos, ganaderia, vinas, mantenimiento, etc.")
    parser.add_argument("--mode", type=str, default="simulation",
                        choices=["simulation", "real", "cameras"],
                        help="Modo de ejecución")
    args = parser.parse_args()

    config = load_config()
    print(f"🚀 MaiarMind iniciado | Dominio: {args.domain.upper()} | Modo: {args.mode}")

    # Crear agentes
    scout = ScoutAgent(domain=args.domain)
    planner = PlannerAgent(domain=args.domain)
    executor = ExecutorAgent(domain=args.domain)
    reporter = ReporterAgent()

    # Crear el equipo
    crew = Crew(
        agents=[scout, planner, executor, reporter],
        tasks=[scout.task, planner.task, executor.task, reporter.task],
        verbose=2,
        memory=True
    )

    # Ejecutar el sistema
    result = crew.kickoff(inputs={"domain": args.domain, "mode": args.mode})
    
    print("\n" + "="*60)
    print("✅ EJECUCIÓN FINALIZADA")
    print(result)
    print("="*60)

if __name__ == "__main__":
    main()
