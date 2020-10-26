function changeDisplay(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}

async function register(){

	let memberName = $(".member_list").value;
	changeDisplay("listening");
	let firstTouch = await eel.read_idm_wrapper()();
	changeDisplay("touch_again");
	let secondTouch = await eel.read_idm_wrapper()();

	if(firstTouch == secondTouch){
		changeDisplay("sending");
		let status = await eel.registrar_wrapper(memberName,idm);
		changeDisplay(status);
	}else{
		changeDisplay("not_available_card"); 
	}
	
	setTimeout(1000);
	changeDisplay("select_user");
}

window.onload=()=>{
	$(".register_start").click(register);
	changeDisplay("select_user");
}
