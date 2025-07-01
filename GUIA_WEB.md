# 🌐 Guía para Subir tu Conversor WEBM a MP4 a Internet GRATIS

## 🎯 **Opciones Gratuitas para Hospedar tu App**

### 🚀 **Opción 1: Render.com (RECOMENDADO)**

#### ✅ **Ventajas:**
- ✅ **Completamente GRATIS** para proyectos pequeños
- ✅ **750 horas gratis** por mes (más que suficiente)
- ✅ **Fácil de configurar** con GitHub
- ✅ **HTTPS automático** (SSL incluido)
- ✅ **URL personalizada** gratuita

#### 📋 **Pasos para subir a Render:**

1. **Crear cuenta gratuita en Render:**
   - Ve a: https://render.com
   - Regístrate con tu email o GitHub

2. **Subir tu código a GitHub:**
   - Crea una cuenta en https://github.com (si no tienes)
   - Crea un repositorio nuevo llamado `webm-converter`
   - Sube todos los archivos de tu carpeta `Programa`

3. **Conectar con Render:**
   - En Render, haz clic en "New +" → "Web Service"
   - Conecta tu repositorio de GitHub
   - Selecciona tu repositorio `webm-converter`

4. **Configurar el servicio:**
   ```
   Name: webm-converter
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn web_app:app --bind 0.0.0.0:$PORT
   ```

5. **¡Deploy automático!**
   - Render instalará todo automáticamente
   - En 5-10 minutos tendrás tu URL pública
   - Ejemplo: `https://webm-converter-abc123.onrender.com`

---

### 🌈 **Opción 2: Railway.app**

#### 📋 **Pasos rápidos:**
1. Ve a: https://railway.app
2. Conecta tu GitHub
3. Selecciona tu repositorio
4. ¡Railway detecta Python automáticamente!

---

### ☁️ **Opción 3: Heroku (Limitado)**

Heroku cambió a planes de pago, pero puedes usar los créditos gratuitos iniciales.

---

## 🛠️ **Preparar tu Proyecto para Internet**

### 📁 **Estructura de Archivos Necesaria:**
```
tu-proyecto/
├── web_app.py          ← App principal
├── requirements.txt    ← Dependencias
├── Procfile           ← Configuración del servidor
├── runtime.txt        ← Versión de Python
├── templates/
│   └── index.html     ← Interfaz web
├── uploads/           ← Se crea automáticamente
└── converted/         ← Se crea automáticamente
```

### ⚙️ **Archivos ya incluidos:**
- ✅ `web_app.py` - Aplicación Flask
- ✅ `requirements.txt` - Con Flask y dependencias
- ✅ `Procfile` - Para el servidor
- ✅ `runtime.txt` - Versión de Python
- ✅ `templates/index.html` - Interfaz hermosa

---

## 🎨 **Características de tu Web App:**

### 📱 **Responsive Design:**
- ✅ **Funciona perfecto en móviles**
- ✅ **Tablets y computadoras**
- ✅ **Drag & Drop** en escritorio
- ✅ **Botones grandes** para móvil

### 🎯 **Funcionalidades:**
- 🎬 **Subir archivos WEBM** (hasta 500MB)
- ⚙️ **Elegir calidad** (Baja/Media/Alta)
- 📊 **Progreso en tiempo real**
- 💾 **Descarga automática** del MP4
- 🗑️ **Limpieza automática** de archivos

### 🎨 **Interfaz Moderna:**
- 🌈 **Gradientes hermosos**
- 🎯 **Iconos FontAwesome**
- 📱 **Optimizada para móviles**
- 🌙 **Tema profesional**

---

## 🚀 **Guía Paso a Paso - Render.com**

### 1️⃣ **Preparar GitHub (5 minutos)**
```bash
# Si no tienes git instalado, descárgalo de: https://git-scm.com

# En tu carpeta del proyecto:
git init
git add .
git commit -m "Mi conversor WEBM a MP4"

# Crear repositorio en GitHub y subir:
git remote add origin https://github.com/tu-usuario/webm-converter.git
git push -u origin main
```

### 2️⃣ **Configurar Render (3 minutos)**
1. **Ir a Render.com** y crear cuenta
2. **New Web Service** → Conectar GitHub
3. **Seleccionar tu repositorio**
4. **Configuración automática** (Render detecta Python)
5. **Deploy** - ¡Listo en 5-10 minutos!

### 3️⃣ **¡Tu app estará online!**
- URL única: `https://tu-app.onrender.com`
- Acceso desde cualquier dispositivo
- Completamente GRATIS

---

## 📱 **Cómo Usar tu App Web:**

### 🌐 **En el Navegador:**
1. **Abre tu URL** en cualquier navegador
2. **Arrastra archivo WEBM** o usa el botón
3. **Selecciona calidad** (recomendado: Media)
4. **Espera la conversión** (progreso en tiempo real)
5. **Descarga tu MP4** cuando termine

### 📱 **En el Móvil:**
1. **Abre la URL** en Chrome/Safari
2. **Toca "Seleccionar Archivo"** 
3. **Elige desde Galería/Archivos**
4. **Configura y convierte**
5. **Descarga directo al móvil**

---

## 💡 **Tips Pro para tu App Web:**

### 🚀 **Optimización:**
- ✅ **Calidad Media** es perfecta para la mayoría
- ✅ **Máximo 500MB** por archivo (límite del servidor)
- ✅ **Una conversión** a la vez
- ✅ **Archivos se borran** automáticamente

### 🔒 **Seguridad:**
- ✅ **Solo archivos WEBM** permitidos
- ✅ **Limpieza automática** de archivos
- ✅ **Sin almacenamiento permanente**
- ✅ **Conexión HTTPS** segura

### 📊 **Límites Gratuitos (Render):**
- ✅ **750 horas/mes** de uso
- ✅ **512MB RAM** (suficiente)
- ✅ **Ancho de banda ilimitado**
- ✅ **SSL/HTTPS** incluido

---

## 🎊 **¡Felicidades!**

### 🌟 **Has creado:**
- 🎬 **Conversor profesional** WEBM → MP4
- 📱 **App móvil-friendly** 
- 🌐 **Servicio web gratuito**
- 🎨 **Interfaz hermosa y moderna**

### 📱 **Comparte tu app:**
- 👥 **Con amigos y familia**
- 💼 **En redes sociales**
- 🎯 **Para uso personal**
- 🚀 **Portfolio profesional**

---

## 🆘 **Solución de Problemas:**

### ❌ **"Error al deployar"**
- Verifica que `requirements.txt` esté completo
- Asegúrate de que `Procfile` esté en la raíz
- Revisa los logs en Render

### ❌ **"App muy lenta"**
- Es normal en planes gratuitos
- Render "duerme" la app si no se usa
- Primera carga puede tardar 30 segundos

### ❌ **"Error de conversión"**
- Verifica límite de 500MB por archivo
- Solo archivos WEBM válidos
- Intenta con calidad más baja

---

## 🎯 **URLs de Servicios Gratuitos:**

- 🚀 **Render:** https://render.com (RECOMENDADO)
- 🌈 **Railway:** https://railway.app  
- ☁️ **Vercel:** https://vercel.com (para apps simples)
- 🔥 **Netlify:** https://netlify.com (solo archivos estáticos)

---

**🎊 ¡Disfruta tu conversor WEBM a MP4 en internet! 🌐✨**
