
chrome.runtime.onMessage.addListener((data)=>{

fetch("http://localhost:5000/predict",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)
})
.then(res=>res.json())
.then(result=>{

chrome.storage.local.set({score:result.risk_score,attack:result.attack})

let color="green"

if(result.risk_score>70) color="red"
else if(result.risk_score>40) color="orange"

chrome.action.setBadgeText({text:String(result.risk_score)})
chrome.action.setBadgeBackgroundColor({color:color})

if(result.risk_score>70){
chrome.tabs.update({
url:chrome.runtime.getURL("warning.html")+"?attack="+result.attack
})
}

})

})
