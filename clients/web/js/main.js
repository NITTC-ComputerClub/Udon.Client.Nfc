function changeDisplayWithId(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}



window.onload=()=>{
	const socket= new WebSocket("ws://localhost:9999");

	socket.onmessage = (message)=>{
		changeDisplayWithId(message.data);
		if(message !== "sending"){
			setTimeout(()=>{
				changeDisplayWithId("listening");
				socket.send("client_ready");
				},1000);
		}
	};
	
	socket.onopen = ()=>{
		changeDisplayWithId("listening");
		socket.send("client_ready");
	}
}
