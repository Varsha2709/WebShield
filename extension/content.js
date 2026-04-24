
let data={
url:window.location.href,
html:document.documentElement.outerHTML
}

chrome.runtime.sendMessage(data)
