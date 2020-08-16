window.onload = async () => {
    const socket = await new WebSocket("ws://localhost:9999/");
    socket.addEventListener('open', function (event) {
        console.log("connected");
        $("#listening").css("display", "block");
        socket.send("client_ready");
    });
    socket.addEventListener('message', function (event) {
        console.log(event.data)
        $(".components").css("display", "none");
        switch (event.data) {
            case "listening":
                $("#listening").css("display", "block");
                break;
            case "sending":
                $("#sending").css("display", "block");
                break;
            case "record_succeed":
                $("#record_succeed").css("display", "block");
            case "3":
                $("#connection_error").css("display", "block");
            case "incorrect_tag":
                $("#tag_error").css("display", "block");
            case "other_error":
                $("#other_error").css("display", "block");
            case "touch_again":
                socket.send("client_ready");
                break;
            case "registing":
                $("#sending").css("display", "block");
                break;
            case "regist_succeed":
                $("#regist_succeed").css("display", "block");
            case "regist_error":
                $("#sending").css("display", "block");
            default:
                console.log("Something Wrong...");
                console.log(event.data);
                drawingOut();
        }
    });
    function drawingOut() {
        socket.send("client_ready");
    }
}