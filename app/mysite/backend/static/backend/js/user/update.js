// Добавьте эти переменные в начало файла
const saveButton = document.getElementById('saveButton');
const totalCount = document.getElementById('totalCount');

// Обновленная функция сохранения
function updateCriteria() {
    const criteriasData = {
        titles: Array.from(document.querySelectorAll('.redact_gr')).map(link => ({
            id: link.dataset.id,
            title: link.textContent
        })),
        counts: Array.from(document.querySelectorAll('.count')).map(counter => ({
            id: counter.closest('.raschet').querySelector('.redact_gr').dataset.id,
            count: parseInt(counter.innerText)
        }))
    };

    fetch(saveButton.dataset.url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(criteriasData)
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showSuccessMessage();
                updateTotalCount(); // Обновляем общую сумму
            } else {
                console.error('Ошибка при сохранении:', data.message);
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
}

// Функция для получения CSRF-токена из cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Функция показа сообщения об успехе
function showSuccessMessage() {
    const saveSuccess = document.getElementById('saveSuccess');
    saveSuccess.style.display = 'block';
    setTimeout(() => {
        saveSuccess.style.display = 'none';
    }, 2000);
}

// Замените старый обработчик на новый
saveButton.addEventListener('click', function (e) {
    e.preventDefault();
    updateCriteria();
});
