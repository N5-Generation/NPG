function reloadContent(url = null, target = null) {
    let this_url = window.location.href
    
    if (url == null) {
        $("#content").empty()
        $("#content").load(this_url + " #content")
        console.log(this_url);
    } else {
        $("#content").empty()
        $("#content").load(`${url} ${target}`)
    }
}
