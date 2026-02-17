document.addEventListener('DOMContentLoaded', () => {
    // 1. Obtener el parámetro 'tema' de la URL
    const urlParams = new URLSearchParams(window.location.search);
    const themeId = urlParams.get('tema');
    
    // Elementos del DOM
    const examTitle = document.getElementById('exam-title');
    const questionContainer = document.getElementById('question-container');
    const resultsContainer = document.getElementById('results-container');
    const scoreElement = document.getElementById('score');
    const restartBtn = document.getElementById('restart-btn');
    const backBtn = document.getElementById('back-btn');

    if (!themeId) {
        showError('No se ha especificado un tema.');
        return;
    }

    // 2. Cargar el archivo JSON correspondiente
    fetch(`data/tema_${themeId}.json`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`No se pudo cargar el archivo data/tema_${themeId}.json`);
            }
            return response.json();
        })
        .then(data => {
            // 3. Inicializar el examen con los datos cargados
            initExam(data);
        })
        .catch(error => {
            console.error('Error:', error);
            showError(`Error al cargar el examen: ${error.message}`);
        });

    function initExam(data) {
        // Establecer el título
        examTitle.textContent = data.title || `Tema ${themeId}`;
        document.title = data.title || `Examen Tema ${themeId}`;

        // Generar las preguntas
        renderQuestions(data.items);
    }

    function renderQuestions(questions) {
        questionContainer.innerHTML = '';
        
        questions.forEach((item, index) => {
            const questionCard = document.createElement('div');
            questionCard.className = 'card question-card';
            
            // Header de la pregunta
            const questionHeader = document.createElement('div');
            questionHeader.className = 'question-header';
            questionHeader.innerHTML = `<h3>Pregunta ${index + 1}</h3>`;
            questionCard.appendChild(questionHeader);

            // Texto de la pregunta
            const questionText = document.createElement('p');
            questionText.className = 'question-text';
            questionText.textContent = item.question;
            questionCard.appendChild(questionText);

            // Opciones
            const optionsContainer = document.createElement('div');
            optionsContainer.className = 'options-container';

            item.options.forEach((option, optionIndex) => {
                const button = document.createElement('button');
                button.className = 'option-btn';
                button.textContent = option;
                button.dataset.index = optionIndex;
                
                button.addEventListener('click', () => {
                    handleAnswer(button, item, optionsContainer, optionIndex);
                });

                optionsContainer.appendChild(button);
            });

            questionCard.appendChild(optionsContainer);

            // Explicación (oculta inicialmente)
            const explanation = document.createElement('div');
            explanation.className = 'explanation hidden';
            explanation.innerHTML = `<strong>Explicación:</strong> ${item.explanation}`;
            questionCard.appendChild(explanation);

            questionContainer.appendChild(questionCard);
        });
    }

    function handleAnswer(selectedButton, item, container, selectedIndex) {
        // Evitar múltiples respuestas
        if (container.classList.contains('answered')) return;
        
        container.classList.add('answered');
        const buttons = container.querySelectorAll('.option-btn');
        const explanation = container.parentElement.querySelector('.explanation');
        
        // Marcar correcta e incorrecta
        if (selectedIndex === item.correctAnswer) {
            selectedButton.classList.add('correct');
            updateScore(1);
        } else {
            selectedButton.classList.add('incorrect');
            buttons[item.correctAnswer].classList.add('correct'); // Mostrar la correcta
        }

        // Deshabilitar botones
        buttons.forEach(btn => btn.disabled = true);

        // Mostrar explicación
        if (explanation) {
            explanation.classList.remove('hidden');
            explanation.classList.add('visible');
        }
    }

    let currentScore = 0;
    let totalQuestions = 0;

    function updateScore(points) {
        currentScore += points;
        // Calcular total de preguntas dinámicamente si no se ha hecho
        if (totalQuestions === 0) {
            totalQuestions = document.querySelectorAll('.question-card').length;
        }
        
        // Actualizar UI del score si existiera un contador en tiempo real, 
        // pero por ahora solo mostraremos el resultado final si se implementa un botón de "Finalizar",
        // o simplemente dejamos el feedback inmediato.
        
        // En este diseño tipo lista, el feedback es inmediato y scroll.
    }

    function showError(message) {
        questionContainer.innerHTML = `<div class="error-message">${message}</div>`;
    }

    // Botón Volver
    backBtn.addEventListener('click', () => {
        window.location.href = 'index.html';
    });
});
