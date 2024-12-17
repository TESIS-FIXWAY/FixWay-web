# 🚗 **FixWay Web**  
**Una extensión web de la aplicación de escritorio para la gestión eficiente de talleres mecánicos.**

---

## 📋 **Descripción del Proyecto**  

**FixWay Web** es una plataforma e-commerce que complementa la aplicación de escritorio **FixWay Escritorio**, diseñada para la gestión integral de talleres mecánicos. Esta extensión web permite a los usuarios visualizar y adquirir productos del inventario creado desde la aplicación de escritorio, facilitando así la gestión del negocio y brindando una experiencia optimizada para clientes y administradores.

El proyecto está desarrollado de manera privada en colaboración con mi equipo, utilizando tecnologías modernas para garantizar rendimiento, funcionalidad y una interfaz atractiva.

---

## 🚀 **Tecnologías Utilizadas**  

### **Frontend**  
- **React.js**: Framework principal para la construcción de una interfaz dinámica y atractiva, asegurando una experiencia de usuario fluida y responsiva.  

### **Backend**  
- **Firebase**:  
  - **Base de datos en tiempo real**: Para garantizar sincronización instantánea entre los productos del inventario y la web.  
  - **Autenticación segura**: Para proteger el acceso a la plataforma.  

### **Aplicación de Escritorio**  
- **Tauri.js**: Permite empaquetar la aplicación web como un programa de escritorio ligero y eficiente en recursos.  

---

## 🎯 **Funcionalidades Principales**  

- **Visualización del Inventario**: Productos cargados desde **FixWay Escritorio** se muestran de forma clara y accesible.  
- **E-commerce Integrado**: Permite la gestión de compras de manera rápida y organizada.  
- **Autenticación de Usuarios**: Registro e inicio de sesión seguros mediante Firebase.  
- **Sincronización en Tiempo Real**: Actualización constante entre la aplicación de escritorio y la plataforma web.  

---

## 🖥️ **FixWay Escritorio**  

La versión de escritorio de FixWay sirve como núcleo para la gestión completa del inventario y las operaciones de un taller mecánico. Los productos del inventario se sincronizan con la plataforma web, permitiendo a los clientes explorar y realizar compras online.  

Más detalles sobre **FixWay Escritorio** disponibles en:  
- [LinkedIn - Proyectos de Samuel Gajardo](https://www.linkedin.com/in/samuel-gajardos/details/projects/)  

---

## 📂 **Estructura del Proyecto**  

```bash
FixWay-web/
├── public/          # Archivos estáticos
├── src/             # Código fuente principal
│   ├── components/  # Componentes reutilizables
│   ├── pages/       # Páginas de la aplicación
│   ├── services/    # Integración con Firebase
│   ├── assets/      # Imágenes y recursos
│   └── App.js       # Componente raíz
├── package.json     # Dependencias y scripts
└── README.md        # Documentación
