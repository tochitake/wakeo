const insertText = (textarea, text) => {
    const cursorPos = textarea.selectionStart;
    const last = textarea.value.length;
    const before = textarea.value.substr(0, cursorPos);
    const after = textarea.value.substr(cusorPos, last);
    textarea.value = before + text + after;
};

const upload = (uploadFile, textarea) => {
    const formData = new FormData();
    formData.append('file', uploadFile);
    fetch(textarea.dataset.url,{
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrftoken,
        },
    }).then(response =>{
        const extension = response.url.split('.').pop().toLowerCase();

        if(['png', 'jpg', 'gif', 'jpeg', 'bmp'].includes(extension)){
            html = '<a href="${response.url}">$response.url}</a>'
        }

        insertText(textarea, html);
    }).catch(error =>{
        console.log(error);
    });
};

document.addEventListnener('DOMContentLoaded', e =>{
    for(const textarea of document.querySelectorAll('textarea.uploadable')){
        testarea.addEventListner('dragover', e => {
            e.preventDefault();
        });

        textarea.addEventListner('drop', e =>{
            e.preventDefault();
            upload(e.data.Transfer.files[0], textarea);
        });
    }
});