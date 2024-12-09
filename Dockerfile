# Imagem base
FROM node:14

# Configuração do diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY . .

# Instalar dependências
RUN npm install

# Expor a porta da aplicação
EXPOSE 3000

# Comando para rodar o servidor
CMD ["node", "server.js"]
