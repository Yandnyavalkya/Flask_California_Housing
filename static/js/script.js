const form = document.getElementById("predictionForm");
const predictBtn = document.getElementById("predictBtn");
const clearBtn = document.getElementById("clearBtn");


/* =========================================
   Prediction Button Loading State
========================================= */

form.addEventListener("submit", function () {

    predictBtn.classList.add("loading");

    predictBtn.disabled = true;

});


/* =========================================
   Clear Form
========================================= */

clearBtn.addEventListener("click", function () {

    const inputs = form.querySelectorAll("input");

    inputs.forEach(function (input) {
        input.value = "";
    });

    inputs[0].focus();

});


/* =========================================
   Prevent Negative Values
========================================= */

const numberInputs =
    form.querySelectorAll('input[type="number"]');

numberInputs.forEach(function (input) {

    input.addEventListener("input", function () {

        if (this.value < 0) {
            this.value = 0;
        }

    });

});
