function changeDisplayWithId(elementId){
    $(".components").css("display","none");
    $(`#${elementId}`).css("display","block");
}
async function fetchAndSetMemberList(){
	const responce = fetch("https://api.github.com/repos/nittc-computerclub/members-db-dist/contents/members.json",{
		headers:{
			'Accept':'application/vnd.github.raw+json',
			'Authorization':'token '
		}
	}).then(async(responce)=>{
		
		if(!responce.ok){
			throw new Error(`responce wasn't ok:${responce.status}`);
		}
		let membersdb = await responce.json();
		let base64decoder = new TextDecoder();
		console.log(membersdb);
		console.log(await decodeURIComponent(atob(membersdb.content)));
		return JSON.parse(atob(membersdb.content));
	}).then((membersdb)=>{
		console.log();
		membersdb.map(member=>member.name).forEach((name)=>{
			$("#member_list").append(`<option class=\"list-group-item\" value =${name}>${name}</option>`);
		});
	}).catch((error)=>{
		console.error(error);
		changeDisplayWithId("connection_error");
	})
}

const socket = new WebSocket("ws://localhost:9999");

socket.onopen = ()=>{

	async function register(){
		socket.send("client_ready");
		let memberName = $("#memberList").val();
		changeDisplayWithId("listening");
		socket.send(memberName);
	}
	
	$("#register_start").click=register;
	
	socket.addEventListener("message",(message)=>{
		changeDisplayWithId(message);
		if(message !== "sending"){
			setTimeout(()=>{
				changeDisplayWithId("listening");
				socket.send("client_ready");
			},1000);
		}
	});
	fetchAndSetMemberList();
	changeDisplayWithId("select_user");
}

