document.addEventListener('DOMContentLoaded', function () {
    const criteriaContainer = document.querySelector('.form-container'); // Получаем контейнер
    const addButton = document.getElementById('addCriteriaButton'); // Кнопка добавления
    const newCriteriaInput = document.getElementById('newCriteriaInput'); // Поле ввода нового критерия

    // Обработка кликов по всем элементам
    document.addEventListener('click', function (e) {
        // Удаление критерия
        if (e.target.classList.contains('delete-image')) {
            e.preventDefault(); // предотвращаем поведение по умолчанию
            const raschetItem = e.target.closest('.raschet'); // находим родительский элемент
            if (raschetItem) {
                raschetItem.remove(); // Удаление элемента из DOM
            }
        }
    });

    // Добавление нового критерия
    function addNewCriteria() {
        const newCriteriaText = newCriteriaInput.value.trim(); // Получаем текст из input

        // Проверяем введенный текст
        if (newCriteriaText) {
            // Создаем новый элемент критерия
            const newDiv = document.createElement('div');
            newDiv.classList.add('raschet');

            const newLink = document.createElement('a');
            newLink.href = "#"; // Замените на нужную ссылку
            newLink.classList.add('redact_gr');
            newLink.textContent = newCriteriaText; // Устанавливаем текст нового критерия

            const deleteImage = document.createElement('img');
            deleteImage.src = "img/delete.svg"; // Путь к изображению удаления;
            deleteImage.alt = "Удалить";
            deleteImage.classList.add('delete-image');
            // Добавляем функционал удаления на новый элемент
        deleteImage.addEventListener('click', function (e) {
            e.preventDefault();
            newDiv.remove(); // Удалить элемент при клике
        });

        // Добавляем ссылки и изображение в новый div
        newDiv.appendChild(newLink);
        newDiv.appendChild(deleteImage);

        // Добавляем новый элемент в контейнер
        criteriaContainer.appendChild(newDiv);

        // Очищаем input
        newCriteriaInput.value = '';
        } else {
            alert('Пожалуйста, введите текст критерия.'); // Если текст пустой, предупредить
        }
    }

    // Обработчик события для кнопки добавления
    addButton.addEventListener('click', addNewCriteria);
});