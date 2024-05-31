$(document).ready(function () {
    // Overlay
    //$.LoadingOverlay("show", {
    //    image: "",
    //    fontawesome: "fa fa-cog fa-spin"
    //});
    //$.LoadingOverlaySetup({
    //    background: "rgba(0, 0, 0, 0.5)",
    //    image: "",
    //    imageAnimation: "1.5s fadein",
    //    imageColor: "#2A46B9"
    //});
    //$.LoadingOverlay("show");

    new DataTable('#acervoTable', {
        //columnDefs: [
        //    { orderable: false, target: [9] }
        //],
        layout: {
            bottomEnd: {
                paging: {
                    boundaryNumbers: false
                }
            }
        },
        language:
        {
            "aria": {
                "sortAscending": "Activar para ordenar la columna de manera ascendente",
                "sortDescending": "Activar para ordenar la columna de manera descendente"
            },
            "infoThousands": ",",
            "loadingRecords": "Cargando...",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "processing": "Procesando...",
            "search": "Buscar:",
            "searchPanes": {
                "clearMessage": "Borrar todo",
                "count": "{total}",
                "showMessage": "Mostrar Todo"
            },
            "thousands": ",",
            "datetime": {
                "previous": "Anterior",
                "hours": "Horas",
                "minutes": "Minutos",
                "seconds": "Segundos",
                "unknown": "-",
                "amPm": [
                    "am",
                    "pm"
                ],
                "next": "Siguiente",
                "months": {
                    "0": "Enero",
                    "1": "Febrero",
                    "10": "Noviembre",
                    "11": "Diciembre",
                    "2": "Marzo",
                    "3": "Abril",
                    "4": "Mayo",
                    "5": "Junio",
                    "6": "Julio",
                    "7": "Agosto",
                    "8": "Septiembre",
                    "9": "Octubre"
                },
                "weekdays": [
                    "Domingo",
                    "Lunes",
                    "Martes",
                    "Miércoles",
                    "Jueves",
                    "Viernes",
                    "Sábado"
                ]
            },
            "decimal": ".",
            "emptyTable": "No hay datos disponibles en la tabla",
            "zeroRecords": "No se encontraron coincidencias",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ entradas",
            "infoFiltered": "(Filtrado de _MAX_ total de entradas)",
            "lengthMenu": "Mostrar _MENU_ entradas",
            "stateRestore": {
                "creationModal": {
                    "search": "Buscar",
                    "button": "Crear"
                },
            },
            "infoEmpty": "No hay datos para mostrar"
        }
    })

    $('#acervoTable').on('click', 'tbody tr td a#more_info', function () {
        let data = $(this).closest('tr').data(),
            title = data['title'],
            autor = data['autor'],
            editorial = data['edit'],
            cantidad = data['cant'],
            colocacion = data['coloca'],
            edicion = data['edicion'],
            año = data['anio'],
            type_adqui = data['adqui'],
            state = data['state']

        if (state == 'EXC') {
            estado = 'Excelente'
        } else if (state == 'BUE') {
            estado = 'Bueno'
        } else if (state == 'REG') {
            estado = 'Regular'
        } else if (state == 'MAL') {
            estado = 'Malo'
        }

        $('#show_more').append('<div class="info-box mb-3" style="background-color: #3c6382; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-heading"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Título</span>'
            + '<span class="info-box-number">' + title + '</span>'
            + '</div>'
            + '</div>'
            + '<div class="row">'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #0a3d62; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-feather-alt"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Autor</span>'
            + '<span class="info-box-number">' + autor + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #002078; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-user-edit"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Editorial</span>'
            + '<span class="info-box-number">' + editorial + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="row">'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #0a3d62; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-boxes"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Cantidad</span>'
            + '<span class="info-box-number">' + cantidad + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #002078; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-wave-square"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Colocación</span>'
            + '<span class="info-box-number">' + colocacion + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="row">'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #0a3d62; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-newspaper"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Edición</span>'
            + '<span class="info-box-number">' + edicion + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #002078; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-calendar-alt"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Año de publicación</span>'
            + '<span class="info-box-number">' + año + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="row">'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #0a3d62; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-shopping-cart"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Tipo de adquisición</span>'
            + '<span class="info-box-number">' + type_adqui + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '<div class="col-xl-6">'
            + '<div class="info-box mb-3" style="background-color: #002078; color: white;">'
            + '<span class="info-box-icon"><i class="fas fa-eye"></i></span>'
            + '<div class="info-box-content">'
            + '<span class="info-box-text">Estado</span>'
            + '<span class="info-box-number">' + estado + '</span>'
            + '</div>'
            + '</div>'
            + '</div>'
            + '</div>');

        $('#more_info_modal').modal('show')
    })

    $('#acervoTable').on('click', 'tbody tr td a#remove_register', function (e) {
        let data = $(this).closest('tr').data(),
            coloca = data['coloca'],
            title = data['title'],
            text = "El registro no se podrá recuperar",
            icon = "warning",
            rute = '/delete_acervo/'
        // Llama el SweetAlert del script notification
        register_deleteSwal(title, coloca, text, icon, rute)
    })
})

