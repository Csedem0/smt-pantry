document.addEventListener('DOMContentLoaded', function () {
    const sideLinks = document.querySelectorAll('.sidebar .side-menu li a:not(.logout)');

    sideLinks.forEach(item => {
        const li = item.parentElement;
        item.addEventListener('click', () => {
            sideLinks.forEach(i => {
                i.parentElement.classList.remove('active');
            });
            li.classList.add('active');
        });
    });

    const menuBar = document.querySelector('.content nav .bx.bx-menu');
    const sideBar = document.querySelector('.sidebar');

    menuBar.addEventListener('click', () => {
        sideBar.classList.toggle('open');
    });

    const searchBtn = document.querySelector('.content nav form .form-input button');
    const searchBtnIcon = document.querySelector('.content nav form .form-input button .bx');
    const searchForm = document.querySelector('.content nav form');

    searchBtn.addEventListener('click', function (e) {
        if (window.innerWidth < 576) {
            e.preventDefault();
            searchForm.classList.toggle('show');
            if (searchForm.classList.contains('show')) {
                searchBtn.innerHTML = '<i class=\'bx bx-x\'></i>';
            } else {
                searchBtn.innerHTML = '<i class=\'bx bx-search\'></i>';
            }
        }
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth < 768) {
            sideBar.classList.add('close');
        } else {
            sideBar.classList.remove('close');
        }
        if (window.innerWidth > 576) {
            searchBtn.innerHTML = '<i class=\'bx bx-search\'></i>';
            searchForm.classList.remove('show');
        }
    });

    const toggler = document.getElementById('theme-toggle');

    toggler.addEventListener('change', function () {
        if (this.checked) {
            document.body.classList.add('dark');
        } else {
            document.body.classList.remove('dark');
        }
    });

    // Ensure sidebar is closed by default on mobile view
    function checkWidth() {
        if (window.innerWidth < 768) {
            sideBar.classList.add('close');
        } else {
            sideBar.classList.remove('close');
        }
    }

    checkWidth();

    // Close search form when clicking outside
    document.addEventListener('click', function (event) {
        const isClickInside = searchForm.contains(event.target);
        if (!isClickInside && searchForm.classList.contains('show')) {
            searchForm.classList.remove('show');
            searchBtn.innerHTML = '<i class=\'bx bx-search\'></i>';
        }
    });
});
