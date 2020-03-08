const myBox = document.getElementById("cchild1"); // select the div responsable of incubing the responses
let mediaResp = "result"; // varriable will take the string return of place's story
const waitSigne = disp => {
  const waiting = document.querySelector(".wait");
  $(waiting).hide();
};

// make a function to create the bot icon into all boxes of the bot's answers
const profilBot = element => {
  const img = document.createElement("img");
  img.src = "static/img/pybot.png";
  img.classList.add("pybotInBox");

  //Make a try and catch the img added
  try {
    element.appendChhild(img);
  } catch (error) {
    console.log(error);
  }
};

// function to add the user's question to the chatbox
const addUserQuestion = question => {
  const userRespBox = document.createElement("div"); // create a div of the user question
  userRespBox.classList.add("userBox"); // add class to style the responses
  asking = `<p class="userVous">Vous :  </p>
                    <p class="userQues">${question}</p>
                `;
  userRespBox.innerHTML = asking;
  myBox.append(userRespBox);
};

// function to get and add the map
const getMap = Url => {
  const respBox = document.createElement("div"); // create a div that will contain the map
  url = Url;
  const frameMap = document.createElement('iframe');

  console.log(url)
  respBox.classList.add("Box"); // add class to style the map covering all the div
  frameMap.src = url;
  frameMap.classList.add("framMap");
  respBox.appendChild(frameMap);
  myBox.append(respBox);
};

// function to add the response returned to the chat box
const getMediaResponse = result => {
  mediaResp = result;
  const respBox = document.createElement("div"); // create a div of the media response

  respBox.classList.add("Box"); // add class to style the responses
  // add the pybot img
  profilBot(respBox);
  respBox.innerHTML = mediaResp;
  myBox.append(respBox);
};
