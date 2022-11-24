// 删除行
function del_tr(self) {
    var trEle = self.parentElement.parentElement;
    trEle.remove();
}

// 修改行
function edit_tr(self) {
    self.innerText = '保存';
    self.setAttribute('onclick', 'save_tr(this)');

    var tdEles = self.parentElement.parentElement.children;
    for (var i = 0; i < tdEles.length - 2; i++) {
        var inputEle = document.createElement('input');
        inputEle.type = 'text';
        inputEle.value = tdEles[i].innerHTML;
        tdEles[i].innerHTML = '';
        tdEles[i].appendChild(inputEle);
    }
}

// 保存事件
function save_tr(self) {
    var tdEles = self.parentElement.parentElement.children;
    // console.log(tdEles);
    for (var i = 0; i < tdEles.length - 2; i++) {
        var inputEle = tdEles[i].firstChild;
        // console.log(inputEle);
        var inputText = inputEle.value;
        tdEles[i].innerHTML = inputText;
    }

    self.innerText = '编辑'
    self.setAttribute('onclick', 'edit_tr(this)');
}

var tbodyEle = document.getElementsByClassName('tbody')[0];
var addBtn = document.querySelector('.add-btn');
// 添加行事件
addBtn.onclick = function () {
    var ele = document.querySelectorAll('#name,#age,#dep');
    var trEle = document.createElement('tr');
    console.log(ele);
    for (var i = 0; i < ele.length; i++) {
        var val = ele[i].value;
        if (!val) {
            val = 'null';
        }
        var tdEle = document.createElement('td');
        tdEle.innerText = val;
        trEle.appendChild(tdEle);
        ele[i].value = '';
    }

    // 构建两个btn
    td = create_td('编辑', 'edit_tr(this)');
    trEle.appendChild(td);
    td = create_td('删除', 'del_tr(this)');
    trEle.appendChild(td);
    tbodyEle.appendChild(trEle);
}

// 构建btn
function create_td(text, func_text) {
    var tdEle = document.createElement('td');
    var btnEle = document.createElement('button');
    btnEle.setAttribute('onclick', func_text);
    btnEle.innerText = text;
    tdEle.appendChild(btnEle);
    return tdEle;
}