```md
# ✅ Task Tracker CLI
https://roadmap.sh/projects/task-tracker
O **Task Tracker CLI** é uma ferramenta simples para gerenciar tarefas diretamente pelo terminal.  
Com ele, você pode adicionar, listar, atualizar e excluir tarefas, além de marcar como "em andamento" ou "concluído".

---

## 📌 **Funcionalidades**
- 📌 Adicionar tarefas  
- 📌 Listar todas as tarefas ou filtrar por status  
- 📌 Atualizar a descrição de uma tarefa  
- 📌 Excluir tarefas  
- 📌 Marcar tarefas como **"em andamento"** ou **"concluídas"**  
- 📌 Armazenamento das tarefas em um arquivo JSON  

---

## 🚀 **Instalação e Uso**

### 🔹 **1. Clone o repositório ou baixe o arquivo**
```sh
git clone https://github.com/tchingala18/task-tracker-cli.git
cd task-tracker-cli
```
Ou baixe e salve o arquivo `task-cli.py`.

### 🔹 **2. Execute os comandos no terminal**
Use **Python 3** para rodar o script.  

---

## 🛠 **Comandos disponíveis**

### ✅ **Adicionar uma nova tarefa**
```sh
python task-cli.py add "Descrição da tarefa"
```
📌 *Exemplo:*  
```sh
python task-cli.py add "Comprar pão"
```
💡 *Saída:* `Tarefa adicionada: 1 - Comprar pão`

---

### ✅ **Listar todas as tarefas**
```sh
python task-cli.py list
```
💡 *Saída:*  
```
1: Comprar pão [todo]
2: Estudar Python [todo]
```

---

### ✅ **Listar tarefas por status**
📌 Listar tarefas concluídas:  
```sh
python task-cli.py list done
```

📌 Listar tarefas em andamento:  
```sh
python task-cli.py list in-progress
```

📌 Listar tarefas pendentes:  
```sh
python task-cli.py list todo
```

---

### ✅ **Atualizar uma tarefa**
```sh
python task-cli.py update <id> "Nova descrição"
```
📌 *Exemplo:*  
```sh
python task-cli.py update 1 "Comprar pão e leite"
```
💡 *Saída:* `Tarefa atualizada!`

---

### ✅ **Excluir uma tarefa**
```sh
python task-cli.py delete <id>
```
📌 *Exemplo:*  
```sh
python task-cli.py delete 1
```
💡 *Saída:* `Tarefa excluída!`

---

### ✅ **Marcar uma tarefa como "Em Andamento"**
```sh
python task-cli.py mark-in-progress <id>
```
📌 *Exemplo:*  
```sh
python task-cli.py mark-in-progress 2
```
💡 *Saída:* `Tarefa marcada como in-progress!`

---

### ✅ **Marcar uma tarefa como "Concluída"**
```sh
python task-cli.py mark-done <id>
```
📌 *Exemplo:*  
```sh
python task-cli.py mark-done 2
```
💡 *Saída:* `Tarefa marcada como done!`

---

## 📂 **Armazenamento das Tarefas**
As tarefas são armazenadas no arquivo `tasks.json`, localizado no mesmo diretório do script.

---

## ⚙ **Requisitos**
- Python 3 instalado  
- Nenhuma biblioteca extra necessária  

---

## 📌 **Melhorias futuras**
- Adicionar prazos para tarefas  
- Criar categorias para tarefas  
- Melhorar a exibição da lista de tarefas  

---

## 📜 **Licença**
Este projeto é de código aberto e pode ser usado livremente.  

---

Feito com ❤️ por Carlitos Tchingala (https://github.com/tchingala18)
```

---

## 📝 **README.md**  
https://roadmap.sh/projects/task-tracker

```md
# ✅ Task Tracker CLI

The **Task Tracker CLI** is a simple tool for managing tasks directly from the terminal.  
With it, you can add, list, update, and delete tasks, as well as mark them as "in progress" or "completed."

---

## 📌 **Features**
- 📌 Add tasks  
- 📌 List all tasks or filter by status  
- 📌 Update a task description  
- 📌 Delete tasks  
- 📌 Mark tasks as **"in progress"** or **"completed"**  
- 📌 Store tasks in a JSON file  

---

## 🚀 **Installation and Usage**

### 🔹 **1. Clone the repository or download the file**
```sh
git clone https://github.com/tchingala18/task-tracker-cli.git
cd task-tracker-cli
```
Or download and save the `task-cli.py` file.

### 🔹 **2. Run commands in the terminal**
Use **Python 3** to run the script.  

---

## 🛠 **Available Commands**

### ✅ **Add a new task**
```sh
python task-cli.py add "Task description"
```
📌 *Example:*  
```sh
python task-cli.py add "Buy bread"
```
💡 *Output:* `Task added: 1 - Buy bread`

---

### ✅ **List all tasks**
```sh
python task-cli.py list
```
💡 *Output:*  
```
1: Buy bread [todo]
2: Study Python [todo]
```

---

### ✅ **List tasks by status**
📌 List completed tasks:  
```sh
python task-cli.py list done
```

📌 List tasks in progress:  
```sh
python task-cli.py list in-progress
```

📌 List pending tasks:  
```sh
python task-cli.py list todo
```

---

### ✅ **Update a task**
```sh
python task-cli.py update <id> "New description"
```
📌 *Example:*  
```sh
python task-cli.py update 1 "Buy bread and milk"
```
💡 *Output:* `Task updated!`

---

### ✅ **Delete a task**
```sh
python task-cli.py delete <id>
```
📌 *Example:*  
```sh
python task-cli.py delete 1
```
💡 *Output:* `Task deleted!`

---

### ✅ **Mark a task as "In Progress"**
```sh
python task-cli.py mark-in-progress <id>
```
📌 *Example:*  
```sh
python task-cli.py mark-in-progress 2
```
💡 *Output:* `Task marked as in-progress!`

---

### ✅ **Mark a task as "Completed"**
```sh
python task-cli.py mark-done <id>
```
📌 *Example:*  
```sh
python task-cli.py mark-done 2
```
💡 *Output:* `Task marked as done!`

---

## 📂 **Task Storage**
Tasks are stored in the `tasks.json` file, located in the same directory as the script.

---

## ⚙ **Requirements**
- Python 3 installed  
- No additional libraries required  

---

## 📌 **Future Improvements**
- Add due dates for tasks  
- Create task categories  
- Improve task list display  

---

## 📜 **License**
This project is open-source and can be used freely.  

---

Made with ❤️ by Carlitos Tchingala (https://github.com/tchingala18)
```