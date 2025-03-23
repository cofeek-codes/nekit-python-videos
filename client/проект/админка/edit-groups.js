document.addEventListener('DOMContentLoaded', function () {
    const criteriaContainer = document.getElementById('criteriaContainer');
    const addButton = document.getElementById('addCriteriaButton');
    const newCriteriaInput = document.getElementById('newCriteriaInput');

    // Обработка кликов по всем контейнерам
    document.addEventListener('click', function (e) {
        // Удаление элемента
        if (e.target.classList.contains('delete-image')) {
            e.preventDefault(); // предотвращаем поведение по умолчанию
            const raschetItem = e.target.closest('.raschet'); // находим ближайший родительский элемент с классом .raschet
            if (raschetItem) {
                raschetItem.remove(); // Удаляем элемент из DOM
            }
        }
    });

    // Функция для добавления нового критерия
    function addNewCriteria() {
        const newCriteriaText = newCriteriaInput.value.trim(); // Получаем введенный текст
        
        // Проверяем, что текст не пустой
        if (newCriteriaText) {
            // Создаем новый элемент
            const newDiv = document.createElement('div');
            newDiv.classList.add('raschet');

            const newLink = document.createElement('a');
            newLink.href = "#"; // Поставьте нужную ссылку здесь
            newLink.classList.add('redact_gr');
            newLink.textContent = newCriteriaText; // Текст нового критерия

            const deleteImage = document.createElement('img');
            deleteImage.src = "img/delete.svg"; // Путь к изображению удаления
            deleteImage.alt = "Удалить";
            deleteImage.classList.add('delete-image');

            // Добавляем обработчик для удаления
            deleteImage.addEventListener('click', function(e) {
                e.preventDefault();
                newDiv.remove(); // Удаляем элемент при клике
            });

            // Добавляем элементы в новый div
            newDiv.appendChild(newLink);
            newDiv.appendChild(deleteImage);

            // Добавляем новый элемент в контейнер
            criteriaContainer.appendChild(newDiv);

            // Очищаем input после добавления элемента
            newCriteriaInput.value = '';
        } else {
            alert('Пожалуйста, введите текст критерия.'); // Предупреждение, если текст пустой
        }
    }

    // Добавляем обработчик на кнопку
    addButton.addEventListener('click', addNewCriteria);
});
