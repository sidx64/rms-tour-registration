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

        console.log(state);

    });

});