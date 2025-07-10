function toggleVideo() {
    const video = document.getElementById("video-feed");
    if (video.style.display === "none") {
        video.style.display = "block";
    } else {
        video.style.display = "none";
    }
}

function updateDateTime() {
    const now = new Date();
    const dateString = now.toLocaleDateString();
    const timeString = now.toLocaleTimeString();
    document.getElementById("datetime").textContent = `${dateString} ${timeString}`;
}

setInterval(updateDateTime, 1000); // Update every second
updateDateTime(); // Initial call
