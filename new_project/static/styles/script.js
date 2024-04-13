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

//password
function changeVis (event) {
    event.preventDefault();
    let icon1 = document.getElementById("icon1");
    let password1 = document.getElementById("password1");

    if (password1.type == "password") {
        password1.type = "text";
        icon1.classList.remove("fa-eye-slash");
        icon1.classList.add("fa-eye");
    } else {
        password1.type = "password";
        icon1.classList.remove("fa-eye");
        icon1.classList.add("fa-eye-slash");
    }
}
