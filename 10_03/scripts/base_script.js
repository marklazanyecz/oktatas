let i = 0;

document.getElementById('alertGomb').addEventListener('click', function() {
    alert("HELLÓ");
    i++;
    console.log(i);
});

document.getElementById("valtoztatoGomb").addEventListener("click", function() {
    const focim = document.getElementById("focim");
    focim.textContent = "Megváltozott a főcim";
    focim.style.color = "red";
});