
    document.addEventListener('DOMContentLoaded', function() {
    var folders = document.getElementsByClassName('folder-name');

    for (var i = 0; i < folders.length; i++) {
        folders[i].addEventListener('click', function(e) {
        e.stopPropagation();
        this.parentNode.classList.toggle('open');
        });
    }
    });
