'use strict';

let listaHermanos = [];
let root;
let header;
let csrfToken;

let limpiarElemento = (elemento) => { 
    while (elemento.firstChild) elemento.removeChild(elemento.firstChild);
};

let crearInputOculto = (nombre, valor) => {
    let input = document.createElement('input');
    input.type = 'hidden';
    input.name = nombre;
    input.value = valor;
    return input;
};

let validarFormulario = (formulario) => {
    let esValido = true;
    let erroresPrevios = formulario.querySelectorAll('.error-feedback');
    let inputsConError = formulario.querySelectorAll('.input-error');
    
    erroresPrevios.forEach(elemento => elemento.remove());
    inputsConError.forEach(elemento => elemento.classList.remove('input-error'));

    let mostrarError = (input, mensaje) => {
        esValido = false;
        input.classList.add('input-error');
        let span = document.createElement('span');
        span.className = 'error-feedback';
        span.textContent = mensaje;
        input.parentNode.appendChild(span);
    };

    let email = formulario.querySelector('[name="email"]');
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
        mostrarError(email, "Email no válido.");
    }

    let dni = formulario.querySelector('[name="dni"]');
    let dniRegex = /^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$/i;
    if (!dniRegex.test(dni.value.trim())) {
        mostrarError(dni, "DNI no válido (8 números y letra).");
    }

    let nombre = formulario.querySelector('[name="nombre"]');
    if (!nombre.value.trim()) {
        mostrarError(nombre, "El nombre es obligatorio.");
    }

    return esValido;
};

let crearTarjeta = (hermano) => {
    let art = document.createElement('article');
    art.className = 'tarjeta';

    let cont = document.createElement('div');
    cont.className = 'contenido-tarjeta-evento';

    let h3 = document.createElement('h3');
    h3.className = 'nombre-hermano';
    h3.textContent = hermano.nombre;

    let badge = document.createElement('span');
    badge.className = 'etiqueta etiqueta-activo badge-tipo';
    badge.textContent = hermano.tipo;
    h3.appendChild(badge);

    let det = document.createElement('div');
    det.className = 'detalles-evento';

    let pDni = document.createElement('p');
    pDni.textContent = "DNI: " + hermano.dni;
    
    let pNum = document.createElement('p');
    pNum.textContent = "Nº Hermano: " + hermano.numero;

    det.appendChild(pDni);
    det.appendChild(pNum);

    let btns = document.createElement('div');
    btns.className = 'button-group margen-superior-1';

    let btnE = document.createElement('button');
    btnE.className = 'btn btn-secondary btn-small';
    btnE.textContent = 'Editar';
    btnE.onclick = () => mostrarFormulario(hermano);

    let btnB = document.createElement('button');
    btnB.className = 'btn btn-primary btn-small btn-borrar';
    btnB.textContent = 'Borrar';
    btnB.onclick = () => {
        if (confirm("¿Eliminar a " + hermano.nombre + "?")) {
            document.getElementById('input-borrado-email').value = hermano.email;
            document.getElementById('form-borrado-global').submit();
        }
    };

    btns.appendChild(btnE);
    btns.appendChild(btnB);
    cont.appendChild(h3);
    cont.appendChild(det);
    cont.appendChild(btns);
    art.appendChild(cont);
    return art;
};

let mostrarListado = () => {
    limpiarElemento(root);
    limpiarElemento(header);
    header.className = 'page-header d-flex justify-content-between align-items-center';
    
    let h1 = document.createElement('h1');
    h1.textContent = 'Gestión de Hermanos';
    let btnN = document.createElement('button');
    btnN.className = 'btn btn-primary';
    btnN.textContent = 'Nuevo Hermano';
    btnN.onclick = () => mostrarFormulario(null);

    header.appendChild(h1);
    header.appendChild(btnN);

    let grid = document.createElement('div');
    grid.className = 'grid-tarjetas';

    if (listaHermanos.length === 0) {
        let p = document.createElement('p');
        p.textContent = 'No hay hermanos registrados.';
        root.appendChild(p);
    } else {
        listaHermanos.forEach(hermano => grid.appendChild(crearTarjeta(hermano)));
        root.appendChild(grid);
    }
};

