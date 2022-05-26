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

let images = document.querySelectorAll('img').forEach(img => {
    img.addEventListener('click', _ => {
        let figure = document.createElement('figure')
        let figureImage = document.createElement('img')
        let figureCaption = document.createElement('figcaption')

        figureImage.src = img.src
        figureCaption.innerText = img.alt // if it does not have an alt, thats your problem not mine
        
        figure.appendChild(figureImage)
        figure.appendChild(figureCaption)

        let wrapper = document.createElement('div')
        let underlay = document.createElement('div')

        underlay.classList.add('underlay')
        wrapper.classList.add('fullscreenImage')

        wrapper.appendChild(underlay)
        wrapper.appendChild(figure)

        underlay.addEventListener('click', _ => {
            wrapper.remove()
        }, {once: true})

        document.body.appendChild(wrapper)

    })
})