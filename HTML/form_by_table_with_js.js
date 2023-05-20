function output_display(){

    // name
    let a1=document.getElementsByClassName("name")[0];
    document.getElementById("data1_name").innerHTML=a1.value; // id="data1_name"

    // email
    let a2=document.getElementsByClassName("email")[0];
    document.getElementById("data2_email").innerHTML=a2.value;  // id="data2_email"

    //phone no
    let a3=document.getElementsByClassName("phone")[0];
    document.getElementById("data3_pno").innerHTML=a3.value; // id="data3_pno"

    // address
    let a4=document.getElementsByClassName("address")[0];
    document.getElementById("data4_address").innerHTML=a4.value; // id="data4_address"

    // gender male
    let a5=document.getElementsByClassName("ra")[0];
    if(a5.checked){ 				     
    document.getElementById("data5_gender").innerHTML=a5.value; // id="data5_gender"
    }

    // gender female
    let a6=document.getElementsByClassName("ra")[1];
    if(a6.checked){ 				    
     document.getElementById("data5_gender").innerHTML=a6.value; // 
    }

    // age 1-12
    let a7=document.getElementsByClassName("age")[0];
    if(a7.checked){
        document.getElementById("data6_age").innerHTML=a7.value;  // id="data6_age"  
    }

    // age 13-17
    let a71=document.getElementsByClassName("age")[1];
    if(a71.checked){
        document.getElementById("data6_age").innerHTML=a71.value;  // id="data6_age"
    }

    // age 18-20
    let a72=document.getElementsByClassName("age")[2];
    if(a72.checked){
        document.getElementById("data6_age").innerHTML=a72.value; // id="data6_age"
    }

    // age 21-64
    let a73=document.getElementsByClassName("age")[3];
    if(a73.checked){
        document.getElementById("data6_age").innerHTML=a73.value; // id="data6_age"
    }

    // sub maths
    let a8=document.getElementsByClassName("sub")[0];
    if(a8.checked){
        document.getElementById("data7_sub").innerHTML 
        =a8.value; // id="data7_sub"
    }

    // sub science
    let a81=document.getElementsByClassName("sub")[1];
    if(a81.checked){
        document.getElementById("data7_sub").innerHTML+=a81.value; // id="data7_sub"
    }

    // sub histry
    let a82=document.getElementsByClassName("sub")[2];
    if(a82.checked){
        document.getElementById("data7_sub").innerHTML+=a82.value; // id="data7_sub"
    }

    // state
    let a9=document.getElementsByClassName("state")[0];
    document.getElementById("data10_state").innerHTML=a9.value;  // id="data8_state"

    // let a9=document.getElementsByClassName("dist")[0];
    // document.getElementById("data8_dist").innerHTML=a9.value;

    }