/**
 * LCM Campus Ministry - Professional JS
 * Handles UI interactions, search filtering, and enhanced UX.
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log("LCM Portal initialized.");

    // 1. Smooth Navbar Transition
    const nav = document.querySelector('nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                nav.style.background = "rgba(255, 255, 255, 0.95)";
                nav.style.backdropFilter = "blur(10px)";
                nav.style.boxShadow = '0 4px 20px rgba(0,0,0,0.08)';
            } else {
                nav.style.background = "white";
                nav.style.boxShadow = 'none';
            }
        });
    }

    // 2. Resource Hub Search Logic
    const searchInput = document.getElementById('resourceSearch');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const term = e.target.value.toLowerCase();
            const cards = document.querySelectorAll('.resource-card');
            
            cards.forEach(card => {
                const title = card.querySelector('h3').innerText.toLowerCase();
                card.style.display = title.includes(term) ? 'flex' : 'none';
            });
        });
    }

    // 3. Admin Button Processing State
    // Updated: Only triggers on actual submit, not modal cancels
    const adminForms = document.querySelectorAll('form');
    adminForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const btn = form.querySelector('button[type="submit"]');
            if (btn) {
                btn.disabled = true;
                btn.style.opacity = "0.7";
                btn.innerHTML = `Processing...`;
            }
        });
    });

    // 4. Personalized Time-Based Greeting
    updateGreeting();
});

/**
 * Tab Switching Logic for Admin Powerpanel
 */
function openTab(evt, tabName) {
    const adminCard = document.getElementsByClassName("admin-card");
    for (let i = 0; i < adminCard.length; i++) adminCard[i].classList.remove("active");
    
    const navPill = document.getElementsByClassName("nav-pill");
    for (let i = 0; i < navPill.length; i++) navPill[i].classList.remove("active");
    
    document.getElementById(tabName).classList.add("active");
    evt.currentTarget.classList.add("active");
}

/**
 * Event Modal Controls
 */
function openEditEvent(id, title, loc) {
    document.getElementById('edit_event_id').value = id;
    document.getElementById('edit_event_title').value = title;
    document.getElementById('edit_event_loc').value = loc;
    document.getElementById('editEventModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('editEventModal').style.display = 'none';
}

/**
 * Resource Modal Controls (NEW)
 */
function openEditResource(id, name) {
    document.getElementById('edit_file_id').value = id;
    document.getElementById('edit_file_name').value = name;
    document.getElementById('editResourceModal').style.display = 'block';
}

function closeResourceModal() {
    document.getElementById('editResourceModal').style.display = 'none';
}

/**
 * Updates the welcome text based on the time of day
 */
function updateGreeting() {
    const greetingArea = document.getElementById('dynamic-greeting');
    if (!greetingArea) return;

    const hour = new Date().getHours();
    let message = "Welcome to LCM Portal";

    if (hour < 12) message = "Good Morning! Wishing you a productive day.";
    else if (hour < 17) message = "Good Afternoon! Take a break and join us.";
    else if (hour < 21) message = "Good Evening! Hope your day was blessed.";
    else message = "Rest well. See you tomorrow!";

    greetingArea.innerText = message;
}

/**
 * Universal Modal Closer (Closes when clicking outside the box)
 */
window.onclick = function(event) {
    if (event.target.className === 'modal') {
        closeModal();
        closeResourceModal();
    }
}