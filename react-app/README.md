# --------------------------------- README CREACION APP REACT, DJANGO API CON DOCKER ------------------------------



# PASO 1 CREAR docker-compose 
 # NOTA: SINO SE CREAN EL PROYECTO MANUAL, AGREGAR image: node:14-alpine A CAMBIO DEL build: ./react-app DESPUES VUELVE Y SE CAMBIA
version: '3.5'
services:
  api_django:
    build: ./api_django
    command: python api_django/manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/my_app_django_dir
    ports:
      - "8000:8000"
  app:
    build: ./react-app
    command: npm start
    volumes:
      - './react-app:/app'
    ports:
      - "3000:3000"
    depends_on:
      - api_django
    tty: true


# PASO 2 CREAR PROYECTO REACT
    - sudo docker-compose run --rm app npx create-react-app react-app ######### image: node:14-alpine EN docker-compose
    - npx create-react-app react-app ###### TOCA INSTALAR REACT EN EL PC PARA ESTA OPCION

# PASO 3 CREAR Dockerfile EN AMBOS PROYECTOS/CARPETAS DjangoAPI Y ReactAPP Y AGREGAR build: EN docker-compose
    FROM node:14-alpine
    RUN mkdir /app
    WORKDIR /app
    ENV PATH /app/node_modules/.bin:$PATH
    # install app dependencies
    COPY package.json ./
    COPY package-lock.json ./
    RUN npm install
    COPY . /app/
    CMD ["npm", "start"]


# ACTUALIZACIONES EN ARCHIVOS DOCKER DEBO HACER UN BUILD
  docker-compose build





















# --------------------------------- README POR DEFECTO DE REACT ------------------------------


# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
