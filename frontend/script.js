// Smooth scrolling function
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Navigation link smooth scroll
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        scrollToSection(targetId);
    });
});

// Animate elements on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeIn 0.6s ease forwards';
        }
    });
}, observerOptions);

document.querySelectorAll('.module-card').forEach(card => {
    observer.observe(card);
});

// Add click handlers for buttons
document.querySelectorAll('.btn-secondary').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        const parentCard = this.closest('.module-card');
        const cardTitle = parentCard.querySelector('h3').textContent;
        showNotification(`${cardTitle} feature clicked!`);
    });
});

// Notification function
function showNotification(message) {
    // Create notification element
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #10b981;
        color: white;
        padding: 1rem 2rem;
        border-radius: 5px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        font-weight: 500;
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Add CSS animations for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Add active state to nav links
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');
    
    sections.forEach(section => {
        const top = section.offsetTop;
        const offset = section.offsetHeight;
        
        if (window.scrollY >= top - 200) {
            navLinks.forEach(link => {
                link.classList.remove('active');
            });
            
            const activeLink = document.querySelector(`.nav-link[href="#${section.id}"]`);
            if (activeLink) {
                activeLink.style.borderBottom = '3px solid white';
            }
        }
    });
});

// Counter animation for stats
function animateCounter(element, target, duration = 2000) {
    const start = parseInt(element.textContent.replace(/\D/g, ''));
    const increment = (target - start) / (duration / 16);
    let current = start;
    
    const counter = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target;
            clearInterval(counter);
        } else {
            element.textContent = Math.ceil(current);
        }
    }, 16);
}

// Animate stats when they come into view
document.querySelectorAll('.stat-number').forEach(stat => {
    observer.observe(stat);
    stat.addEventListener('animationend', function() {
        const targetText = this.parentElement.querySelector('h3').textContent;
        if (targetText === 'Total Students') {
            animateCounter(this, 250);
        } else if (targetText === 'Total Faculty') {
            animateCounter(this, 45);
        } else if (targetText === 'Total Courses') {
            animateCounter(this, 32);
        }
    });
});

console.log('College Management System Frontend Loaded Successfully!');
