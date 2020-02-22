var table = $('#enronData').DataTable();

$(document).ready(function() {
    getEnronData();
});

function getEnronData() {
    $('#loading').show();
    $('#enronData').hide();
    $('#enronData_wrapper').hide();
    $.ajax({
        type: "GET",
        url: '/getEnronData',
        success: function(data) {
            data = JSON.parse(data);
            table.destroy();
            $('#enronData tbody').empty();
            //loop through data
            for (var i = 0; i < data.length; i++) {
                var row = data[i];

                //Init Row
                var tableRow = "<tr>";
                //Add Row Data
                Object.values(row).forEach(element => {
                    var tableCell = "<td>" + element + "</td>";
                    tableRow += tableCell;
                });
                //Close Row
                tableRow += "</tr>";
                //Append Row
                tableBody = $("#enronData tbody").append(tableRow);
            }

            //Make Data Table
            $('#loading').hide()
            $('#enronData').show();
            $('#enronData_wrapper').show();
            table = $('#enronData').DataTable({
                "dom": "<'row'<'col-sm-12 col-md-6'B><'col-sm-12 col-md-6'fl>>" +
                    "<'row'<'col-sm-12'tr>>" +
                    "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
                "columnDefs": [{
                    "targets": [0, 5, 7, 8, 9, 10, 11, 12, 13, 14, 18],
                    "visible": false
                }],
                "order": [
                    [7, "asc"]
                ],
                "buttons": [{ extend: 'copyHtml5' },
                    { extend: 'csvHtml5' },
                    {
                        extend: 'pdfHtml5',
                        title: function() { return "Enron Data"; },
                        orientation: 'landscape',
                        pageSize: 'A2',
                        text: 'PDF',
                        titleAttr: 'PDF'
                    },
                    { extend: 'colvis' }
                ]
            });
        }
    });
}