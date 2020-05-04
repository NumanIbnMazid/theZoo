// date-time picker

$(document).ready(function () {
    function now() {
        var d = new Date();
        var month = d.getMonth() + 1;
        var day = d.getDate();
        var output =
            d.getFullYear() +
            "/" +
            (month < 10 ? "0" : "") +
            month +
            "/" +
            (day < 10 ? "0" : "") +
            day;
        return output;
    }

    // function checkDate() {
    //     var input = $("#date_to");
    //     return input.val();
    // }

    $("#date_from").datetimepicker({
        timepicker: false,
        format: "Y-m-d",
        // maxDate: now(),
        validateOnBlur: true,
        closeOnDateSelect: true,
        todayButton: true,
        // onShow: function (ct) {
        //     this.setOptions({
        //         // maxDate: jQuery('#date_to').val() ? jQuery('#date_to').val() : false,
        //         maxDate: checkDate()
        //     })
        // },
    });
});

// date-time picker
$(document).ready(function () {
    function now() {
        var d = new Date();
        var month = d.getMonth() + 1;
        var day = d.getDate();
        var output =
            d.getFullYear() +
            "/" +
            (month < 10 ? "0" : "") +
            month +
            "/" +
            (day < 10 ? "0" : "") +
            day;
        return output;
    }

    // function checkDate(){
    //     var input = $("#date_from");
    //     return input.val();
    // }

    $("#date_to").datetimepicker({
        timepicker: false,
        format: "Y-m-d",
        // maxDate: now(),
        validateOnBlur: true,
        closeOnDateSelect: true,
        todayButton: true,
        // onShow: function (ct) {
        //     this.setOptions({
        //         // maxDate: jQuery('#date_from').val() ? jQuery('#date_to').val() : false,
        //         maxDate: checkDate()
        //     })
        // },
    });
});

// preventing form from autocomplete
$(document).ready(function () {
    $(document).on("focus", ":input", function () {
        $(this).attr("autocomplete", "off");
    });
});

function resetMessage() {
    $(".error").html("");
}

function dateFilterFunction() {
    // resetMessage();
    var date_from_input = $("#date_from");
    var date_to_input = $("#date_to");
    // console.log(date_from_input);
    // console.log(date_to_input);
    var df = date_from_input.val().split("-");
    var dt = date_to_input.val().split("-");
    // console.log(df);
    // console.log(dt);
    var df_j = df.join(' ');
    var dt_j = dt.join(' ');
    // console.log(df_j);
    // console.log(dt_j);
    var date_f = new Date(df_j);
    var date_t = new Date(dt_j);
    // console.log(date_f);
    // console.log(date_t);
    if (date_from_input.val() == "" && date_to_input.val() != "") {
        $("#from_error_msg").html("This field is required !");
        $("#report_filter_form").submit(function (e) {
            e.preventDefault();
        });
    }
    else if (date_f > date_t) {
        $("#error_msg").html("From Date must be smaller than or equal To Date!");
        $("#report_filter_form").submit(function (e) {
            e.preventDefault();
        });
    }
    else {
        // console.log("Perfect !!!");
        $("#report_filter_form").submit(function (e) {
            e.preventDefault();
            $('#report_filter_form').unbind('submit').submit();
        });
    }
    if (date_to_input.val() == "") {
        $("#from_error_msg").html("");
        $("#error_msg").html("");
    }
    if (date_to_input.val() != "" && date_from_input.val() != "") {
        $("#from_error_msg").html("");
        $("#to_error_msg").html("");
    }
}

// Data Tables

$(document).ready(function () {
    var filter_html = $("#filter_stat_html").html();
    var data_name = $("#data_name").val();
    // console.log(data_name)
    var table = $('#statisticsOverallDataTable').DataTable({
        destroy: true,
        //"retrieve": true,
        //"order": [[ 1, 'desc' ]],
        "ordering": false,
        "select": true,
        "scrollCollapse": true,
        "stateSave": true,
        "pagingType": "full_numbers",
        //"searching": false,
        //"paging": false,
        //"scrollY": 400,
        //"scrollX": 400,
        //"scrollY": '62vh',
        //"scrollX": '50vh',
        'dom': 'Bfrtip',
        "lengthMenu": [
            [10, 25, 50, -1],
            ['10 rows', '25 rows', '50 rows', 'Show all']
        ],
        'buttons': [
            // 'copy', 'csv', 'excel', 'pdf', 'print',
            {
                extend: 'colvis',
                collectionLayout: 'fixed two-column',
                postfixButtons: ['colvisRestore'],
                className: 'text-primary font-bold font-italic'
            },
            {
                extend: 'pdfHtml5',
                orientation: 'landscape',
                pageSize: 'LEGAL',
                title: "Exported Data |PDF| " + data_name + " Statistics | theZoo",
                footer: true,
                className: 'text-secondary font-bold'
            },
            {
                extend: 'excelHtml5',
                autoFilter: true,
                sheetName: "Exported Data |EXCEL| " + data_name + " Statistics | theZoo",
                title: "Exported Data |EXCEL| " + data_name + " Statistics | theZoo",
                footer: true,
                className: 'text-secondary font-bold'
            },
            {
                extend: 'csvHtml5',
                title: "Exported Data |CSV| " + data_name + " Statistics | theZoo",
                footer: true,
                className: 'text-secondary font-bold'
            },
            {
                extend: 'copyHtml5',
                footer: true,
                className: 'text-secondary font-bold'
            },
            {
                extend: 'print',
                messageTop: "PRINT | " + filter_html + " | " + data_name + " Statistics | theZoo",
                exportOptions: {
                    columns: ':visible'
                },
                className: 'text-secondary font-bold'
            },
            // 'columnsToggle',
            // 'colvis',
            {
                extend: 'pageLength',
                className: 'text-success font-italic'
            },
            // 'pageLength'
        ],
        "columnDefs": [
            {
                targets: -1,
                visible: false
            }
        ],
        "language": {
            // "lengthMenu": "Display _MENU_ records per page. <span class='ml-4 text-primary'>Total Records: <span class='font-13 font-bold'>" +
            //     $("#total_records_count").val() + "</span></span>",
            // "zeroRecords": "Nothing found - sorry",
            // "info": "Showing page _PAGE_ of _PAGES_",
            // "infoEmpty": "No records available",
            // "infoFiltered": "(filtered from _MAX_ total records)",
            buttons: {
                copyTitle: 'Added to the clipboard',
                copyKeys: 'Press <i> ctrl </ i> or <i> \ u2318 </ i> + <i> C </ i> to copy the data from the table to your clipboard. <br> <br> To cancel, click on this message or press Esc.',
                copySuccess: {
                    _: '%d lines copied',
                    1: '1 line copied'
                },
                colvis: 'Column Visibility',
            }
        },
    });
    // jqueryUI Style
    // table.buttons().container().insertBefore('#statisticsOverallDataTable_filter');
    // bootstrap4 Style
    // table.buttons().container().appendTo('#example_wrapper .col-md-6:eq(0)');
});