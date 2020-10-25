eel.expose(changeDisplay);

function changeDisplay(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}

async function start(){
	changeDisplay("listening");
	let res = await eel.callme()();
	changeDisplay("record_succeed")
	setTimeout(start,1000);
}

window.onload=start();