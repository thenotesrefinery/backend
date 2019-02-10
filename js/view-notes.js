$( document ).ready(function() {
    PDFObject.embed("sampleNotes/respiration.pdf", "#pdf-notes");
});

function toggleGood() {
    var btn = $("#good-btn");

    if(btn.hasClass("btn-outline-success")) { // increase thumbs up
        btn.removeClass("btn-outline-success");
        btn.addClass("btn-success");

        var count = parseInt($("#good-btn > span").text());
        $("#good-btn > span").text(++count);

        // if previously pressed thumbs down
        if($("#bad-btn").hasClass("btn-danger")) {
            $("#bad-btn").removeClass("btn-danger");
            $("#bad-btn").addClass("btn-outline-danger");

            count = parseInt($("#bad-btn > span").text());
            $("#bad-btn > span").text(--count);
        }

    } else { // remove thumbs up
        btn.removeClass("btn-success");
        btn.addClass("btn-outline-success");

        count = parseInt($("#good-btn > span").text());
        $("#good-btn > span").text(--count);
    }
}

function toggleBad() {
    var btn = $("#bad-btn");

    if(btn.hasClass("btn-outline-danger")) { // increase thumbs down
        btn.removeClass("btn-outline-danger");
        btn.addClass("btn-danger");

        var count = parseInt($("#bad-btn > span").text());
        $("#bad-btn > span").text(++count);

        // if previously pressed thumbs up
        if($("#good-btn").hasClass("btn-success")) {
            $("#good-btn").removeClass("btn-success");
            $("#good-btn").addClass("btn-outline-success");

            count = parseInt($("#good-btn > span").text());
            $("#good-btn > span").text(--count);
        }

    } else { // remove thumbs down
        btn.removeClass("btn-danger");
        btn.addClass("btn-outline-danger");

        var count = parseInt($("#bad-btn > span").text());
        $("#bad-btn > span").text(--count);
    }
}
