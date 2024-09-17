const desde = document.getElementById('vr-fecha-desde');
const hasta = document.getElementById('vr-fecha-hasta');




window.addEventListener("load", async () => {
    agregarItems();
    fechaActual();
});





const choiceComercio = new Choices('#selector_comercio', {
    allowHTML: true,
    shouldSort: false,
    searchPlaceholderValue: 'Escriba para buscar..',
    itemSelectText: ''
});

const choiceCliente = new Choices('#selector_cliente', {
    allowHTML: true,
    shouldSort: false,
    searchPlaceholderValue: 'Escriba para buscar..',
    itemSelectText: ''
});

const choiceEspecie = new Choices('#selector_especie', {
    allowHTML: true,
    shouldSort: false,
    searchPlaceholderValue: 'Escriba para buscar..',
    itemSelectText: ''
});

const choiceEnvase = new Choices('#selector_envase', {
    allowHTML: true,
    shouldSort: false,
    searchPlaceholderValue: 'Escriba para buscar..',
    itemSelectText: ''
});

const choiceBarco = new Choices('#selector_barco', {
    allowHTML: true,
    shouldSort: false,
    searchPlaceholderValue: 'Escriba para buscar..',
    itemSelectText: ''
});

const choiceVariedad = new Choices('#selector_variedad', {
    allowHTML: true,
    shouldSort: false,
    searchPlaceholderValue: 'Escriba para buscar..',
    itemSelectText: ''
});

const choiceMarca = new Choices('#selector_marca', {
    allowHTML: true,
    shouldSort: false,
    searchPlaceholderValue: 'Escriba para buscar..',
    itemSelectText: ''
});



function agregarItems() {
    let nuevosItems = [
        { idEspecie: 'P', Especie: 'PERA' },
        { idEspecie: 'M', Especie: 'MANZANA' },
        { idEspecie: 'S', Especie: 'SANDÍA' },
    ];
    let items = []
    nuevosItems.forEach(item => {
        items.push({
            value: item.idEspecie,
            label: item.Especie,
            // customProperties: JSON.stringify({ centro: item.centro })
        });
    });
    choiceEspecie.clearChoices();
    choiceEspecie.setChoices(items, 'value', 'label', true);
}





































function fechaActual() {
    var fecha = new Date();
    var mes = fecha.getMonth() + 1;
    var dia = fecha.getDate();
    var ano = fecha.getFullYear();
    if (dia < 10) dia = '0' + dia;
    if (mes < 10) mes = '0' + mes;
    const formattedDate = `${ano}-${mes}-${dia}`;
    const formattedDateDesde = `${ano}-${mes}-${'01'}`;
    desde.value = formattedDateDesde;
    hasta.value = formattedDate;
}




// const divMovible = document.querySelector('.div-movible');
// let posicionX = 0;
// let posicionY = 0;
// let mouseDown = false;

// divMovible.addEventListener('mousedown', (e) => {
//     mouseDown = true;
//     posicionX = e.clientX;
//     posicionY = e.clientY;
// });

// document.addEventListener('mousemove', (e) => {
//     if (mouseDown) {
//         const dx = e.clientX - posicionX;
//         const dy = e.clientY - posicionY;
//         divMovible.style.top = `${divMovible.offsetTop + dy}px`;
//         divMovible.style.left = `${divMovible.offsetLeft + dx}px`;
//         posicionX = e.clientX;
//         posicionY = e.clientY;
//     }
// });

// document.addEventListener('mouseup', () => {
//     mouseDown = false;
// });

/* <div class="div-movible"
        style="background-color: black; width: 350px; height: 350px; position: absolute; top: 0; left: 0; cursor: move;">
</div> */