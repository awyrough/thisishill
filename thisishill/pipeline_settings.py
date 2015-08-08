PIPELINE_ENABLED = False

PIPELINE_CSS = {
    "bootstrap": {
        "source_filenames": (
            "lib/bootstrap/css/bootstrap.min.css",
        ),
        "output_filename": "pipeline/css/bootstrap.css",
    },
    "bootstrap-datetimepicker": {
        "source_filenames": (
            "lib/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css",
        ),
        "output_filename": "pipeline/css/bootstrap-datetimepicker.css",
    },
}

PIPELINE_JS = {
    "d3": {
        "source_filenames": (
            "lib/d3/d3.min.js",
        ),
        "output_filename": "pipeline/js/d3.js",
    },
    "jquery": {
        "source_filenames": (
            "lib/jquery/jquery-1.11.1.min.js",
        ),
        "output_filename": "pipeline/js/jquery.js",
    },
    "bootstrap": {
        "source_filenames": (
            "lib/bootstrap/js/bootstrap.min.js",
        ),
        "output_filename": "pipeline/js/bootstrap.js",
    },
    "bootstrap-datetimepicker": {
        "source_filenames": (
            "lib/momentjs/moment.min.js",
            "lib/bootstrap-datetimepicker/js/bootstrap-datetimepicker.min.js",
        ),
        "output_filename": "pipeline/js/bootstrap-datetimepicker.js",
    },
}