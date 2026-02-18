# 🎓 Plantilla de Exámenes Interactivos (Estilo Neon)

> **Repositorio de Referencia**: Este proyecto ha sido diseñado como una plantilla moderna y reutilizable para crear aplicaciones de exámenes tipo test para cualquier asignatura.

![Preview](https://via.placeholder.com/800x400?text=Preview+del+Examen)
*(Puedes reemplazar esta imagen con una captura de pantalla de tu examen)*

## ✨ Características

*   **Diseño Premium**: Interfaz moderna con tema "Neon Business" (Oro/Rojo) y fondo animado.
*   **Totalmente Responsivo**: Funciona perfectamente en ordenadores, tablets y móviles.
*   **Sistema de Examen Completo**:
    *   Navegación por preguntas con estado (Acierto/Fallo/Omitido).
    *   Barra de progreso circular y estadísticas en tiempo real.
    *   Feedback inmediato con explicaciones.
    *   "Memoria" de navegación: revisa tus respuestas anteriores.
*   **Fácil de Configurar**: Todo el contenido se carga desde archivos JSON simples.
*   **Integración IA**: Botón discreto para conectar con asistentes de estudio (ej. Notion, NotebookLM).

---

## 🚀 Cómo usar esta plantilla para tu asignatura

Sigue estos pasos para crear tu propia web de exámenes en minutos:

### 1. Clonar el Repositorio
Usa este botón de "Use this template" o clona el código:
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
```

### 2. Personalizar la Asignatura
1.  Abre `index.html` y cambia el título `<title>` y el `<h1>` por el nombre de tu materia.
2.  (Opcional) Cambia el logo/icono en la etiqueta `<link rel="icon">`.

### 3. Crear tus Exámenes
Los datos están en la carpeta `data/`. Para añadir un nuevo tema:
1.  Crea un archivo `data/tema_1.json` (o el número que quieras).
2.  Usa este formato:

```json
{
  "title": "NOMBRE DEL TEMA",
  "items": [
    {
      "question": "Enunciado de la pregunta...",
      "options": [
        "Opción A",
        "Opción B",
        "Opción C",
        "Opción D"
      ],
      "correctAnswer": 0,
      "explanation": "Explicación opcional que sale al responder."
    }
  ]
}
```
*Importante: `correctAnswer` es el número de la opción correcta, empezando por 0 (0 es la primera, 1 la segunda...)*

### 4. Configurar el Menú Principal
En `index.html`, edita las tarjetas para que apunten a tus archivos:
```html
<div class="card" onclick="window.location.href='exam.html?tema=1'">
    <h2>TEMA 01</h2>
    <p>Descripción del tema</p>
</div>
```

---

## 🎨 Personalización Visual

Si los colores Oro/Rojo no encajan con tu asignatura, edita `css/style.css`. Al principio del archivo encontrarás las variables principales:

```css
:root {
    --bg: #0f100a;       /* Fondo */
    --gold: #EAB308;     /* Color Principal */
    --red: #DC2626;      /* Color Secundario/Error */
}
```
¡Cámbialas por las que quieras y toda la web se actualizará automáticamente!

---

## 🌐 Publicar en Internet (Gratis)

1.  Sube tu código a GitHub.
2.  Ve a la pestaña **Settings** > **Pages** de tu repositorio.
3.  En "Source", elige la rama `main` o `master`.
4.  ¡Listo! GitHub te dará un enlace (ej: `tu-usuario.github.io/tu-repo`) para compartir.

---

## 🤝 Créditos

Creado como proyecto de referencia para la digitalización de exámenes de Simulación Empresarial y otras materias.
Diseño inspirado en `EMPLEABILIDAD-II`.
