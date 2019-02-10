$( document ).ready(function() {
    $('#advanced-search').hide();
});

$(document).on('change', '.checkbox', function() {
    // uncheck checkbox for all
    var self = $(this);
    if (self.is(":checked")) {
        $("#all").prop("checked", false);
    }
});

function showAdvanced() {
    $('#basic-search').hide();
    $('#advanced-button-section').hide();
    $('#advanced-search').show();
}

function showBasic() {
    $('#basic-search').show();
    $('#advanced-button-section').show();
    $('#advanced-search').hide();
}
