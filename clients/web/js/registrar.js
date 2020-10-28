function changeDisplayWithId(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}

const socket = new WebSocket("ws://localhost:3000");
async function register(){

	let memberName = $("#memberList").val();
	changeDisplayWithId("listening");
	socket.send(memberName);
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


socket.addEventListener("message",(message)=>{
	changeDisplayWithId(message);
	if(message !== "sending"){
		setTimeout(startRegister,1000);
	}
})

function startRegister(){
	socket.send("client_ready");
	changeDisplayWithId("listening");
}

window.onload=startRegister();
