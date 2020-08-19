window.onload = function () {
    const socket = new WebSocket("ws://localhost:9999/");
    socket.onerror = function () {
        $("#ws_error").css("display", "block");
    }
    socket.onopen = function (event) {
        console.log("connected");
        $("#listening").css("display", "block");
        socket.send("client_ready");
    };
    socket.onmessage = function (event) {
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
                drawingOut();
                break;
            case "connection_error":
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
            case "touch_again":
                $("#touch_again").css("display", "block");
                socket.send("client_ready");
                break;
            case "registing":
                $("#sending").css("display", "block");
                break;
            case "regist_succeed":
                $("#regist_succeed").css("display", "block");
                drawingOut();
                break;
            case "regist_error":
                $("#regist_error").css("display", "block");
                drawingOut();
                break;
            default:
                console.log("Something Wrong...");
                console.log(event.data);
                drawingOut();
        }
    };
    function drawingOut() {
        socket.send("client_ready");
    }
}