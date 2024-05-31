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

// AJAX for courses for a given lecturer
$(document).ready(function() {
$('#controlSelectLecturer').on('change', function() {
  var selected_lecturer = $(this).val();
  if (selected_lecturer) {
    $.ajax({
      type: 'POST',
      url: '/get_lecturer_courses',
      data: { selected_lecturer: selected_lecturer },
      success: function(data) {
        $('#controlSelectCourse').empty().append('<option value="">Choose...</option>');
        $.each(data, function(index, value) {
          $('#controlSelectCourse').append('<option name="course" value="'+ value +'">'+ value +'</option>');
        });
      }
    });
  } else {
    $('#controlSelectCourse').empty().append('<option value="">Choose...</option>');
  }
});
});

// Infinite scrolling
$(document).ready(function() {
    var page = 1;

    function loadComments() {
        $.ajax({
            url: "/get_comments",
            method: "GET",
            data: {
                page: page,
                per_page: 5
            },
            success: function(comments) {
                if (comments.length > 0) {
                    comments.forEach(function(comment) {
                        var commentHtml = `
                            <div class="comment-box">
                                <div class="comment-header">
                                    <p><h4>${comment.lecturer_name}</h4></p>
                                    <h4 style="margin-left: auto">${comment.username}</h4>
                                </div>
                                 <h4>${comment.course_name}</h4>
                                <div class="scores">
                                    <div class="score">
                                        <p>Nastawienie:</p>
                                        <p>${comment.nastawienie}</p>
                                    </div>
                                    <div class="score">
                                        <p>Przekazywanie wiedzy:</p>
                                        <p>${comment.przekazywanie}</p>
                                    </div>
                                    <div class="score">
                                        <p>Inicjatywa:</p>
                                        <p>${comment.inicjatywa}</p>
                                    </div>
                                    <div class="score">
                                        <p>Przygotowanie:</p>
                                        <p>${comment.przygotowanie}</p>
                                    </div>
                                    <div class="score">
                                        <p>Dostosowanie:</p>
                                        <p>${comment.dostosowanie}</p>
                                    </div>
                                </div>
                                <div class="comment-body">
                                    <p>${comment.comment}</p>
                                </div>
                            </div>
                        `;
                        $("#comment-section").append(commentHtml);
                    });
                    page++;
                }
            }
        });
    }

    $(window).scroll(function() {
        if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
            loadComments();
        }
    });

    // Initial load
    loadComments();
});