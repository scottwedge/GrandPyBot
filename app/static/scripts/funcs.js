const myBox = document.getElementById('cchild1');// select the div responsable of incubing the responses
let mediaResp = "resul";

// const waitSigne = (disp) => {
//     const waiting = document.querySelector(".wait");
//     $(waiting).hide();
// };


const addUserQuestion = question=>{
    const respBox = document.createElement("div");// create a div of the user question
    respBox.classList.add('userBox');// add class to style the responses

    asking = 'Vous:'+' '+question;
    respBox.innerHTML = asking;
    myBox.append(asking);
};


const getMediaResponse = result => {
    mediaResp = result;
    const respBox = document.createElement("div");// create a div of the media response

    respBox.classList.add('Box');// add class to style the responses
    
    respBox.innerHTML = mediaResp;
    myBox.append(respBox)
};



// function to get the longetitude and laltitude
const getMap =  ()=> {
    console.log('mapdata')
 
};