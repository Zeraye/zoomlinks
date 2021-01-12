$(document).ready(function () {
    $(document).on('click', '.card', function () {
        $('.inside2').remove();
        $('.inside4').remove();
        $('.physics').text('Fizyka');
        $('.math').text('Matematyka');
        $('.english').text('Angielski');

        if ($(this).text() == 'Matematyka' && $(this).hasClass('math')) {
            $(this).text('');
            $(this).addClass('add');
            $(this).append($("<div class='inside2'><a href='https://us04web.zoom.us/j/2483015118?pwd=WEtHK0llaWZmTWtmTnhPUlVqRmlGUT09' class='no-decoration' target='_blank'>Buba</a></div>"))
            $(this).append($("<div class='inside2'><a href='https://us02web.zoom.us/j/2693771475?pwd=SFNmQUIvT0tRaHlDaVYrN3l5bzJVQT09' class='no-decoration' target='_blank'>Rubaj</a></div>"))
        }
        else if ($(this).text() == 'Fizyka' && $(this).hasClass('physics')) {
            $(this).text('');
            $(this).addClass('add');
            $(this).append($("<div class='inside2'><a href='https://zoom.us/j/2838246804?pwd=Umh1eEJ5VFJqVE1NSmZZUytlMUdGZz09' class='no-decoration' target='_blank'>Mazi</a></div>"))
            $(this).append($("<div class='inside2'><a href='https://zoom.us/j/4861451584?pwd=RFFxWGRJelE2T3BtdWpQUk5SQjFBQT09' class='no-decoration' target='_blank'>Radek</a></div>"))
        }
        else if ($(this).text() == 'Angielski' && $(this).hasClass('english')) {
            $(this).text('');
            $(this).addClass('add');
            $(this).append($("<div class='inside4'><a href='https://us04web.zoom.us/j/6708313679?pwd=RWlUODlGOTFndFZSbHBRdFZoT0V3dz09' class='no-decoration' target='_blank'>Denys</a></div>"))
            $(this).append($("<div class='inside4'><a href='https://us04web.zoom.us/j/75537981297?pwd=L3BHL0tkZXFsTEx5VjV3WS8yQ2VJUT09' class='no-decoration' target='_blank'>Kotlińska</a></div>"))
            $(this).append($("<div class='inside4'><a href='https://zoom.us/j/6717774670?pwd=REhhSXdCaXphRFQyM0pVUGJ3THFBZz09' class='no-decoration' target='_blank'>Skowron</a></div>"))
            $(this).append($("<div class='inside4'><a href='https://us04web.zoom.us/j/4312598558?pwd=RDlUelJXTk1mUmxoMzNPOUZJa2IxZz09' class='no-decoration' target='_blank'>Kowalczyk</a></div>"))
        }
    });
});
