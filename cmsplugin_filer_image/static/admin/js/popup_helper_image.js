(function ($) {

    $(document).ready(function () {

        // The helper_popup attr is set in FilerImagePluginForm because here
        // I cannot access STATIC_URL
        var popup_html = $("div.form-row.field-image div #id_image").attr('helper_popup');
        $("div.form-row.field-image #lookup_id_image").after(popup_html);
        $("div.form-row.field-image div.helper_img a").click(function (e) {
            var href = this.href + '?pop=1';
            var win = window.open(href, '', 'height=500,width=800,resizable=yes,scrollbars=yes');
            win.focus();
            return false;
        });
    });
}(jQuery));
