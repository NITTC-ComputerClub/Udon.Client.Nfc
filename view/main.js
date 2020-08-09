const socket = new WebSocket();
socket.addEventListener('open', function (event) {
    console.log("System Ready");
});
socket.addEventListener('open', function (event) {
    switch (event.data) {
        case "":
        case "":
        default:
            console.log("Something Wrong...");
    }
});