let mostrarFormulario = (hermano) => {
    limpiarElemento(root);
    limpiarElemento(header);
    let edit = (hermano !== null);

    let proximoNumero;
    if (edit) {
        proximoNumero = hermano.numero;
    } else {
        if (listaHermanos.length > 0) {
            let numerosActuales = listaHermanos.map(hermano => parseInt(hermano.numero));
            let maximoActual = Math.max(...numerosActuales);
            proximoNumero = maximoActual + 1;
        } else {
            proximoNumero = 1;
        }
    }

    let titulo = document.createElement('h1');
    titulo.textContent = edit ? 'Editar Hermano' : 'Nuevo Registro';
    header.appendChild(titulo);

    let container = document.createElement('div');
    container.className = 'form-container';

    let form = document.createElement('form');
    form.method = 'POST';
    form.noValidate = true;

    form.appendChild(crearInputOculto('csrfmiddlewaretoken', csrfToken));
    form.appendChild(crearInputOculto('accion', 'guardar'));

    let campos = [
        { label: 'Email (ID)', name: 'email', type: 'email', val: edit ? hermano.email : '', read: edit },
        { label: 'Nombre', name: 'nombre', type: 'text', val: edit ? hermano.nombre : '', read: false },
        { label: 'DNI', name: 'dni', type: 'text', val: edit ? hermano.dni : '', read: false },
        { label: 'Número de Hermano (Asignado)', name: 'numero_hermano', type: 'number', val: proximoNumero, read: true }
    ];

    campos.forEach(c => {
        let group = document.createElement('div');
        group.className = 'form-group';
        let label = document.createElement('label');
        label.textContent = c.label;
        let input = document.createElement('input');
        input.name = c.name;
        input.type = c.type;
        input.value = c.val;
        if (c.read) {
            input.readOnly = true;
            input.classList.add('input-readonly');
        }
        group.appendChild(label);
        group.appendChild(input);
        form.appendChild(group);
    });

    let groupSel = document.createElement('div');
    groupSel.className = 'form-group';
    let labelSel = document.createElement('label');
    labelSel.textContent = 'Tipo de Hermano';
    let select = document.createElement('select');
    select.name = 'tipo_hermano';
    let tipos = ['Protector', 'Costalero', 'Nazareno', 'Tambor'];
    tipos.forEach(tipo => {
        let opt = document.createElement('option');
        opt.value = tipo;
        opt.textContent = tipo;
        if (edit && hermano.tipo === tipo) opt.selected = true;
        select.appendChild(opt);
    });
    groupSel.appendChild(labelSel);
    groupSel.appendChild(select);
    form.appendChild(groupSel);

    let bGroup = document.createElement('div');
    bGroup.className = 'button-group';
    let bSave = document.createElement('button');
    bSave.type = 'submit';
    bSave.className = 'btn btn-primary';
    bSave.textContent = 'Guardar';
    let bBack = document.createElement('button');
    bBack.type = 'button';
    bBack.className = 'btn btn-secondary';
    bBack.textContent = 'Cancelar';
    bBack.onclick = () => mostrarListado();

    bGroup.appendChild(bSave);
    bGroup.appendChild(bBack);
    form.appendChild(bGroup);

    form.onsubmit = (e) => {
        e.preventDefault();
        if (validarFormulario(form)) form.submit();
    };

    container.appendChild(form);
    root.appendChild(container);
};

document.addEventListener('DOMContentLoaded', () => {
    root = document.getElementById('app-root');
    header = document.getElementById('header-dinamico');
    let t = document.getElementById('token-seguridad');
    csrfToken = t ? t.dataset.csrf : '';

    let nodos = document.querySelectorAll('.nodo-hermano');
    listaHermanos = Array.from(nodos).map(n => {
        return {
            email: n.dataset.email,
            nombre: n.dataset.nombre,
            numero: n.dataset.numero,
            dni: n.dataset.dni,
            tipo: n.dataset.tipo
        };
    });

    mostrarListado();
});