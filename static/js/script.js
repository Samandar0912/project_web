document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const menuBtn = document.getElementById('menuBtn');
    const closeBtn = document.getElementById('closeBtn');
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    // Sidebar ochilishi/yopilishi
    menuBtn.addEventListener('click', () => {
        sidebar.classList.add('active');
    });

    closeBtn.addEventListener('click', () => {
        sidebar.classList.remove('active');
    });

    document.addEventListener('click', (e) => {
        if (!sidebar.contains(e.target) && !menuBtn.contains(e.target)) {
            sidebar.classList.remove('active');
        }
    });

    // Dropdown ochilishi/yopilishi
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault(); // Linkning standart harakatini to'xtatish
            const dropdown = toggle.parentElement; // .dropdown elementi
            const isActive = dropdown.classList.contains('active');

            // Barcha dropdownlarni yopish
            document.querySelectorAll('.dropdown').forEach(d => {
                d.classList.remove('active');
            });

            // Agar dropdown allaqachon ochiq bo'lmasa, uni ochish
            if (!isActive) {
                dropdown.classList.add('active');
            }
        });
    });
       
    
    document.getElementById('applyFilter').addEventListener('click', function(e) {
        e.preventDefault();
        document.getElementById('filterForm').submit();
    });

    
    document.getElementById('clearFilter').addEventListener('click', function() {
        window.location.href = '{% url "table" %}';
    });

 
});