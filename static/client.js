const socket = new WebSocket("ws://localhost:9999/");
socket.addEventListener('open', function (event) {
    console.log("System Ready");
    $("#listening").css("display", "block");
});
socket.addEventListener('message', function (event) {
    console.log(event.data);
    $(".components").css("display", "none");
    switch (event.data) {
        case "0":
            $("#listening").css("display", "block");
            break;
        case "1":
            $("#sending").css("display", "block");
            break;
        case "2":
            $("#succeeded").css("display", "block");
            break;
        case "3":
            $("#connection_error").css("display", "block");
            break;
        case "4":
            $("#tag_error").css("display", "block");
            break;
        case "5":
            $("#other_error").css("display", "block");
            break;
        default:
            console.log("Something Wrong...");
            console.log(event.data);
    }
    setTimeout(() => {
        socket.send(event.data);
    }, 3000);
});