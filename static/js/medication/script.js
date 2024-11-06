window.onload = () => {
    let red = document.querySelector("#red")
    red.onclick = () => {
        document.querySelector(".meds-box").style = `
        background-color: rgba(255, 0, 0, 0.4);
        `}

    let green = document.querySelector("#green")
    green.onclick = () => {
        document.querySelector(".meds-box").style = `
        background-color: rgba(0, 128, 0, 0.4);
        `}
};