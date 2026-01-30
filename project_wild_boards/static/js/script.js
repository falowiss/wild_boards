// Мобильное меню
document.addEventListener('DOMContentLoaded', function() {
    // Создаем кнопку мобильного меню
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelector('.nav-links');
    
    const menuToggle = document.createElement('button');
    menuToggle.className = 'menu-toggle';
    menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
    navbar.appendChild(menuToggle);
    
    // Переключение мобильного меню
    menuToggle.addEventListener('click', function() {
        navLinks.classList.toggle('active');
        menuToggle.innerHTML = navLinks.classList.contains('active') 
            ? '<i class="fas fa-times"></i>' 
            : '<i class="fas fa-bars"></i>';
    });
    
    // Закрытие меню при клике на ссылку
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function() {
            navLinks.classList.remove('active');
            menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
        });
    });
    
    // Плавная прокрутка
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Анимация при скролле
    const observerOptions = {
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    }, observerOptions);
    
    // Наблюдаем за карточками меню
    document.querySelectorAll('.menu-category-card').forEach(card => {
        observer.observe(card);
    });
    
    // Форма бронирования
    const bookingForm = document.getElementById('booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const bookingData = {
                name: formData.get('name'),
                phone: formData.get('phone'),
                datetime: formData.get('datetime'),
                guests: parseInt(formData.get('guests')),
                message: formData.get('message')
            };
            
            try {
                // Здесь будет запрос к API
                console.log('Данные для бронирования:', bookingData);
                
                // Временное сообщение об успехе
                alert('Запрос на бронирование отправлен! Мы свяжемся с вами в течение 15 минут.');
                this.reset();
            } catch (error) {
                console.error('Error:', error);
                alert('Произошла ошибка. Пожалуйста, попробуйте позже или позвоните нам.');
            }
        });
    }
});

