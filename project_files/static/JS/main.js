


function copytext(id){
    copied_data = document.getElementById(id).innerHTML
    navigator.clipboard.writeText(copied_data)
  }