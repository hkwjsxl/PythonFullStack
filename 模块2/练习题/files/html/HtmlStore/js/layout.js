
jQuery(document).ready(function($) {

    $('.top-menu-item').bind('mouseover',function(){
        $(this).children('.child-menu').removeClass('hide');
        $(this).find('i').removeClass('arrow-down').addClass('arrow-up');
    }).bind('mouseout',function(){
        $(this).children('.child-menu').addClass('hide');
        $(this).find('i').addClass('arrow-down').removeClass('arrow-up');
    });

    $('.top-menu-item .child-menu').bind('mouseover',function(){
        $(this).removeClass('hide');
        $(this).parent().find('i').removeClass('arrow-down').addClass('arrow-up');
    }).bind('mouseout',function(){
        $(this).addClass('hide');
        $(this).parent().find('i').addClass('arrow-down').removeClass('arrow-up');
    });

    var $scalable_menu = $('.scalable-menu-body');
    if($scalable_menu){
        BindFunctionTree($scalable_menu);
    }

    InitGlobalSearch();
});


function BindFunctionTree($menu){
    $menu.find('.item .title').bind('click',function(){
        $(this).find('.fa-caret-down').addClass('fa-caret-up');
        $(this).next().removeClass('hide');
        $(this).parent().siblings().find('.body').addClass('hide');
        $(this).parent().siblings().find('.fa-caret-up').removeClass('fa-caret-up').addClass('fa-caret-down');
    });
}


function InitMenu(sel){
    $(sel).addClass('selected');
    $(sel).parent().removeClass('hide');
    $(sel).parent().prev().find('.fa-caret-down').removeClass('fa-caret-down').addClass('fa-caret-up');
    $(sel).parent().prev().parent().siblings().find('.selected').removeClass('selected');
    $(sel).parent().prev().parent().siblings().find('.fa-caret-up').removeClass('fa-caret-down');
}

function InitGlobalSearch(){

    $('#GlobalSearchIp').focus(function(){
        window.onkeyup = function(event){
            if(event && event.keyCode == 13){
                DoGlobalSearch(1);
            }
        }
    });
}

function DoGlobalSearch(){
    $('#GlobalSearchPage').val('1');
    $("#GlobalSearch").submit();
}
