console.log("🚀 ProductPulse AI Started");

// =====================================
// GLOBAL VARIABLES
// =====================================

let ratingChart = null;
let reviewChart = null;

// =====================================
// DOM ELEMENTS
// =====================================

const compareBtn = document.getElementById("compare-btn");

const loading = document.getElementById("loading-section");

const results = document.getElementById("results-section");

const darkToggle = document.getElementById("dark-mode-toggle");

const backTop = document.getElementById("backToTop");

// =====================================
// DARK MODE
// =====================================

darkToggle.addEventListener("click",()=>{

document.body.classList.toggle("dark");

if(document.body.classList.contains("dark")){

darkToggle.innerHTML=
'<i class="bi bi-sun-fill"></i> Light Mode';

}else{

darkToggle.innerHTML=
'<i class="bi bi-moon-stars-fill"></i> Dark Mode';

}

});

// =====================================
// BACK TO TOP
// =====================================

window.addEventListener("scroll",()=>{

if(window.scrollY>300){

backTop.style.display="flex";

}else{

backTop.style.display="none";

}

});

backTop.onclick=()=>{

window.scrollTo({

top:0,

behavior:"smooth"

});

};

// =====================================
// COMPARE BUTTON
// =====================================

compareBtn.addEventListener("click",async()=>{

const url1=document.getElementById("app1-url").value.trim();

const url2=document.getElementById("app2-url").value.trim();

if(!url1 || !url2){

alert("Enter both URLs");

return;

}

loading.style.display="block";

results.style.display="none";
try{

const response = await fetch("/compare",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

url1:url1,

url2:url2

})

});

if(!response.ok){

throw new Error("Backend Error");

}

const data = await response.json();

console.log(data);

loading.style.display="none";

results.style.display="block";

// =====================================
// APP 1
// =====================================

document.getElementById("app1-name").innerText =
data.product1.name;

document.getElementById("app1-rating").innerText =
Number(data.product1.rating).toFixed(2);

document.getElementById("app1-reviews").innerText =
data.product1.reviews;

// =====================================
// APP 2
// =====================================

document.getElementById("app2-name").innerText =
data.product2.name;

document.getElementById("app2-rating").innerText =
Number(data.product2.rating).toFixed(2);

document.getElementById("app2-reviews").innerText =
data.product2.reviews;

// =====================================
// WINNER
// =====================================

document.getElementById("winner-name").innerText =
data.winner;

// =====================================
// SUMMARY
// =====================================

document.getElementById("summary").innerHTML =

`<strong>${data.product1.name}</strong><br><br>

${data.product1.summary}

<hr>

<strong>${data.product2.name}</strong><br><br>

${data.product2.summary}`;

// =====================================
// PROGRESS BARS
// =====================================

document.getElementById("app1-progress").style.width =
(Number(data.product1.rating)/5*100)+"%";

document.getElementById("app2-progress").style.width =
(Number(data.product2.rating)/5*100)+"%";
// =====================================
// PAIN POINTS
// =====================================

function populateList(id, items, emoji){

    const list=document.getElementById(id);

    list.innerHTML="";

    items.forEach(item=>{

        const li=document.createElement("li");

        li.innerHTML=`${emoji} ${item}`;

        list.appendChild(li);

    });

}

populateList(
"app1-pain",
data.product1.pain_points,
"🔴"
);

populateList(
"app2-pain",
data.product2.pain_points,
"🔴"
);

populateList(
"app1-features",
data.product1.feature_requests,
"🟢"
);

populateList(
"app2-features",
data.product2.feature_requests,
"🟢"
);

// =====================================
// COPY SUMMARY
// =====================================

const copyBtn=document.getElementById("copy-summary-btn");

copyBtn.onclick=async()=>{

try{

await navigator.clipboard.writeText(

document.getElementById("summary").innerText

);

copyBtn.innerHTML="✅ Copied";

setTimeout(()=>{

copyBtn.innerHTML="📋 Copy Summary";

},2000);

}catch{

alert("Clipboard permission denied.");

}

};

// =====================================
// RATING CHART
// =====================================

if(ratingChart){

ratingChart.destroy();

}

ratingChart=new Chart(

document.getElementById("ratingChart"),

{

type:"bar",

data:{

labels:[

data.product1.name,

data.product2.name

],

datasets:[{

label:"Rating",

data:[

data.product1.rating,

data.product2.rating

],

backgroundColor:[

"#2563eb",

"#22c55e"

],

borderRadius:10

}]

},

options:{

responsive:true,

plugins:{

legend:{

display:false

}

},

scales:{

y:{

beginAtZero:true,

max:5

}

}

}

}

);

// =====================================
// REVIEW CHART
// =====================================

if(reviewChart){

reviewChart.destroy();

}

reviewChart=new Chart(

document.getElementById("reviewChart"),

{

type:"bar",

data:{

labels:[

data.product1.name,

data.product2.name

],

datasets:[{

label:"Reviews",

data:[

data.product1.reviews,

data.product2.reviews

],

backgroundColor:[

"#f59e0b",

"#ef4444"

],

borderRadius:10

}]

},

options:{

responsive:true,

plugins:{

legend:{

display:false

}

}

}

}

);
// =====================================
// ANIMATE RESULTS
// =====================================

results.style.opacity = "0";
results.style.display = "block";

setTimeout(() => {

    results.style.transition = "all 0.8s ease";

    results.style.opacity = "1";

}, 100);

// =====================================
// AUTO SCROLL TO RESULTS
// =====================================

results.scrollIntoView({

    behavior: "smooth",

    block: "start"

});

// =====================================
// SUCCESS MESSAGE
// =====================================

console.log("✅ Comparison Loaded Successfully");

}

// =====================================
// ERROR HANDLING
// =====================================

catch(error){

console.error(error);

loading.style.display="none";

alert(

"Unable to connect to backend.\n\nPlease ensure the FastAPI server is running."

);

}

// =====================================
// FINISH
// =====================================

});