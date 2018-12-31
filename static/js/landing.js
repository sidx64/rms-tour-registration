$(document).ready(function () {

    // System State
    let state = {

        "student": false,
        "clicked": false,

    };

    $("#student").on('click', function () {

        state.student = true;
        state.clicked = true;

        $("#student")
            .removeClass("btn-secondary")
            .removeClass("btn-primary")
            .addClass("btn-primary");

        $("#professional")
            .removeClass("btn-primary")
            .removeClass("btn-secondary")
            .addClass("btn-secondary");

        $("#organization").text("Name of your college");
        $("#designation").text("College department");

        console.log(state);

    });

    $("#professional").on('click', function () {

        state.student = false;
        state.clicked = true;

        $("#professional")
            .removeClass("btn-secondary")
            .removeClass("btn-primary")
            .addClass("btn-primary");

        $("#student")
            .removeClass("btn-primary")
            .removeClass("btn-secondary")
            .addClass("btn-secondary");

        $("#organization").text("Name of your organization");
        $("#designation").text("Your designation");

        console.log(state);

    });
});

window.addEventListener('load', function () {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function (form) {
        form.addEventListener('submit', function (event) {
            if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
}, false);