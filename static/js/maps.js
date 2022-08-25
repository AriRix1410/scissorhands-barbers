// Google maps API

// Initialize and add the map
function initMap() {
    // The location of York
    const york = {
        lat: 53.9591772,
        lng: -1.0810208
    };
    // The map, centered at York
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: york,
    });
    // The marker, positioned at York
    const marker = new google.maps.Marker({
        position: york,
        map: map,
    });
}

window.initMap = initMap;