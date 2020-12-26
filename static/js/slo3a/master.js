$(document).ready(function () {
    $(document).on('click', '.box', function () {
        if ($(this).text() == "Matematyka - grupy") {
            if ($('.math')[0]) {
                $('.add').remove();
            }

            else {
                $('.add').remove();
                $(this).after("<a href='https://us02web.zoom.us/j/2693771475?pwd=SFNmQUIvT0tRaHlDaVYrN3l5bzJVQT09' target='_blank'><div class='add math new box d-flex flex-column justify-content-center'>Rubaj</div></a>");
                $(this).after("<a href='https://us04web.zoom.us/j/2483015118?pwd=WEtHK0llaWZmTWtmTnhPUlVqRmlGUT09' target='_blank'><div class='add math new box d-flex flex-column justify-content-center'>Buba</div></a>");
            }
        }

        else if ($(this).text() == "Fizyka - grupy") {
            if ($('.physics')[0]) {
                $('.add').remove();
            }

            else {
                $('.add').remove();
                $(this).after("<a href='https://zoom.us/j/2838246804?pwd=Umh1eEJ5VFJqVE1NSmZZUytlMUdGZz09' target='_blank'><div class='add physics new box d-flex flex-column justify-content-center'>Mazi</div></a>");
                $(this).after("<a href='https://zoom.us/j/4861451584?pwd=RFFxWGRJelE2T3BtdWpQUk5SQjFBQT09' target='_blank'><div class='add physics new box d-flex flex-column justify-content-center'>Radek</div></a>");
            }
        }

        else if ($(this).text() == "Angielski - grupy") {
            if ($('.english')[0]) {
                $('.add').remove();
            }

            else {
                $('.add').remove();
                $(this).after("<a href='https://us04web.zoom.us/j/4312598558?pwd=RDlUelJXTk1mUmxoMzNPOUZJa2IxZz09' target='_blank'><div class='add english new box d-flex flex-column justify-content-center'>Kowalczyk</div></a>");
                $(this).after("<a href='https://zoom.us/j/6717774670?pwd=REhhSXdCaXphRFQyM0pVUGJ3THFBZz09' target='_blank'><div class='add english new box d-flex flex-column justify-content-center'>Skworon</div></a>");
                $(this).after("<a href='https://us04web.zoom.us/j/75537981297?pwd=L3BHL0tkZXFsTEx5VjV3WS8yQ2VJUT09' target='_blank'><div class='add english new box d-flex flex-column justify-content-center'>Kotlińska</div></a>");
                $(this).after("<a href='https://us04web.zoom.us/j/6708313679?pwd=RWlUODlGOTFndFZSbHBRdFZoT0V3dz09' target='_blank'><div class='add english new box d-flex flex-column justify-content-center'>Denys</div></a>");
            }
        }
    });
});