document.addEventListener("DOMContentLoaded", function(event) {
    let sc = document.createElement("script");
    sc.setAttribute("src", "https://cdn.tiny.cloud/1/hr3tb1x9079qo1rwno5n7npfe5zrih8goetprug7q078t4ft/tinymce/5/tinymce.min.js");
    sc.setAttribute("referrerpolicy", "origin");
    document.head.appendChild(sc);
    sc.onload = () => {
        tinymce.init({
            selector : "#id_body",
            height:600,
            plugins: ['codesample image advlist autolink lists charmap print preview anchor textcolor',
            'searchreplace visualblocks code fullscreen',
            'insertdatetime table contextmenu paste code help'
        ],
            toolbar: 'codesample | code | image | insert redo | styleselect | fontselect | fontsizeselect | aligncenter alignright alignjustify | bold italic backcolor | bullist numlist outdent indent | removeformat | help',
            fontsize_formats: '8pt 9pt 10pt 11pt 12pt 14pt 16pt 18pt 24pt 30pt 36pt 48pt 60pt 72pt 96pt',

        })
    }
});