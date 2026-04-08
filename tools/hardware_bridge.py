from typing import Dict, Any

class HardwareBridge:
    def __init__(self):
        self.current_mode = "simulation"  # simulation | real_robot | fixed_cameras

    def execute_command(self, command: Dict[str, Any]) -> Dict:
        """
        Ejecuta comandos físicos o digitales según el modo.
        """
        action = command.get("action")
        params = command.get("params", {})

        print(f"⚙️ Ejecutando acción: {action} | Parámetros: {params}")

        if self.current_mode == "simulation":
            return {
                "status": "success",
                "mode": "simulation",
                "message": f"Simulación: {action} ejecutado correctamente",
                "details": params
            }

        elif self.current_mode == "real_robot":
            # Aquí iría la integración real con ROS2
            return {
                "status": "success",
                "mode": "real_robot",
                "message": f"Robot real: {action} ejecutado"
            }

        else:
            # Modo cámaras fijas + actuadores
            return {
                "status": "success",
                "mode": "fixed_cameras",
                "message": f"Actuador activado: {action}"
            }

# Instancia global
hardware_bridge = HardwareBridge()

def execute_command(command: Dict):
    """Función que usan los agentes"""
    return hardware_bridge.execute_command(command)
