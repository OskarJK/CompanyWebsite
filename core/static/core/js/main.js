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
});