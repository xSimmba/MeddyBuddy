
window.onload = () => {
    let EditImg = document.querySelector(".edit_meds_img");
    EditImg.onmouseover = () => {
        EditImg.src = "/static/media/header/add-btn-hover.svg";
    };
    
    EditImg.onmouseout = () => {
        EditImg.src = "/static/media/header/add-btn.svg";
    };

    let ProfileImg = document.querySelector(".profile_img");
    ProfileImg.onmouseover = () => {
        ProfileImg.src = "/static/media/profile_houver.svg";
    };
    ProfileImg.onmouseout = () => {
        ProfileImg.src = "/static/media/profile.svg";
        console.log("hover")
    };
    
    let logout = document.querySelector(".logout-btn");
    logout.onmouseover = () => {
        logout.src = "/static/media/footer/logout-hover.svg";
    };
    logout.onmouseout = () => {
        logout.src = "/static/media/footer/logout.svg";
    };
}