# Script para gerar comandos kubectl relacionados a PV e PVC

def kubectl_command(action, resource_name):
    actions_to_commands = {
        "criar-pv": "kubectl create -f",
        "deletar-pv": "kubectl delete pv",
        "criar-pvc": "kubectl create -f",
        "deletar-pvc": "kubectl delete pvc"
    }

    if action in actions_to_commands:
        return f"{actions_to_commands[action]} {resource_name}"
    else:
        return "Ação inválida. Use: criar-pv, deletar-pv, criar-pvc ou deletar-pvc."


# Exemplo de uso
if __name__ == "__main__":
    input_string = input("Digite o comando (ação, recurso): ")
    try:
        action, resource = input_string.split(", ")
        print(kubectl_command(action, resource))
    except ValueError:
        print("Entrada inválida. Use o formato: ação, recurso")
