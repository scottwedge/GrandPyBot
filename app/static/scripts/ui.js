const form = document.querySelector("form"); // select the form
const questionVal = document.getElementById("searchbar"); // select the input
const container = document.getElementById("cchild1");
const eventPromise = new Promise(() => {
  form.addEventListener("submit", e => {
    e.preventDefault();
    const question = questionVal.value.trim(); // trim over the input value
    const waiting = document.querySelector(".wait"); // select the waiting image of load
    let mediaResp = ""; // a variabl will get the value of the response ajax of media story
    let mapLink = ""; // a variabl will get the value of the response ajax of the map link

    addUserQuestion(question);
    //first ajax Query to get the map
    const ajxMapQuery = $.ajax({
      type: "POST",
      url: "/map",
      data: JSON.stringify(question),
      success: response => {
        mapLink = response;
      },
      dataType: "json",
      contentType: "application/json;charset=UTF-8",
      beforesend: () => {
        console.log('before');
        $(waiting).css("display", "block");
      },
      erro: error => {
        console.log(error);
      },
      complete: () => {
        console.log('after');

        $(waiting).css("display", "none");
      }
    });

    // callback of the map
    ajxMapQuery
      .then(() => {
        getMap(mapLink);
      }).then(() => {
        // The second Ajax request to get the story
        const ajxMediaQuery = $.ajax({
          type: "POST",
          url: "/",
          data: JSON.stringify(question),
          success: response => {
            mediaResp = response;
          },
          dataType: "json",
          contentType: "application/json;charset=UTF-8",
          beforesend: () => {
            console.log('before');

            $(waiting).css("display", "block");
          },
          erro: error => {
            console.log(error);
          },
          complete: () => {
            console.log('before');

            $(waiting).css("display", "none");
          }
        });
        // The call back then of the mediawiki response
        ajxMediaQuery.then(() => {
          //profilBot();
          getMediaResponse(mediaResp);
          container.scrollTo(0, document.body.scrollHeight);

        });
      });
  });
});
