import json
import os
import sys
from datetime import datetime

FILE_NAME = "tasks.json"


# Função para carregar as tarefas
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


# Função para salvar as tarefas
def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


# Função para adicionar uma nova tarefa
def add_task(description):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarefa adicionada: {task['id']} - {description}")


# Função para listar tarefas (todas ou por status)
def list_tasks(status=None):
    tasks = load_tasks()
    filtered = tasks if not status else [t for t in tasks if t["status"] == status]
    
    if not filtered:
        print("Nenhuma tarefa encontrada.")
        return

    for t in filtered:
        print(f"{t['id']}: {t['description']} [{t['status']}]")
    

# Função para atualizar uma tarefa
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Tarefa atualizada!")
            return
    print("Tarefa não encontrada.")


# Função para excluir uma tarefa
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(new_tasks)
    print("Tarefa excluída!")


# Função para mudar o status da tarefa
def change_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarefa marcada como {status}!")
            return
    print("Tarefa não encontrada.")


# Função principal para interpretar os comandos
def main():
    if len(sys.argv) < 2:
        print("Uso: python task-cli.py <comando> [argumentos]")
        return

    command = sys.argv[1]

    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    elif command == "update":
        update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif command == "delete":
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress":
        change_status(int(sys.argv[2]), "in-progress")
    elif command == "mark-done":
        change_status(int(sys.argv[2]), "done")
    else:
        print("Comando inválido!")


if __name__ == "__main__":
    main()