$(document).ready(function() {
    $("#btnAddUser").click(function(e) {
        e.preventDefault(); 
        $("#addUserModal").modal('show');
    });
    $(".close").click(function(){
        $("#addUserModal").modal('hide');
    })
    $("#addUserForm").submit(function(e) {
        e.preventDefault();
        const nombre = $("#nombre").val();
        const apellido = $("#apellido").val();
        const email = $("#email").val();
        const apodo = $("#apodo").val();
        $("#addUserModal").modal('hide');
    });

    function menuAction(option) {
        const actionDisplay = document.getElementById('action-display');
        actionDisplay.textContent = `Has seleccionado: ${option}`;
        
        // Lógica personalizada para cada opción seleccionada
        switch(option) {
            case 'Opción 1':
                console.log('Ejecutando acción para Opción 1');
                break;
            case 'Opción 2':
                console.log('Ejecutando acción para Opción 2');
                break;
            case 'Opción 3':
                console.log('Ejecutando acción para Opción 3');
                break;
            case 'Opción 4':
                console.log('Ejecutando acción para Opción 4');
                break;
            default:
                console.log('Acción no reconocida');
        }
    }
    
    
    
    

});
