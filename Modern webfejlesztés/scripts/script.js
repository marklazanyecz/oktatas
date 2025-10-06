document.getElementById('alertGomb').addEventListener('click', function() {
  alert('Helló! Ez egy alert üzenet a JavaScriptből!');
});

document.getElementById('valtoztatoGomb').addEventListener('click', function() {
  const focim = document.getElementById('focim');
  focim.textContent = 'A címsor megváltozott!';
  focim.style.color = 'orange';
});
