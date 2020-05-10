(function dragger() {
    let fig = document.querySelector("figure");
    let img = document.querySelector("figure div");
    let art = document.querySelector("article");
    let startX = 0, startY = 0, scrollX = 0, scrollY = 0, zoom = 1;
    function mm(e) {
        let dx = e.pageX - startX, dy = e.pageY - startY;
        art.scrollTo(scrollX - dx, scrollY - dy);
    }
    function mu(e) {
        document.removeEventListener("mousemove", mm, false);
        document.removeEventListener("mouseup", mu, false);
        scrollX = scrollX - (e.pageX - startX), scrollY = scrollY - (e.pageY - startY)
    }
    img.onmousedown = function(e) {
        startX = e.pageX, startY = e.pageY;
        document.addEventListener("mousemove", mm, false);
        document.addEventListener("mouseup", mu, false);
    }
    fig.onwheel = function(e) {
        if (e.deltaY > 0 && zoom > 1) { zoom -= 0.2 } else if (e.deltaY < 0) { zoom += 0.2 }
            fig.style.transformOrigin = e.pageX + "px " + e.pageY + "px";
        fig.style.transform = "scale(" + zoom + ")";
        e.preventDefault();
    }
})()

Array.from(document.querySelectorAll("footer a")).forEach(function(a) {
    let target = document.getElementById(a.dataset.id);
    a.onmouseover = function() {
        target.classList.add("show");
        target.scrollIntoView({behavior: "smooth", block: "center", inline: "center"});
    }
    a.onmouseout = function() { target.classList.remove("show"); }
})