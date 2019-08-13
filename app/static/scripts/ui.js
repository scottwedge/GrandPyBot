const form = document.querySelector('form');
const questionVal = document.getElementById('searchbar');





 const eventPromise = new Promise( 
    () => {
        
    
                 form.addEventListener('submit', e => {
                        e.preventDefault();
                        const question = questionVal.value.trim();
                        const waiting = document.querySelector(".wait");

                        

                        const ajxQuery = $.ajax({
                            type: "POST",
                            url: '/', 
                            data: JSON.stringify(question),
                            success: response => {
                                console.log(response);
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

                            ajxQuery.then(
                                ()=>{
                                    console.log('Heey')
                                }
                            );
                        
                               
                        getMediaResponse();
                        getMap();
                    });
                                                        
                        
            });

         
    