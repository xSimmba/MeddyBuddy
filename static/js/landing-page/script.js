window.onload = () => {
   let login = document.querySelector(".login")
   login.onmouseover = () => {
    login.style =
     `color: #fff;
     background-color:#7F7F80;
     border: 7px solid #7F7F80;
      border-radius: 5px;
    `;
   }
   login.onmouseout = () => {
    login.style = "color: #000";
   }
   let register = document.querySelector(".register")
   register.onmouseover = () => {
    register.style =
     `color: #fff;
     background-color:#7F7F80;
     border: 7px solid #7F7F80;
      border-radius: 5px;
    `;
   }
   register.onmouseout = () => {
    register.style = "color: #000";
   }
   
}