function Show_Favourites(id){

    var Specific_f = document.getElementsByClassName['Specific_Favourites'];
    for(i = 0; i < Specific_f.length; i++){
        document.getElementsByClassName['Specific_Favourites'][i].backgroundColor = '#566573';
    }

    document.getElementById[id].backgroundColor = '#3498DB';
}