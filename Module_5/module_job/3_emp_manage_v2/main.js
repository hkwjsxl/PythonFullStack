$('.my_tbody').on('click', '.btn_edit', function () {
    let $td = $(this).parent().parent().children();
    $td.slice(0, -1).each(function (index, obj) {
        // console.log(index, obj);
        let content = $(this).html();
        let $input = $(`<input type="text" class="form-control" value=${content}>`);
        $(this).html($input);
    })
    $(this).html('保存').removeClass('btn_edit').addClass('lg_btn_save');
})

$('.my_tbody').on('click', '.lg_btn_save', function () {
    let $td = $(this).parent().parent().children();
    $td.slice(0, -1).each(function (index, obj) {
        // console.log(index, obj);
        let content = $(this).children().val();
        $(this).html(content);
    })
    $(this).html('编辑').removeClass('lg_btn_save').addClass('btn_edit');
})

$('.my_tbody').on('click', '.btn_del', function () {
    $(this).parent().parent().remove();
})

$('#btn_save').click(function () {
    // 关闭模态框
    $('#myModal').modal('hide');
    // 构建tr
    let $tr = $(`<tr></tr>`);
    $('.get_v').each(function () {
        let content = $(this).val();
        if (!content) {
            content = 'null';
        }
        let $td = $(`<td>${content}</td>`);
        // console.log($td);
        $tr.append($td);
    })
    $tr.append(
        $('<td>\n                            <button class="btn btn-primary btn-sm btn_edit">编辑</button>\n                            <button class="btn btn-danger btn-sm btn_del">删除</button>\n                        </td>')
    )
    // console.log($tr);
    $('.my_tbody').append($tr);

    // 清空
    $('.get_v').each(function () {
        $(this).val('');
    })
})