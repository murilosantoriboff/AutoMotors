const params = new URLSearchParams(window.location.search);
const key_error = params.get('message');
if (key_error == 'ERROR') {
    alert('Os dados passados podem estar incorretos!')
} else if (key_error == 'EMAIL_ERROR') {
    alert('O e-mail pode estar em uso já!')
}