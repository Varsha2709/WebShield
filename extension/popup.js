
chrome.storage.local.get(["score","attack"],function(data){

let score=data.score||0
let attack=data.attack||"Safe"

let canvas=document.getElementById("gauge")
let ctx=canvas.getContext("2d")

ctx.beginPath()
ctx.lineWidth=15
ctx.strokeStyle="#ddd"
ctx.arc(125,125,90,Math.PI,2*Math.PI)
ctx.stroke()

let color="green"

if(score>70) color="red"
else if(score>40) color="orange"

ctx.beginPath()
ctx.strokeStyle=color
ctx.arc(125,125,90,Math.PI,Math.PI+(score/100)*Math.PI)
ctx.stroke()

ctx.font="28px Arial"
ctx.fillText(score+"%",95,110)

document.getElementById("status").innerText="Threat: "+attack

})
