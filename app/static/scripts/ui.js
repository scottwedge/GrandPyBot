const form = document.querySelector('form');
const questionVal = document.getElementById('searchbar');




form.addEventListener('submit', e => {
    e.preventDefault();
    const question = questionVal.value.trim();

    $.ajax({
        type: "POST",
        url: '/',
        data: JSON.stringify(question),
        success: response => {
            console.log(response);
            console.log('yuuup');
        },
        dataType: "json",
        contentType: 'application/json;charset=UTF-8',
        erro : error=>{
            console.log(error);
        }
        });
    
    


});