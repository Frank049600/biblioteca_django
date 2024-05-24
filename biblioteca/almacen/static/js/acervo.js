$(function () {
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


    function remove_register(id) {
        Swal.fire({
            "title": "¿Estas seguro?",
            "text": "El registro no se podrá recuperar",
            "icon": "warning",
            "showCancelButton": true,
            "cancelButtonText": "Cancelar",
            "confirmButtonText": "Aceptar",
            "reverseButtons": true,
            "confirmButtonColor": "#dc3545"
        })
            .then(function (result) {
                if (result.isConfirmed) {
                    console.log('Se borrara')
                }
            })
    }


    new DataTable('#acervoTable', {
        columnDefs: [
            { orderable: false, target: [9] }
        ],
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

    $('#acervo_add').on('click', 'a#close', function () {
        $('#acervo_add').modal('hide')
    })
})

