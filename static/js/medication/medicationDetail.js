window.onload = () => {

    let editBtn = document.querySelector(".edit-img");
        editBtn.onmouseover = () => {
            editBtn.src = "/static/media/edit_meds_btn_over.svg";
            
        };
        editBtn.onmouseout = () => {
            editBtn.src = "/static/media/edit_meds_btn.svg";
        };

    let deleteBtn = document.querySelector(".delete-img");
        deleteBtn.onmouseover = () => {
            deleteBtn.src = "/static/media/delete_meds_over.svg";
            
        };
        deleteBtn.onmouseout = () => {
            deleteBtn.src = "/static/media/delete_meds.svg";
        };
}