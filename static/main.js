let prevScrollPos = window.pageYOffset,
    navbar = document.getElementById('navbar')

window.onscroll = () => {
    let currScrollPos = window.pageYOffset

    if (prevScrollPos > currScrollPos) {
        navbar.style.top = "5px"
    } else {
        navbar.style.top = "-50px"
    }

    prevScrollPos = currScrollPos
}