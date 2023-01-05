window.onload = () => {
    if (sessionStorage.getItem("theme")) {
        sessionStorage.setItem("theme", "light")
        if (sessionStorage.getItem("theme") == "light") {

            elem.children[0].setAttribute("name", "moon-outline")
        } else {
            elem.children[0].setAttribute("name", "sunny-outline")

        }
    }
    document.querySelector("html").setAttribute("data-theme", sessionStorage.getItem("theme"))
}

function themeSwitch(elem) {
    if (elem.children[0].getAttribute("name") == 'sunny-outline') {
        elem.children[0].setAttribute("name", "moon-outline")
        sessionStorage.setItem("theme", "light")
        document.querySelector("html").setAttribute("data-theme", sessionStorage.getItem("theme"))
    } else {
        elem.children[0].setAttribute("name", "sunny-outline")
        sessionStorage.setItem("theme", "dark")
        document.querySelector("html").setAttribute("data-theme", sessionStorage.getItem("theme"))
    }
}
//<ion-icon name="moon-outline"></ion-icon>