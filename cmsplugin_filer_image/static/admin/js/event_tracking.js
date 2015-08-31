(function($){
    $(document).ready(function(){       
        var toggleEvent = function (toggler) {
             if($(toggler).is(':checked')){
                $('.field-event_category, .field-event_action, .field-event_label').show();
            }else{
                $('.field-event_category, .field-event_action, .field-event_label').hide();
            }
        } 
        
        $('#id_enable_event_tracking').on('click', function(){
            toggleEvent('#id_enable_event_tracking');
        });

       toggleEvent('#id_enable_event_tracking');

        $('#filerimage_form').on('submit', function(){
            //turn off event tracking if the image is not clickable
            if($('#id_link_options option:selected').text() === "No link"){
                $('#id_enable_event_tracking').prop('checked', false);
            }
        });
    });
}(jQuery));
