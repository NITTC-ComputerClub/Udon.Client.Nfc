function changeDisplayWithId(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}

const socket= new WebSocket("ws://localhost:3000");

socket.addEventListener("message",(message)=>{
	changeDisplayWithId(message);
	setTimeout(openConnection,1000);
})

function openConnection(){
	socket.send("client_ready");
	changeDisplayWithId("listening");
}

window.onload=openConnection();
