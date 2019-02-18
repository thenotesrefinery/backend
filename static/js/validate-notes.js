function toggleVerify() {
    var btn = $("#verify-btn");

    if(btn.hasClass("btn-outline-success")) { // verify
        btn.removeClass("btn-outline-success");
        btn.addClass("btn-success");

        var count = parseInt($("#verify-num").text());
        $("#verify-num").text(++count);
        $("#verify-btn > span").text("Verified");

    } else { // remove verify
        btn.removeClass("btn-success");
        btn.addClass("btn-outline-success");

        var count = parseInt($("#verify-num").text());
        $("#verify-num").text(--count);
        $("#verify-btn > span").text("Verify");
    }
}
