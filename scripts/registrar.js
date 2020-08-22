window.onload = function () {
    const socket = new WebSocket("ws://localhost:9999/");
    socket.onerror = function () {
        $("#ws_error").css("display", "block");
    }
    socket.onopen = function (event) {
        console.log("connected");
    };
    socket.onmessage = function (event) {
        console.log(event.data)
        $(".components").css("display", "none");
        if (event.data.substr(0, 11) === "member-list") {
            memberList = event.data.substr(11).split(",");
            memberList.sort();
            window.memberList = memberList;
            memberList.forEach(element => {
                $("#memberList").append("<option value = " + element + ">" + element + "</option>");
            });
            $("#select_user").css("display", "block");
        }
        else {
            switch (event.data) {
                case "listening":
                    $("#listening").css("display", "block");
                    break;
                case "sending":
                    $("#sending").css("display", "block");
                    break;
                case "connection_error":
                    $("#connection_error").css("display", "block");
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
                case "registering":
                    $("#sending").css("display", "block");
                    break;
                case "register_succeed":
                    $("#register_succeed").css("display", "block");
                    drawingOut();
                    break;
                case "register_error":
                    $("#register_error").css("display", "block");
                    drawingOut();
                    break;
                default:
                    console.log("Something Wrong...");
                    console.log(event.data);
                    drawingOut();
            }
        }
    };
    $("#registerStart").click(() => {
        const name = $("#memberList").val();
        socket.send("member:" + name);
        console.log("member:" + name);
    })
    function drawingOut() {
        setTimeout(() => {
            $(".components").css("display", "none");
            $("#select_user").css("display", "block");
        }, 1500);
    }
}