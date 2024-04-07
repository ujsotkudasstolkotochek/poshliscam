//about
document.addEventListener('DOMContentLoaded', function() {
    const footer = document.getElementById('footer');

    footer.addEventListener('click', function() {
        alert('we are robots');
    });
});

//popup

document.getElementById("popup-open").addEventListener('click', function() {
    document.getElementById("popup").classList.add("open");
})

document.getElementById("popup-close").addEventListener('click', function() {
    document.getElementById("popup").classList.remove("open");
})

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("popup").classList.remove("open");
    }
});

document.querySelector("#popup .popup-body").addEventListener('click', event => {
    event._isClickWithInModal = true;
});
document.getElementById("popup").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove("open");
});
