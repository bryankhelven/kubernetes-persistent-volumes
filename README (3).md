
# Kubernetes Persistent Volumes Project

## Sobre o Projeto

Este projeto demonstra o uso de Persistent Volumes (PV) e Persistent Volume Claims (PVC) no Kubernetes, além de automação de comandos `kubectl` utilizando Python e integração com uma aplicação Node.js.

---

## Tecnologias Utilizadas

- **Kubernetes**: Gerenciamento de contêineres e recursos.
- **Node.js**: Back-end para demonstrar integração com armazenamento persistente.
- **Docker**: Construção e execução de contêineres.
- **GitHub Actions**: Pipeline de CI/CD.
- **Python**: Automação de comandos `kubectl`.

---

## Estrutura do Projeto

- **`app/`**: Código da aplicação Node.js.
- **`scripts/`**: Automação para comandos `kubectl`.
- **`pv.yaml`**: Definição de um Persistent Volume.
- **`pvc.yaml`**: Definição de um Persistent Volume Claim.
- **`.github/workflows/`**: Configuração do pipeline de CI/CD.
- **`Dockerfile`**: Configuração do ambiente Docker.

---

## Como Executar o Projeto

### 1. Subir o Ambiente Kubernetes

- Aplique o **Persistent Volume**:
  ```bash
  kubectl apply -f pv.yaml
  ```

- Aplique o **Persistent Volume Claim**:
  ```bash
  kubectl apply -f pvc.yaml
  ```

### 2. Rodar a Aplicação Node.js

- Construa a imagem Docker:
  ```bash
  docker build -t kubernetes-pv-app .
  ```

- Rode o contêiner:
  ```bash
  docker run -p 3000:3000 kubernetes-pv-app
  ```

### 3. Automação de Comandos `kubectl`

- Execute o script Python:
  ```bash
  python3 scripts/kubectl_command.py
  ```

- Insira os comandos como:
  ```
  criar-pv, pv.yaml
  deletar-pvc, my-pvc
  ```

---

## Pipeline de CI/CD

O pipeline realiza:
1. Testes automatizados da aplicação Node.js.
2. Testes do script Python para validação de comandos `kubectl`.

---

## Contribuições

Sinta-se à vontade para abrir issues ou pull requests com melhorias!

---

## Autor

**[Seu Nome](https://github.com/seu-usuario)**
