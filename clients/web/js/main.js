function changeDisplayWithId(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}

const socket= new WebSocket("ws://localhost:3000");

socket.addEventListener("message",(message)=>{
	changeDisplayWithId(message);
	if(message !== "sending"){
		setTimeout(startAttendance,1000);
	}
})

function startAttendance(){
	socket.send("client_ready");
	changeDisplayWithId("listening");
}

window.onload=startAttendance();
