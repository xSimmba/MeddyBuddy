
    let EditImg = document.querySelector(".edit_meds_img");
    EditImg.onmouseover = () => {
        EditImg.src = "/static/media/edit_meds_houver.svg";
        console.log("hover")
    };
    
    EditImg.onmouseout = () => {
        EditImg.src = "/static/media/edit_meds.svg";
        console.log("hover")
    };

    let ProfileImg = document.querySelector(".profile_img");
    ProfileImg.onmouseover = () => {
        ProfileImg.src = "/static/media/profile_houver.svg";
    };
    ProfileImg.onmouseout = () => {
        ProfileImg.src = "/static/media/profile.svg";
        console.log("hover")
    };
    
    let ViewImg = document.querySelector(".view_meds_img");
    ViewImg.onmouseover = () => {
        ViewImg.src = "/static/media/view_meds_houver.svg";
    };
    ViewImg.onmouseout = () => {
        ViewImg.src = "/static/media/view_meds.svg";
        console.log("hover")
    };

    let AddImg = document.querySelector(".add-btn");
    AddImg.onmouseover = () => {
        AddImg.src = "/static/media/add_meds_over.svg";
    };
    AddImg.onmouseout = () => {
        AddImg.src = "/static/media/add_meds.svg";
        console.log("hover")
    };

