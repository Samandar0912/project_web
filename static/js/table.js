document.addEventListener('DOMContentLoaded', function () {

    const crimeFilter = document.getElementById('crimeFilter');
    const bankFilter = document.getElementById('bankFilter');
    const appFilter = document.getElementById('appFilter');
    const dateFilter = document.getElementById('dateFilter');
    const applyFilterButton = document.getElementById('applyFilter');
    const clearFilterButton = document.getElementById('clearFilter');
    const table = document.getElementById('dataTable');
    const toggle = document.querySelector('.navbar-toggle');
    const menu = document.querySelector('.navbar-menu');

    if (crimeFilter && bankFilter && appFilter && dateFilter && applyFilterButton && clearFilterButton && table) {
        const rows = table.getElementsByTagName('tr');

        function filterTable() {
            const crimeValue = crimeFilter.value.toLowerCase();
            const bankValue = bankFilter.value.toLowerCase();
            const appValue = appFilter.value.toLowerCase();
            const dateValue = dateFilter.value;

            for (let i = 1; i < rows.length; i++) {
                const row = rows[i];
                const crime = row.cells[9].textContent.toLowerCase();
                const bank = row.cells[11].textContent.toLowerCase();
                const app = row.cells[12].textContent.toLowerCase();
                const date = row.cells[1].textContent;

                const crimeMatch = crimeValue === '' || crime === crimeValue;
                const bankMatch = bankValue === '' || bank === bankValue;
                const appMatch = appValue === '' || app === appValue;
                const dateMatch = dateValue === '' || date === new Date(dateValue).toLocaleDateString('uz-UZ', { day: '2-digit', month: '2-digit', year: 'numeric' }).replace(/\//g, '.');

                if (crimeMatch && bankMatch && appMatch && dateMatch) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            }
        }

        // Tozalash funksiyasi
        function clearFilters() {
            crimeFilter.value = '';
            bankFilter.value = '';
            appFilter.value = '';
            dateFilter.value = '';
            filterTable(); // Filtrlarni tozalagandan so‘ng jadvalni yangilash
        }

        // Tugma bosilganda filtrni ishga tushiramiz
        applyFilterButton.addEventListener('click', filterTable);
        clearFilterButton.addEventListener('click', clearFilters);

        // Sahifa yuklanganda dastlabki holatda filtrni ishga tushiramiz
        filterTable();
    } else {
        console.error('Filtrlash elementlari topilmadi');
    }

    if (toggle && menu) {
        toggle.addEventListener('click', () => {
            menu.classList.toggle('active');
        });
    } else {
        console.error('Navbar elementlari topilmadi');
    }




    // Navbar uchun mobil menyu funksiyasi
    if (toggle && menu) {
        toggle.addEventListener('click', () => {
            menu.classList.toggle('active');
        });
    } else {
        console.error('Navbar elementlari topilmadi: navbar-toggle yoki navbar-menu');
    }
});



