function setup() {
    $('#stat').html('Wrong');
    $('#titlecount').html('Wrong');
    $('#count').html('Wrong');
    $('#stat').css('color', 'blue');
    $('#count').css('color', 'blue');
}

test("formatDate Test", function () {
    deepEqual(formatDate(new Date(0)), "January 1, 1970", "Date formatted!");
});

test("getOnData Test", function () {
    setup();
    getData('{"data": {"status": true, "count": 1, "last": 1354387929623, "started": 1354387929623}, "type": "status"}');
    deepEqual('Yes.', $('#stat').html(), 'Stat correct.');
    deepEqual($('#red').css('color'), $('#stat').css('color'), 'Color correct');
    deepEqual($('#black').css('color'), $('#count').css('color'), 'Count color correct');
    deepEqual('Toasts: 1', $('#titlecount').html(), 'Title correct.');
    deepEqual('1 toasting events have been recorded since December 1, 2012.', $('#count').html(), 'Count correct');
});

test("getOffData Test", function () {
    setup();
    getData('{"data": {"status": false, "count": 0, "last": 1354387929623, "started": 1354387929623}, "type": "status"}');
    deepEqual('No.', $('#stat').html(), 'Stat correct.');
    deepEqual($('#black').css('color'), $('#stat').css('color'), 'Color correct');
    deepEqual($('#black').css('color'), $('#count').css('color'), 'Count color correct');
    deepEqual('Toasts: 0', $('#titlecount').html(), 'Title correct.');
    deepEqual('No toasting events have been recorded since December 1, 2012.', $('#count').html(), 'Count correct');
});

test("getErrorData Test", function () {
    setup();
    getData('{"data": "Test error", "type": "error"}');
    deepEqual('Well, maybe...', $('#stat').html(), 'Stat correct.');
    deepEqual($('#red').css('color'), $('#stat').css('color'), 'Status color correct');
    deepEqual($('#red').css('color'), $('#count').css('color'), 'Count color correct');
    deepEqual('Busted!', $('#titlecount').html(), 'Title correct.');
    deepEqual('We\'re having a brief technical issue. Hang in there!', $('#count').html(), 'Count correct');
});

test("getBadData Test", function () {
    setup();
    getData('');
    deepEqual('Well, maybe...', $('#stat').html(), 'Stat correct.');
    deepEqual($('#red').css('color'), $('#stat').css('color'), 'Status color correct');
    deepEqual($('#red').css('color'), $('#count').css('color'), 'Count color correct');
    deepEqual('Busted!', $('#titlecount').html(), 'Title correct.');
    deepEqual('We\'re having a brief technical issue. Hang in there!', $('#count').html(), 'Count correct');
});