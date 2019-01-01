"use strict";

var BACKEND_URL = "http://localhost:9000/",
    state = {

        "student": false,
        "clicked": false,

    };


$(document).ready(function () {

    // Show basic divs & hide no-js div
    $("#noJSDiv").hide();

    setTimeout(function () {
        $("#mainDiv").show();
        $("#formDataDiv").show();
    }, 500);


    // $("#formSubmit").on('click', function () {
    //     formSubmit();
    // });

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

        $(".formComponents").show(1000);

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

            event.preventDefault();

            if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
            } else {
                console.log("Running");
                formSubmit();
            }
            form.classList.add('was-validated');


        }, false);
    });
}, false);


// Submit code
function formSubmit() {

    // Collect Data

    let fname = $("#fname").val(),
        lname = $("#lname").val(),
        mail = $("#mail").val(),
        contact = $("#contact").val(),
        org = $("#org").val(),
        title = $("#title").val();

    console.log("fname: " + fname);
    console.log("lname: " + lname);
    console.log("email: " + mail);
    console.log("contact: " + contact);
    console.log("student: " + state.student);
    console.log("org/college: " + org);
    console.log("title/dept: " + title);

    if (state.clicked === false) {
        toastr.error("Please Select Attendee Type : Student or Professional");
    } else {
        let data = {
            "fname": fname,
            "lname": lname,
            "email_id": mail,
            "mobile_number": contact,
            "designation": title,
            "organization": org,
            "is_student": state.student,
        };

        $.ajax({
            type: 'POST',
            url: BACKEND_URL + 'api/register/',
            data: data,
            dataType: "json",
            success: function (data) {

                toastr.success("Registration Form Successfully Submitted");

                // Hide pending div and show granted div
                $("#formDataDiv").hide();
                $("#pageHeader").hide();

                setTimeout(function () {
                    $("#postSubmitDiv").fadeIn(500);
                    $("#FormSubmissionCompleted").fadeIn(500);
                }, 500);

            },
            error: function (data) {
                toastr.error(data.responseText);

            }
        });
    }


}




















