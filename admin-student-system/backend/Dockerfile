FROM node:16-alpine

WORKDIR /app

# Copiar package.json primero
COPY package*.json ./

# Instalar dependencias normalmente
RUN npm install

# Copiar el resto de la aplicación
COPY . .

EXPOSE 4000

CMD ["npm", "start"]