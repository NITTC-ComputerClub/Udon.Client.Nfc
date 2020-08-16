window.onload = async () => {
    const socket = await new WebSocket("ws://localhost:9999/");
    socket.addEventListener('open', function (event) {
        console.log("connected");
        $("#listening").css("display", "block");
        socket.send("client_ready");
        console.log("client_ready");
    });
    socket.addEventListener('message', function (event) {
        console.log(event.data);
        $(".components").css("display", "none");
        switch (event.data) {
            case "listening":
                $("#listening").css("display", "block");
                break;
            case "sending":
                $("#sending").css("display", "block");
                break;
            case "record_succeed":
                $("#succeeded").css("display", "block");
                drawingOut();
                break;
            case "3":
                $("#connection_error").css("display", "block");
                drawingOut();
                break;
            case "incorrect_tag":
                $("#tag_error").css("display", "block");
                drawingOut();
                break;
            case "other_error":
                $("#other_error").css("display", "block");
                drawingOut();
                break;
            default:
                console.log("Something Wrong...");
                console.log(event.data);
                drawingOut();
        }
    });
    function drawingOut() {
        setTimeout(socket.send("client_ready"), 1500);
    }
}