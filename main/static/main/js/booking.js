// Get elements
const modal = document.getElementById("bookingModal");
const openButtons = document.querySelectorAll(".openBookingModal");
const closeBtn = document.getElementById("closeBookingModal");

// Open modal
openButtons.forEach(button => {
    button.addEventListener("click", () => {
        modal.classList.remove("hidden");
        modal.classList.add("flex");
    });
});

// Close modal
closeBtn.addEventListener("click", () => {
    modal.classList.add("hidden");
    modal.classList.remove("flex");
});

// Close when clicking outside
window.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.classList.add("hidden");
        modal.classList.remove("flex");
    }
});