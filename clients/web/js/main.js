eel.expose(changeDisplay);

function changeDisplay(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}

async function start(){
	changeDisplay("listening");
	let status = await eel.start_udon()();
	changeDisplay(status);
	setTimeout(start,1000);
}

window.onload=start();