function formatDate(date) {
    date = new Date(date.getTime() + date.getTimezoneOffset() * 60000);
    var formatString = "";
    switch (date.getMonth()) {
        case 0:
            formatString = "January";
            break;
        case 1:
            formatString = "February";
            break;
        case 2:
            formatString = "March";
            break;
        case 3:
            formatString = "April";
            break;
        case 4:
            formatString = "May";
            break;
        case 5:
            formatString = "June";
            break;
        case 6:
            formatString = "July";
            break;
        case 7:
            formatString = "August";
            break;
        case 8:
            formatString = "September";
            break;
        case 9:
            formatString = "October";
            break;
        case 10:
            formatString = "November";
            break;
        case 11:
            formatString = "December";
            break;
    }

    formatString += " " + date.getDate() + ", " + date.getFullYear();

    return formatString;
}

function getData(data) {
    var result = $.parseJSON(data);
    if (result != null && result.type == 'status') {
        var date = new Date(result.data.started);
        $('#count').html((result.data.count > 0 ? result.data.count : 'No') + ' toasting events have been recorded since ' + formatDate(date) + '.');
        $('#titlecount').html('Toasts: ' + result.data.count);
        $('#stat').html(result.data.status ? 'Yes.' : 'No.');
        if (result.data.status == true)
            $('#stat').css('color', 'red');
        else
            $('#stat').css('color', 'black');
        $('#count').css('color', 'black');
    }
    else {
        $('#stat').html("Well, maybe...");
        $('#count').css('color', 'red');
        $('#stat').css('color', 'red');
        $('#count').html("We're having a brief technical issue. Hang in there!");
        $('#titlecount').html("Busted!");
    }
}

var makeRequest = function () {
    $.get('/api?activity=get', getData);
};