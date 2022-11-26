// 圆圈
$('.circle li').hover(function () {
    $(this).addClass('current').siblings().removeClass('current');
    let index = $(this).index();
    // $('.imgs li').eq(index).removeClass('hide').siblings().addClass('hide');
    $('.imgs li').eq(index).stop().fadeIn(1500).removeClass('hide').siblings().stop().fadeOut(1500).addClass('hide');
})
// 左
$('.left_arrow').click(function () {
    let index = $('.circle .current').index();
    if (index !== 0) {
        $('.imgs li').eq(index).prev().stop().fadeIn(1500).removeClass('hide').siblings().stop().fadeOut(1500).addClass('hide');
        $('.circle li').eq(index).prev().addClass('current').siblings().removeClass('current');
    } else {
        index = $('.circle').children().length - 1;
        $('.imgs li').eq(index).stop().fadeIn(1500).removeClass('hide').siblings().stop().fadeOut(1500).addClass('hide');
        $('.circle li').eq(index).addClass('current').siblings().removeClass('current');
    }
})
// 右
$('.right_arrow').click(right_arrow);

function right_arrow() {
    let index = $('.circle').children().length - 1;
    let current_index = $('.circle .current').index();
    if (current_index !== index) {
        $('.imgs li').eq(current_index).next().stop().fadeIn(1500).removeClass('hide').siblings().stop().fadeOut(1500).addClass('hide');
        $('.circle li').eq(current_index).next().addClass('current').siblings().removeClass('current');
    } else {
        $('.imgs li').eq(0).stop().fadeIn(1500).removeClass('hide').siblings().stop().fadeOut(1500).addClass('hide');
        $('.circle li').eq(0).addClass('current').siblings().removeClass('current');
    }
}

// 自动轮播
let interval = setInterval(right_arrow, 2000);

$('.box').hover(function () {
    clearInterval(interval);
}, function () {
    interval = setInterval(right_arrow, 2000);
})
