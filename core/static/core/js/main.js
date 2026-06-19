document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('serviceModal');
    const closeBtn = document.querySelector('.modal-close-btn');
    const cards = document.querySelectorAll('.open-modal');
    
    // Elementy wewnątrz okna modalnego, które będziemy podmieniać
    const modalTitle = document.getElementById('modalTitle');
    const modalDesc = document.getElementById('modalDescription');
    const modalPrice = document.getElementById('modalPrice');
    const modalImage = document.getElementById('modalImage');
    const modalActionBtn = document.getElementById('modalActionBtn');

    // Otwieranie okna po kliknięciu w kartę
    cards.forEach(card => {
        card.addEventListener('click', function() {
            // Pobieranie danych z klikniętej karty
            const title = this.getAttribute('data-title');
            const desc = this.getAttribute('data-description');
            const price = this.getAttribute('data-price');
            const image = this.getAttribute('data-image');

            // Wstrzykiwanie danych do okna modalnego
            modalTitle.textContent = title;
            modalDesc.textContent = desc;
            modalPrice.textContent = price;
            modalImage.src = image;

            // Pokazanie okna modalnego
            modal.classList.add('active');
            document.body.style.overflow = 'hidden'; // Blokuje przewijanie strony w tle
        });
    });

    // Zamykanie okna za pomocą przycisku X
    if (closeBtn) {
        closeBtn.addEventListener('click', closeModal);
    }

    // Zamykanie okna po kliknięciu w tło poza kartą popup
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeModal();
            }
        });
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto'; // Przywraca przewijanie strony
    }
    // --- ZAKŁADKI KATEGORII ---
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            // Usuń active ze wszystkich
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));

            // Dodaj active do klikniętego
            btn.classList.add('active');
            document.getElementById(btn.dataset.tab).classList.add('active');
        });
    });
    // --- GRADIENT ZAKŁADEK ---
    const tabsContainer = document.querySelector('.tabs-container');
    if (tabsContainer) {
        tabsContainer.addEventListener('scroll', () => {
            if (tabsContainer.scrollLeft > 10) {
                tabsContainer.classList.add('scrolled');
            } else {
                tabsContainer.classList.remove('scrolled');
            }
        });
    }
});