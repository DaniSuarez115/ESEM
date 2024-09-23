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
});
