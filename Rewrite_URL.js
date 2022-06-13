function handler(event) {
    var request = event.request;
    var uri = request.uri;
    var file_name = Math.floor((Math.random() * 10) + 1)+ '.jpg'
    var no_dots = 0
    
    // Check whether the URI is missing a file name.
    if (request.uri.endsWith('/')) {
        request.uri += file_name;
    } 
    // Check whether the URI is missing a file extension.
    else {
        no_dots = (request.uri.split(".").length - 1) //3
        if (no_dots == 2)
        
        request.uri = request.uri + '/' + file_name;
    }

    return request;
}
