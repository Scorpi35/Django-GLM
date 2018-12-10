function navBarColor(){
   var extended_url = window.location.href;
   var get_url = extended_url.replace("http://127.0.0.1:8000/", "");
   if(get_url == "Skills/"){
           document.getElementById("Skills").style.backgroundColor="#3498DB";
           document.getElementById("Skills").style.color = "white";
   }
   if(get_url == "HomePage/"){
            document.getElementById("Home").style.backgroundColor="#3498DB";
           document.getElementById("Home").style.color = "white";
   }

   if(get_url == 'Education/'){
        document.getElementById("Education").style.backgroundColor="#3498DB";
        document.getElementById("Education").style.color = "white";
   }

   if(get_url == 'Portfolio/'){
        document.getElementById("Portfolio").style.backgroundColor="#3498DB";
        document.getElementById("Portfolio").style.color = "white";
   }

   if(get_url == 'AboutMe/'){
        document.getElementById("About_Me").style.backgroundColor="#3498DB";
        document.getElementById("About_Me").style.color = "white";
   }

   if(get_url == 'Experience/'){
        document.getElementById("Experience").style.backgroundColor = "#3498DB";
        document.getElementById("Experience").style.color = "white";
   }

   if(get_url == 'Blog/'){
        document.getElementById("Blog").style.backgroundColor = "#3498DB";
        document.getElementById("Blog").style.color = "white";
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

function Go_AboutMe(){
    window.location.href = "http://127.0.0.1:8000/AboutMe/";
}

function Go_Experience(){
    window.location.href = "http://127.0.0.1:8000/Experience/";
}

function Go_Blog(){
    window.location.href = "http://127.0.0.1:8000/Blog/";
}



