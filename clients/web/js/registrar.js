function changeDisplay(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}

async function start(){
	//await loading memberdata
	let status = await eel.start_udon()();
	changeDisplay(status);
	setTimeout(start,1000);
}

window.onload=start();