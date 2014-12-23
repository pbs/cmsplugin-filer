function overlay(element){
    $(element).click(function(){
        var imgURL = $(this).data('rel');
        $(element).after('<div class="frame" style="position: absolute; left: 0; top: 0; height: 100%; width: 100%; text-align: center; background-color: rgba(0, 0, 0, 0.88);"> <span style="display: inline-block; height: 100%; vertical-align: middle;"></span><img style="vertical-align: middle; max-height: 90%; max-width: 90%;" src="' + imgURL + '" /></div>');
        $('.frame').click(function() {$('.frame').remove();} );
    });
}
