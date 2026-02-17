# Plantilla de Exámenes Interactivos (Estilo Neon Business)

Este repositorio contiene una aplicación web moderna para realizar exámenes tipo test, diseñada para ser reutilizable en otras asignaturas.

## 🚀 Cómo usar este proyecto para otra asignatura

Si quieres crear una web igual para otra materia (por ejemplo, "Gestión Financiera"), sigue estos pasos:

### 1. Clonar o Descargar
Descarga este código o clona el repositorio en tu ordenador.

### 2. Personalizar el Nombre y Tema
Abre el archivo `index.html` y cambia los títulos:
```html
<title>TU ASIGNATURA - Exámenes</title>
...
<h1>TU ASIGNATURA</h1>
```

Si quieres cambiar los colores (por ejemplo, a Azul/Cian en lugar de Oro/Rojo), edita `css/style.css` y cambia las variables al principio del archivo:
```css
:root {
    --bg: #0f172a;       /* Fondo oscuro */
    --gold: #38bdf8;     /* Color principal (ej. Cian) */
    --red: #f43f5e;      /* Color secundario */
}
```

### 3. Añadir tus Preguntas
La aplicación lee las preguntas de la carpeta `data/`.
Para crear un nuevo examen:
1. Crea un archivo `data/tema_1.json`.
2. Pega la estructura siguiente:

```json
{
  "title": "TÍTULO DEL TEMA",
  "items": [
    {
      "question": "¿Cuál es la capital de Francia?",
      "options": [
        "Londres",
        "Berlín",
        "París",
        "Madrid"
      ],
      "correctAnswer": 2,
      "explanation": "París es la capital de Francia desde..."
    }
  ]
}
```
*Nota: `correctAnswer` es el índice de la respuesta correcta (empieza en 0).*

### 4. Configurar el Menú
Abre `index.html` y actualiza los enlaces de los botones para que apunten a tus nuevos temas:
```html
<div class="card" onclick="window.location.href='exam.html?tema=1'">
    <h2>TEMA 01</h2>
    <p>Nombre del Tema</p>
</div>
```

### 5. Personalizar el Botón de IA
En `exam.html`, busca el botón "PREGUNTAME" y cambia el enlace de `notebooklm.google.com` por tu propio cuaderno de inteligencia artificial.

## 🛠️ Estructura de Archivos
- `index.html`: Menú principal.
- `exam.html`: Plantilla del examen (no necesitas tocarla mucho).
- `css/style.css`: Diseño y colores.
- `js/app.js`: Lógica del examen (¡no tocar si no sabes programación!).
- `data/`: Aquí van tus preguntas en formato JSON.

## 📦 Despliegue (Publicar en Internet)
La forma más fácil es usar **GitHub Pages**:
1. Sube tu código a un repositorio de GitHub.
2. Ve a **Settings** > **Pages**.
3. En **Source**, selecciona `main` o `master` y guarda.
4. ¡Tu web estará online en minutos!
