const register_deleteSwal = (title, coloca, text, icon, rute) => {
    Swal.fire({
        "title": '¿Eliminar ' + title + '-' + coloca + '?',
        "text": text,
        "icon": icon,
        "showCancelButton": true,
        "cancelButtonText": "Cancelar",
        "confirmButtonText": "Aceptar",
        "reverseButtons": true,
        "confirmButtonColor": "#dc3545",
    })
        .then(function (result) {
            if (result.isConfirmed) {
                // Envía la colocación del registro a eliminar
                location.href = rute + coloca
            }
        })
}