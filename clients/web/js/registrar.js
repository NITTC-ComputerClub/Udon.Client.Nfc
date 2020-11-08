async function changeDisplayWithId(elementId){
    
	console.log(elementId.data);
	$(".components").css("display","none");
	$(`#${elementId.data || elementId}`).css("display","block");
}

async function fetchAndSetMemberList(){
	const responce = fetch("https://api.github.com/repos/nittc-computerclub/members-db-dist/contents/members.json",{
		headers:{
			'Accept':'application/vnd.github.raw+json',
			'Authorization':'token '//Set token
		}
	}).then(async(responce)=>{
		
		if(!responce.ok){
			throw new Error(`responce wasn't ok:${responce.status}`);
		}
		let membersdb = await responce.json();
		let base64decoder = new TextDecoder();
		console.log(membersdb);
		console.log(await decodeURIComponent(atob(membersdb.content)));

		return JSON.parse(atob(membersdb.content));//日本語が正しくデコードされない問題

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

	fetchAndSetMemberList();
	changeDisplayWithId("select_user");

	
	$("#register_start").click(async ()=>{
		let memberName = $("#member_list").val();
		changeDisplayWithId("listening");
		socket.send(memberName);
		console.log("start!");
	});
	
	socket.addEventListener("message",(message)=>{
		changeDisplayWithId(message.data);

		const onTheWayStatuses = ["sending","listening","touch_again"];

		if(!onTheWayStatuses.includes(message.data)){
			setTimeout(()=>{
				changeDisplayWithId("select_user");
			},2000);
		}
	});
}

