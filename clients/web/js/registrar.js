function changeDisplayWithId(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}

async function register(){

	let memberName = $("#memberList").val();
	changeDisplayWithId("listening");
	let firstTouch = await eel.read_idm_wrapper()();
	changeDisplayWithId("touch_again");
	let secondTouch = await eel.read_idm_wrapper()();

	if(firstTouch == secondTouch){
		changeDisplayWithId("sending");
		let status = await eel.registrar_wrapper(memberName,idm);
		changeDisplayWithId(status);
	}else{
		changeDisplayWithId("not_available_card"); 
	}

	setTimeout(1000);
	changeDisplayWithId("select_user");
}

async function fetchAndSetMemberList(){
	//TODO set GitHub Token const GitHubToken = ;
	const responce = fetch("https://api.github.com/repos/nittc-computerclub/members-db-dist/contents/members.json",{
		headers:{
			'Accept': 'application/vnd.github.raw+json',
			'Authorization':`${GitHubToken}`
		}
	}).then((responce)=>{
		if(!responce.ok){
			throw new Error(`responce wasn't ok:${responce.status}`);
		}
		return responce.json();
	}).then((element)=>{
		element.name.forEach((name)=>{
			$("#memberList").append(`<option class=\"list-group-item\" value =${name}>${name}</option>`);
		});
	}).catch((error)=>{
		console.error(error);
		changeDisplayWithId("connection_error");
	})
}

window.onload = ()=>{
	$(".register_start").click(register);
	changeDisplayWithId("select_user");
	fetchAndSetMemberList();
}
