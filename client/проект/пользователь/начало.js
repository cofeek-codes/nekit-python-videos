document.addEventListener('DOMContentLoaded', function () {
    const incrementButtons = document.querySelectorAll('.increment');
    const decrementButtons = document.querySelectorAll('.decrement');
    const uploadButtons = document.querySelectorAll('.uploadButton');
    const fileInputs = document.querySelectorAll('.fileInput');
    const totalCount = document.getElementById('totalCount');
    const saveButton = document.getElementById('saveButton');
    const saveSuccess = document.getElementById('saveSuccess');
    const criteriaLinks = document.querySelectorAll('.redact_gr');

    // Обработчики для кнопок увеличения и уменьшения счетчиков (с вызовом updateTotalCount)
    incrementButtons.forEach(button => {
        button.addEventListener('click', function () {
            const counter = button.closest('.counter').querySelector('.count');
            counter.innerText = parseInt(counter.innerText) + 1;
            updateTotalCount(); // Важно!
        });
    });

    decrementButtons.forEach(button => {
        button.addEventListener('click', function () {
            const counter = button.closest('.counter').querySelector('.count');
            let newValue = parseInt(counter.innerText) - 1;
            if (newValue < 0) newValue = 0;
            counter.innerText = newValue;
            updateTotalCount(); // Важно!
        });
    });

    // Функция createUploadSuccessNotification (без изменений)
    function createUploadSuccessNotification(message, index) {
        const uploadButton = uploadButtons[index];
        if (!uploadButton) return null;

        const notification = document.createElement('div');
        notification.className = 'uploadSuccessNotification';
        notification.textContent = message;
        notification.style.display = 'block';

        uploadButton.parentNode.insertBefore(notification, uploadButton.nextSibling);
        localStorage.setItem(`uploadSuccessMessage_${index}`, message);

        return notification;
    }

    // Обработчики для кнопок "Загрузить файл" (без изменений)
    uploadButtons.forEach((button, index) => {
        button.addEventListener('click', function () {
            fileInputs[index].click();
        });
    });

    // Обработчики для полей input type="file" (без изменений)
    fileInputs.forEach((fileInput, index) => {
        fileInput.addEventListener('change', function (event) {
            const file = event.target.files[0];

            if (file) {
                console.log(`Выбран файл для критерия ${index + 1}: ${file.name}`);

                const message = `Файл успешно загружен!`;
                createUploadSuccessNotification(message, index);
            } else {
                console.log(`Файл для критерия ${index + 1} не выбран.`);
            }
        });
    });

     // Функция для подсчета общей суммы значений счетчиков
    function updateTotalCount() {
        const counters = document.querySelectorAll('.count');
        let total = 0;
        counters.forEach(counter => {
            total += parseInt(counter.innerText);
        });

        if (total > 0) {
            totalCount.style.display = 'block';
            totalCount.textContent = `Количество баллов: ${total}`;
            localStorage.setItem('totalCountVisible', 'true');
        } else {
            totalCount.style.display = 'none';
            localStorage.removeItem('totalCountVisible');
        }
    }

    // Функция loadData (с вызовом updateTotalCount)
    function loadData() {
        const savedData = JSON.parse(localStorage.getItem('data'));
        if (savedData) {
            criteriaLinks.forEach((link, index) => {
                link.textContent = savedData.criteria[index] || link.textContent;
            });

            const counters = document.querySelectorAll('.count');
            counters.forEach((counter, index) => {
                counter.innerText = savedData.counters[index] || '0';
            });
        }

        uploadButtons.forEach((button, index) => {
            const message = localStorage.getItem(`uploadSuccessMessage_${index}`);
            if (message) {
                createUploadSuccessNotification(message, index);
            }
        });

        const totalCountVisible = localStorage.getItem('totalCountVisible') === 'true';

        if (totalCountVisible) {
            totalCount.style.display = 'block';
            updateTotalCount(); // Важно!
        } else {
          totalCount.style.display = 'none'; // Added to hide if not visible in localStorage
        }
    }


    // Добавляем обработчик для кнопки сохранения (с таймером)
    saveButton.addEventListener('click', function () {
        const savedData = {
            criteria: Array.from(criteriaLinks).map(link => link.textContent),
            counters: Array.from(document.querySelectorAll('.count')).map(counter => counter.innerText)
        };
        localStorage.setItem('data', JSON.stringify(savedData));

        saveSuccess.style.display = 'block';

        setTimeout(() => {
            saveSuccess.style.display = 'none';
        }, 2000);
    });

    loadData();
});
