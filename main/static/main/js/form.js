console.log("Form script loaded");
document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("bookingForm");
    const messageBox = document.getElementById("bookingMessage");

    if (!form) return;

    form.addEventListener("submit", function (e) {

        e.preventDefault();

        fetch(form.action, {

            method: "POST",

            body: new FormData(form),

            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }

        })

        .then(response => response.json())

        .then(data => {

            if (data.success) {

                messageBox.innerHTML = `
                    <div class="mb-6 rounded-xl bg-green-600/20 border border-green-500 p-4 text-green-300">
                        ${data.message}
                    </div>
                `;

                form.reset();

            } else {

                messageBox.innerHTML = `
                    <div class="mb-6 rounded-xl bg-red-600/20 border border-red-500 p-4 text-red-300">
                        ${data.message}
                    </div>
                `;
            }

        })

        .catch(error => {

            console.log(error);

            messageBox.innerHTML = `
                <div class="mb-6 rounded-xl bg-red-600/20 border border-red-500 p-4 text-red-300">
                    Something went wrong.
                </div>
            `;

        });

    });

});