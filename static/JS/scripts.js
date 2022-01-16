let button = document.getElementsByID("btn-top");

window.onscroll = function(){
    scrollFunction();
};

function scrollFunction(){
    if(
        document.body.scrollTop > 20 ||
        document.documentElement.scrollTop > 20
    ){
        button.style.display = "block";
    }else{
        button.style.display = "none";
    }
}

button.addEventListener("click", backToTop);

function backToTop(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}


