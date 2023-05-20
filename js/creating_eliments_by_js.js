let a=document.createElement("p");
    a.setAttribute("Id","abc")
    a.innerHTML="jgfagjskdhasjgj";

// document..append("b")
let b=document.createElement("button");
b.innerHTML="kjasdkk"
document.body.append(b)
document.body.append(a)

let h=document.createElement("h1")
h.innerHTML="hello"
h.setAttribute("id","h1")
document.getElementById("p1").append(h)
let  b1=document.createElement("b");

document.getElementById("h1").appendChild(b1);
b1.innerHTML="  xyz"

document.getElementById("p1").style.border="10px solid red"