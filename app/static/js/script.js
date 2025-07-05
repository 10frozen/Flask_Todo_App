// Auto-hide flash messages after 5 seconds
setTimeout(() => {
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(flash => {
        flash.style.transition = 'opacity 0.5s ease-out';
        flash.style.opacity = '0';
        setTimeout(() => flash.remove(), 500);
    });
}, 5000);

// Confirm before clearing all tasks
const clearBtn = document.querySelector('form[action$="/clear"] button');
if (clearBtn) {
    clearBtn.addEventListener('click', function (e) {
        if (!confirm("Are you sure you want to clear all tasks?")) {
            e.preventDefault();
        }
    });
}

// Toggle password visibility on login/register
document.querySelectorAll('input[type="password"]').forEach(input => {
    const toggle = document.createElement('span');
    toggle.innerText = '👁️';
    toggle.style.marginLeft = '10px';
    toggle.style.cursor = 'pointer';
    toggle.style.userSelect = 'none';
    toggle.title = 'Show/hide password';

    toggle.addEventListener('click', () => {
        input.type = input.type === 'password' ? 'text' : 'password';
    });

    input.parentElement.appendChild(toggle);
});
