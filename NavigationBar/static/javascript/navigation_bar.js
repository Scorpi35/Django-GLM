function navBarColor(){
   var extended_url = window.location.href;
   var get_url = extended_url.replace("http://127.0.0.1:8000/", "");
   if(get_url == "Skills/"){
           document.getElementById("Skills").style.color="#BDC3C7";
   }
   if(get_url == "HomePage/"){
            document.getElementById("Home").style.color = "#BDC3C7";
   }

   if(get_url == 'Education/'){
        document.getElementById("Education").style.color = "#BDC3C7";
   }

   if(get_url == 'Portfolio/'){
        document.getElementById("Portfolio").style.color = "#BDC3C7";
   }
}

function Go_HomePage(){
    window.location.href ="http://127.0.0.1:8000/HomePage/";
}

function Go_Skills(){
    window.location.href = "http://127.0.0.1:8000/Skills/";
}

function Go_Education(){
    window.location.href = "http://127.0.0.1:8000/Education/";
}

function Go_Portfolio(){
    window.location.href = "http://127.0.0.1:8000/Portfolio/";
}



