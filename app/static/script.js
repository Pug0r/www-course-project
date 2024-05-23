// Search on table
$(document).ready(function() {
    var $rows = $('#mainTable tr:gt(0)');
    $('#searchMainTable').keyup(function () {
        var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase(); // multiple spaces
        $rows.show().filter(function () {
            var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
            return !~text.indexOf(val); // efficient check if val not in text
        }).hide();
    });
});

// Color table cells
$(document).ready(function () {

function getColor(value){
// https://stackoverflow.com/questions/7128675/from-green-to-red-color-depend-on-percentage
    //value from 0 to 1
    const MAX_VALUE = 5.0
    value = value * 1.0 / MAX_VALUE
    var hue=(value*120).toString(10);
    return ["hsl(",hue,",100%,50%)"].join("");
}
    $(".mainTableCell").each(function () {
        const value = parseInt($(this).text());
        const color = getColor(value);
        $(this).css("background-color", color);
    });
});

