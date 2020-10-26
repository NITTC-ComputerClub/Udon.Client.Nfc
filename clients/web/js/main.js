function changeDisplayWithId(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}

async function start(){
	changeDisplayWithId("listening");
	let status = await eel.start_udon()();
	changeDisplayWithId(status);
	setTimeout(start,1000);
}

window.onload=start();