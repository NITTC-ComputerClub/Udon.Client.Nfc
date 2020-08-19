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
            window.memberList = memberList
            memberList.forEach(element => {
                $("#memberList").append("<option value = " + element + ">" + element + "</option>");
            });
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
        }
    };
    $("#memberSelectButton").click(() => {
        const name = $("#memberList").val();
        socket.send("member"+name.toString());
	console.log("member"+name.toString());
    });
    $("#registStart").click(() => {
        socket.send("client_ready");
	
    })
    function drawingOut() {
        window.memberList.forEach(element => {
            $("#memberList").append("<option value = " + element + ">" + element + "</option>");
        });
    }
}