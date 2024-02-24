document.getElementById("pastebinForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const text = document.getElementById("text").value;
    console.log("Text to be saved: ", text);

    window.location.href("succes-page.html")
});