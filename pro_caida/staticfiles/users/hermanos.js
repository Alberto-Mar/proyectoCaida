function cargarCoches() {
  fetch("http://localhost:85/api/coche_list/?ordering=marca")
    .then(response => response.json())
    .then(data => {
      const lista = document.getElementById("lista");
      lista.innerHTML = "";

      data.results.forEach(coche => {
        const li = document.createElement("li");
        li.textContent = `${coche.marca} ${coche.modelo} - ${coche.precio}â‚¬`;
        lista.appendChild(li);
      });
    })
    .catch(error => console.error("Error:", error));
}