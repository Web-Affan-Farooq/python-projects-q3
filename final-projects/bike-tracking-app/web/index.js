document.addEventListener("DOMContentLoaded", () => {
    const iframe = document.querySelector("iframe");

    // Check if Geolocation is supported
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                let lat = position.coords.latitude;
                let lon = position.coords.longitude;

                // Generate Google Maps Embed URL with user coordinates
                let newSrc = `https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d5000!2d${lon}!3d${lat}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2s!4v${Date.now()}!5m2!1sen!2s`;

                // Update the iframe source
                iframe.src = newSrc;
            },
            (error) => {
                console.error("Error getting location:", error.message);
            }
        );
    } else {
        console.error("Geolocation is not supported by this browser.");
    }
});
