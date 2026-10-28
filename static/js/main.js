/**
 * Global Fuel Analytics - Client-Side Interactive Script
 * Author: Suhan
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Navbar elevation on scroll
    const navbar = document.getElementById('siteNavbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                navbar.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.4)';
            } else {
                navbar.style.boxShadow = 'none';
            }
        });
    }

    // 2. Auto-dismiss alerts after 6 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach((alert) => {
        setTimeout(() => {
            try {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            } catch (e) {
                // Ignore if bootstrap is not ready or alert already closed
            }
        }, 6000);
    });

    // 3. Form validation helper
    const contactForm = document.querySelector('form[action*="contact"]');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            const name = document.getElementById('name');
            const email = document.getElementById('email');
            const message = document.getElementById('message');

            if (!name.value.trim() || !email.value.trim() || !message.value.trim()) {
                e.preventDefault();
                alert('Kripya sabhi zaroori fields (Name, Email, Message) bharein.');
            }
        });
    }

    console.log('Global Fuel Analytics platform initialized successfully.');
});

