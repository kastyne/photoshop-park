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

let tableOfContents = document.querySelector('#toc')
let articleHeadings = document.querySelectorAll(`
    div.content h1,
    div.content h2,
    div.content h3,
    div.content h4,
    div.content h5,
    div.content h6
`)

if (tableOfContents && articleHeadings.length >=2) {

    let tocList = document.createElement('ul')
    articleHeadings.forEach( (heading, i) => {
        if (!heading.id) {
            heading.id = "articleHeading" + i
        }

        let tocElement = document.createElement('li')
        let tocLink = document.createElement('a')

        tocLink.href = "#" + heading.id
        tocLink.innerText = heading.innerText

        tocElement.appendChild(tocLink)
        tocList.appendChild(tocElement)
    })

    tableOfContents.appendChild(tocList)
}

/* tried doing some fancy nesting stuff, it didnt work anyway
let tocSubheadings = document.createElement('ul')

        let level = Number(heading.tagName[-1]) // naming stujf is hard

        tocSubheadings.class = "tocLevel" + level
        tocLink.href = "#" + heading.id
        tocLink.innerText = heading.innerText

        tocElement.appendChild(tocLink)
        tocElement.appendChild(tocSubheadings)

        if (level == 1) {
            tocList.appendChild(tocElement)
        } else {
            let parent = tocList.querySelector('.tocLevel' + (level + 1) + ":last-of-type" )
            console.log(parent)
            if (parent) parent.appendChild(tocElement)
            else tocList.append(tocElement)
        }
*/