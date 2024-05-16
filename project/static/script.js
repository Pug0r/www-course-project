$(document).ready(function() {
    var $rows = $('#mainTable tr:gt(0)');
    console.log($rows)
    $('#searchMainTable').keyup(function () {
        var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();

        $rows.show().filter(function () {
            var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
            return !~text.indexOf(val);
        }).hide();
    });
});

