FROM node:16-alpine

WORKDIR /app

# Usar usuario root temporalmente para la instalación
USER root

COPY package.json ./
RUN npm install

# Dar permisos completos al directorio
RUN chmod -R 777 /app/node_modules

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host"]