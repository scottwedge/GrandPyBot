const form = document.querySelector('form');
const questionVal = document.getElementById('searchbar');





 const eventPromise = new Promise( 
    () => {
        
    
                 form.addEventListener('submit', e => {
                                                    e.preventDefault();
                                                    const question = questionVal.value.trim();
                                                    

                                                    $.ajax({
                                                        type: "POST",
                                                        url: '/', 
                                                        data: JSON.stringify(question),
                                                        success: response => {
                                                            console.log(response);
                                                        },
                                                        dataType: "json",
                                                        contentType: 'application/json;charset=UTF-8',
                                                        erro : error=>{
                                                            console.log(error);
                                                        }
                                                        });
                                                        
                                                        
                                                        

                                                        getMediaResponse();
                                                        getMap();
                                                        
                                                        
                                                    });
                                                        
                        
            });

         
    