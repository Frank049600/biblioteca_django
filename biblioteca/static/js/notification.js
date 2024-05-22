const sweetalert_confirm = (title, text, icon, id) => {
    Swal.fire({
        title: title,
        text: text,
        icon: icon,
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Aceptar",
        showLoaderOnConfirm: true
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "{% url 'delete_acervo' " + id + " %}"
            Swal.fire({
                title: "Borrado correctamente",
                icon: "success"
            });
        }
    });
}