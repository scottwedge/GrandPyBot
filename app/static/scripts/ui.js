const form = document.querySelector('form');// select the form
const questionVal = document.getElementById('searchbar');// select the input





 const eventPromise = new Promise( 
    () => {
        
    
                 form.addEventListener('submit', e => {
                        e.preventDefault();
                        const question = questionVal.value.trim();// trim over the input value
                        const waiting = document.querySelector(".wait");// select the waiting image of load
                        let mediaResp=""; // a variabl will get the value of the response ajax of media story
                        let mapResp="";// a variabl will get the value of the response ajax of the map link 


                        addUserQuestion(question);
                        //first ajax Query to get the story
                        const ajxMediaQuery = $.ajax({
                            type: "POST",
                            url: '/', 
                            data: JSON.stringify(question),
                            success: response => {
                                 mediaResp = response;
                            },
                            dataType: "json",
                            contentType: 'application/json;charset=UTF-8',
                            beforesend : ()=>{
                                $(waiting).css("display", "block");
                            },
                            erro : error=>{
                                console.log(error);
                            },
                            complete: ()=>{
                                $(waiting).css("display", "none");
                            },
                            });
                            // The call back then of the mediawiki response
                            ajxMediaQuery.then(
                                ()=>{
                                getMediaResponse(mediaResp);
                                }
                                            );
                        
                            // The second Ajax request to get the map link
                            const ajxMapQuery = $.ajax({
                                type: "POST",
                                url: '/map', 
                                data: JSON.stringify(question),
                                success: response => {
                                        mapResp = response;
                                },
                                dataType: "json",
                                contentType: 'application/json;charset=UTF-8',
                                beforesend : ()=>{
                                    $(waiting).css("display", "block");
                                },
                                erro : error=>{
                                    console.log(error);
                                },
                                complete: ()=>{
                                    $(waiting).css("display", "none");
                                },
                                });

                            // callback of the map
                            ajxMapQuery.then(
                                ()=>{
                                    console.log(mapResp);
                                }
                            )






                        // getMap();
                    });
                                                        
                        
            });

         
    