document.addEventListener('DOMContentLoaded', function (event) {
    console.log("The admin has loaded");
    let sc = document.createElement('script')
    sc.setAttribute('src', 'https://cdn.tiny.cloud/1/phrs3oxrm4z2zzctve8v8rhjubt6w5pqkw69mm3fz30tgv8j/tinymce/6/tinymce.min.js');
    sc.setAttribute('referrerpolicy', 'origin');

    document.head.appendChild(sc);
    sc.onload = () => {

        // import 'tinymce/icons/default';

        tinymce.init({
            selector: '#id_content',
            plugins: [
                'a11ychecker', 'advcode', 'advlist', 'anchor', 'autolink', 'codesample', 'fullscreen', 'help',
                'image', 'editimage', 'tinydrive', 'lists', 'link', 'media', 'powerpaste', 'preview',
                'searchreplace', 'table', 'template', 'tinymcespellchecker', 'visualblocks', 'wordcount'
            ],
        });
    }
});



