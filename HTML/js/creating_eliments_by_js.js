let a=document.createElement("p"); // creating element of " <p>______</p>"
    a.setAttribute("Id","abc")      // adding " id/class/name/giving value " to element by calling variable
    a.innerHTML="jgfagjskdhasjgj"; // writing content in element  

    document.body.append(a)  // giving access to body in HTML DOC


let b=document.createElement("button");
b.innerHTML="kjasdkk"
document.body.append(b)


let h=document.createElement("h1")
h.innerHTML="hello"
h.setAttribute("id","h1")
document.getElementById("p1").append(h)
let  b1=document.createElement("b");

document.getElementById("h1").appendChild(b1);
b1.innerHTML="  xyz"

document.getElementById("p1").style.border="10px solid red"